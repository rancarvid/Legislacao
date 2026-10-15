# -*- coding: utf-8 -*-
"""Minuta de email à Diretora-Geral sobre o PL n.º 780/XVII/2.ª."""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

BASE = os.path.dirname(os.path.abspath(__file__))
PRETO = RGBColor(0, 0, 0)

doc = Document()
sec = doc.sections[0]
sec.top_margin = sec.bottom_margin = Cm(2.5)
sec.left_margin = sec.right_margin = Cm(2.5)

est = doc.styles['Normal']
est.font.name = 'Calibri'
est.font.size = Pt(11)
est.font.color.rgb = PRETO


def p(txt='', antes=0, depois=8, alinhar=WD_ALIGN_PARAGRAPH.JUSTIFY):
    par = doc.add_paragraph()
    par.alignment = alinhar
    pf = par.paragraph_format
    pf.space_before = Pt(antes)
    pf.space_after = Pt(depois)
    pf.line_spacing = 1.15
    r = par.add_run(txt)
    r.font.size = Pt(11)
    r.font.color.rgb = PRETO
    return par


ESQ = WD_ALIGN_PARAGRAPH.LEFT

p('Para: Diretor-Geral de Alimentação e Veterinária <dirgeral@dgav.pt>', depois=2, alinhar=ESQ)
p('Assunto: RE: FW: Projeto Lei 780_XVII_2ª', depois=2, alinhar=ESQ)
p('Anexo: Parecer_DGAV_PL780_XVII_final.docx', depois=18, alinhar=ESQ)

p('Senhora Diretora-Geral,', depois=12, alinhar=ESQ)

p('Em resposta ao solicitado, junta-se o contributo sobre o Projeto de Lei n.º 780/XVII/2.ª, no que '
  'respeita ao bem-estar dos animais de companhia.')

p('A iniciativa altera o artigo 387.º do Código Penal e adita a alínea h) ao n.º 3 do artigo 1.º da Lei '
  'n.º 92/95, de 12 de setembro. Tipifica a ofensa sexual a animal, no plano penal quanto aos animais de '
  'companhia e no plano contraordenacional quanto a qualquer animal.')

p('Tanto o n.º 3 do artigo 7.º do Decreto-Lei n.º 276/2001, de 17 de outubro, como o n.º 3 do artigo '
  '387.º do Código Penal exigem a prova de dor, sofrimento ou lesão, pelo que a ofensa sexual de que não '
  'resulte sofrimento nem lesão demonstráveis não tem hoje sanção. O efeito útil da iniciativa é '
  'dispensar essa prova.')

p('Concorrem para a premência da alteração o impacto destas condutas no bem-estar animal e os riscos '
  'higiossanitários e zoonóticos associados, havendo casuística de lesões por esta via em número não '
  'residual, nem sempre com evidência externa identificável.')

p('Não se identificam objeções técnicas quanto ao bem-estar animal, pelo que o parecer é favorável.',
  depois=16)

p('Com os melhores cumprimentos,', depois=20, alinhar=ESQ)
p('[assinatura]', depois=0, alinhar=ESQ)

out = os.path.join(BASE, 'Email_DG_PL780_XVII.docx')
doc.save(out)
print('gerado:', os.path.basename(out))
