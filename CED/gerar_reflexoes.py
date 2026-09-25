# -*- coding: utf-8 -*-
"""Gera o documento Reflexoes sobre o CED."""
import sys, os
BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(BASE), 'criador informal'))
sys.path.insert(0, BASE)
from _memo_engine import novo_doc
import _reflexoes_ced

d = novo_doc('Reflexões sobre o CED · zonas cinzentas do regime')
_reflexoes_ced.construir(d)
out = os.path.join(BASE, 'Reflexoes_sobre_CED.docx')
d.save(out)
print('gerado:', os.path.basename(out))
