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
    for tema in (D.TEMA_T, D.TEMA_C):
        ver(tema["titulo"], "tema")
        for p in tema["intro"]:
            ver(p, tema["titulo"])
        for f in tema["fichas"]:
            if f["cod"] in codigos:
                erros.append(f"Código repetido: {f['cod']}")
            codigos.add(f["cod"])
            if f["origem"] not in D.ORIGENS:
                erros.append(f"{f['cod']}: origem inválida {f['origem']}")
            if f["estado"] not in D.ESTADOS:
                erros.append(f"{f['cod']}: estado inválido {f['estado']}")
            for campo in ("titulo", "proposta"):
                ver(f[campo], f"{f['cod']}.{campo}")
            for x in f["onde"] + f["problema"] + f["levantado"]:
                ver(x, f["cod"])
    for f in D.TEMA_T["fichas"] + D.TEMA_C["fichas"]:
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
    for row in tabela.rows:
        for i, c in enumerate(row.cells):
            c.width = Cm(cms[i])


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
    for sec in doc.sections:
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
    entradas = [
        ("1.", "Como ler este memorando", []),
        ("2.", D.TEMA_T["titulo"], D.TEMA_T["fichas"]),
        ("3.", D.TEMA_C["titulo"], D.TEMA_C["fichas"]),
        ("4.", "Pontos já resolvidos no RGAC", []),
        ("Anexo A.", "Quadro-resumo das fichas", []),
        ("Anexo B.", "Posições de entidades externas", []),
        ("Anexo C.", "Fontes", []),
        ("", "Registo de alterações", []),
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
    for f in D.TEMA_T["fichas"] + D.TEMA_C["fichas"]:
        r = t.add_row()
        celula(r.cells[0], f["cod"])
        celula(r.cells[1], f["titulo"])
        celula(r.cells[2], f["onde"][0])
        celula(r.cells[3], curtas[f["origem"]])
        celula(r.cells[4], f["estado"])
    larguras(t, [1.5, 5.5, 4.0, 2.7, 2.3])
    doc.add_paragraph()
    abertas = sum(1 for f in D.TEMA_T["fichas"] + D.TEMA_C["fichas"] if f["estado"] == "Aberto")
    total = len(D.TEMA_T["fichas"]) + len(D.TEMA_C["fichas"])
    par(doc, f"Total: {total} fichas, das quais {abertas} em aberto.")


def anexo_stakeholders(doc):
    titulo(doc, "Anexo B. Posições de entidades externas", 1)
    par(doc, "Posições públicas e contributos recolhidos sobre os dois temas deste memorando. As citações "
             "estão entre aspas e foram transcritas das fontes indicadas. Tema T: titular, detentor, "
             "proprietário e operador. Tema C: CED, colónias e animais errantes.")
    if not D.STAKEHOLDERS:
        par(doc, "Por preencher.")
        return
    grupos = {}
    for s in D.STAKEHOLDERS:
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
    larguras(t, [3.2, 1.2, 7.6, 4.0])


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
    par(doc, "Origem do problema:", depois=2)
    for v in D.ORIGENS.values():
        q = par(doc, v + ".", depois=1)
        q.paragraph_format.left_indent = Cm(0.8)

    for n, tema in (("2", D.TEMA_T), ("3", D.TEMA_C)):
        doc.add_page_break()
        titulo(doc, f"{n}. {tema['titulo']}", 1)
        for p in tema["intro"]:
            par(doc, p)
        for f in tema["fichas"]:
            ficha(doc, f)

    doc.add_page_break()
    titulo(doc, "4. Pontos já resolvidos no RGAC", 1)
    par(doc, "Registo dos problemas do regime vigente que o RGAC já resolve, para não se perderem em revisões futuras.")
    for a, b in D.RESOLVIDOS:
        p = doc.add_paragraph()
        r = p.add_run(a + ". ")
        r.bold = True
        p.add_run(b)

    doc.add_page_break()
    quadro_resumo(doc)
    doc.add_page_break()
    anexo_stakeholders(doc)
    doc.add_page_break()
    titulo(doc, "Anexo C. Fontes", 1)
    for f in D.FONTES:
        par(doc, f, depois=3)
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

    rodape_paginas(doc)
    doc.save(SAIDA)
    print("Gerado:", SAIDA)


if __name__ == "__main__":
    gerar()
