#!/usr/bin/env python3
"""
Gera documento Word comparativo com PREÂMBULO
Reutiliza estética e estrutura de gerar_word.py
Adiciona seção de preâmbulo após os artigos
"""

import os
import sys
from docx import Document
from docx.shared import Pt, Cm

# Importar tudo de gerar_word.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_word import (
    add_page_title, add_legenda, add_article_section,
    cell_header, cell_body, set_table_width, remove_table_borders,
    set_cell_bg, set_cell_borders, add_run_styled,
    hex_to_rgb
)
from gerar_comparativo_reuniao import ARTIGOS, COR
from gerar_html_com_preamb_v2 import extrair_preamb, TEMA_CONSIDERANDOS

# Extrair dados
ARTIGOS_DATA = ARTIGOS
preamb, preamb_por_tema = extrair_preamb()
TEMAS_ORDEM = list(TEMA_CONSIDERANDOS.keys())

# ─────────────────────────────────────────────────────────────────────────────
# CRIAR DOCUMENTO
# ─────────────────────────────────────────────────────────────────────────────
doc = Document()

# Setup de margens
section = doc.sections[0]
section.top_margin = Cm(1.5)
section.bottom_margin = Cm(1.5)
section.left_margin = Cm(2)
section.right_margin = Cm(2)

# ── PÁGINA 1: TÍTULO ──────────────────────────────────────────────────────────
add_page_title(doc)
add_legenda(doc)

# ── ARTIGOS ────────────────────────────────────────────────────────────────────
for art in ARTIGOS_DATA:
    add_article_section(doc, art)

# ── PÁGINA 2: PREÂMBULO ────────────────────────────────────────────────────────
doc.add_page_break()

# Cabeçalho do preâmbulo (similar ao cabeçalho de artigos)
t_preamb_title = doc.add_table(rows=1, cols=1)
set_table_width(t_preamb_title, pct=5000)
remove_table_borders(t_preamb_title)
cell_preamb = t_preamb_title.cell(0, 0)
set_cell_bg(cell_preamb, "1A1A2E")
set_cell_borders(cell_preamb, "1A1A2E")
p_preamb = cell_preamb.paragraphs[0]
p_preamb.alignment = 1  # Center
p_preamb.paragraph_format.space_before = Pt(14)
p_preamb.paragraph_format.space_after = Pt(14)
add_run_styled(p_preamb, "PREÂMBULO — Considerandos do Regulamento 2023/0447",
               bold=True, font_size=16, color_hex="FFFFFF")

doc.add_paragraph().paragraph_format.space_after = Pt(8)

# ── TEMAS DO PREÂMBULO ──────────────────────────────────────────────────────
for tema in TEMAS_ORDEM:
    considerandos = preamb_por_tema.get(tema, [])
    if not considerandos:
        continue
    
    # Cabeçalho do tema
    t_tema = doc.add_table(rows=1, cols=1)
    set_table_width(t_tema, pct=5000)
    remove_table_borders(t_tema)
    cell_tema = t_tema.cell(0, 0)
    set_cell_bg(cell_tema, "2C3E6B")
    set_cell_borders(cell_tema, "2C3E6B")
    p_tema = cell_tema.paragraphs[0]
    p_tema.paragraph_format.space_before = Pt(6)
    p_tema.paragraph_format.space_after = Pt(6)
    p_tema.paragraph_format.left_indent = Pt(10)
    add_run_styled(p_tema, tema, bold=True, font_size=11, color_hex="7EC8E3")
    
    # Considerandos deste tema
    for cons in considerandos:
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
        
        # Considerando EN
        t_cons_en = doc.add_table(rows=2, cols=1)
        set_table_width(t_cons_en, pct=5000)
        ref = f"Considerando {cons['numero']} — EN"
        cell_header(t_cons_en.cell(0, 0), ref, COR["regulamento_header"])
        cell_body(t_cons_en.cell(1, 0),
                 cons['regulamento']['texto'],
                 COR["regulamento_body"],
                 font_size=9)
        
        # Considerando PT
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
        t_cons_pt = doc.add_table(rows=2, cols=1)
        set_table_width(t_cons_pt, pct=5000)
        cell_header(t_cons_pt.cell(0, 0),
                   f"Considerando {cons['numero']} — PT",
                   "2471A3")
        cell_body(t_cons_pt.cell(1, 0),
                 cons['regulamento']['traducao'],
                 COR["regulamento_trad"],
                 font_size=9,
                 italic=True)
        
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

# Salvar
filename = 'comparativo_reuniao_exemplo_preamb.docx'
doc.save(filename)
print(f"✅ {filename}")
print(f"   - {len(ARTIGOS_DATA)} artigos")
print(f"   - {len(TEMAS_ORDEM)} temas de preâmbulo")
print(f"   - Estética: IDÊNTICA ao comparativo_reuniao_exemplo.docx")
