# -*- coding: utf-8 -*-
"""Gera a nota juridica sobre a titularidade dos gatos em programas CED."""
import sys, os
BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(BASE), 'criador informal'))
sys.path.insert(0, BASE)
from _memo_engine import novo_doc
import _titularidade_ced

d = novo_doc('Titularidade dos gatos em programas CED')
_titularidade_ced.construir(d)
out = os.path.join(BASE, 'Titularidade_CED.docx')
d.save(out)
print('gerado:', os.path.basename(out))
