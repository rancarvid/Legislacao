# -*- coding: utf-8 -*-
"""Gera as notas de apoio à atividade ministerial a partir de `dados_notas.py`.

    python3 notas_ministeriais/gerar_nota.py rgac        # nota temática (8 linhas)
    python3 notas_ministeriais/gerar_nota.py --mensal    # nota mensal (todas as fichas)

Formato conferido contra a nota do Gabinete de 28.08.2026: A4, margens 3 cm
(superior 4,25), Segoe UI, título a 14 pt negrito, tabela «Table Grid» com
coluna de rótulos de 4,18 cm a 12 pt negrito e sombreado D9D9D9 nas quatro
linhas do modelo do Gabinete e D0CECE nas quatro acrescentadas pela DGAV.
"""
import os
import re
import sys
from datetime import date

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
import dados_notas as D  # noqa: E402

PRETO = RGBColor(0, 0, 0)
FUNDO = {"modelo": "D9D9D9", "dgav": "D0CECE"}

MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]


# ───────────────────────── validação ─────────────────────────

def validar(slug, ficha):
    """Devolve a lista de problemas. Com problemas, não se gera."""
    erros = []
    campos = [c for c, _, _ in D.ROTULOS]

    for campo in campos:
        if campo not in ficha:
            erros.append("falta o campo «%s»" % campo)
            continue
        if not ficha[campo]:
            erros.append(
                "o campo «%s» está vazio. Na nota de 28.08.2026 foi precisamente este o campo "
                "deixado em branco, e é o que o Senhor Ministro mais precisa de levar para uma "
                "audição. Preencher antes de gerar." % campo)

    texto = " ".join(p for c in campos if c in ficha for p in ficha[c])

    # as exceções são nomes próprios onde a forma «errada» está certa
    neutro = texto
    for excecao in getattr(D, "EXCECOES_DESIGNACAO", []):
        neutro = neutro.replace(excecao, "")
    for errada, certa in D.DESIGNACOES_PROIBIDAS:
        if errada in neutro:
            erros.append("designação errada: «%s». Usar «%s»." % (errada, certa))

    # frases truncadas: a nota de agosto terminava com «que foi publicado dia»
    for campo in campos:
        for i, par in enumerate(ficha.get(campo, [])):
            p = par.rstrip()
            if p and p[-1] not in ".:;!?»)":
                erros.append("«%s», parágrafo %d: termina sem pontuação final — frase truncada? «…%s»"
                             % (campo, i + 1, p[-45:]))
            if re.search(r"\b(publicado|remetido|aprovado|previsto)\s+(dia|em)\s*$", p):
                erros.append("«%s», parágrafo %d: data em falta." % (campo, i + 1))

    if "—" in texto or "–" in texto:
        pass  # travessões são admitidos nestas notas

    if not ficha.get("tema"):
        erros.append("falta o tema.")
    return erros


# ───────────────────────── construção ─────────────────────────

def _sombrear(celula, cor):
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear")
    sh.set(qn("w:color"), "auto")
    sh.set(qn("w:fill"), cor)
    celula._tc.get_or_add_tcPr().append(sh)


def _escrever(celula, paragrafos, tamanho=11, alinhar=WD_ALIGN_PARAGRAPH.JUSTIFY,
              negrito=False, fonte=None):
    celula.text = ""
    primeiro = celula.paragraphs[0]
    for i, txt in enumerate(paragrafos):
        p = primeiro if i == 0 else celula.add_paragraph()
        marca = txt.startswith("- ")
        if marca:
            txt = txt[2:]
            p.style = celula.part.document.styles["List Bullet"]
        p.alignment = alinhar
        pf = p.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(6)
        r = p.add_run(txt)
        r.font.size = Pt(tamanho)
        r.font.bold = negrito
        r.font.color.rgb = PRETO
        if fonte:
            r.font.name = fonte


def _documento():
    doc = Document()
    s = doc.sections[0]
    s.page_width, s.page_height = Cm(21), Cm(29.7)
    s.left_margin = s.right_margin = s.bottom_margin = Cm(3)
    s.top_margin = Cm(4.25)
    est = doc.styles["Normal"]
    est.font.name = "Segoe UI"
    est.font.size = Pt(11)
    est.font.color.rgb = PRETO
    return doc


def _cabecalho(doc, tema):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run("Notas de apoio à atividade ministerial")
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = PRETO
    doc.add_paragraph()
    p = doc.add_paragraph()
    r = p.add_run("Tema: ")
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = PRETO
    r = p.add_run(tema)
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = PRETO


def _fixar_grelha(tb, larguras_cm):
    """O python-docx não escreve a grelha; sem isto o Word reparte as colunas
    em partes iguais e a nota sai diferente do modelo do Gabinete."""
    tblPr = tb._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    grid = tb._tbl.find(qn("w:tblGrid"))
    if grid is not None:
        tb._tbl.remove(grid)
    grid = OxmlElement("w:tblGrid")
    for cm in larguras_cm:
        col = OxmlElement("w:gridCol")
        col.set(qn("w:w"), str(int(cm * 567)))  # 1 cm = 567 twips
        grid.append(col)
    tb._tbl.insert(list(tb._tbl).index(tblPr) + 1, grid)


def _tabela(doc, ficha, campos):
    linhas = [(c, rot, grupo) for c, rot, grupo in D.ROTULOS if c in campos]
    tb = doc.add_table(rows=len(linhas), cols=2)
    tb.style = "Table Grid"
    tb.alignment = WD_TABLE_ALIGNMENT.LEFT
    tb.autofit = False
    _fixar_grelha(tb, (4.18, 10.82))
    for i, (campo, rotulo, grupo) in enumerate(linhas):
        lin = tb.rows[i]
        lin.cells[0].width = Cm(4.18)
        lin.cells[1].width = Cm(10.82)
        _escrever(lin.cells[0], rotulo.split("\n"), tamanho=12,
                  alinhar=WD_ALIGN_PARAGRAPH.LEFT, negrito=True, fonte="Aptos")
        _sombrear(lin.cells[0], FUNDO[grupo])
        _escrever(lin.cells[1], ficha[campo])
    return tb


# ───────────────────────── saídas ─────────────────────────

def nota_tematica(slug):
    ficha = D.FICHAS[slug]
    erros = validar(slug, ficha)
    if erros:
        print("NÃO GERADO — %d problema(s):" % len(erros))
        for e in erros:
            print("  - " + e)
        return None
    doc = _documento()
    _cabecalho(doc, ficha["tema"])
    _tabela(doc, ficha, [c for c, _, _ in D.ROTULOS])
    hoje = date.today()
    out = os.path.join(BASE, "%s_%s_Notas_apoio_atividade_ministerial.docx"
                       % (hoje.strftime("%d.%m.%Y"), slug.upper()))
    doc.save(out)
    return out


def nota_mensal():
    """Nota mensal: só os pontos 2 e 4 do modelo, com o subcapítulo obrigatório
    de todas as medidas já tomadas."""
    problemas = {}
    for slug, ficha in D.FICHAS.items():
        e = validar(slug, ficha)
        if e:
            problemas[slug] = e
    if problemas:
        print("NÃO GERADO — fichas com problemas:")
        for slug, e in problemas.items():
            print("  %s:" % slug)
            for x in e:
                print("    - " + x)
        return None

    hoje = date.today()
    doc = _documento()
    p = doc.add_paragraph()
    r = p.add_run("Notas de apoio à atividade ministerial")
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = PRETO
    p = doc.add_paragraph()
    r = p.add_run("Nota mensal de temas em destaque — %s de %d"
                  % (MESES[hoje.month - 1], hoje.year))
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = PRETO
    doc.add_paragraph()

    for slug, ficha in D.FICHAS.items():
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(12)
        pf.space_after = Pt(6)
        r = p.add_run(ficha["tema"])
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = PRETO
        # o modelo do Gabinete para a nota mensal: pontos 2 e 4
        campos = ["pontos_sensiveis", "contexto"]
        _tabela(doc, ficha, campos)
        # subcapítulo obrigatório
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        r = p.add_run("Medidas já tomadas")
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = PRETO
        for txt in ficha["acoes_medidas"]:
            q = doc.add_paragraph(style="List Bullet")
            q.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            q.paragraph_format.space_after = Pt(4)
            r = q.add_run(txt)
            r.font.size = Pt(11)
            r.font.color.rgb = PRETO

    out = os.path.join(BASE, "%s_Nota_mensal_temas_destaque.docx" % hoje.strftime("%d.%m.%Y"))
    doc.save(out)
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    if "--mensal" in args:
        r = nota_mensal()
    elif args:
        slug = args[0]
        if slug not in D.FICHAS:
            print("ficha desconhecida: %s. Disponíveis: %s" % (slug, ", ".join(D.FICHAS)))
            sys.exit(1)
        r = nota_tematica(slug)
    else:
        print(__doc__)
        sys.exit(0)
    if r:
        print("gerado:", os.path.basename(r))
    else:
        sys.exit(1)
