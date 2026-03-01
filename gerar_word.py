"""
Gera documento Word (.docx) comparativo artigo a artigo — visualmente fiel ao HTML.
Lê os dados de gerar_comparativo_reuniao.py e produz comparativo_reuniao_exemplo.docx
"""

import os
import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Twips
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

# Importar dados do script existente
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_comparativo_reuniao import ARTIGOS, COR

# ---------------------------------------------------------------------------
# UTILITÁRIOS DE COR E ESTILO
# ---------------------------------------------------------------------------

def hex_to_rgb(hex_str):
    """Converte string hex (sem #) para tuplo (R, G, B)."""
    h = hex_str.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def set_cell_bg(cell, hex_color):
    """Define cor de fundo de uma célula de tabela."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color.lstrip("#"))
    tcPr.append(shd)


def set_cell_borders(cell, color="CCCCCC"):
    """Define bordas finas em todas as faces da célula."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement("w:tcBorders")
    for side in ("top", "left", "bottom", "right"):
        border = OxmlElement(f"w:{side}")
        border.set(qn("w:val"), "single")
        border.set(qn("w:sz"), "4")
        border.set(qn("w:space"), "0")
        border.set(qn("w:color"), color)
        tcBorders.append(border)
    tcPr.append(tcBorders)


def set_cell_vertical_align(cell, align="top"):
    """Define alinhamento vertical da célula."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    vAlign = OxmlElement("w:vAlign")
    vAlign.set(qn("w:val"), align)
    tcPr.append(vAlign)


def add_run_styled(paragraph, text, bold=False, italic=False,
                   font_name="Calibri", font_size=10,
                   color_hex=None):
    """Adiciona run com estilo completo ao parágrafo."""
    run = paragraph.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.name = font_name
    run.font.size = Pt(font_size)
    if color_hex:
        r, g, b = hex_to_rgb(color_hex)
        run.font.color.rgb = RGBColor(r, g, b)
    return run


def remove_table_borders(table):
    """Remove bordas externas da tabela (deixa apenas bordas de células)."""
    tbl = table._tbl
    tblPr = tbl.find(qn("w:tblPr"))
    if tblPr is None:
        tblPr = OxmlElement("w:tblPr")
        tbl.insert(0, tblPr)
    tblBorders = OxmlElement("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        b = OxmlElement(f"w:{side}")
        b.set(qn("w:val"), "none")
        b.set(qn("w:sz"), "0")
        b.set(qn("w:space"), "0")
        b.set(qn("w:color"), "auto")
        tblBorders.append(b)
    existing = tblPr.find(qn("w:tblBorders"))
    if existing is not None:
        tblPr.remove(existing)
    tblPr.append(tblBorders)


def set_table_width(table, width_cm=None, pct=None):
    """Define largura da tabela (cm ou percentagem 0-5000)."""
    tbl = table._tbl
    tblPr = tbl.find(qn("w:tblPr"))
    if tblPr is None:
        tblPr = OxmlElement("w:tblPr")
        tbl.insert(0, tblPr)
    tblW = OxmlElement("w:tblW")
    if pct is not None:
        tblW.set(qn("w:w"), str(pct))
        tblW.set(qn("w:type"), "pct")
    elif width_cm is not None:
        tblW.set(qn("w:w"), str(int(width_cm * 567)))
        tblW.set(qn("w:type"), "dxa")
    existing = tblPr.find(qn("w:tblW"))
    if existing is not None:
        tblPr.remove(existing)
    tblPr.append(tblW)


def set_col_width(col_cells, width_cm):
    """Define largura de coluna via primeira célula."""
    for cell in col_cells:
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        tcW = OxmlElement("w:tcW")
        tcW.set(qn("w:w"), str(int(width_cm * 567)))
        tcW.set(qn("w:type"), "dxa")
        existing = tcPr.find(qn("w:tcW"))
        if existing is not None:
            tcPr.remove(existing)
        tcPr.append(tcW)


def cell_header(cell, text, bg_hex, text_hex="FFFFFF",
                font_size=9, bold=True, align="center"):
    """Preenche célula como cabeçalho colorido."""
    set_cell_bg(cell, bg_hex)
    set_cell_borders(cell)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if align == "center" else WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    add_run_styled(p, text, bold=bold, font_size=font_size, color_hex=text_hex)


def cell_body(cell, text, bg_hex, ref_text=None,
              font_size=9.5, bold=False, italic=False,
              text_hex="222222"):
    """Preenche célula como corpo de conteúdo com texto verbatim."""
    set_cell_bg(cell, bg_hex)
    set_cell_borders(cell)
    set_cell_vertical_align(cell, "top")
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.left_indent = Pt(4)
    p.paragraph_format.right_indent = Pt(4)
    if ref_text:
        add_run_styled(p, ref_text + "\n", bold=True, font_size=8,
                       color_hex="555555", italic=True)
    # Texto verbatim — preserva parágrafos internos
    paragraphs = text.split("\n\n")
    for i, para in enumerate(paragraphs):
        if i == 0:
            add_run_styled(p, para.strip(), bold=bold, italic=italic,
                           font_size=font_size, color_hex=text_hex)
        else:
            new_p = OxmlElement("w:p")
            cell._tc.append(new_p)
            from docx.text.paragraph import Paragraph
            new_para = Paragraph(new_p, cell)
            new_para.paragraph_format.space_before = Pt(6)
            new_para.paragraph_format.space_after = Pt(0)
            new_para.paragraph_format.left_indent = Pt(4)
            add_run_styled(new_para, para.strip(), bold=bold, italic=italic,
                           font_size=font_size, color_hex=text_hex)


# ---------------------------------------------------------------------------
# SECÇÕES DO DOCUMENTO
# ---------------------------------------------------------------------------

def add_page_title(doc):
    """Adiciona página de título / cabeçalho do documento."""
    # Bloco de título com fundo escuro (simulado via tabela 1x1)
    t = doc.add_table(rows=1, cols=1)
    set_table_width(t, pct=5000)
    cell = t.cell(0, 0)
    set_cell_bg(cell, "1A1A2E")
    set_cell_borders(cell, "1A1A2E")
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    add_run_styled(p, "Comparativo Artigo a Artigo", bold=True,
                   font_size=16, color_hex="FFFFFF")
    p2 = cell.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_before = Pt(2)
    p2.paragraph_format.space_after = Pt(14)
    add_run_styled(p2, "Regulamento 2023/0447 — Cães e Gatos",
                   bold=False, font_size=11, color_hex="7EC8E3")
    doc.add_paragraph()  # espaço


def add_legenda(doc):
    """Adiciona tabela de legenda das cores."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    add_run_styled(p, "LEGENDA DO SISTEMA DE CORES", bold=True,
                   font_size=9, color_hex="4A4A4A")

    legenda = [
        ("@regulamento (texto EN)", COR["regulamento_body"]),
        ("@regulamento (tradução PT)", COR["regulamento_trad"]),
        ("@rgbeac (proposta jun. 2025)", COR["rgbeac_body"]),
        ("@codigo (DL n.º 214/2013)", COR["codigo_body"]),
        ("@legislacao (legislação vigente)", COR["legislacao_body"]),
        ("Divergência face ao Regulamento", COR["divergencia_body"]),
        ("Notas de Reunião", COR["notas_body"]),
    ]
    t = doc.add_table(rows=len(legenda), cols=2)
    set_table_width(t, pct=2500)
    for i, (label, cor) in enumerate(legenda):
        c0 = t.cell(i, 0)
        c1 = t.cell(i, 1)
        set_cell_bg(c0, cor)
        set_cell_bg(c1, cor)
        set_cell_borders(c0)
        set_cell_borders(c1)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(3)
        p0.paragraph_format.space_after = Pt(3)
        p0.paragraph_format.left_indent = Pt(6)
        add_run_styled(p0, label, bold=True, font_size=9, color_hex="222222")
    doc.add_paragraph()


def add_article_section(doc, art):
    """Adiciona secção completa de um artigo."""

    # ── Cabeçalho do Artigo ──────────────────────────────────────────────
    t_badge = doc.add_table(rows=1, cols=2)
    set_table_width(t_badge, pct=5000)
    remove_table_borders(t_badge)

    c_id = t_badge.cell(0, 0)
    set_cell_bg(c_id, "1A1A2E")
    set_cell_borders(c_id, "1A1A2E")
    p_id = c_id.paragraphs[0]
    p_id.paragraph_format.space_before = Pt(8)
    p_id.paragraph_format.space_after = Pt(8)
    p_id.paragraph_format.left_indent = Pt(10)
    add_run_styled(p_id, art["id"], bold=True, font_size=11, color_hex="FFFFFF")

    c_tema = t_badge.cell(0, 1)
    set_cell_bg(c_tema, "2C3E6B")
    set_cell_borders(c_tema, "2C3E6B")
    p_tema = c_tema.paragraphs[0]
    p_tema.paragraph_format.space_before = Pt(8)
    p_tema.paragraph_format.space_after = Pt(8)
    p_tema.paragraph_format.left_indent = Pt(10)
    add_run_styled(p_tema, art["tema"], bold=True, font_size=11, color_hex="7EC8E3")

    # ── Tabela 4 colunas: Regulamento | RGBEAC | Código | Legislação vigente ──
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    t3 = doc.add_table(rows=2, cols=4)
    set_table_width(t3, pct=5000)

    # Cabeçalhos
    cell_header(t3.cell(0, 0), "@regulamento (texto original EN)",
                COR["regulamento_header"])
    cell_header(t3.cell(0, 1), "@rgbeac (proposta jun. 2025)",
                COR["rgbeac_header"])
    cell_header(t3.cell(0, 2), "@codigo (DL n.º 214/2013)",
                COR["codigo_header"])
    cell_header(t3.cell(0, 3), "@legislacao (legislação vigente)",
                COR["legislacao_header"])

    # Corpos
    cell_body(t3.cell(1, 0),
              art["regulamento"]["texto"],
              COR["regulamento_body"],
              ref_text=art["regulamento"]["ref"])
    cell_body(t3.cell(1, 1),
              art["rgbeac"]["texto"],
              COR["rgbeac_body"],
              ref_text=art["rgbeac"]["ref"])
    cell_body(t3.cell(1, 2),
              art["codigo"]["texto"],
              COR["codigo_body"],
              ref_text=art["codigo"]["ref"])
    cell_body(t3.cell(1, 3),
              art["legislacao"]["texto"],
              COR["legislacao_body"],
              ref_text=art["legislacao"]["ref"])

    # ── Tradução do Regulamento ───────────────────────────────────────────
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    t_trad = doc.add_table(rows=2, cols=1)
    set_table_width(t_trad, pct=5000)
    cell_header(t_trad.cell(0, 0),
                "Tradução do @regulamento (PT-PT)",
                "2471A3")
    cell_body(t_trad.cell(1, 0),
              art["regulamento"]["traducao"],
              COR["regulamento_trad"],
              italic=True)

    # ── Divergência ───────────────────────────────────────────────────────
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    t_div = doc.add_table(rows=2, cols=1)
    set_table_width(t_div, pct=5000)
    cell_header(t_div.cell(0, 0),
                f"DIVERGÊNCIA FACE AO REGULAMENTO  ·  Necessidade de alteração: {art['necessidade_alteracao']}",
                COR["divergencia_header"])
    cell_body(t_div.cell(1, 0),
              art["divergencia"],
              COR["divergencia_body"],
              bold=True, text_hex="3D1A6E")

    # ── Notas de Reunião ──────────────────────────────────────────────────
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    t_notas = doc.add_table(rows=2, cols=1)
    set_table_width(t_notas, pct=5000)
    cell_header(t_notas.cell(0, 0),
                "NOTAS DE REUNIÃO",
                COR["notas_header"])
    # Célula com espaço em branco para preenchimento manual
    c_notas = t_notas.cell(1, 0)
    set_cell_bg(c_notas, COR["notas_body"])
    set_cell_borders(c_notas)
    notas_text = art["notas"] if art["notas"] else "(espaço para anotações da reunião)"
    p_notas = c_notas.paragraphs[0]
    p_notas.paragraph_format.space_before = Pt(6)
    p_notas.paragraph_format.space_after = Pt(40)  # altura mínima para escrita
    p_notas.paragraph_format.left_indent = Pt(4)
    add_run_styled(p_notas, notas_text, italic=True,
                   font_size=9.5, color_hex="888888" if not art["notas"] else "222222")

    # Separador entre artigos
    doc.add_paragraph()
    p_sep = doc.add_paragraph()
    p_sep.paragraph_format.space_before = Pt(0)
    p_sep.paragraph_format.space_after = Pt(16)
    run_sep = p_sep.add_run("─" * 80)
    run_sep.font.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)
    run_sep.font.size = Pt(8)


# ---------------------------------------------------------------------------
# CONFIGURAÇÃO DO DOCUMENTO
# ---------------------------------------------------------------------------

def configurar_documento(doc):
    """Define margens e estilos base do documento."""
    from docx.oxml.ns import nsmap
    section = doc.sections[0]
    section.page_width = Cm(29.7)   # A4 horizontal
    section.page_height = Cm(21.0)
    section.left_margin = Cm(1.5)
    section.right_margin = Cm(1.5)
    section.top_margin = Cm(1.5)
    section.bottom_margin = Cm(1.5)

    # Estilo normal base
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(10)


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def criar_word(path):
    doc = Document()
    configurar_documento(doc)

    # Capa / título
    add_page_title(doc)

    # Legenda de cores
    add_legenda(doc)

    # Quebra de página antes dos artigos
    doc.add_page_break()

    # Um artigo por página (exceto o último)
    for i, art in enumerate(ARTIGOS):
        add_article_section(doc, art)
        if i < len(ARTIGOS) - 1:
            doc.add_page_break()

    doc.save(path)
    print(f"Word guardado: {path}")


if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(base, "comparativo_reuniao_exemplo.docx")
    criar_word(output)
    print("Concluído.")
