# -*- coding: utf-8 -*-
"""Análise da proposta OMV/ANVETEM de procedimento-tipo de intervenção (v3.0, 26.8.2026).

Perspetiva da DGAV e necessidades face à legislação vigente, em dois âmbitos:
A. retirada de animais de alojamentos fora de emergência;
B. socorro animal em emergência.
Foco nos animais de companhia.

Gera: Analise_Proposta_OMV_ANVETEM_Retirada_e_Socorro.docx (na mesma pasta).
Executar a partir da raiz do repositório:
    python3 "Protocolo de retirada de alojamentos/_analise_proposta_omv_anvetem.py"
"""
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

PASTA = Path(__file__).resolve().parent
SAIDA = PASTA / 'Analise_Proposta_OMV_ANVETEM_Retirada_e_Socorro.docx'

AZUL = RGBColor(0x1F, 0x3B, 0x63)
CINZA = RGBColor(0x55, 0x55, 0x55)
VERDE = RGBColor(0x2E, 0x6B, 0x3A)

doc = Document()
# O modelo do python-docx traz <w:zoom> sem o atributo obrigatório «percent».
_zoom = doc.settings.element.find(qn('w:zoom'))
if _zoom is not None:
    _zoom.set(qn('w:percent'), '100')
for s in doc.sections:
    s.left_margin = s.right_margin = Cm(2.5)
    s.top_margin = s.bottom_margin = Cm(2.2)

st = doc.styles['Normal']
st.font.name = 'Calibri'
st.font.size = Pt(10.5)
st.paragraph_format.space_after = Pt(6)
st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY


def p(txt='', bold=False, italic=False, size=10.5, cor=None, space=6, left=0):
    par = doc.add_paragraph()
    par.paragraph_format.space_after = Pt(space)
    if left:
        par.paragraph_format.left_indent = Cm(left)
    r = par.add_run(txt)
    r.bold = bold
    r.italic = italic
    r.font.size = Pt(size)
    if cor is not None:
        r.font.color.rgb = cor
    return par


def rot(rotulo, txt, cor=AZUL):
    """Parágrafo com rótulo inicial a negrito (ex.: «Apreciação.»)."""
    par = doc.add_paragraph()
    par.paragraph_format.space_after = Pt(6)
    r = par.add_run(rotulo + ' ')
    r.bold = True
    r.font.color.rgb = cor
    par.add_run(txt)
    return par


def h1(txt):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(18)
    par.paragraph_format.space_after = Pt(6)
    par.paragraph_format.keep_with_next = True
    r = par.add_run(txt)
    r.bold = True
    r.font.size = Pt(13.5)
    r.font.color.rgb = AZUL


def h2(txt):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(12)
    par.paragraph_format.space_after = Pt(4)
    par.paragraph_format.keep_with_next = True
    r = par.add_run(txt)
    r.bold = True
    r.font.size = Pt(11.5)
    r.font.color.rgb = AZUL


def h3(txt):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(8)
    par.paragraph_format.space_after = Pt(3)
    par.paragraph_format.keep_with_next = True
    r = par.add_run(txt)
    r.bold = True
    r.font.size = Pt(10.5)


def cit(txt, fonte):
    # Um parágrafo por número ou alínea: evita linhas esticadas antes de quebras manuais.
    for seg in txt.split('\n'):
        par = doc.add_paragraph()
        par.paragraph_format.left_indent = Cm(0.8)
        par.paragraph_format.right_indent = Cm(0.4)
        par.paragraph_format.space_after = Pt(2)
        r = par.add_run(seg)
        r.italic = True
        r.font.size = Pt(9.5)
    f = doc.add_paragraph()
    f.paragraph_format.left_indent = Cm(0.8)
    f.paragraph_format.space_after = Pt(8)
    rf = f.add_run(fonte)
    rf.font.size = Pt(8.5)
    rf.font.color.rgb = CINZA


def bullet(txt, rotulo=None):
    par = doc.add_paragraph(style='List Bullet')
    par.paragraph_format.space_after = Pt(3)
    par.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if rotulo:
        r0 = par.add_run(rotulo + ' ')
        r0.bold = True
    r = par.add_run(txt)
    r.font.size = Pt(10.5)


def tabela(cab, linhas, larguras=None, size=8.5):
    t = doc.add_table(rows=1, cols=len(cab))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, c in enumerate(cab):
        cell = t.rows[0].cells[i]
        cell.text = ''
        par = cell.paragraphs[0]
        par.paragraph_format.space_after = Pt(2)
        r = par.add_run(c)
        r.bold = True
        r.font.size = Pt(size + 0.5)
        r.font.color.rgb = AZUL
    for linha in linhas:
        cells = t.add_row().cells
        for i, c in enumerate(linha):
            cells[i].text = ''
            par = cells[i].paragraphs[0]
            par.paragraph_format.space_after = Pt(2)
            par.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = par.add_run(c)
            r.font.size = Pt(size)
    if larguras:
        for row in t.rows:
            for i, w in enumerate(larguras):
                row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)


# Designações abreviadas usadas nas fontes
DL276 = 'Decreto-Lei n.º 276/2001, de 17 de outubro (versão consolidada)'
L92 = 'Lei n.º 92/95, de 12 de setembro (versão consolidada)'
CPP = 'Código de Processo Penal, na redação da Lei n.º 39/2020, de 18 de agosto'
RJCE = 'Regime Jurídico das Contraordenações Económicas, anexo ao Decreto-Lei n.º 9/2021, de 29 de janeiro'
L27 = 'Lei n.º 27/2016, de 23 de agosto'
DL82 = 'Decreto-Lei n.º 82/2019, de 27 de junho'
DL116 = 'Decreto-Lei n.º 116/98, de 5 de maio (texto publicado no DR, I série-A, n.º 103)'
LBPC = 'Lei de Bases da Proteção Civil (Lei n.º 27/2006, de 3 de julho), na redação da Lei n.º 38/2026, de 3 de agosto'
SIOPS = 'Sistema Integrado de Operações de Proteção e Socorro, anexo ao Decreto-Lei n.º 90-A/2022, de 30 de dezembro'
RGAC = ('projeto de RGAC, versão de trabalho (revisão formal DAJA V1, revista pelo grupo, 30.6.2026, 18h00). '
        'Proposta, não é legislação vigente')

# ───────────────────────────── Capa ─────────────────────────────
p('DIREÇÃO-GERAL DE ALIMENTAÇÃO E VETERINÁRIA', bold=True, size=9.5, cor=CINZA, space=0)
p('Direção de Serviços de Bem-Estar Animal', size=9.5, cor=CINZA, space=14)

par = doc.add_paragraph()
par.paragraph_format.space_after = Pt(2)
r = par.add_run('ANÁLISE DA PROPOSTA OMV / ANVETEM')
r.bold = True
r.font.size = Pt(16)
r.font.color.rgb = AZUL

p('Procedimento-tipo de intervenção em operações de retirada e apreensão de animais e de socorro animal '
  '(v3.0, de 26.8.2026)', bold=True, size=12, space=2)
p('Apreciação na perspetiva da DGAV e das necessidades face à legislação vigente, separada em dois '
  'âmbitos: A. retirada de animais de alojamentos fora de emergência; B. socorro em emergência. '
  'Foco nos animais de companhia.', size=10.5, cor=CINZA, space=4)
p('Documento de trabalho, 14.10.2026 (v1.1: acrescentada a via do DL 315/2009 e corrigido o destino na via do DL '
  '314/2003, na sequência das notas ao ficheiro anotado). Analisa o ficheiro «Proposta de Procedimento '
  'Integrado_DGAV_OMV_ANVETEM_v26_08_2026_signed_signed.pdf».', size=9, cor=CINZA, space=14)

h2('Como ler este documento')
bullet('«Âmbito A» e «Âmbito B» são a divisão pedida para esta análise. Não confundir com as «tipologias A a D» '
       'da proposta (A animais de companhia; B espécies pecuárias; C animais de produção e saúde pública; '
       'D socorro de qualquer espécie). O âmbito A desta análise corresponde, para os animais de companhia, à '
       'tipologia A da proposta; o âmbito B corresponde à tipologia D.')
bullet('As partes descritivas (o que diz a lei, o que diz a proposta) estão separadas das partes de opinião, '
       'assinaladas como «Apreciação» ou «Recomendação».')
bullet('A legislação vigente é citada verbatim, a partir do texto publicado no Diário da República ou da versão '
       'consolidada que consta do repositório. O projeto de RGAC é citado como proposta, nunca como lei vigente. '
       'O estado de verificação de cada fonte está no Anexo II.')

# ───────────────────────────── 1. Síntese ─────────────────────────────
h1('1. Síntese')

h2('1.1 Juízo global')
rot('Apreciação.',
    'A proposta é útil e chega no momento certo. Acerta no que mais falha hoje nas operações: o registo '
    'individual de cada animal, a cadeia de custódia, o inventário fechado, o auto de entrega com encargos '
    'escritos, a proibição de ceder animais antes de decisão e o planeamento prévio. Estes pontos protegem os '
    'animais, protegem a prova e protegem a DGAV. Merecem ser aproveitados quase sem alterações.')
p('Tem, porém, cinco fragilidades de fundo, que justificam que a DGAV aceite o grupo de trabalho mas não o '
  'texto tal como está:')
bullet('A proposta assenta quase só no art.º 19.º e no art.º 3.º-G do DL 276/2001. Omite a base legal mais '
       'forte para retirar animais de companhia em maus-tratos: o art.º 1.º-A da Lei n.º 92/95 e as regras do '
       'Código de Processo Penal sobre apreensão e guarda de animais, ambos na redação da Lei n.º 39/2020. '
       'Omite também as medidas cautelares e a apreensão de «seres vivos» do Regime Jurídico das '
       'Contraordenações Económicas (RJCE), que se aplica às contraordenações do DL 276/2001 desde 2021.',
       rotulo='Base legal incompleta.')
bullet('Faz da DGAV a entidade coordenadora, com comando único, de todas as operações em que participe. A lei '
       'não dá esse papel à DGAV no processo penal (dirigido pelo Ministério Público), na remoção municipal por '
       'insalubridade (DL 314/2003) nem no socorro em emergência, onde o comando cabe ao comandante das '
       'operações de socorro (COS), nos termos do SIOPS.', rotulo='Comando atribuído sem título legal.')
bullet('Um despacho ou orientação técnica da DGAV vincula os serviços da DGAV. Não vincula câmaras municipais, '
       'forças de segurança, Ministério Público ou associações. A «credenciação», a «suspensão da lista» e a '
       '«exclusão» de entidades (pontos 8.8 e 9.5) criam efeitos externos sem base legal.',
       rotulo='Instrumento que não chega a quem pretende obrigar.')
bullet('Não diz quem decide o destino dos animais nem quem paga a custódia, porque a lei vigente tem pelo menos '
       'quatro regimes concorrentes, com decisores diferentes. É a maior necessidade face à lei vigente e não '
       'se resolve por procedimento.', rotulo='O problema central fica por resolver.')
bullet('Aplica ao socorro o modelo da apreensão (fiel depositário, decisão de destino, dever de reserva). No '
       'socorro, o detentor é vítima, o animal continua a ser seu e a prioridade é a reunificação, que a '
       'proposta não trata.', rotulo='Os âmbitos A e B têm lógicas opostas.')

h2('1.2 Quadro-síntese')
tabela(
    ['Tema', 'Âmbito A: retirada fora de emergência', 'Âmbito B: socorro em emergência'],
    [
        ['Natureza da intervenção', 'Medida contra a vontade do detentor. Apreensão, prova, decisão de destino.',
         'Socorro a animais de detentores que são vítimas. Guarda temporária e reunificação.'],
        ['Quem comanda, segundo a lei',
         'Depende da via: MP (penal), diretor-geral (RJCE e art.º 3.º-G), DGAV com câmaras e polícias '
         '(art.º 19.º, n.º 8), câmara municipal (DL 314/2003).',
         'O COS (art.º 9.º do SIOPS). A DGAV integra o CCON, os CCOR, a Comissão Nacional e as comissões '
         'distritais de proteção civil.'],
        ['O que a proposta faz bem', 'Cadeia de custódia, ficha individual, inventário, auto de entrega, '
         'proibição de cedência antecipada, faseamento acima de 50 animais.',
         'Põe a DGAV a preparar-se para a Lei n.º 38/2026; mobiliza a bolsa de 106 médicos veterinários da OMV '
         'e a rede municipal.'],
        ['O que falta', 'Lei 92/95, art.º 1.º-A; CPP; RJCE; DL 314/2003; presunção de abandono de 15 dias; '
         'cedência voluntária; acumulação de animais; SIAC; custos.',
         'Integração no SIOPS; designação dos representantes da DGAV; reunificação via SIAC; presunção de '
         '15 dias; planos de evacuação de alojamentos; eutanásia no terreno.'],
        ['Necessidade legislativa principal', 'Regime único de retirada, custódia, destino e custos dos animais '
         'de companhia (a tratar no RGAC).', 'Norma sobre animais de companhia em emergência articulada com a '
         'Lei n.º 38/2026 (o projeto de RGAC é omisso).'],
    ],
    larguras=[3.2, 6.4, 6.4])

# ───────────────────────────── 2. O documento ─────────────────────────────
h1('2. O documento em análise')
p('Texto conjunto da Ordem dos Médicos Veterinários (OMV) e da Associação Nacional dos Médicos Veterinários dos '
  'Municípios (ANVETEM), dirigido à Diretora-Geral de Alimentação e Veterinária, na sequência do Of. n.º '
  '88/CD/2026, de 2.7.2026, e da reunião de 12.8.2026. Versão 3.0, de 26.8.2026, assinada digitalmente pelo '
  'Bastonário da OMV e pelo Presidente da ANVETEM.')
p('A proposta declara que «não cria competências novas nem altera o quadro legal» e que se limita a '
  'operacionalizar o DL 276/2001, o DL 64/2000, o DL 142/2006, o DL 116/98 e a Lei n.º 38/2026. Pede que seja '
  'aprovada «por despacho ou orientação técnica da DGAV, dirigida às DSAVR, aos médicos veterinários municipais e '
  'às entidades participantes».')
p('Estrutura: sete princípios (comando único, autoridade veterinária, responsabilidade clínica, cadeia de '
  'custódia, comunicação institucional, credenciação, planeamento); quatro tipologias; doze pontos (objeto, '
  'definições, planeamento, cinco fases operacionais, requisitos das entidades, encerramento, articulação com a '
  'proteção civil, calendário); Anexo I com os elementos mínimos de seis modelos (plano de operação, declaração '
  'de comando, ficha individual e registo de lote, auto de sequestro sanitário, auto de entrega e custódia, termo '
  'de compromisso).')
p('O calendário proposto (ponto 12) prevê a constituição de um grupo de trabalho DGAV, OMV e ANVETEM em 30 dias e '
  'a versão final em 90 dias. Contados de 26.8.2026, o primeiro prazo terminou em 25.9.2026.')

# ───────────────────────────── 3. Questões comuns ─────────────────────────────
h1('3. Questões comuns aos dois âmbitos')

h2('3.1 Que instrumento é e a quem vincula')
p('Um despacho ou orientação técnica do diretor-geral obriga os serviços da DGAV, incluindo as DSAVR, por via '
  'hierárquica. Os médicos veterinários municipais estão numa posição diferente. Dependem hierarquicamente do '
  'presidente da câmara e a relação com os serviços do Ministério é funcional:')
cit('«1 — Os médicos veterinários municipais dependem, hierárquica e disciplinarmente, do presidente da câmara da '
    'respectiva área da sua intervenção.\n'
    '2 — As relações funcionais dos médicos veterinários com o MADRP são asseguradas através das direcções '
    'regionais de agricultura e da articulação destas com a DGV e a DGFCQA, consoante a natureza das respectivas '
    'atribuições.\n'
    '3 — Entre os médicos veterinários municipais e os serviços mencionados no número anterior será estabelecido '
    'um programa de contactos regulares, sem prejuízo da possibilidade de convocação extraordinária por motivo '
    'urgente.\n'
    '4 — Em caso de concorrência de obrigações, prevalece o serviço municipal.»',
    'n.ºs 1 a 4 do art.º 4.º do ' + DL116)
p('As câmaras municipais, as forças de segurança, o Ministério Público e as associações não estão sujeitos a '
  'orientações da DGAV, salvo onde a lei lhes impõe um dever concreto (por exemplo, o n.º 6 do art.º 3.º-G e o '
  'n.º 9 do art.º 19.º do DL 276/2001).')
rot('Apreciação.',
    'O texto só produz os efeitos pretendidos se for desdobrado em três instrumentos: despacho do diretor-geral '
    'para os serviços da DGAV; protocolo com a ANMP, a OMV e a ANVETEM (e, idealmente, com a GNR e a PSP) para '
    'os restantes; termo de compromisso para as entidades que colaborem. A «convocação formal» do médico '
    'veterinário municipal com 48 horas (ponto 5.1.2) tem apoio na «convocação extraordinária por motivo '
    'urgente», mas o n.º 4 do art.º 4.º faz prevalecer o serviço municipal. A convocação deve ser dirigida '
    'também ao presidente da câmara.')

h2('3.2 A nota dos proponentes sobre o DL 116/98 está só parcialmente certa')
p('A nota ao ponto 5.1.1 afirma que o DL 116/98 não refere expressamente competências em bem-estar animal. É '
  'verdade quanto aos poderes de autoridade sanitária, que se limitam à sanidade animal e à saúde pública:')
cit('«3 — Os poderes de autoridade sanitária veterinária são conferidos aos médicos veterinários municipais, por '
    'inerência de cargo, pela Direcção-Geral de Veterinária (DGV), enquanto autoridade sanitária veterinária '
    'nacional, e pela Direcção-Geral de Fiscalização e Controlo da Qualidade Alimentar (DGFCQA), a título '
    'pessoal, não delegável e abrangendo a actividade por eles exercida na respectiva área concelhia, quando '
    'esteja em causa a sanidade animal ou a saúde pública.»',
    'n.º 3 do art.º 2.º do ' + DL116)
p('Não é verdade quanto ao dever de colaboração, que nomeia expressamente o bem-estar animal:')
cit('«1 — Os médicos veterinários municipais têm o dever de, nos termos da legislação vigente, colaborar com o '
    'Ministério da Agricultura, do Desenvolvimento Rural e das Pescas (MADRP), na área do respectivo município, em '
    'todas as acções levadas a efeito nos domínios da saúde e bem-estar animal, da saúde pública veterinária, da '
    'segurança da cadeia alimentar de origem animal, da inspecção hígio-sanitária, do controlo de higiene da '
    'produção, da transformação e da alimentação animal e dos controlos veterinários de animais e produtos '
    'provenientes das trocas intracomunitárias e importados de países terceiros, programadas e desencadeadas '
    'pelos serviços competentes, designadamente a DGV e a DGFCQA.»',
    'n.º 1 do art.º 3.º do ' + DL116)
p('Acresce que o DL 276/2001 inclui os médicos veterinários municipais entre as autoridades competentes para '
  'efeitos desse diploma:')
cit('«x) «Autoridade competente» a Direção-Geral de Alimentação e Veterinária (DGAV), enquanto autoridade sanitária '
    'veterinária nacional, os médicos veterinários municipais, enquanto autoridades sanitárias veterinárias '
    'concelhias, as câmaras municipais, o Instituto da Conservação da Natureza e das Florestas, I. P. (ICNF, '
    'I. P.), a Guarda Nacional Republicana (GNR), a Polícia de Segurança Pública (PSP) e a Polícia Municipal '
    '(PM);»',
    'al. x), do n.º 1, do art.º 2.º do ' + DL276)
rot('Apreciação.',
    'A convocação do médico veterinário municipal tem, assim, três fundamentos e não dois: o dever de '
    'colaboração em bem-estar animal (n.º 1 do art.º 3.º do DL 116/98), a qualidade de autoridade competente no '
    'DL 276/2001 e as competências municipais de recolha. A lacuna que os proponentes apontam existe, mas é mais '
    'estreita: o que falta é estender ao bem-estar animal a decisão «sem dependência hierárquica» do n.º 4 do '
    'art.º 2.º do DL 116/98, que hoje só cobre a saúde pública. É matéria legislativa, não de procedimento.')

h2('3.3 Remissões e designações a corrigir')
tabela(
    ['Ponto', 'O que diz a proposta', 'Verificação', 'Correção sugerida'],
    [
        ['6.1', 'Responsabilidade clínica «nos termos do artigo 4.º do DL n.º 276/2001».',
         'O art.º 4.º trata do médico veterinário responsável pelo alojamento, ao serviço do titular. O n.º 2, '
         'al. c), obriga-o a colaborar com as autoridades. O n.º 3 põe os CRO sob responsabilidade técnica do '
         'médico veterinário municipal. Não funda a direção clínica de uma operação oficial.',
         'Fundar a responsabilidade clínica na designação pela autoridade. Citar o art.º 4.º apenas para o dever '
         'de colaboração do veterinário do alojamento e para os animais que dão entrada em CRO.'],
        ['2 e 11.1', '«Zona de Concentração para Acolhimento de Animais» (ZCAA).',
         'A designação legal é «zona de concentração de acolhimento de animais» (al. d) do art.º 13.º do SIOPS).',
         'Usar a designação legal.'],
        ['9.1', 'Reconhecimento pelo município «nos termos da Lei n.º 38/2026».',
         'A Lei n.º 38/2026 só usa o reconhecimento municipal para definir quem integra a comissão municipal de '
         'proteção civil (al. k) do art.º 41.º da LBPC). Não cria um regime de reconhecimento para operações.',
         'Apresentar como recomendação aos municípios, não como requisito legal.'],
        ['9.1', '«Registo Nacional de Associações Zoófilas (SIAC/RNAZ), nos termos da RCM n.º 78/2021».',
         'A RCM n.º 78/2021 previu um registo nacional das associações zoófilas «junto do ICNF, I. P.». É ato '
         'programático; não cria requisitos com efeitos externos. A existência e a gestão atuais do registo '
         'estão por confirmar.',
         'Confirmar o estado do registo. Não o usar como condição legal.'],
        ['11.1', 'Integração da DGAV nos níveis «nacional, regional e distrital» de coordenação.',
         'Correto em substância: Comissão Nacional (al. f) do n.º 1 do art.º 37.º da LBPC), comissões '
         'distritais (al. i) do n.º 1 do art.º 39.º), CCON (al. k) do n.º 2 do art.º 3.º do SIOPS) e CCOR '
         '(al. j) do n.º 2 do art.º 4.º do SIOPS). A DGAV não integra os CCO sub-regionais.',
         'Manter, com as normas indicadas.'],
        ['7.1', 'Alojamento em CRO «nos termos do n.º 9 do artigo 19.º».',
         'Correto. O mesmo n.º 9 prevê ainda «designadamente o seu abate», hoje limitado pelos n.ºs 4 a 6 do '
         'art.º 3.º da Lei n.º 27/2016.', 'Acrescentar a ressalva da Lei n.º 27/2016.'],
        ['4.5', 'Mandado judicial «a que se refere o n.º 8 do artigo 19.º».',
         'Correto, mas incompleto. Há também o n.º 2 do art.º 67.º-A do DL 276/2001 (alojamentos), o n.º 2 do '
         'art.º 1.º-A da Lei n.º 92/95 (crime de maus-tratos) e as buscas do CPP.',
         'Indicar todas as bases, por via legal (ver 4.2).'],
    ],
    larguras=[1.2, 3.6, 6.0, 5.2])

h2('3.4 Um só texto para quatro tipologias')
rot('Apreciação.',
    'Para quem trabalha com animais de companhia, boa parte do texto é ruído: sequestro sanitário, registo de '
    'lote, SNIRA, occisão segundo o Regulamento (CE) n.º 1099/2009, intervalos de segurança e cadeia alimentar. '
    'O inverso também é verdade. Recomenda-se um tronco comum (princípios, registo, custódia, biossegurança, '
    'comunicação, relatório) e módulos por espécie e por situação. Para os animais de companhia, dois módulos: '
    'retirada fora de emergência e socorro.')

# ───────────────────────────── 4. Âmbito A ─────────────────────────────
h1('4. Âmbito A: retirada de animais de alojamentos fora de emergência')

h2('4.1 Situações-tipo')
p('Para animais de companhia, a retirada fora de emergência aparece em cinco situações, com regimes legais '
  'diferentes:')
bullet('Alojamento registado por mera comunicação prévia (criação comercial ou hospedagem) com maus-tratos ou '
       'graves problemas de saúde e bem-estar. O requerimento parlamentar de 13.7.2026 sobre o caso de Amarante '
       'refere «mais de 300 cães de um alojamento pertencente a uma criadora registada» na DGAV.',
       rotulo='a)')
bullet('Alojamento ou criação sem registo, que funciona como estabelecimento.', rotulo='b)')
bullet('Habitação com número excessivo de animais, insalubridade ou acumulação patológica (Síndrome de Noé), '
       'muitas vezes com detentor em situação de vulnerabilidade.', rotulo='c)')
bullet('Maus-tratos a um ou poucos animais num domicílio.', rotulo='d)')
bullet('Suspeita de uso de animais em lutas.', rotulo='e)')
bullet('Cão que agrediu uma pessoa, ou cão perigoso ou potencialmente perigoso detido sem as condições legais.', rotulo='f)')

h2('4.2 Legislação vigente: sete vias, vários decisores')
p('O quadro seguinte é descritivo. Indica, para cada via, a base legal, quem decide, quem executa, onde ficam '
  'os animais e quem decide o destino.')
tabela(
    ['Via', 'Base legal vigente', 'Decide', 'Executa', 'Custódia', 'Destino'],
    [
        ['V1. Penal', 'CP, arts. 387.º e 388.º; Lei 92/95, art.º 1.º-A; CPP, arts. 159.º-A, 178.º, 186.º e 249.º',
         'Ministério Público; juiz (mandados); OPC em urgência', 'OPC; DGAV e municípios (art.º 1.º-A)',
         'Depositário idóneo (CPP, art.º 178.º, n.º 2)',
         'Autoridade judiciária; perda a favor do Estado ou pena acessória (CP, art.º 388.º-A)'],
        ['V2. Contraordenacional cautelar', 'DL 276/2001, arts. 68.º a 70.º; RJCE, arts. 48.º a 52.º',
         'Diretor-geral (ou diretor do OPC instrutor)', 'DGAV; OPC',
         'Detentor como fiel depositário, salvo manifesto inconveniente (RJCE, art.º 49.º, n.º 3)',
         'Autoridade administrativa; destino antecipado (RJCE, art.º 50.º); perda (DL 276/2001, art.º 69.º, al. a))'],
        ['V3. Recolha por bem-estar', 'DL 276/2001, art.º 19.º, n.ºs 8 e 9',
         'DGAV', 'DGAV, câmaras «se necessário» e polícias', 'CRO', 'DGAV'],
        ['V4. Suspensão ou encerramento do alojamento', 'DL 276/2001, arts. 3.º-G a 3.º-I e 67.º-A',
         'Diretor-geral, sob proposta da DSAVR', 'Câmaras municipais (art.º 3.º-G, n.º 6)',
         'Recolha pela câmara; local não definido', 'Não regulado'],
        ['V5. Salubridade e limites por fogo', 'DL 314/2003, art.º 3.º, n.ºs 1 a 6',
         'Câmara municipal, após vistoria conjunta do delegado de saúde e do MVM', 'Câmara municipal',
         'Canil ou gatil municipal, ou outro destino escolhido pelo detentor',
         'MVM, após exame clínico e permanência mínima de oito dias (DL 314/2003, art.º 9.º, n.º 1)'],
        ['V6. Regime do CRO (aplica-se por arrastamento)', 'Lei 27/2016, art.º 3.º; DL 276/2001, art.º 4.º, '
         'n.º 3; DL 82/2019, art.º 11.º, n.º 5', 'Câmara / MVM', 'CRO', 'CRO',
         'Presunção de abandono aos 15 dias e encaminhamento para adoção'],
        ['V7. Animais perigosos e agressores', 'DL 315/2009, arts. 14.º, 15.º, 30.º, n.º 3, 30.º-A e 39.º',
         'Autoridade competente; MVM (destino e eutanásia do agressor)', 'Autoridades do art.º 30.º; mandado do '
         'tribunal cível da comarca', 'CRO (art.º 14.º); fiel depositário, nos termos do RJCE (art.º 39.º)',
         'MVM (art.º 15.º); perda e privação de detenção (art.º 30.º-A)'],
    ],
    larguras=[2.2, 3.6, 2.6, 2.4, 2.6, 2.6], size=8)

h3('V1. A via penal e a Lei n.º 92/95')
p('Desde 1.10.2020, a lei impõe um dever de atuação a quatro entidades, entre as quais a DGAV:')
cit('«1 - Em caso de evidência de sinais da prática de crimes de maus-tratos contra animais de companhia, as '
    'forças de segurança, os órgãos de polícia criminal, a Direção-Geral de Alimentação e Veterinária e os '
    'municípios devem desencadear os meios para proceder à recolha ou captura dos mesmos.\n'
    '2 - Para o efeito previsto no número anterior, pode ser solicitada a emissão de mandado judicial através da '
    'autoridade judiciária competente que assegure o acesso das forças de segurança ou órgãos de polícia criminal '
    'aos locais onde os referidos animais se encontrem.»',
    'n.ºs 1 e 2 do art.º 1.º-A da ' + L92 + ', aditado pela Lei n.º 39/2020')
p('O Código de Processo Penal passou a tratar os animais apreendidos de forma própria:')
cit('«2 — Os instrumentos, produtos ou vantagens e demais objetos apreendidos nos termos do número anterior são '
    'juntos ao processo, quando possível, e, quando não, confiados à guarda do funcionário de justiça adstrito ao '
    'processo ou de um depositário, de tudo se fazendo menção no auto, devendo os animais apreendidos ser '
    'confiados à guarda de depositários idóneos para a função com a possibilidade de serem ordenadas as '
    'diligências de prestação de cuidados, como a alimentação e demais deveres previstos no Código Civil.»',
    'n.º 2 do art.º 178.º do ' + CPP)
cit('«1 — Logo que se tornar desnecessário manter a apreensão para efeito de prova, os animais, as coisas ou os '
    'objetos apreendidos são restituídos a quem de direito ou, no caso dos animais, a quem tenha sido nomeado seu '
    'fiel depositário.»',
    'n.º 1 do art.º 186.º do ' + CPP)
cit('«7 — No que respeita à restituição de animais, deve ser sempre salvaguardado que estão reunidas as condições '
    'de bem-estar animal previstas na lei.»',
    'n.º 7 do art.º 186.º do ' + CPP)
cit('«c) Proceder a apreensões no decurso de revistas ou buscas ou em caso de urgência ou perigo na demora, bem '
    'como adotar as medidas cautelares necessárias à conservação da integridade dos animais e à conservação ou '
    'manutenção das coisas e dos objetos apreendidos.»',
    'al. c), do n.º 2, do art.º 249.º do ' + CPP)
cit('«1 — As perícias médico-veterinárias legais e forenses devem ser realizadas por entidades designadas pela '
    'autoridade judiciária, nomeadamente o Instituto Nacional de Investigação Agrária e Veterinária, as '
    'faculdades que reúnam as condições para o efeito, bem como médicos veterinários e médicos veterinários '
    'municipais.»',
    'n.º 1 do art.º 159.º-A do ' + CPP)
p('As associações zoófilas têm posição processual própria:')
cit('«As associações zoófilas legalmente constituídas têm legitimidade para requerer a todas as autoridades e '
    'tribunais as medidas preventivas e urgentes necessárias e adequadas para evitar violações em curso ou '
    'iminentes da presente lei.»', 'art.º 9.º da ' + L92)
cit('«1 - As associações zoófilas podem constituir-se assistentes em todos os processos originados ou relacionados '
    'com a violação da presente lei e ficam dispensadas de pagamento de custas e taxa de justiça, beneficiando do '
    'regime previsto na Lei n.º 83/95, de 31 de agosto, com as necessárias adaptações.»',
    'n.º 1 do art.º 10.º da ' + L92)

h3('V2. A via contraordenacional e as medidas cautelares do RJCE')
p('As contraordenações do DL 276/2001 são contraordenações económicas (art.º 68.º). O RJCE permite medidas '
  'cautelares sem audição prévia e a apreensão de seres vivos:')
cit('«1 — Quando esteja em causa o exercício ilegal de atividades, a existência de risco grave ou iminente para a '
    'saúde e a segurança das pessoas, animais ou bens ou para o ambiente, a violação grave de direitos dos '
    'consumidores ou quando se revele necessário para a instrução do processo de contraordenação, a autoridade '
    'administrativa competente pode determinar, sem audição prévia dos interessados, as seguintes medidas '
    'cautelares:\n'
    'a) A suspensão, total ou parcial, do exercício de atividades económicas;\n'
    'b) A cessação de práticas proibidas nos termos das disposições legais aplicáveis que se encontrem em curso;\n'
    'c) O encerramento, no todo ou em parte, de estabelecimentos ou de espaços que se encontrem adstritos ao apoio '
    'às atividades exercidas;\n'
    'd) A apreensão ou selagem de todos ou parte dos bens;\n'
    'e) A imposição das medidas que se mostrem adequadas à prevenção de danos à saúde e à segurança das pessoas, '
    'animais ou bens ou de danos ambientais, à reposição da situação anterior à infração e à minimização dos '
    'efeitos decorrentes da mesma.»',
    'n.º 1 do art.º 48.º do ' + RJCE)
cit('«1 — A autoridade administrativa competente pode, sem audição prévia do interessado, determinar a apreensão '
    'de bens ou seres vivos e de documentos, que serviram ou estavam destinados a servir para a prática de uma '
    'contraordenação económica ou que em consequência desta foram produzidos, ou quando tais bens ou seres vivos '
    'representem, pela sua natureza ou pelas circunstâncias do caso, perigo para a saúde e a segurança de pessoas '
    'e bens ou exista sério risco da sua utilização para a prática de um crime ou de outra contraordenação, ou '
    'quaisquer outros que forem suscetíveis de servir de prova.»', 'n.º 1 do art.º 49.º do ' + RJCE)
cit('«3 — Salvo se houver manifesto inconveniente, o detentor dos bens ou seres vivos e documentos apreendidos ou, '
    'na sua falta, quem o represente no ato de apreensão, é constituído seu fiel depositário pela autoridade '
    'administrativa competente, com a obrigação de não utilizar os bens apreendidos sob pena da prática do crime '
    'de desobediência.»', 'n.º 3 do art.º 49.º do ' + RJCE)
cit('«2 — Nos casos de risco de deterioração dos bens ou seres vivos, de conveniência da sua utilização imediata '
    'para abastecimento do mercado, de perigo para a saúde ou para o bem-estar de animais ou, em ambos os casos, '
    'de perigosidade, os bens apreendidos, logo que se tornem desnecessários, podem ser afetos a finalidade '
    'pública ou socialmente útil ou destruídos de forma imediata, por ordem da autoridade administrativa '
    'competente.»', 'n.º 2 do art.º 50.º do ' + RJCE)
cit('«3 — O recurso não tem efeito suspensivo da medida cautelar impugnada nem do procedimento '
    'contraordenacional.»', 'n.º 3 do art.º 52.º do ' + RJCE)

h3('V3 e V4. O DL 276/2001')
cit('«8 - Em caso de forte suspeita ou evidência de sinais de uso de animais em lutas ou quando esteja em causa a '
    'saúde e o bem-estar dos animais, a DGAV, com a intervenção das câmaras municipais, se necessário, e as '
    'autoridades mencionadas no número anterior devem proceder à recolha ou captura dos mesmos, podendo para o '
    'efeito solicitar a emissão de mandato judicial que lhes permita aceder aos locais onde estes se encontrem, '
    'designadamente estabelecimentos, casas de habitação e terrenos privados.\n'
    '9 - Os animais recolhidos nos termos do número anterior são alojados em centros de recolha oficial, devendo o '
    'médico veterinário municipal comunicar o facto à DGAV, que decide o destino dos mesmos, designadamente o seu '
    'abate, sem direito a indemnização.\n'
    '10 - A recolha, captura e abate compulsivo de cães e gatos é regulada por legislação própria.»',
    'n.ºs 8 a 10 do art.º 19.º do ' + DL276)
p('Os n.ºs 8 e 10 entraram no diploma ao mesmo tempo, pelo DL n.º 315/2003, de 17 de dezembro, publicado no mesmo '
  'dia que o DL n.º 314/2003 (a «legislação própria» dos cães e gatos).')
cit('«1 - O diretor-geral de Alimentação e Veterinária pode, mediante despacho, determinar a suspensão da '
    'atividade ou o encerramento do alojamento, designadamente quando se verifique uma das seguintes situações:\n'
    'a) Existência de riscos higiossanitários que ponham em causa a saúde das pessoas e ou dos animais;\n'
    'b) Maus tratos aos animais;\n'
    'c) Existência de graves problemas de saúde e bem-estar dos animais;\n'
    'd) Falta de condições de segurança e de tranquilidade para as pessoas ou animais, bem como de proteção do '
    'meio ambiente.»', 'n.º 1 do art.º 3.º-G do ' + DL276)
cit('«6 - Compete às câmaras municipais executar as medidas necessárias ao cumprimento da decisão a que se referem '
    'os n.os 3 e 4, nomeadamente proceder, quando necessário, à recolha dos animais.»',
    'n.º 6 do art.º 3.º-G do ' + DL276)

h3('V6. O regime do CRO, que se aplica a quem lá entra')
cit('«1 — Os animais acolhidos pelos centros de recolha oficial de animais que não sejam reclamados pelos seus '
    'detentores no prazo de 15 dias, a contar da data da sua recolha, presumem-se abandonados e são '
    'obrigatoriamente esterilizados e encaminhados para adoção, sem direito a indemnização dos detentores que '
    'venham a identificar-se como tal após o prazo previsto.»', 'n.º 1 do art.º 3.º da ' + L27)
cit('«6 — A eutanásia pode ser realizada em centros de recolha oficial de animais ou centros de atendimento médico '
    'veterinário, por médico veterinário, em casos comprovados de doença manifestamente incurável e quando se '
    'demonstre ser a via única e indispensável para eliminar a dor e o sofrimento irrecuperável do animal.»',
    'n.º 6 do art.º 3.º da ' + L27)
cit('«5 - Os animais que sejam recolhidos num Centro de Recolha Oficial (CRO) e que não sejam reclamados pelos seus '
    'proprietários devem ser registados no SIAC em nome do titular desse CRO, após o período de 15 dias previsto no '
    'n.º 4 do artigo 8.º da Portaria n.º 146/2017, de 26 de abril.»', 'n.º 5 do art.º 11.º do ' + DL82)

h2('4.3 O que a proposta resolve bem')
rot('Apreciação.', 'Os pontos seguintes devem ser mantidos. Respondem a falhas reais e dão à DGAV '
    'rastreabilidade e defesa, perante tribunais e perante a opinião pública.')
bullet('Planeamento escrito antes da operação, com destino previsto e capacidade confirmada (3.1, 3.2 e Anexo I, '
       'modelo A). A regra de que a urgência comprime o planeamento mas não o dispensa (3.1) é a formulação certa.')
bullet('Declaração escrita de base legal, responsável da operação e responsável clínico (4.1 e modelo B). Fixa a '
       'autoria dos atos e evita que a operação seja atribuída, na comunicação pública, a quem só colaborou.')
bullet('Observação individual de cada animal antes da saída e faseamento obrigatório acima de 50 animais, com '
       'posto de triagem (5.2.2 e 5.2.4). Serve o bem-estar e serve a prova: é a descrição do estado dos animais '
       'a que se refere o art.º 171.º do CPP.')
bullet('Ficha individual por animal (6.4 e modelo C) e colheita de amostras com cadeia de custódia (6.9).')
bullet('Auto de entrega com identificação dos animais, da qualidade em que a entidade os recebe e de quem paga '
       '(7.4 e modelo E); proibição de cedência ou adoção antes de decisão escrita (7.6); inventário único, '
       'encerrado em 15 dias (7.8); relatório em 30 dias (10.1).')
bullet('Proteção de dados e presunção de inocência na comunicação (8.6) e reconhecimento público de quem colabora '
       '(8.7).')

h2('4.4 O que a proposta não resolve ou resolve mal')

h3('a) Quem comanda depende da via legal, não da presença da DGAV')
p('Descrição: o ponto 1.2 aplica o procedimento a «todas as operações em que participem serviços da DGAV» e o '
  'ponto 4.2 põe a direção na DGAV ou na DSAVR. O ponto 1.4 reconhece a direção do Ministério Público no '
  'processo penal, mas só como aplicação subsidiária. O ponto 4.6 manda identificar o «fundamento prevalecente».')
rot('Apreciação.',
    'Nos casos de maus-tratos a animais de companhia, a via penal é a regra e não a exceção. Nela, a DGAV é '
    'executante (art.º 1.º-A da Lei n.º 92/95) e pode ser perita (art.º 159.º-A do CPP), mas não dirige. Na via '
    'do DL 314/2003 quem decide é a câmara. Fazer da DGAV a entidade que «responde» por todas as operações em que '
    'participa expõe-a a responsabilidade por atos que a lei atribui a outros. A regra do fundamento prevalecente '
    '(4.6) é a solução certa e deve passar a ser o eixo do texto: quem tem o título legal da operação coordena; '
    'a DGAV assegura sempre a direção técnico-veterinária e o registo.')

h3('b) Falta o equivalente, para animais de companhia, do sequestro sanitário')
p('Descrição: para espécies pecuárias, a proposta prevê a permanência no local sob sequestro (7.2 e modelo D). '
  'Para animais de companhia, a única saída prevista é o CRO (7.1) ou a entidade depositária (7.4).')
rot('Apreciação.',
    'Quando a operação é faseada (5.2.2) ou o CRO não tem lugar, os animais que ficam no local precisam de um '
    'título jurídico que os mantenha sob controlo da autoridade. Esse título existe: a apreensão com o detentor '
    'como fiel depositário e a imposição de medidas de correção (als. d) e e) do n.º 1 do art.º 48.º e n.º 3 do '
    'art.º 49.º do RJCE), ou a apreensão penal com depositário idóneo. Falta um modelo de «auto de apreensão com '
    'permanência no local», com deveres de alimentação, água, cuidados e visitas de verificação.')

h3('c) Falta a cedência voluntária')
rot('Apreciação.',
    'Em muitas operações o detentor aceita ceder os animais. Uma declaração de cedência, assinada no ato e '
    'registada no SIAC, transfere a titularidade sem processo e encurta a custódia de anos para dias. A proposta '
    'não a prevê. Recomenda-se um modelo G, «termo de cedência voluntária», com advertência de que a cedência não '
    'extingue a responsabilidade contraordenacional ou criminal e, no processo penal, com comunicação ao '
    'Ministério Público antes de qualquer destino.')

h3('d) Quem decide o destino: a proposta não identifica a «entidade competente»')
p('Descrição: o ponto 7.6 proíbe a cedência «antes de decisão expressa da entidade competente». O ponto 7.5 '
  'reserva a decisão à «autoridade veterinária».')
rot('Apreciação.',
    'O quadro 4.2 mostra que a entidade competente muda com a via: autoridade judiciária (V1), autoridade '
    'administrativa do processo de contraordenação (V2), DGAV (V3), e nada (V4). A proposta deve ter uma matriz '
    'de destino por via. Dois pontos práticos merecem destaque. Primeiro, no processo penal, quando o animal '
    'deixa de ser necessário à prova é entregue «a quem tenha sido nomeado seu fiel depositário» (n.º 1 do '
    'art.º 186.º do CPP): a escolha do depositário define, na prática, quem fica com o animal. Segundo, na via '
    'contraordenacional, o destino antecipado por «perigo para a saúde ou para o bem-estar de animais» (n.º 2 do '
    'art.º 50.º do RJCE) permite afetar os animais a finalidade socialmente útil antes da decisão final. Nenhum '
    'destes instrumentos é usado na proposta.')

h3('e) A presunção de abandono de 15 dias e o registo em nome do CRO')
rot('Apreciação.',
    'Animais retirados ao abrigo do n.º 8 do art.º 19.º do DL 276/2001 entram em CRO (n.º 9). A Lei n.º 27/2016 '
    'presume abandonados os animais «não reclamados» em 15 dias e manda encaminhá-los para adoção; o DL 82/2019 '
    'manda registá-los em nome do CRO. Lidas à letra, estas regras podem levar um município a dar para adoção um '
    'animal apreendido, cuja guarda decorre de decisão de autoridade e cujo destino cabe à DGAV ou ao tribunal. '
    'O risco existe nos dois sentidos: adoção indevida ou animais retidos sem decisão. A proposta não o trata. A '
    'DGAV pode emitir orientação interpretativa (estes animais não estão «não reclamados»; estão sob decisão de '
    'autoridade) e marcar o estado no SIAC (ver i)). A solução definitiva é legislativa.')

h3('f) Eutanásia: critério e local')
p('Descrição: o ponto 6.2 admite, na triagem, «eutanásia ou occisão». O ponto 6.8 exige indicação clínica '
  'fundamentada e prática por médico veterinário.')
rot('Apreciação.',
    'Para animais de companhia, o critério legal é mais estreito: «doença manifestamente incurável» e ser «a via '
    'única e indispensável para eliminar a dor e o sofrimento irrecuperável», em CRO ou CAMV (n.º 6 do art.º 3.º '
    'da Lei n.º 27/2016). A eutanásia no local da operação só se justifica em estado de necessidade, e deve ser '
    'registada como tal. Quando há processo penal, o animal é prova: a decisão deve ser comunicada ao Ministério '
    'Público e acompanhada de exame ou necropsia (art.º 159.º-A do CPP). O texto deve separar a eutanásia de '
    'animais de companhia da occisão de animais de produção.')

h3('g) Credenciação, lista e exclusão de entidades')
p('Descrição: só participam entidades «credenciadas» (princípio 6 e ponto 9), com requisitos comuns (alojamento '
  'registado, médico veterinário responsável, seguro, formação, termo de compromisso). A DGAV mantém e publicita '
  'a lista (9.3) e pode suspender entidades, com audiência prévia (9.5). O incumprimento das regras de '
  'comunicação determina a exclusão (8.8).')
rot('Apreciação.',
    'O objetivo é bom. O instrumento tem um problema de legalidade: criar por despacho uma lista com efeitos '
    'externos e sanções para particulares, sem norma habilitante. Há duas alternativas mais seguras. A primeira, '
    'uma bolsa de entidades colaboradoras por protocolo, com adesão voluntária e com a única consequência do '
    'incumprimento a ser a não convocação. A segunda, apoiar a lista em títulos que já existem: a mera comunicação '
    'prévia do alojamento (al. a) do n.º 1 do art.º 3.º e art.º 3.º-A do DL 276/2001) e o médico veterinário '
    'responsável (n.º 1 do art.º 4.º), que já são obrigatórios. Duas notas: no processo penal o depositário é '
    'escolhido pela autoridade judiciária, pelo que a lista só pode ser indicativa; e a partir de 31.8.2028 quem '
    'detenha animais confiscados para os colocar no mercado será um «abrigo» na aceção do Regulamento (UE) '
    '2026/1818, sujeito ao registo e às obrigações desse regulamento (ver 6.2).')

h3('h) Comunicação pública')
p('Descrição: porta-voz único da entidade coordenadora (8.1); dever de reserva das entidades participantes (8.2); '
  'proibição de divulgar imagens e dados (8.3); proibição de angariar fundos com imagens de animais retirados '
  'sem autorização (8.4); cessação imediata de transmissões em direto e de conteúdos para redes sociais (8.5). O '
  'resumo dos princípios fala em dissuadir «de forma contundente» a espetacularização.')
rot('Apreciação.',
    'As finalidades são legítimas: proteger a investigação, os dados pessoais, a presunção de inocência e a '
    'credibilidade das operações. A DGAV conhece o custo da exposição mediática desorganizada. Mas a '
    'administração não pode, por despacho, restringir a expressão de terceiros. Estas regras só valem como '
    'cláusulas do termo de compromisso, aceites por quem quer participar, e, no processo penal, pelas regras do '
    'próprio processo. As associações zoófilas podem ser assistentes (n.º 1 do art.º 10.º da Lei n.º 92/95) e '
    'requerer medidas urgentes (art.º 9.º): o procedimento não pode tratar como infração o exercício destes '
    'direitos. A linguagem («contundente», «não são eventos mediáticos») deve ser retirada de um texto normativo. '
    'Do lado da DGAV, falta o dever positivo: informar, no fim, o que foi feito e com que resultado (8.7 vai '
    'nesse sentido e deve ser reforçado).')

h3('i) SIAC: o que a DGAV pode fazer sem mudar a lei')
p('Descrição: o ponto 6.3 exige identificação eletrónica e registo no SIAC antes do alojamento definitivo.')
cit('«4 - As normas e procedimentos relativos ao funcionamento do SIAC, bem como a gestão das entidades com acesso '
    'e respetivos perfis de acesso, são aprovados pelo diretor-geral de Alimentação e Veterinária e devem constar '
    'de um Manual de Procedimentos SIAC.\n'
    '5 - O diretor-geral de Alimentação e Veterinária pode determinar, por decisão fundamentada, a suspensão '
    'provisória e cautelar do acesso ao SIAC a uma entidade, médico veterinário, ou titular de animais de '
    'companhia, sempre que sejam identificados incumprimentos graves das normas previstas no Manual de '
    'Procedimentos SIAC, até à decisão que aplique a pertinente contraordenação, designadamente as previstas no '
    'artigo 21.º do presente decreto-lei.»', 'n.ºs 4 e 5 do art.º 8.º do ' + DL82)
rot('Apreciação.',
    'O registo, por si, não diz que o animal está apreendido. Pelo Manual de Procedimentos SIAC, a DGAV pode '
    'criar um estado «sob apreensão ou custódia», com indicação do processo e do local, que impeça transferências '
    'de titularidade e o registo automático em nome do CRO. Pode ainda suspender cautelarmente o acesso do '
    'detentor ao SIAC quando houver incumprimento grave. São das medidas com melhor relação custo-efeito ao '
    'alcance da DGAV.')

h3('j) Acumulação de animais e detentores vulneráveis')
p('Descrição: a proposta não menciona a acumulação patológica nem a articulação com saúde e ação social. A '
  'autoridade de saúde, que o DL 314/2003 põe na vistoria conjunta, não aparece no texto.')
cit('«h) A promoção da elaboração e publicação, durante o ano de 2021, pelo ICNF, I. P., em articulação com o '
    'provedor do animal, e ouvida a autoridade sanitária veterinária nacional no âmbito das suas competências, de '
    'um guia de procedimentos que auxilie as autoridades públicas na abordagem aos fenómenos de acumulação de '
    'animais ou Síndrome de Noé, considerando as dimensões da justiça, dos municípios, da ação social, da saúde e '
    'do ambiente e da ação climática.»',
    'al. h) da Resolução do Conselho de Ministros n.º 78/2021, de 25 de junho (Programa Nacional para os Animais '
    'de Companhia)')
rot('Apreciação.',
    'Na situação c) de 4.1, retirar os animais sem tratar a pessoa produz reincidência. O módulo A deve prever, '
    'nesses casos, a participação da autoridade de saúde e dos serviços de ação social, a avaliação da pessoa e '
    'o acompanhamento depois da operação, com a esterilização dos animais que fiquem.')

h3('k) Encargos')
p('Descrição: os encargos são «imputados à entidade responsável» (7.7), sem dizer qual. A nota ao ponto 7.8 '
  'afirma que a custódia não pode depender de angariação de fundos junto do público.')
rot('Apreciação.',
    'A lei vigente não tem uma regra de financiamento antecipado da custódia. O n.º 3 do art.º 19.º do DL 276/2001 '
    'só faz pagar as despesas quando o animal é restituído, e refere-se aos animais do n.º 1. No processo penal, a '
    'custódia pode durar anos. Na prática, o encargo cai no município que tem o CRO ou na associação '
    'depositária. A proposta identifica bem o problema e não o resolve, nem pode. O procedimento pode, no '
    'máximo, exigir que o auto de entrega diga quem adianta e quem reembolsa, e que a DGAV registe os custos de '
    'cada operação para fundamentar uma solução legislativa e financeira.')

h3('l) O peso que a proposta põe na DGAV')
rot('Apreciação.',
    'A proposta atribui à DGAV: planos de contingência-tipo para cinco cenários (3.3); simulacros anuais em cada '
    'região (3.4); inventário permanente da capacidade mobilizável (3.5); lista anual de entidades (9.3); '
    'suspensões com audiência prévia (9.5); inventário de cada operação em 15 dias (7.8); relatório em 30 dias '
    '(10.1); reunião anual de avaliação (10.4). Nenhum destes deveres vem com meios. Recomenda-se proporcionalidade: '
    'deveres completos acima de um limiar (por exemplo, mais de 50 animais ou mais de duas entidades), modelos '
    'simplificados abaixo dele, e inventário de capacidade alimentado pelos relatórios anuais dos CRO previstos '
    'nos n.ºs 9 e 10 do art.º 3.º da Lei n.º 27/2016, que já existem.')

h3('m) Rigidez que pode virar argumento de defesa')
rot('Apreciação.',
    'A regra «nenhuma operação se inicia sem» documento escrito (4.1) e o prazo de 48 horas (5.1.2) protegem a '
    'operação planeada. Numa situação de flagrante, os OPC atuam ao abrigo do CPP sem esperar. O texto deve '
    'dizer expressamente que é uma norma de organização interna e que a sua inobservância não afeta a validade '
    'dos atos praticados ao abrigo da lei. Sem essa cláusula, a defesa de um arguido pode invocar o '
    'incumprimento do procedimento.')

h3('n) Um risco de interpretação no art.º 19.º do DL 276/2001')
rot('Apreciação.',
    'O n.º 10 do art.º 19.º diz que a recolha e captura de cães e gatos «é regulada por legislação própria». Pode '
    'ser invocado para afastar o n.º 8 quando os animais são cães ou gatos, que são a grande maioria dos casos. A '
    'leitura mais sólida é outra: os dois números entraram juntos, pelo DL 315/2003, e o n.º 10 remete para o DL '
    '314/2003 a recolha por razões de saúde pública (n.ºs 1 a 7), não a recolha por bem-estar do n.º 8. Ainda '
    'assim, a proposta fica mais segura se, para cães e gatos em maus-tratos, invocar em primeiro lugar o art.º '
    '1.º-A da Lei n.º 92/95, que é específico e posterior, e o n.º 8 do art.º 19.º como base complementar.')

h2('4.5 Necessidades face à legislação vigente (âmbito A)')
p('O que um procedimento não consegue resolver e exige lei, em princípio no RGAC:')
tabela(
    ['N.º', 'Necessidade', 'Porque não se resolve por procedimento'],
    [
        ['A1', 'Regime único de retirada e custódia de animais de companhia: quem decide, onde ficam, por quanto '
               'tempo, quem paga, quando muda a titularidade.',
         'Há sete vias com decisores diferentes (quadro 4.2). Só a lei pode ordená-las.'],
        ['A2', 'Exceção expressa à presunção de abandono de 15 dias e ao registo em nome do CRO para animais '
               'apreendidos ou retirados por decisão de autoridade.',
         'A presunção está na Lei n.º 27/2016 e no DL 82/2019. Uma orientação reduz o risco, não o elimina.'],
        ['A3', 'Financiamento antecipado da custódia e recuperação dos custos junto do detentor.',
         'Não há norma que imponha o adiantamento a ninguém.'],
        ['A4', 'Destino antecipado de animais apreendidos com base no bem-estar, também no processo penal.',
         'O RJCE já o permite na via contraordenacional; no CPP depende da decisão da autoridade judiciária.'],
        ['A5', 'Atualização do n.º 9 do art.º 19.º do DL 276/2001 («designadamente o seu abate») e clarificação do '
               'n.º 10.', 'É texto de lei.'],
        ['A6', 'Decisão sem dependência hierárquica do médico veterinário municipal também em bem-estar animal.',
         'O n.º 4 do art.º 2.º do DL 116/98 só a prevê para a saúde pública.'],
        ['A7', 'Intervenção multidisciplinar nos casos de acumulação de animais.',
         'Envolve serviços de saúde e de ação social fora da tutela da DGAV.'],
        ['A8', 'Destino dos animais quando o alojamento é encerrado (art.º 3.º-G).',
         'O artigo manda as câmaras recolher, mas não diz para onde nem quem decide o destino.'],
    ],
    larguras=[1.0, 8.0, 7.0])

h2('4.6 Recomendações para a posição da DGAV (âmbito A)')
for i, (rotulo, txt) in enumerate([
    ('Aceitar o grupo de trabalho', 'com mandato para reestruturar o texto em tronco comum e módulos (ver 7).'),
    ('Matriz de liderança e de destino por via legal', 'substitui a regra «DGAV coordena sempre». Mantém a '
     'regra do fundamento prevalecente (4.6) e a direção técnico-veterinária da DGAV em todas as vias.'),
    ('Completar a base legal', 'com o art.º 1.º-A, o art.º 9.º e o n.º 1 do art.º 10.º da Lei n.º 92/95; os '
     'arts. 159.º-A, 178.º, 186.º e 249.º do CPP; os arts. 48.º a 52.º do RJCE; o art.º 3.º do DL 314/2003; o '
     'art.º 3.º da Lei n.º 27/2016; os arts. 8.º e 11.º do DL 82/2019; os arts. 14.º, 15.º, 30.º e 39.º do DL '
     '315/2009.'),
    ('Novos modelos', 'auto de apreensão com permanência no local (fiel depositário) e termo de cedência '
     'voluntária.'),
    ('Cláusula de salvaguarda', 'o procedimento é de organização interna; a sua inobservância não afeta a '
     'validade dos atos praticados ao abrigo da lei; há uma via urgente simplificada.'),
    ('Bolsa de entidades por protocolo', 'em vez de credenciação com sanções; requisitos assentes em títulos '
     'legais existentes.'),
    ('Comunicação', 'regras de reserva como cláusula do termo de compromisso; coordenação com o Ministério '
     'Público quando há processo penal; dever da DGAV de informar no fim; retirar a linguagem valorativa.'),
    ('SIAC', 'criar no Manual de Procedimentos o estado «sob apreensão ou custódia» e usar a suspensão cautelar '
     'de acesso.'),
    ('Orientação interpretativa sobre a presunção de 15 dias', 'dirigida aos municípios, enquanto a lei não for '
     'alterada.'),
    ('Eutanásia', 'separar companhia e produção; critério do n.º 6 do art.º 3.º da Lei n.º 27/2016; estado de '
     'necessidade no local; comunicação ao Ministério Público e exame quando há processo penal.'),
    ('Acumulação de animais', 'submódulo com autoridade de saúde e ação social.'),
    ('Proporcionalidade dos deveres da DGAV', 'limiar a partir do qual se aplicam todos os deveres.'),
    ('Levar ao RGAC as necessidades A1 a A8', 'ver 6.1.'),
], start=1):
    bullet(txt, rotulo='R%d. %s:' % (i, rotulo))

# ───────────────────────────── 5. Âmbito B ─────────────────────────────
h1('5. Âmbito B: socorro animal em emergência')

h2('5.1 Situações-tipo')
bullet('Incêndio rural, cheia ou outro acidente grave que atinge habitações com animais. As pessoas são '
       'evacuadas e os animais ficam, fogem ou são levados pelos detentores para locais que não os aceitam.')
bullet('Acidente que atinge um alojamento com muitos animais: CRO, abrigo de associação, criador. O incêndio de '
       'julho de 2020 em Santo Tirso, que atingiu abrigos sem registo, é o precedente nacional mais conhecido.')
bullet('Animais errantes ou perdidos na sequência da catástrofe, sem detentor presente.')

h2('5.2 Legislação vigente')
p('A Lei n.º 38/2026, de 3 de agosto, em vigor desde 8.8.2026, integrou o socorro animal na proteção civil. As '
  'normas alteradas, citadas a partir do texto publicado no Diário da República:')
cit('«1 — A proteção civil é a atividade desenvolvida pelo Estado, Regiões Autónomas e autarquias locais, pelos '
    'cidadãos e por todas as entidades públicas e privadas com a finalidade de prevenir riscos coletivos inerentes '
    'a situações de acidente grave ou catástrofe, de atenuar os seus efeitos e proteger e socorrer as pessoas, os '
    'animais e bens em perigo quando aquelas situações ocorram.»', 'n.º 1 do art.º 1.º da ' + LBPC)
cit('«e) Planeamento de soluções de emergência, visando a busca, o salvamento, a prestação de socorro e de '
    'assistência, bem como a evacuação, alojamento e abastecimento dos animais;»',
    'al. e), do n.º 2, do art.º 4.º da ' + LBPC)
cit('«f) Um representante de saúde e bem-estar animal a designar pela Direção-Geral de Alimentação e Veterinária '
    '(DGAV).»', 'al. f), do n.º 1, do art.º 37.º da ' + LBPC + ' (Comissão Nacional de Proteção Civil)')
cit('«i) Um representante de saúde e bem-estar animal a designar pela DGAV.»',
    'al. i), do n.º 1, do art.º 39.º da ' + LBPC + ' (comissões distritais de proteção civil)')
cit('«j) Um representante da autoridade sanitária veterinária concelhia;\n'
    'k) Representantes de entidades legalmente constituídas no âmbito da busca, salvamento, prestação de socorro, '
    'assistência, evacuação, alojamento ou abastecimento de animais, reconhecidos pelo município;»',
    'als. j) e k) do art.º 41.º da ' + LBPC + ' (comissões municipais de proteção civil)')
cit('«e) Planeamento de soluções de emergência, visando a busca, o salvamento a prestação de socorro e de '
    'assistência, bem como a evacuação, alojamento e abastecimento dos animais presentes no município, incluindo a '
    'realização de simulacros;»',
    'al. e), do n.º 2, do art.º 2.º da Lei n.º 65/2007, de 12 de novembro, na redação da Lei n.º 38/2026')
cit('«k) Direção-Geral de Alimentação e Veterinária (DGAV);»',
    'al. k), do n.º 2, do art.º 3.º do ' + SIOPS + ', na redação da Lei n.º 38/2026 (CCON)')
cit('«j) DGAV;»', 'al. j), do n.º 2, do art.º 4.º do ' + SIOPS + ', na redação da Lei n.º 38/2026 (CCOR)')
cit('«d) Uma zona de concentração de acolhimento de animais, onde se localizam temporariamente os meios e '
    'recursos disponíveis e se mantém um sistema de apoio logístico à acomodação, salvamento e triagem de '
    'animais.»', 'al. d) do art.º 13.º do ' + SIOPS + ', na redação da Lei n.º 38/2026')
p('O comando no teatro de operações não foi alterado:')
cit('«1 — A responsabilidade pela operação de proteção e socorro incumbe ao comandante da operação de socorro '
    '(COS).»', 'n.º 1 do art.º 9.º do ' + SIOPS)
cit('«e) Comandar os meios humanos e materiais das entidades presentes no teatro de operações, através das '
    'respetivas estruturas hierárquicas;»\n'
    '[…]\n'
    '«l) Fornecer a informação operacional para divulgação aos órgãos de comunicação social;»',
    'als. e) e l), do n.º 1, do art.º 10.º do ' + SIOPS)
p('A Comissão Nacional de Proteção Civil, onde a DGAV passou a ter representante, define as normas técnicas dos '
  'planos de emergência:')
cit('«h) Definir os critérios e as normas técnicas sobre a elaboração e operacionalização de planos de emergência '
    'de proteção civil;»',
    'al. h), do n.º 2, do art.º 36.º da Lei de Bases da Proteção Civil, na redação da Lei n.º 80/2015, de 3 de '
    'agosto')
p('Dois deveres gerais completam o quadro:')
cit('«2 - Os animais doentes, feridos ou em perigo devem, na medida do possível, ser socorridos.»',
    'n.º 2 do art.º 1.º da ' + L92)
cit('«As instalações dos alojamentos referidos nas alíneas p) a t) do n.º 1 do artigo 2.º devem dispor de um '
    'sistema de proteção contra incêndios, de alarme para aviso de avarias deste sistema e, ainda, dos '
    'equipamentos referidos no artigo 8.º, quando se tratar de alojamentos em edifícios fechados.»',
    'art.º 11.º do ' + DL276)

h2('5.3 O que a proposta resolve bem')
rot('Apreciação.', 'A proposta é, até agora, o primeiro texto que leva a sério a Lei n.º 38/2026 do lado '
    'veterinário. São positivos:')
bullet('a previsão de planos e simulacros articulados com os municipais (3.3 e 3.4);')
bullet('o inventário da capacidade mobilizável (3.5), que é exatamente a informação que os planos municipais vão '
       'pedir;')
bullet('a oferta concreta da OMV: bolsa de 106 médicos veterinários por valência, rede de CAMV (P.A.R.A.) e '
       'comissão técnica (11.4); e a rede de médicos veterinários municipais da ANVETEM (11.5);')
bullet('a ideia de que os requisitos das entidades sirvam de base ao reconhecimento municipal, para evitar '
       'sistemas duplicados (11.2);')
bullet('a recomendação de formação específica dos representantes (11.6).')

h2('5.4 O que a proposta não resolve ou resolve mal')

h3('a) Comando e porta-voz: conflito com o SIOPS')
rot('Apreciação.',
    'O princípio do comando único da autoridade veterinária (princípio 1 e ponto 4) e o porta-voz único da '
    'entidade coordenadora (8.1) não podem valer no socorro. Pelo SIOPS, a responsabilidade é do COS, que comanda '
    'todos os meios no teatro de operações e fornece a informação à comunicação social. A posição útil da DGAV é '
    'outra, a três níveis: estratégico, no CCON, nos CCOR, na Comissão Nacional e nas comissões distritais; '
    'técnico, como responsável do setor ou célula de socorro animal no posto de comando, sob o COS (o n.º 1, al. '
    'e), do art.º 12.º do SIOPS admite representantes das entidades com meios empenhados); e de planeamento, '
    'pelos critérios técnicos da componente animal dos planos. O módulo B deve ser reescrito nestes termos.')

h3('b) Planeamento: o dever é municipal; a alavanca da DGAV é a Comissão Nacional')
rot('Apreciação.',
    'A Lei n.º 38/2026 pôs o dever de planear e de fazer simulacros nos municípios. A proposta põe a DGAV a fazer '
    'planos de contingência e simulacros anuais em cada região (3.3 e 3.4), o que duplica e sobrecarrega. A via '
    'com mais efeito é outra: através do seu representante na Comissão Nacional, a DGAV propor os critérios '
    'técnicos da componente animal dos planos de emergência (al. h) do n.º 2 do art.º 36.º da LBPC). Conteúdo '
    'mínimo sugerido: levantamento dos alojamentos e CRO do concelho; locais pré-definidos para a zona de '
    'concentração de acolhimento de animais; transporte e caixas; médicos veterinários mobilizáveis; leitura de '
    'transponders e consulta ao SIAC; alojamento conjunto de pessoas e animais.')

h3('c) Um dever novo da DGAV que a proposta não trata')
rot('Apreciação.',
    'A Lei n.º 38/2026 obriga a DGAV a designar representantes de saúde e bem-estar animal na Comissão Nacional e '
    'em cada comissão distrital de proteção civil, e a ter representante no CCON e nos CCOR. É um dever em vigor '
    'desde 8.8.2026. Exige despacho de designação, suplentes, disponibilidade quando os centros são ativados e '
    'formação. As cinco DSAVR têm designação territorial próxima das cinco regiões dos CCOR, o que facilita a '
    'designação; os limites territoriais devem ser confirmados. A proposta, centrada na OMV e na ANVETEM, não '
    'tem este ponto.')

h3('d) Socorro não é apreensão: falta a reunificação')
rot('Apreciação.',
    'No socorro, o animal continua a ser do detentor, que é vítima. A guarda é temporária e o objetivo é devolver. '
    'A proposta aplica o vocabulário e os modelos da apreensão (fiel depositário, decisão de destino pela '
    'autoridade, dever de reserva). Falta o essencial: leitura do transponder à entrada, consulta ao SIAC, contacto '
    'com o titular, registo de cada animal acolhido com local e hora, listas públicas de animais acolhidos, e um '
    'prazo de reunificação adaptado a pessoas deslocadas. A DGAV gere o SIAC (n.º 2 do art.º 8.º do DL 82/2019) e '
    'é a entidade que pode tornar isto possível. Neste âmbito, a comunicação certa é a contrária da do âmbito A: '
    'informação ativa aos detentores sobre onde estão os animais.')

h3('e) A presunção de 15 dias pode fazer perder animais de pessoas deslocadas')
rot('Apreciação.',
    'Se os animais socorridos forem levados para um CRO, a Lei n.º 27/2016 presume-os abandonados aos 15 dias e o '
    'DL 82/2019 manda registá-los em nome do CRO. Uma família desalojada por um incêndio pode não os reclamar a '
    'tempo. Um despacho não suspende a lei. Até haver norma, a DGAV pode recomendar que os animais socorridos '
    'fiquem na zona de concentração ou em alojamento temporário identificado como tal, e não como entrada '
    'corrente em CRO, e que a contagem do prazo se faça só a partir da notificação do titular identificado pelo '
    'SIAC. É uma solução de recurso; a definitiva é legislativa.')

h3('f) Eutanásia no terreno')
rot('Apreciação.',
    'Em incêndios há animais com queimaduras incompatíveis com a vida, longe de qualquer CRO ou CAMV. A Lei n.º '
    '27/2016 só prevê a eutanásia nesses locais (n.º 6 do art.º 3.º). O médico veterinário que atua no terreno '
    'fá-lo em estado de necessidade. A DGAV deve emitir orientação técnica para estes casos: critérios clínicos, '
    'métodos, registo, identificação do animal e comunicação ao titular.')

h3('g) Os alojamentos como pontos de risco')
rot('Apreciação.',
    'O art.º 11.º do DL 276/2001 só exige proteção contra incêndios em edifícios fechados. Não há dever de plano '
    'de evacuação em CRO, abrigos ou criadores, muitos em zonas rurais ou florestais. A DGAV tem a lista dos '
    'alojamentos com mera comunicação prévia: partilhá-la com os serviços municipais de proteção civil, para '
    'efeitos do planeamento que a Lei n.º 38/2026 lhes impõe, é uma medida imediata. O dever de plano de '
    'evacuação é matéria para o RGAC.')

h3('h) Reconhecimento das entidades e voluntários')
rot('Apreciação.',
    'O reconhecimento municipal da Lei n.º 38/2026 serve para compor a comissão municipal. Os requisitos do ponto 9 '
    'podem ser propostos aos municípios como referência, via Comissão Nacional ou ANEPC, mas a DGAV não os pode '
    'impor. A bolsa da OMV deve entrar por protocolo, com seguro e com integração sob o COS. Falta prever a gestão '
    'de voluntários espontâneos, que nas catástrofes chegam em número e sem enquadramento.')

h3('i) Passagem do socorro à retirada')
rot('Apreciação.',
    'O socorro pode revelar maus-tratos ou um alojamento ilegal (foi o caso de Santo Tirso). O procedimento deve '
    'prever a passagem do âmbito B para o âmbito A: preservar a prova, registar o estado dos animais, comunicar à '
    'autoridade competente e mudar o título da guarda.')

h2('5.5 Necessidades face à legislação vigente (âmbito B)')
tabela(
    ['N.º', 'Necessidade', 'Onde tratar'],
    [
        ['B1', 'Norma sobre animais de companhia em acidente grave ou catástrofe: guarda temporária, '
               'reunificação, prazos, presunção de abandono suspensa.', 'RGAC (hoje omisso).'],
        ['B2', 'Plano de evacuação obrigatório para CRO, abrigos e alojamentos acima de certa dimensão.', 'RGAC.'],
        ['B3', 'Requisitos da zona de concentração de acolhimento de animais e critérios de reconhecimento das '
               'entidades.', 'Normas técnicas da Comissão Nacional ou diretiva da ANEPC, com proposta da DGAV.'],
        ['B4', 'Eutanásia fora de CRO e CAMV em emergência.', 'Lei n.º 27/2016 ou RGAC; até lá, orientação da DGAV.'],
        ['B5', 'Financiamento do dever municipal de alojar animais em emergência.',
         'Instrumentos de apoio aos municípios, incluindo os Avisos de bem-estar animal da DGAV.'],
        ['B6', 'Partilha de dados do SIAC e da lista de alojamentos com a proteção civil.',
         'Base legal clara no RGAC e regras de proteção de dados.'],
    ],
    larguras=[1.0, 9.0, 6.0])

h2('5.6 Recomendações para a posição da DGAV (âmbito B)')
for i, (rotulo, txt) in enumerate([
    ('Reescrever a tipologia D', 'integrada no SIOPS: COS comanda; a DGAV dirige tecnicamente o setor animal e '
     'garante o registo e a reunificação; a informação pública é do COS, com conteúdos sobre animais preparados '
     'pela DGAV.'),
    ('Despacho interno de designação', 'dos representantes na Comissão Nacional, nas comissões distritais, no '
     'CCON e nos CCOR, com suplentes, contactos e formação.'),
    ('Proposta de critérios técnicos', 'para a componente animal dos planos municipais, a apresentar na Comissão '
     'Nacional.'),
    ('Protocolo de reunificação no SIAC', 'registo de animais acolhidos em emergência, consulta e listas '
     'públicas.'),
    ('Partilha da lista de alojamentos', 'com os serviços municipais de proteção civil.'),
    ('Orientação técnica sobre eutanásia no terreno', ''),
    ('Protocolo com a OMV', 'para a bolsa de voluntários, com seguro e enquadramento sob o COS.'),
    ('Cláusula de passagem do socorro à retirada', ''),
    ('Levar ao RGAC as necessidades B1, B2, B4 e B6', 'ver 6.1.'),
], start=14):
    bullet(txt, rotulo=('R%d. %s' % (i, rotulo)) + (':' if txt else '.'))

# ───────────────────────────── 6. RGAC e Regulamento ─────────────────────────────
h1('6. Ligação ao projeto de RGAC e ao Regulamento (UE) 2026/1818')

h2('6.1 O projeto de RGAC muda o modelo em que a proposta assenta')
p('Descrição. O projeto de RGAC (' + RGAC + ') faz três escolhas relevantes:')
cit('«5 - Quando esteja em causa a saúde e o bem-estar dos animais, as câmaras municipais, quando possível com a '
    'colaboração das autoridades policiais, devem proceder à recolha ou captura dos mesmos, podendo para o efeito '
    'solicitar a emissão de mandado judicial que lhes permita aceder aos locais onde estes se encontrem, '
    'designadamente, veículos, estabelecimentos, casas de habitação e terrenos privados.»\n'
    '[…]\n'
    '«8 - Os animais recolhidos nos termos dos n.ºs anteriores são alojados em centros de recolha, devendo o MVM '
    'ou médico-veterinário do município decidir o destino dos mesmos.»',
    'n.ºs 5 e 8 do art.º 91.º do projeto de RGAC')
cit('«8 - Sempre que o titular ou o detentor se recuse a assumir a qualidade de fiel depositário ou quando aquele '
    'seja desconhecido, a entidade apreensora pode diligenciar no sentido de encaminhar os animais para locais onde '
    'possa estar garantido o seu bem-estar, nomeadamente o retorno ao local de origem, ficando as despesas a cargo '
    'do detentor dos animais.»', 'n.º 8 do art.º 139.º do projeto de RGAC')
cit('«13 - Os animais acolhidos pelos CRO que não sejam reclamados pelos seus no prazo de quinze dias, a contar da '
    'data da sua recolha, presumem-se abandonados e são obrigatoriamente esterilizados e encaminhados para '
    'adoção, sem direito a compensação financeira dos que venham a identificar-se como tal após o prazo previsto no '
    'artigo XX.»', 'n.º 13 do art.º 98.º do projeto de RGAC')
rot('Apreciação.',
    'O projeto passa a recolha por bem-estar da DGAV para as câmaras e a decisão de destino da DGAV para o médico '
    'veterinário municipal. A proposta OMV/ANVETEM assenta no modelo vigente, com a DGAV a decidir. Se o RGAC for '
    'aprovado assim, o procedimento terá de ser refeito. O art.º 139.º regula a apreensão só para '
    'contraordenações, sem articulação com o CPP nem com o RJCE, e admite o «retorno ao local de origem», que '
    'em maus-tratos é o pior destino possível. Essa fórmula vem do DL 315/2009 (art.º 39.º, n.º 8), cujo n.º 1 já '
    'remete a apreensão para o RJCE; o RGAC deixa cair essa remissão. O art.º 98.º, n.º 13 mantém a presunção de 15 dias sem ressalva '
    'para animais apreendidos ou socorridos. O projeto não tem norma sobre emergências nem refere a Lei n.º '
    '38/2026. A DGAV tem vantagem em fazer convergir agora as duas peças: o procedimento e o RGAC. Estes pontos '
    'foram registados no memorando de acompanhamento do RGAC.')

h2('6.2 O Regulamento (UE) 2026/1818')
p('Descrição. O Regulamento, aplicável em regra a partir de 31.8.2028 (art.º 33.º), define abrigo assim:')
cit('«(r) ‘shelter’ means any premises or structure, including households, where unwanted, abandoned, lost, '
    'confiscated or formerly stray dogs or cats are kept for the purpose of placing on the market;»',
    'art.º 4.º, al. r) do Regulamento (UE) 2026/1818 (EN, JO L de 10.8.2026)')
cit('«r) «Abrigo», qualquer instalação ou estrutura, incluindo as casas particulares, onde são detidos cães ou gatos '
    'não desejados, abandonados, perdidos, confiscados ou anteriormente errantes, para efeitos de colocação no '
    'mercado;»', 'art.º 4.º, al. r) do Regulamento (UE) 2026/1818 (PT, JO L de 10.8.2026)')
rot('Apreciação.',
    'A partir de 2028, as entidades que recebam animais confiscados para os encaminhar para adoção serão '
    'operadores de abrigos, com registo e obrigações próprias, e os controlos nos estabelecimentos passam a ser '
    'controlos oficiais nos termos do Regulamento (UE) 2017/625. A bolsa de entidades do âmbito A deve ser '
    'desenhada desde já sobre o registo de estabelecimentos, para não ter de ser refeita. O Regulamento não trata '
    'de emergências nem de apreensões: o âmbito B e a parte penal do âmbito A continuam a ser matéria nacional.')

# ───────────────────────────── 7. Reorganização ─────────────────────────────
h1('7. Proposta de reorganização do texto e próximos passos')
h2('7.1 Estrutura sugerida')
tabela(
    ['Parte', 'Conteúdo', 'Origem'],
    [
        ['Tronco comum', 'Princípios; definições; registo e ficha individual; cadeia de custódia; biossegurança; '
         'relatório; cláusula de salvaguarda; proporcionalidade.', 'Pontos 2, 5.3, 6.4, 6.9, 7.8, 10 da proposta'],
        ['Módulo A (companhia)', 'Matriz de vias legais (liderança e destino); apreensão com permanência no local; '
         'cedência voluntária; eutanásia; SIAC; acumulação; encargos; comunicação por termo de compromisso.',
         'Pontos 3 a 9, reescritos'],
        ['Módulo B (socorro)', 'Integração no SIOPS; representação da DGAV; critérios técnicos para os planos '
         'municipais; reunificação; eutanásia no terreno; voluntários; passagem para o módulo A.',
         'Pontos 3.3, 3.4, 9.1 e 11, reescritos'],
        ['Módulos pecuários', 'Sequestro sanitário, registo de lote, SNIRA, occisão, cadeia alimentar.',
         'Tipologias B e C da proposta'],
        ['Modelos', 'Os seis do Anexo I, mais: auto de apreensão com permanência no local; termo de cedência '
         'voluntária; registo de animal acolhido em emergência.', 'Anexo I'],
        ['Instrumentos de adoção', 'Despacho do diretor-geral (serviços DGAV); protocolo com ANMP, OMV e ANVETEM '
         '(e forças de segurança); termo de compromisso das entidades.', 'Ponto 3.1 desta análise'],
    ],
    larguras=[3.0, 8.5, 4.5])

h2('7.2 Próximos passos')
bullet('Resposta da DGAV à OMV e à ANVETEM, a aceitar o grupo de trabalho e a apresentar a estrutura de 7.1 e as '
       'recomendações R1 a R22 como base de revisão.')
bullet('Designação, em despacho autónomo e sem esperar pelo grupo de trabalho, dos representantes da DGAV '
       'previstos na Lei n.º 38/2026 (R15).')
bullet('Medidas imediatas que dependem só da DGAV: estado «sob apreensão ou custódia» no SIAC (R8); orientação '
       'sobre a presunção de 15 dias (R9); partilha da lista de alojamentos com a proteção civil (R18).')
bullet('Levar as necessidades A1 a A8 e B1 a B6 à revisão do RGAC.')

# ───────────────────────────── Anexo I ─────────────────────────────
h1('Anexo I. Quadro ponto a ponto (animais de companhia)')
tabela(
    ['Ponto', 'Síntese do ponto', 'Apreciação', 'Proposta'],
    [
        ['Princípio 1 e 4.2', 'Comando único da autoridade veterinária.', 'Sem título legal no processo penal, '
         'no DL 314/2003 e no socorro.', 'Matriz por via; direção técnico-veterinária sempre da DGAV.'],
        ['1.2', 'Aplica-se a todas as operações com serviços da DGAV.', 'Excessivo.', 'Aplicar às operações de '
         'que a DGAV é titular; nas restantes, como referência técnica.'],
        ['1.4', 'Processo penal: aplicação subsidiária.', 'Correto, mas a via penal é a regra em maus-tratos.',
         'Submódulo penal próprio.'],
        ['3.1 a 3.2', 'Planeamento obrigatório.', 'Bom.', 'Manter; via urgente simplificada.'],
        ['3.3 a 3.6', 'Planos-tipo, simulacros anuais, inventário.', 'Pesado para a DGAV.',
         'Proporcionalidade; usar relatórios dos CRO.'],
        ['4.1', 'Nenhuma operação sem documento escrito.', 'Bom para operações planeadas.',
         'Cláusula de salvaguarda.'],
        ['4.5', 'Mandado judicial (art.º 19.º, n.º 8).', 'Incompleto.', 'Juntar art.º 67.º-A, Lei 92/95, CPP.'],
        ['5.1', 'Convocação do MVM com 48 h.', 'Com fundamento, mas prevalece o serviço municipal.',
         'Convocar também o presidente da câmara; corrigir a nota sobre o DL 116/98.'],
        ['5.2.2 e 5.2.4', 'Faseamento acima de 50 animais; observação individual.', 'Muito bom.',
         'Juntar título para os animais que ficam (apreensão com fiel depositário).'],
        ['6.1', 'Responsabilidade clínica (art.º 4.º DL 276/2001).', 'Remissão inadequada.', 'Ver 3.3.'],
        ['6.2 e 6.8', 'Eutanásia na triagem.', 'Critério mais largo do que a Lei 27/2016.', 'Ver 4.4, f).'],
        ['6.3', 'Registo no SIAC.', 'Insuficiente.', 'Estado «sob apreensão ou custódia».'],
        ['6.4, 6.9', 'Ficha individual; amostras.', 'Muito bom.', 'Manter.'],
        ['7.1', 'Animais de companhia para CRO.', 'Correto (art.º 19.º, n.º 9).', 'Ressalva da Lei 27/2016; '
         'presunção de 15 dias.'],
        ['7.4 a 7.6', 'Entidade depositária; destino; proibição de cedência.', 'Bom, mas sem identificar a '
         'entidade competente.', 'Matriz de destino por via; cedência voluntária.'],
        ['7.7', 'Encargos à «entidade responsável».', 'Indefinido.', 'Auto diz quem adianta e quem reembolsa; '
         'registo de custos.'],
        ['7.8', 'Inventário em 15 dias.', 'Muito bom.', 'Manter.'],
        ['8', 'Comunicação e reserva.', 'Finalidade legítima; meio sem base legal.',
         'Termo de compromisso; retirar linguagem valorativa.'],
        ['9', 'Credenciação, lista, suspensão.', 'Efeitos externos sem norma habilitante.',
         'Bolsa por protocolo assente em títulos legais.'],
        ['10', 'Relatório em 30 dias.', 'Bom.', 'Manter, com limiar.'],
        ['11', 'Proteção civil.', 'Base certa; falta integração no SIOPS.', 'Ver 5.4 e 5.6.'],
        ['12', 'Grupo de trabalho em 30 dias.', 'Prazo já ultrapassado.', 'Responder com estrutura de 7.1.'],
    ],
    larguras=[1.8, 4.2, 4.6, 5.4], size=8)

# ───────────────────────────── Anexo II ─────────────────────────────
h1('Anexo II. Fontes e estado de verificação')
tabela(
    ['Fonte', 'Onde foi lida', 'Estado'],
    [
        ['Proposta OMV/ANVETEM, v3.0, 26.8.2026', 'repositório: Protocolo de retirada de alojamentos/', 'Lida na íntegra'],
        ['Lei n.º 38/2026, de 3 de agosto', 'DR, 1.ª série, n.º 148, de 3.8.2026 (data.dre.pt, rota ELI)',
         'Texto publicado, conferido'],
        ['Lei n.º 39/2020, de 18 de agosto (CP, CPP, Lei 92/95)', 'DR, 1.ª série, n.º 160, de 18.8.2020 (rota ELI)',
         'Texto publicado, conferido; consolidação posterior do CPP por confirmar'],
        ['Lei n.º 92/95 (versão consolidada)', 'repositório: Legislação vigente/', 'Conferida (inclui Lei 39/2020 e '
         'Lei 6/2022)'],
        ['DL 276/2001 (versão consolidada)', 'repositório: 10a DL 276_2001 - VERSAO ATUALIZADA E CONSOLIDADA.pdf; '
         'versões 2a a 5a para a origem do art.º 19.º', 'Conferido'],
        ['RJCE (DL 9/2021, anexo)', 'repositório: Legislação vigente/ (DR, 1.ª série, n.º 20, de 29.1.2021)',
         'Texto publicado; consolidação por confirmar'],
        ['DL 116/98', 'DR, I série-A, n.º 103, de 5.5.1998 (rota ELI)', 'Texto publicado, conferido'],
        ['SIOPS (DL 90-A/2022)', 'DR, 1.ª série, n.º 251, de 30.12.2022 (rota ELI)', 'Texto publicado, conferido'],
        ['Lei n.º 80/2015 (LBPC republicada)', 'DR, 1.ª série, n.º 149, de 3.8.2015 (rota ELI)', 'Conferida'],
        ['Lei n.º 27/2016; DL 82/2019; RCM 78/2021', 'repositório: Legislação vigente/', 'Conferidos'],
        ['DL 314/2003, arts. 3.º e 9.º', 'repositório: Legislação vigente/ (versão consolidada) e '
         'CHECKPOINT-FOGO-vs-ALOJAMENTO-REGISTADO.md (conferido no DR)', 'Conferido'],
        ['DL 315/2009, arts. 14.º, 15.º, 30.º, 30.º-A e 39.º', 'repositório: Legislação vigente/ (versão consolidada)',
         'Conferido'],
        ['Regulamento (UE) 2026/1818', 'repositório: Regulamento Versao final en-en.pdf e Regulamento '
         '2026_01818_PT.pdf (JO)', 'Conferido'],
        ['Projeto de RGAC', 'repositório: ficheiro ⭐ da tabela 2.1 do CLAUDE.md', 'Proposta, não vigente'],
        ['Requerimento do LIVRE de 13.7.2026', 'repositório: criador informal/REQ 54_7CAPes…pdf', 'Lido'],
    ],
    larguras=[5.0, 7.0, 4.0])

doc.save(SAIDA)
print('Gerado:', SAIDA)
