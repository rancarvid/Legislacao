# -*- coding: utf-8 -*-
"""Gera o parecer DGAV sobre o Projeto de Lei n.º 780/XVII/2.ª."""
import sys, os
BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
sys.path.insert(0, os.path.join(os.path.dirname(BASE), 'criador informal'))
from _memo_engine import novo_doc
import _parecer_pl780

d = novo_doc('Parecer · PL n.º 780/XVII/2.ª · ofensas sexuais contra animais')
_parecer_pl780.construir(d)
out = os.path.join(BASE, 'Parecer_DGAV_PL780_XVII.docx')
d.save(out)
print('gerado:', os.path.basename(out))
