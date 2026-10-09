# -*- coding: utf-8 -*-
"""
Gera o Memorando de acompanhamento do RGAC (Word) a partir de dados_memorando_rgac.py.

Uso (a partir da raiz do repositorio):
    python3 memorando_rgac/gerar_memorando_rgac.py

Saida: memorando_rgac/Memorando_Acompanhamento_RGAC.docx
Requer: python-docx (pip install python-docx)

Estilo: preto sobre branco, Arial, sem cores, sem italico, sem travessoes longos.
O script recusa gerar o documento se encontrar travessoes longos no texto.
"""
import os
import sys
import importlib.util

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
SAIDA = os.path.join(AQUI, "Memorando_Acompanhamento_RGAC.docx")

spec = importlib.util.spec_from_file_location("dados", os.path.join(AQUI, "dados_memorando_rgac.py"))
D = importlib.util.module_from_spec(spec)
spec.loader.exec_module(D)

PRETO = RGBColor(0, 0, 0)
FONTE = "Arial"
PROIBIDOS = ["—", "–"]  # travessao e meia-risca


# ------------------------------------------------------------------ verificacoes
def verificar_texto():
    erros = []

    def ver(txt, onde):
        for c in PROIBIDOS:
            if c in txt:
                erros.append(f"{onde}: contém '{c}' -> «{txt[:80]}»")

    ver(D.VERSAO_RGAC, "VERSAO_RGAC")
    for i, p in enumerate(D.INTRODUCAO):
        ver(p, f"INTRODUCAO[{i}]")
    codigos = set()
    letras = set()
    for tema in D.TEMAS:
        if tema["letra"] in letras or tema["letra"] == "L":
            erros.append(f"Letra de tema repetida ou reservada: {tema['letra']}")
        letras.add(tema["letra"])
        ver(tema["titulo"], "tema")
        for p in tema["intro"]:
            ver(p, tema["titulo"])
        for f in tema["fichas"]:
            if f["cod"] in codigos:
                erros.append(f"Código repetido: {f['cod']}")
            if not f["cod"].startswith(tema["letra"] + "-"):
                erros.append(f"{f['cod']}: código não começa pela letra do tema {tema['letra']}")
            codigos.add(f["cod"])
            if f["origem"] not in D.ORIGENS:
                erros.append(f"{f['cod']}: origem inválida {f['origem']}")
            if f["estado"] not in D.ESTADOS:
                erros.append(f"{f['cod']}: estado inválido {f['estado']}")
            for campo in ("titulo", "proposta"):
                ver(f[campo], f"{f['cod']}.{campo}")
            for x in f["onde"] + f["problema"] + f["levantado"]:
                ver(x, f["cod"])
    for s in D.STAKEHOLDERS:
        if e_imprensa(s[5]):
            erros.append(f"Anexo B com fonte de imprensa: {s[1]} ({s[5][:60]})")
    biblio = {b[2] for b in D.BIBLIOGRAFIA}
    for s in D.STAKEHOLDERS:
        if s[5] not in biblio:
            erros.append(f"Fonte do Anexo B fora da bibliografia: {s[1]} ({s[5][:60]})")
    for b in D.BIBLIOGRAFIA:
        ver(b[1], "BIBLIOGRAFIA")
        if b[2].startswith("repositório: "):
            if not os.path.exists(os.path.join(RAIZ, b[2][len("repositório: "):])):
                erros.append(f"Ficheiro do repositório inexistente: {b[2]}")
        elif not b[2].startswith("http"):
            erros.append(f"Ligação inválida na bibliografia: {b[2]}")
    chaves = {a["chave"] for a in estrutura()}
    lcod = set()
    for l in D.LAPSOS:
        if l["cod"] in lcod or not l["cod"].startswith("L-"):
            erros.append(f"Lapso com código repetido ou inválido: {l['cod']}")
        lcod.add(l["cod"])
        if l["estado"] not in D.ESTADOS:
            erros.append(f"{l['cod']}: estado inválido {l['estado']}")
        for k in l["onde"]:
            if k not in chaves:
                erros.append(f"{l['cod']}: artigo inexistente {k}")
        if l["ficha"] and l["ficha"] not in codigos:
            erros.append(f"{l['cod']}: ficha inexistente {l['ficha']}")
        ver(l["lapso"] + l["correcao"], l["cod"])
    for k, v in D.REVISAO.items():
        if k not in chaves:
            erros.append(f"REVISAO: artigo inexistente {k}")
        if v.get("estado") not in D.ESTADOS_REVISAO:
            erros.append(f"REVISAO {k}: estado inválido {v.get('estado')}")
        if v.get("regulamento", "A verificar") not in D.ESTADOS_REGULAMENTO:
            erros.append(f"REVISAO {k}: valor inválido em regulamento")
        ver(v.get("nota", ""), f"REVISAO {k}")
    for f in todas_fichas():
        for x in f["levantado"]:
            if "imprensa" in x:
                erros.append(f"{f['cod']}: referência de imprensa em levantado -> {x[:60]}")
        for r in f.get("rel", []):
            if r not in codigos:
                erros.append(f"{f['cod']}: ficha relacionada inexistente {r}")
    for s in D.STAKEHOLDERS:
        for x in s:
            ver(str(x), "STAKEHOLDERS")
    for a, b in D.RESOLVIDOS:
        ver(a + b, "RESOLVIDOS")
    if erros:
        print("ERROS no ficheiro de dados:")
        for e in erros:
            print("  -", e)
        sys.exit(1)


# ------------------------------------------------------------------ estrutura e temas
import json
import re as _re


def estrutura():
    with open(os.path.join(AQUI, "estrutura_rgac.json"), encoding="utf-8") as f:
        e = json.load(f)
    if e["ficheiro"] != D.FICHEIRO_RGAC:
        print("AVISO: estrutura_rgac.json foi extraída de outro ficheiro. Correr extrair_estrutura_rgac.py.")
        sys.exit(1)
    return e["artigos"]


def todas_fichas():
    return [f for tema in D.TEMAS for f in tema["fichas"]]


def temas_com_fichas():
    return [t for t in D.TEMAS if t["fichas"]]


def artigos_citados(textos):
    """Números de artigo do RGAC citados em referências «art. N.º» (sem nome de outro diploma)."""
    nums = set()
    for x in textos:
        if _re.search(r"\b(DL|Lei|Portaria|Código|Regulamento)\b", x):
            continue
        for m in _re.finditer(r"arts?\.\s*(\d+)\.º(?:\s*(?:,|e)\s*(\d+)\.º)*", x):
            for n in _re.findall(r"(\d+)\.º", m.group(0)):
                nums.add(n)
    return nums


# ------------------------------------------------------------------ utilitarios
def estilo_base(doc):
    st = doc.styles["Normal"]
    st.font.name = FONTE
    st.font.size = Pt(11)
    st.font.color.rgb = PRETO
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONTE)
    st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.line_spacing = 1.15
    for nome, tam in (("Title", 20), ("Heading 1", 15), ("Heading 2", 12), ("Heading 3", 11)):
        s = doc.styles[nome]
        s.font.name = FONTE
        s.font.size = Pt(tam)
        s.font.bold = True
        s.font.italic = False
        s.font.color.rgb = PRETO
        rpr = s.element.get_or_add_rPr()
        rpr.get_or_add_rFonts().set(qn("w:ascii"), FONTE)
        rpr.get_or_add_rFonts().set(qn("w:hAnsi"), FONTE)
        s.paragraph_format.space_before = Pt(12 if nome != "Heading 3" else 6)
        s.paragraph_format.space_after = Pt(6)
    for sec in doc.sections:
        sec.page_height = Cm(29.7)
        sec.page_width = Cm(21.0)
        sec.left_margin = sec.right_margin = Cm(2.5)
        sec.top_margin = sec.bottom_margin = Cm(2.2)


def par(doc, texto, negrito=False, alinh=None, tam=None, antes=None, depois=None):
    p = doc.add_paragraph()
    r = p.add_run(texto)
    r.bold = negrito
    r.italic = False
    if tam:
        r.font.size = Pt(tam)
    if alinh:
        p.alignment = alinh
    if antes is not None:
        p.paragraph_format.space_before = Pt(antes)
    if depois is not None:
        p.paragraph_format.space_after = Pt(depois)
    return p


def titulo(doc, texto, nivel):
    h = doc.add_heading(texto, level=nivel)
    for r in h.runs:
        r.font.color.rgb = PRETO
        r.italic = False
    return h


def bordas(tabela):
    tbl = tabela._tbl
    tblPr = tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for lado in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{lado}")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "4")
        e.set(qn("w:space"), "0")
        e.set(qn("w:color"), "000000")
        b.append(e)
    tblPr.append(b)


def larguras(tabela, cms):
    """Fixa as larguras das colunas de forma que o Word as respeite:
    largura total da tabela, grelha de colunas, layout fixo e largura de cada celula."""
    tabela.autofit = False
    tbl = tabela._tbl
    tblPr = tbl.tblPr
    total = sum(cms)
    for tag in ("w:tblW", "w:tblLayout"):
        for e in tblPr.findall(qn(tag)):
            tblPr.remove(e)
    w = OxmlElement("w:tblW")
    w.set(qn("w:w"), str(int(Cm(total).twips)))
    w.set(qn("w:type"), "dxa")
    tblPr.append(w)
    lay = OxmlElement("w:tblLayout")
    lay.set(qn("w:type"), "fixed")
    tblPr.append(lay)
    grid = tbl.tblGrid
    cols = grid.findall(qn("w:gridCol"))
    for i, gc in enumerate(cols):
        if i < len(cms):
            gc.set(qn("w:w"), str(int(Cm(cms[i]).twips)))
    for row in tabela.rows:
        idx = 0
        for tc in row._tr.tc_lst:
            span = tc.grid_span
            largura = sum(cms[idx:idx + span])
            tcPr = tc.get_or_add_tcPr()
            for e in tcPr.findall(qn("w:tcW")):
                tcPr.remove(e)
            tcw = OxmlElement("w:tcW")
            tcw.set(qn("w:w"), str(int(Cm(largura).twips)))
            tcw.set(qn("w:type"), "dxa")
            tcPr.insert(0, tcw)
            idx += span


def celula(c, textos, negrito=False):
    c.text = ""
    if isinstance(textos, str):
        textos = [textos]
    for i, t in enumerate(textos):
        p = c.paragraphs[0] if i == 0 else c.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(t)
        r.bold = negrito
        r.font.size = Pt(10)


def cabecalho_tabela(row):
    tr = row._tr
    trPr = tr.get_or_add_trPr()
    e = OxmlElement("w:tblHeader")
    e.set(qn("w:val"), "true")
    trPr.append(e)


def rodape_paginas(doc):
    # As secções seguintes herdam o rodapé da primeira (ligação à anterior).
    for sec in doc.sections[:1]:
        p = sec.footer.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("Memorando de acompanhamento do RGAC, versão " + D.VERSAO_MEMORANDO + ". Página ")
        r.font.size = Pt(8)
        for tipo, txt in (("begin", None), (None, "PAGE"), ("end", None)):
            run = p.add_run()
            run.font.size = Pt(8)
            if tipo:
                fc = OxmlElement("w:fldChar")
                fc.set(qn("w:fldCharType"), tipo)
                run._r.append(fc)
            else:
                it = OxmlElement("w:instrText")
                it.set(qn("xml:space"), "preserve")
                it.text = txt
                run._r.append(it)


ORDEM_TBLPR = ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual", "tblStyleRowBandSize",
               "tblStyleColBandSize", "tblW", "jc", "tblCellSpacing", "tblInd", "tblBorders",
               "shd", "tblLayout", "tblCellMar", "tblLook", "tblCaption", "tblDescription"]


def ordenar_tblpr(doc):
    """O Word ignora propriedades de tabela fora da ordem do esquema (ex.: largura e layout fixo
    depois de tblLook). Reordena os filhos de w:tblPr de todas as tabelas."""
    for tbl in doc.element.body.iter(qn("w:tbl")):
        tblPr = tbl.find(qn("w:tblPr"))
        if tblPr is None:
            continue
        filhos = list(tblPr)
        pos = {qn("w:" + n): i for i, n in enumerate(ORDEM_TBLPR)}
        filhos.sort(key=lambda e: pos.get(e.tag, 99))
        for e in list(tblPr):
            tblPr.remove(e)
        for e in filhos:
            tblPr.append(e)


def paisagem(doc):
    from docx.enum.section import WD_SECTION, WD_ORIENT
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    s.orientation = WD_ORIENT.LANDSCAPE
    s.page_width, s.page_height = Cm(29.7), Cm(21.0)
    s.left_margin = s.right_margin = Cm(2.0)
    s.top_margin = s.bottom_margin = Cm(2.0)


def retrato(doc):
    from docx.enum.section import WD_SECTION, WD_ORIENT
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    s.orientation = WD_ORIENT.PORTRAIT
    s.page_width, s.page_height = Cm(21.0), Cm(29.7)
    s.left_margin = s.right_margin = Cm(2.5)
    s.top_margin = s.bottom_margin = Cm(2.2)


# ------------------------------------------------------------------ blocos
def ficha(doc, f):
    titulo(doc, f"{f['cod']}. {f['titulo']}", 2)
    linhas = [
        ("Onde", "; ".join(f["onde"])),
        ("Origem", D.ORIGENS[f["origem"]]),
        ("Problema", f["problema"]),
        ("Proposta", f["proposta"]),
        ("Quem levantou", "; ".join(f["levantado"])),
        ("Estado", f["estado"]),
    ]
    if f.get("rel"):
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


def indice(doc):
    titulo(doc, "Índice", 1)
    entradas = [("1.", "Como ler este memorando", [])]
    for i, tema in enumerate(temas_com_fichas(), start=2):
        entradas.append((f"{i}.", tema["titulo"], tema["fichas"]))
    entradas += [
        (f"{len(entradas) + 1}.", "Pontos já resolvidos no RGAC", []),
        ("Anexo A.", "Quadro-resumo das fichas", []),
        ("Anexo B.", "Posições de entidades externas", []),
        ("Anexo C.", "Lapsos formais", []),
        ("Anexo D.", "Cobertura da revisão, artigo a artigo", []),
        ("", "Registo de alterações", []),
        ("", "Bibliografia", []),
    ]
    for num, nome, fichas in entradas:
        p = par(doc, (num + " " if num else "") + nome, negrito=True, depois=2)
        for f in fichas:
            q = par(doc, f"{f['cod']}. {f['titulo']}", depois=0)
            q.paragraph_format.left_indent = Cm(1)
        if fichas:
            doc.add_paragraph().paragraph_format.space_after = Pt(2)


def quadro_resumo(doc):
    titulo(doc, "Anexo A. Quadro-resumo das fichas", 1)
    t = doc.add_table(rows=1, cols=5)
    bordas(t)
    cab = ["Código", "Assunto", "Onde", "Origem", "Estado"]
    for i, h in enumerate(cab):
        celula(t.rows[0].cells[i], h, negrito=True)
    cabecalho_tabela(t.rows[0])
    curtas = {"RGAC": "Criado pelo RGAC", "VIGENTE": "Já existia", "PARCIAL": "Resolvido em parte"}
    for f in todas_fichas():
        r = t.add_row()
        celula(r.cells[0], f["cod"])
        celula(r.cells[1], f["titulo"])
        celula(r.cells[2], f["onde"][0])
        celula(r.cells[3], curtas[f["origem"]])
        celula(r.cells[4], f["estado"])
    larguras(t, [1.8, 9.2, 7.0, 4.2, 3.4])
    doc.add_paragraph()
    abertas = sum(1 for f in todas_fichas() if f["estado"] == "Aberto")
    total = len(todas_fichas())
    par(doc, f"Total: {total} fichas, das quais {abertas} em aberto.")


def e_imprensa(fonte):
    return any(d in fonte for d in getattr(D, "DOMINIOS_IMPRENSA", []))


def tabela_stakeholders(doc, entradas, larg):
    grupos = {}
    for s in entradas:
        grupos.setdefault(s[0], []).append(s)
    t = doc.add_table(rows=1, cols=4)
    bordas(t)
    for i, h in enumerate(["Entidade", "Tema", "Posição", "Fonte"]):
        celula(t.rows[0].cells[i], h, negrito=True)
    cabecalho_tabela(t.rows[0])
    for tipo in sorted(grupos):
        r = t.add_row()
        a = r.cells[0].merge(r.cells[3])
        celula(a, tipo, negrito=True)
        for s in grupos[tipo]:
            _, entidade, data, tema, posicao, fonte = s
            r = t.add_row()
            celula(r.cells[0], f"{entidade} ({data})" if data else entidade)
            celula(r.cells[1], tema)
            celula(r.cells[2], posicao)
            celula(r.cells[3], fonte)
    larguras(t, larg)


def anexo_stakeholders(doc):
    titulo(doc, "Anexo B. Posições de entidades externas", 1)
    par(doc, "Posições recolhidas em documentos oficiais, pareceres, estratégias, doutrina, artigos "
             "científicos e decisões judiciais sobre os dois temas deste memorando. Não se usam notícias de imprensa. As citações estão entre "
             "aspas e foram transcritas das fontes indicadas. Tema T: titular, detentor, proprietário e "
             "operador. Tema C: CED, colónias e animais errantes.")
    if not D.STAKEHOLDERS:
        par(doc, "Por preencher.")
        return
    tabela_stakeholders(doc, D.STAKEHOLDERS, [5.0, 1.6, 12.1, 7.0])




def anexo_lapsos(doc):
    titulo(doc, "Anexo C. Lapsos formais", 1)
    par(doc, "Remissões erradas, números repetidos, gralhas e marcas de trabalho no texto. Quando o mesmo ponto "
             "já tem ficha, a correção remete para ela. A coluna Onde usa o número do artigo; «81-b» é a segunda "
             "ocorrência de um número repetido.")
    if not D.LAPSOS:
        par(doc, "Sem lapsos registados.")
        return
    t = doc.add_table(rows=1, cols=5)
    bordas(t)
    for i, h in enumerate(["Código", "Onde", "Lapso", "Correção proposta", "Estado"]):
        celula(t.rows[0].cells[i], h, negrito=True)
    cabecalho_tabela(t.rows[0])
    for l in D.LAPSOS:
        r = t.add_row()
        celula(r.cells[0], l["cod"])
        celula(r.cells[1], ", ".join(f"art. {k}" for k in l["onde"]))
        celula(r.cells[2], l["lapso"])
        celula(r.cells[3], l["correcao"])
        celula(r.cells[4], l["estado"])
    larguras(t, [1.6, 3.0, 11.0, 7.6, 2.5])
    doc.add_paragraph()
    abertos = sum(1 for l in D.LAPSOS if l["estado"] == "Aberto")
    par(doc, f"Total: {len(D.LAPSOS)} lapsos, dos quais {abertos} em aberto.")


def anexo_cobertura(doc):
    titulo(doc, "Anexo D. Cobertura da revisão, artigo a artigo", 1)
    par(doc, "Por rever: o artigo ainda não foi lido com esse fim. Parcial: tem fichas ou lapsos, mas ainda não "
             "foi revisto por inteiro. Em revisão e Revisto: estado indicado pelo grupo. A última coluna diz a "
             "relação com o Regulamento (UE) 2026/1818.")
    arts = estrutura()
    fichas_por, lapsos_por = {}, {}
    for f in todas_fichas():
        for n in artigos_citados(f["onde"]):
            fichas_por.setdefault(n, []).append(f["cod"])
    for l in D.LAPSOS:
        for k in l["onde"]:
            lapsos_por.setdefault(k, []).append(l["cod"])

    def estado(a):
        if a["chave"] in D.REVISAO:
            return D.REVISAO[a["chave"]]["estado"]
        if fichas_por.get(a["chave"]) or lapsos_por.get(a["chave"]):
            return "Parcial"
        return "Por rever"

    # resumo por capítulo
    caps = []
    for a in arts:
        if a["capitulo"] not in caps:
            caps.append(a["capitulo"])
    t = doc.add_table(rows=1, cols=6)
    bordas(t)
    for i, h in enumerate(["Capítulo", "Artigos", "Revistos", "Em revisão", "Parcial", "Por rever"]):
        celula(t.rows[0].cells[i], h, negrito=True)
    cabecalho_tabela(t.rows[0])
    tot = [0, 0, 0, 0, 0]
    for c in caps:
        est = [estado(a) for a in arts if a["capitulo"] == c]
        v = [len(est), est.count("Revisto"), est.count("Em revisão"), est.count("Parcial"), est.count("Por rever")]
        tot = [x + y for x, y in zip(tot, v)]
        r = t.add_row()
        celula(r.cells[0], c)
        for i, x in enumerate(v, start=1):
            celula(r.cells[i], str(x))
    r = t.add_row()
    celula(r.cells[0], "Total", negrito=True)
    for i, x in enumerate(tot, start=1):
        celula(r.cells[i], str(x), negrito=True)
    larguras(t, [6.0, 3.0, 3.0, 3.0, 3.0, 3.0])
    doc.add_paragraph()

    t = doc.add_table(rows=1, cols=6)
    bordas(t)
    for i, h in enumerate(["Artigo", "Epígrafe", "Revisão", "Fichas e lapsos", "Regulamento (UE) 2026/1818", "Nota"]):
        celula(t.rows[0].cells[i], h, negrito=True)
    cabecalho_tabela(t.rows[0])
    cap = None
    for a in arts:
        if a["capitulo"] != cap:
            cap = a["capitulo"]
            r = t.add_row()
            celula(r.cells[0].merge(r.cells[5]), f"{cap}. {a['epigrafe_capitulo']}", negrito=True)
        rv = D.REVISAO.get(a["chave"], {})
        r = t.add_row()
        celula(r.cells[0], f"{a['chave']}.º" if "-" not in a["chave"] else a["chave"])
        celula(r.cells[1], a["epigrafe"])
        e = estado(a)
        celula(r.cells[2], e + (f" ({rv['data']})" if rv.get("data") else ""))
        celula(r.cells[3], ", ".join(fichas_por.get(a["chave"], []) + lapsos_por.get(a["chave"], [])))
        celula(r.cells[4], rv.get("regulamento", "A verificar"))
        celula(r.cells[5], rv.get("nota", ""))
    larguras(t, [1.8, 7.5, 3.2, 4.0, 3.6, 5.6])


def hiperligacao(p, url, texto):
    rid = p.part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
                           is_external=True)
    h = OxmlElement("w:hyperlink")
    h.set(qn("r:id"), rid)
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rpr.append(u)
    r.append(rpr)
    t = OxmlElement("w:t")
    t.text = texto
    t.set(qn("xml:space"), "preserve")
    r.append(t)
    h.append(r)
    p._p.append(h)


def bibliografia(doc):
    titulo(doc, "Bibliografia", 1)
    par(doc, f"Todas as ligações foram verificadas em {D.DATA_LIGACOES}. Os documentos do repositório estão na "
             "pasta do projeto. Os textos legais citados foram confirmados online, na pasta Legislação vigente "
             "e no repositório.")
    grupos = []
    for g, *_ in D.BIBLIOGRAFIA:
        if g not in grupos:
            grupos.append(g)
    for g in grupos:
        titulo(doc, g, 2)
        for gg, ref, lig, _ in D.BIBLIOGRAFIA:
            if gg != g:
                continue
            p = par(doc, ref + " ", depois=4)
            p.paragraph_format.left_indent = Cm(0.8)
            p.paragraph_format.first_line_indent = Cm(-0.8)
            if lig.startswith("http"):
                hiperligacao(p, lig, lig)
            else:
                p.add_run(lig[0].upper() + lig[1:] + ".")


def gerar():
    verificar_texto()
    doc = Document()
    estilo_base(doc)

    par(doc, "Memorando de acompanhamento do RGAC", negrito=True, tam=20, depois=4)
    par(doc, "Problemas identificados no projeto de Regime Geral do Animal de Companhia", tam=12, depois=12)
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
    par(doc, "Letras dos códigos das fichas:", depois=2)
    for tema in D.TEMAS:
        q = par(doc, f"{tema['letra']}: {tema['titulo']}", depois=1)
        q.paragraph_format.left_indent = Cm(0.8)
    q = par(doc, "L: lapsos formais (Anexo C)", depois=1)
    q.paragraph_format.left_indent = Cm(0.8)
    par(doc, "")
    par(doc, "Origem do problema:", depois=2)
    for v in D.ORIGENS.values():
        q = par(doc, v + ".", depois=1)
        q.paragraph_format.left_indent = Cm(0.8)

    for n, tema in enumerate(temas_com_fichas(), start=2):
        doc.add_page_break()
        titulo(doc, f"{n}. {tema['titulo']}", 1)
        for p in tema["intro"]:
            par(doc, p)
        for f in tema["fichas"]:
            ficha(doc, f)

    doc.add_page_break()
    titulo(doc, f"{len(temas_com_fichas()) + 2}. Pontos já resolvidos no RGAC", 1)
    par(doc, "Registo dos problemas do regime vigente que o RGAC já resolve, para não se perderem em revisões futuras.")
    for a, b in D.RESOLVIDOS:
        p = doc.add_paragraph()
        r = p.add_run(a + ". ")
        r.bold = True
        p.add_run(b)

    paisagem(doc)
    quadro_resumo(doc)
    doc.add_page_break()
    anexo_stakeholders(doc)
    doc.add_page_break()
    anexo_lapsos(doc)
    doc.add_page_break()
    anexo_cobertura(doc)
    retrato(doc)
    titulo(doc, "Registo de alterações", 1)
    t = doc.add_table(rows=1, cols=3)
    bordas(t)
    for i, h in enumerate(["Versão", "Data", "Alterações"]):
        celula(t.rows[0].cells[i], h, negrito=True)
    for v, d, txt in D.REGISTO_ALTERACOES:
        r = t.add_row()
        celula(r.cells[0], v)
        celula(r.cells[1], d)
        celula(r.cells[2], txt)
    larguras(t, [1.8, 2.5, 11.7])

    bibliografia(doc)
    rodape_paginas(doc)
    ordenar_tblpr(doc)
    zoom = doc.settings.element.find(qn("w:zoom"))
    if zoom is not None and zoom.get(qn("w:percent")) is None:
        zoom.set(qn("w:percent"), "100")
    doc.save(SAIDA)
    print("Gerado:", SAIDA)


if __name__ == "__main__":
    gerar()
