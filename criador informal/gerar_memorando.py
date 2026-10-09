# -*- coding: utf-8 -*-
"""Gera as duas versoes do memorando e o anexo autonomo sobre o DL 314/2003."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _memo_engine import novo_doc
import _memo_conteudo, _anexo_dl314, _anexo_juris, _estudo_fogo

BASE = os.path.dirname(os.path.abspath(__file__))
COR = 'Criação de cães e gatos em pequena escala'

for modo, suf in (('A', 'refs-completas'), ('B', 'refs-leves')):
    d = novo_doc(COR)
    _memo_conteudo.construir(d, modo)
    out = os.path.join(BASE, f'Memorando_Criacao_Pequena_Escala_{suf}.docx')
    d.save(out)
    print('gerado:', os.path.basename(out))

d = novo_doc('Delimitação DL 314/2003 · DL 276/2001')
_anexo_dl314.construir(d)
out = os.path.join(BASE, 'Anexo_Delimitacao_DL314_2003.docx')
d.save(out)
print('gerado:', os.path.basename(out))

d = novo_doc('Jurisprudência e doutrina · DL 314/2003')
_anexo_juris.construir(d)
out = os.path.join(BASE, 'Anexo_Jurisprudencia_Doutrina_DL314.docx')
d.save(out)
print('gerado:', os.path.basename(out))

# «314 vs alojamentos» — estudo autonomo dos limites por fogo vs lotacao registada
d = novo_doc('Limites por fogo · lotação dos alojamentos registados')
_estudo_fogo.construir(d)
out = os.path.join(BASE, 'Estudo_Limites_por_Fogo.docx')
d.save(out)
print('gerado:', os.path.basename(out))
