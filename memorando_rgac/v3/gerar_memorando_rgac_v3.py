# -*- coding: utf-8 -*-
"""
Gera o Memorando de acompanhamento do RGAC, versão 3.0 (ENSAIO da opção B).

Uso (a partir da raiz do repositório):
    python3 memorando_rgac/v3/gerar_memorando_rgac_v3.py

Saída: memorando_rgac/v3/Memorando_Acompanhamento_RGAC_v3_ensaio.docx

Lê os dados de dados_memorando_rgac_v3.py e a estrutura do RGAC de ../estrutura_rgac.json.
As referências [[epígrafe]] são trocadas pelo número atual do artigo. Se uma epígrafe não existir na
versão atual do RGAC, o gerador pára e mostra a lista «a reconciliar», com as epígrafes mais parecidas.

A formatação (tabelas, larguras, rodapé, bibliografia) reaproveita as funções do gerador da versão 1.x.
"""
import difflib
import importlib.util
import json
import os
import re
import sys

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

AQUI = os.path.dirname(os.path.abspath(__file__))
PASTA_V1 = os.path.dirname(AQUI)
RAIZ = os.path.dirname(PASTA_V1)
SAIDA = os.path.join(AQUI, "Memorando_Acompanhamento_RGAC_v3_ensaio.docx")


def _carregar(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


D = _carregar("dados_v3", os.path.join(AQUI, "dados_memorando_rgac_v3.py"))
G1 = _carregar("gerador_v1", os.path.join(PASTA_V1, "gerar_memorando_rgac.py"))
G1.D = D  # as funções partilhadas (bibliografia, stakeholders) passam a ler os dados da 2.0

par, titulo, bordas, larguras, celula = G1.par, G1.titulo, G1.bordas, G1.larguras, G1.celula
cabecalho_tabela, paisagem, retrato = G1.cabecalho_tabela, G1.paisagem, G1.retrato

PROIBIDOS = G1.PROIBIDOS
MARCA = re.compile(r"\[\[([^\]]+)\]\]")


# ------------------------------------------------------------------ estrutura e âncoras
def carregar_estrutura():
    with open(os.path.join(PASTA_V1, "estrutura_rgac.json"), encoding="utf-8") as f:
        e = json.load(f)
    if e["ficheiro"] != D.FICHEIRO_RGAC:
        print("ERRO: estrutura_rgac.json foi extraída de outro ficheiro. Correr extrair_estrutura_rgac.py.")
        sys.exit(1)
    arts = e["artigos"]
    for i, a in enumerate(arts):
        a["ordem"] = i
    cont, vistos, anc = {}, {}, {}
    for a in arts:
        ep = a["epigrafe"].strip()
        cont[ep] = cont.get(ep, 0) + 1
    for a in arts:
        ep = a["epigrafe"].strip()
        vistos[ep] = vistos.get(ep, 0) + 1
        chave = f"{ep}#{vistos[ep]}" if cont[ep] > 1 else ep
        a["ancora"] = chave
        anc[chave] = a
    return arts, anc


ARTS, ANC = carregar_estrutura()
A_RECONCILIAR = []


def artigo(ancora, onde="?"):
    ancora = ancora.strip()
    ancora = D.RENOMEACOES.get(ancora, ancora)
    a = ANC.get(ancora)
    if a is None:
        parecidas = difflib.get_close_matches(ancora, list(ANC), n=3, cutoff=0.5)
        A_RECONCILIAR.append((onde, ancora, parecidas))
    return a


def num(a):
    return f"{a['numero']}.º"


def cap_curto(a):
    return a["capitulo"].replace("Capítulo", "cap.").replace("Anexo", "anexo")


def r(texto, onde="?"):
    """Troca [[epígrafe]] pelo número do artigo na versão atual."""
    def rep(m):
        a = artigo(m.group(1), onde)
        return num(a) if a else f"[[{m.group(1)}]]"
    return MARCA.sub(rep, texto)


def ancoras_em(textos):
    out = []
    for x in textos:
        for m in MARCA.finditer(x):
            if m.group(1).strip() not in out:
                out.append(m.group(1).strip())
    return out


def artigo_principal(f):
    return artigo(f["artigo"], f["cod"])


def fichas_ordenadas():
    return sorted(D.FICHAS, key=lambda f: ((artigo_principal(f) or {"ordem": 9999})["ordem"], f["cod"]))


def capitulos_com_fichas():
    caps = []
    for f in fichas_ordenadas():
        a = artigo_principal(f)
        c = (a["capitulo"], a["epigrafe_capitulo"])
        if c not in caps:
            caps.append(c)
    return caps


# ------------------------------------------------------------------ verificações
def verificar():
    erros = []

    def ver(txt, onde):
        for c in PROIBIDOS:
            if c in txt:
                erros.append(f"{onde}: contém '{c}' -> «{txt[:80]}»")

    codigos = set()
    for f in D.FICHAS:
        m = re.fullmatch(r"([A-Z]{3})-(\d\d+)", f["cod"])
        if f["cod"] in codigos or not m:
            erros.append(f"Código repetido ou inválido: {f['cod']}")
        elif m.group(1) != f["etiquetas"][0]:
            erros.append(f"{f['cod']}: a sigla do código tem de ser a do tema principal ({f['etiquetas'][0]})")
        codigos.add(f["cod"])
        if f["origem"] not in D.ORIGENS:
            erros.append(f"{f['cod']}: origem inválida")
        if f["estado"] not in D.ESTADOS:
            erros.append(f"{f['cod']}: estado inválido")
        for e in f["etiquetas"]:
            if e not in D.ETIQUETAS:
                erros.append(f"{f['cod']}: etiqueta desconhecida {e}")
        textos = [f["titulo"], f["proposta"]] + f["onde"] + f["problema"] + f["levantado"]
        for x in textos:
            ver(x, f["cod"])
            r(x, f["cod"])
            if "imprensa" in x and x in f["levantado"]:
                erros.append(f"{f['cod']}: referência de imprensa em levantado")
        artigo_principal(f)
    for f in D.FICHAS:
        for rel in f["rel"]:
            if rel not in codigos:
                erros.append(f"{f['cod']}: ficha relacionada inexistente {rel}")
    for l in D.LAPSOS:
        for k in l["onde"]:
            artigo(k, l["cod"])
        r(l["lapso"], l["cod"])
        r(l["correcao"], l["cod"])
        if l["ficha"] and l["ficha"] not in codigos:
            erros.append(f"{l['cod']}: ficha inexistente {l['ficha']}")
        ver(l["lapso"] + l["correcao"], l["cod"])
    for k, v in D.REVISAO.items():
        artigo(k, "REVISAO")
        if v.get("estado") not in D.ESTADOS_REVISAO:
            erros.append(f"REVISAO {k}: estado inválido")
    for t in D.TRANSVERSAIS:
        for x in t["intro"]:
            ver(x, t["etiqueta"])
            r(x, t["etiqueta"])
    for a, b in D.RESOLVIDOS:
        ver(a + b, "RESOLVIDOS")
        r(b, "RESOLVIDOS")
    biblio = {b[2] for b in D.BIBLIOGRAFIA}
    for s in D.STAKEHOLDERS:
        if s[5] not in biblio:
            erros.append(f"Fonte do Anexo B fora da bibliografia: {s[1]}")
    if A_RECONCILIAR:
        print("A RECONCILIAR: epígrafes que não existem na versão atual do RGAC")
        print(f"(RGAC: {D.FICHEIRO_RGAC})")
        vistos = set()
        for onde, anc, parecidas in A_RECONCILIAR:
            if (onde, anc) in vistos:
                continue
            vistos.add((onde, anc))
            sug = "; ".join(f"«{p}» (art. {num(ANC[p])})" for p in parecidas) or "nenhuma parecida"
            print(f"  - {onde}: «{anc}». Candidatas: {sug}")
        print("Para cada epígrafe, acrescentar a RENOMEACOES em dados_memorando_rgac_v3.py a linha")
        print("  «epígrafe antiga»: «epígrafe nova», ou mudar a ficha de lugar se o artigo desapareceu. Gerar de novo.")
    if erros:
        print("ERROS no ficheiro de dados:")
        for e in erros:
            print("  -", e)
    if erros or A_RECONCILIAR:
        sys.exit(1)


# ------------------------------------------------------------------ blocos
def linha_onde(f):
    partes = [r(x, f["cod"]) for x in f["onde"]]
    a = artigo_principal(f)
    return partes + [f"Artigo principal: art. {num(a)}, {a['epigrafe']} ({a['capitulo']}, {a['epigrafe_capitulo']})."]


def ficha(doc, f):
    titulo(doc, f"{f['cod']}. {r(f['titulo'], f['cod'])}", 2)
    linhas = [
        ("Onde", linha_onde(f)),
        ("Etiquetas", "; ".join(D.ETIQUETAS[e] for e in f["etiquetas"])),
        ("Origem", D.ORIGENS[f["origem"]]),
        ("Problema", [r(x, f["cod"]) for x in f["problema"]]),
        ("Proposta", r(f["proposta"], f["cod"])),
        ("Quem levantou", "; ".join(r(x, f["cod"]) for x in f["levantado"])),
        ("Estado", f["estado"]),
    ]
    if f["rel"]:
        linhas.append(("Fichas relacionadas", ", ".join(f["rel"])))
    t = doc.add_table(rows=0, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    bordas(t)
    for k, v in linhas:
        row = t.add_row()
        celula(row.cells[0], k, negrito=True)
        celula(row.cells[1], v)
    larguras(t, [3.5, 12.5])
    doc.add_paragraph()


def seccoes():
    """Lista de (número, título, fichas) do corpo do memorando."""
    s = [("2.", "Temas transversais: enquadramento", [])]
    n = 3
    for cap, ep in capitulos_com_fichas():
        fs = [f for f in fichas_ordenadas() if artigo_principal(f)["capitulo"] == cap]
        s.append((f"{n}.", f"{cap}. {ep}", fs))
        n += 1
    s.append((f"{n}.", "Pontos já resolvidos no RGAC", []))
    return s


def indice(doc):
    titulo(doc, "Índice", 1)
    entradas = [("1.", "Como ler este memorando", [])] + seccoes() + [
        ("Anexo A.", "Quadro-resumo das fichas, pela ordem do RGAC", []),
        ("Anexo B.", "Posições de entidades externas", []),
        ("Anexo C.", "Lapsos formais", []),
        ("Anexo D.", "Cobertura da revisão, artigo a artigo", []),
        ("Anexo E.", "Fichas por tema", []),
        ("Anexo F.", "Correspondência com os códigos anteriores", []),
        ("", "Registo de alterações", []),
        ("", "Bibliografia", []),
    ]
    for n, nome, fichas in entradas:
        par(doc, (n + " " if n else "") + nome, negrito=True, depois=2)
        for f in fichas:
            a = artigo_principal(f)
            q = par(doc, f"{f['cod']}. {r(f['titulo'], f['cod'])} (art. {num(a)})", depois=0)
            q.paragraph_format.left_indent = Cm(1)
        if fichas:
            doc.add_paragraph().paragraph_format.space_after = Pt(2)


def quadro_resumo(doc):
    titulo(doc, "Anexo A. Quadro-resumo das fichas, pela ordem do RGAC", 1)
    t = doc.add_table(rows=1, cols=6)
    bordas(t)
    for i, h in enumerate(["Código", "Assunto", "Artigo principal", "Etiquetas", "Origem", "Estado"]):
        celula(t.rows[0].cells[i], h, negrito=True)
    cabecalho_tabela(t.rows[0])
    curtas = {"RGAC": "Criado pelo RGAC", "VIGENTE": "Já existia", "PARCIAL": "Resolvido em parte"}
    cap = None
    for f in fichas_ordenadas():
        a = artigo_principal(f)
        if a["capitulo"] != cap:
            cap = a["capitulo"]
            row = t.add_row()
            celula(row.cells[0].merge(row.cells[5]), f"{cap}. {a['epigrafe_capitulo']}", negrito=True)
        row = t.add_row()
        celula(row.cells[0], f["cod"])
        celula(row.cells[1], r(f["titulo"], f["cod"]))
        celula(row.cells[2], f"art. {num(a)}, {a['epigrafe']}")
        celula(row.cells[3], "; ".join(D.ETIQUETAS[e] for e in f["etiquetas"]))
        celula(row.cells[4], curtas[f["origem"]])
        celula(row.cells[5], f["estado"])
    larguras(t, [1.6, 7.6, 6.4, 4.2, 3.2, 2.7])
    doc.add_paragraph()
    abertas = sum(1 for f in D.FICHAS if f["estado"] == "Aberto")
    par(doc, f"Total: {len(D.FICHAS)} fichas, das quais {abertas} em aberto.")


def anexo_stakeholders(doc):
    titulo(doc, "Anexo B. Posições de entidades externas", 1)
    par(doc, "Posições recolhidas em documentos oficiais, pareceres, estratégias, doutrina, artigos científicos "
             "e decisões judiciais. Não se usam notícias de imprensa. As citações estão entre aspas e foram "
             "transcritas das fontes indicadas.")
    nomes = {"T": "Titularidade", "C": "CED e errantes", "T e C": "Titularidade; CED e errantes",
             "C e T": "Titularidade; CED e errantes"}
    entradas = [(s[0], s[1], s[2], nomes.get(s[3], s[3]), s[4], s[5]) for s in D.STAKEHOLDERS]
    G1.tabela_stakeholders(doc, entradas, [5.0, 2.4, 11.3, 7.0])


def anexo_lapsos(doc):
    titulo(doc, "Anexo C. Lapsos formais", 1)
    par(doc, "Remissões erradas, números repetidos, gralhas e marcas de trabalho no texto. Quando o mesmo ponto "
             "já tem ficha, a correção remete para ela.")
    t = doc.add_table(rows=1, cols=5)
    bordas(t)
    for i, h in enumerate(["Código", "Onde", "Lapso", "Correção proposta", "Estado"]):
        celula(t.rows[0].cells[i], h, negrito=True)
    cabecalho_tabela(t.rows[0])
    for l in D.LAPSOS:
        row = t.add_row()
        celula(row.cells[0], l["cod"])
        celula(row.cells[1], "; ".join(f"art. {num(artigo(k))} ({cap_curto(artigo(k))})" for k in l["onde"]))
        celula(row.cells[2], r(l["lapso"], l["cod"]))
        celula(row.cells[3], r(l["correcao"], l["cod"]))
        celula(row.cells[4], l["estado"])
    larguras(t, [1.6, 3.4, 10.6, 7.6, 2.5])


def anexo_cobertura(doc):
    titulo(doc, "Anexo D. Cobertura da revisão, artigo a artigo", 1)
    par(doc, "Por rever: o artigo ainda não foi lido com esse fim. Parcial: tem fichas ou lapsos, mas ainda não "
             "foi revisto por inteiro. Em revisão e Revisto: estado indicado pelo grupo.")
    fichas_por, lapsos_por = {}, {}
    for f in D.FICHAS:
        for anc in ancoras_em(f["onde"]):
            fichas_por.setdefault(anc, []).append(f["cod"])
    for l in D.LAPSOS:
        for k in l["onde"]:
            lapsos_por.setdefault(k, []).append(l["cod"])

    def estado(a):
        if a["ancora"] in D.REVISAO:
            return D.REVISAO[a["ancora"]]["estado"]
        return "Parcial" if fichas_por.get(a["ancora"]) or lapsos_por.get(a["ancora"]) else "Por rever"

    caps = []
    for a in ARTS:
        if a["capitulo"] not in caps:
            caps.append(a["capitulo"])
    t = doc.add_table(rows=1, cols=6)
    bordas(t)
    for i, h in enumerate(["Capítulo", "Artigos", "Revistos", "Em revisão", "Parcial", "Por rever"]):
        celula(t.rows[0].cells[i], h, negrito=True)
    cabecalho_tabela(t.rows[0])
    tot = [0] * 5
    for c in caps:
        est = [estado(a) for a in ARTS if a["capitulo"] == c]
        v = [len(est), est.count("Revisto"), est.count("Em revisão"), est.count("Parcial"), est.count("Por rever")]
        tot = [x + y for x, y in zip(tot, v)]
        row = t.add_row()
        celula(row.cells[0], c)
        for i, x in enumerate(v, start=1):
            celula(row.cells[i], str(x))
    row = t.add_row()
    celula(row.cells[0], "Total", negrito=True)
    for i, x in enumerate(tot, start=1):
        celula(row.cells[i], str(x), negrito=True)
    larguras(t, [6.0, 3.0, 3.0, 3.0, 3.0, 3.0])
    doc.add_paragraph()

    t = doc.add_table(rows=1, cols=6)
    bordas(t)
    for i, h in enumerate(["Artigo", "Epígrafe", "Revisão", "Fichas e lapsos", "Regulamento (UE) 2026/1818", "Nota"]):
        celula(t.rows[0].cells[i], h, negrito=True)
    cabecalho_tabela(t.rows[0])
    cap = None
    for a in ARTS:
        if a["capitulo"] != cap:
            cap = a["capitulo"]
            row = t.add_row()
            celula(row.cells[0].merge(row.cells[5]), f"{cap}. {a['epigrafe_capitulo']}", negrito=True)
        rv = D.REVISAO.get(a["ancora"], {})
        row = t.add_row()
        celula(row.cells[0], num(a))
        celula(row.cells[1], a["epigrafe"])
        celula(row.cells[2], estado(a) + (f" ({rv['data']})" if rv.get("data") else ""))
        celula(row.cells[3], ", ".join(fichas_por.get(a["ancora"], []) + lapsos_por.get(a["ancora"], [])))
        celula(row.cells[4], rv.get("regulamento", "A verificar"))
        celula(row.cells[5], rv.get("nota", ""))
    larguras(t, [1.8, 7.5, 3.2, 4.0, 3.6, 5.6])


def anexo_etiquetas(doc):
    titulo(doc, "Anexo E. Fichas por tema", 1)
    par(doc, "Cada ficha aparece em todos os temas a que pertence. Entre parênteses, o artigo principal.")
    for sigla, nome in D.ETIQUETAS.items():
        fs = [f for f in fichas_ordenadas() if sigla in f["etiquetas"]]
        if not fs:
            continue
        titulo(doc, f"{sigla}. {nome} ({len(fs)})", 2)
        for f in fs:
            a = artigo_principal(f)
            q = par(doc, f"{f['cod']}. {r(f['titulo'], f['cod'])} (art. {num(a)}, {cap_curto(a)})", depois=1)
            q.paragraph_format.left_indent = Cm(0.8)


def anexo_correspondencia(doc):
    titulo(doc, "Anexo F. Correspondência com os códigos anteriores", 1)
    par(doc, "As versões 1 a 1.7 do memorando usavam T para titularidade e C para CED. O ensaio 2.0 usava "
             "números P sem significado. A partir desta versão, o código é a sigla do tema principal e um "
             "número dentro do tema.")
    t = doc.add_table(rows=1, cols=4)
    bordas(t)
    for i, h in enumerate(["Versão 1.x", "Ensaio 2.0", "Código atual", "Assunto"]):
        celula(t.rows[0].cells[i], h, negrito=True)
    cabecalho_tabela(t.rows[0])
    por_cod = {f["cod"]: f for f in D.FICHAS}
    for antigo, ensaio, novo in D.CORRESPONDENCIA:
        row = t.add_row()
        celula(row.cells[0], antigo)
        celula(row.cells[1], ensaio)
        celula(row.cells[2], novo)
        celula(row.cells[3], r(por_cod[novo]["titulo"], novo))
    larguras(t, [2.2, 2.2, 2.6, 9.0])


def proximos_codigos():
    usados = {}
    for f in D.FICHAS:
        s, n = f["cod"].split("-")
        usados[s] = max(usados.get(s, 0), int(n))
    return ", ".join(f"{s}-{usados.get(s, 0) + 1:02d}" for s in D.ETIQUETAS)


# ------------------------------------------------------------------ documento
def gerar():
    verificar()
    doc = Document()
    G1.estilo_base(doc)

    par(doc, "Memorando de acompanhamento do RGAC", negrito=True, tam=20, depois=4)
    par(doc, "Problemas identificados no projeto de Regime Geral do Animal de Companhia", tam=12, depois=4)
    par(doc, "ENSAIO DA VERSÃO 3.0 (opção B). Documento de trabalho para decidir a organização; não substitui a versão 1.7.",
        negrito=True, depois=12)
    t = doc.add_table(rows=0, cols=2)
    bordas(t)
    for k, v in (("Versão do memorando", D.VERSAO_MEMORANDO), ("Data", D.DATA_MEMORANDO),
                 ("Versão do RGAC analisada", D.VERSAO_RGAC),
                 ("Destinatário", "Grupo de trabalho do RGAC. Documento interno.")):
        row = t.add_row()
        celula(row.cells[0], k, negrito=True)
        celula(row.cells[1], v)
    larguras(t, [4.5, 11.5])
    doc.add_paragraph()

    indice(doc)
    doc.add_page_break()

    titulo(doc, "1. Como ler este memorando", 1)
    for p in D.INTRODUCAO:
        par(doc, p)
    par(doc, "Cada ficha tem os seguintes campos:", depois=2)
    for k, v in D.CAMPOS_FICHA:
        q = par(doc, f"{k}: {v}", depois=1)
        q.paragraph_format.left_indent = Cm(0.8)
    par(doc, "")
    par(doc, "Origem do problema:", depois=2)
    for v in D.ORIGENS.values():
        q = par(doc, v + ".", depois=1)
        q.paragraph_format.left_indent = Cm(0.8)

    sec = seccoes()
    doc.add_page_break()
    titulo(doc, f"{sec[0][0]} {sec[0][1]}", 1)
    par(doc, "Dois temas atravessam vários capítulos do RGAC. O enquadramento fica aqui; as fichas estão nos "
             "capítulos onde cada problema aparece e o Anexo E junta-as por tema.")
    for tr in D.TRANSVERSAIS:
        titulo(doc, tr["titulo"], 2)
        for p in tr["intro"]:
            par(doc, r(p, tr["etiqueta"]))
        fs = [f for f in fichas_ordenadas() if tr["etiqueta"] in f["etiquetas"]]
        par(doc, "Fichas deste tema: " + ", ".join(f["cod"] for f in fs) + ".")

    for n, nome, fichas in sec[1:-1]:
        doc.add_page_break()
        titulo(doc, f"{n} {nome}", 1)
        for f in fichas:
            ficha(doc, f)

    doc.add_page_break()
    titulo(doc, f"{sec[-1][0]} {sec[-1][1]}", 1)
    par(doc, "Registo dos problemas do regime vigente que o RGAC já resolve, para não se perderem em revisões futuras.")
    for a, b in D.RESOLVIDOS:
        p = doc.add_paragraph()
        rr = p.add_run(a + ". ")
        rr.bold = True
        p.add_run(r(b, "RESOLVIDOS"))

    paisagem(doc)
    quadro_resumo(doc)
    doc.add_page_break()
    anexo_stakeholders(doc)
    doc.add_page_break()
    anexo_lapsos(doc)
    doc.add_page_break()
    anexo_cobertura(doc)
    retrato(doc)
    anexo_etiquetas(doc)
    doc.add_page_break()
    anexo_correspondencia(doc)
    doc.add_page_break()
    titulo(doc, "Registo de alterações", 1)
    t = doc.add_table(rows=1, cols=3)
    bordas(t)
    for i, h in enumerate(["Versão", "Data", "Alterações"]):
        celula(t.rows[0].cells[i], h, negrito=True)
    for v, d, txt in D.REGISTO_ALTERACOES:
        row = t.add_row()
        celula(row.cells[0], v)
        celula(row.cells[1], d)
        celula(row.cells[2], txt)
    larguras(t, [2.2, 2.5, 11.3])

    G1.bibliografia(doc)
    G1.rodape_paginas(doc)
    G1.ordenar_tblpr(doc)
    zoom = doc.settings.element.find(qn("w:zoom"))
    if zoom is not None and zoom.get(qn("w:percent")) is None:
        zoom.set(qn("w:percent"), "100")
    doc.save(SAIDA)
    print("Gerado:", SAIDA)
    print("Próximos códigos livres:", proximos_codigos())


if __name__ == "__main__":
    gerar()
