# -*- coding: utf-8 -*-
"""Gera o contributo da DSBEA ao projeto de DL 405/XXV/2026 (CLAE)."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

AZUL = RGBColor(0x1F, 0x3B, 0x63)
CINZA = RGBColor(0x55, 0x55, 0x55)

doc = Document()
for s in doc.sections:
    s.left_margin = s.right_margin = Cm(2.5)
    s.top_margin = s.bottom_margin = Cm(2.2)

st = doc.styles['Normal']
st.font.name = 'Calibri'
st.font.size = Pt(10.5)
st.paragraph_format.space_after = Pt(6)
st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

def p(txt='', bold=False, italic=False, size=10.5, cor=None, align=None, space=6, left=0):
    par = doc.add_paragraph()
    par.paragraph_format.space_after = Pt(space)
    if left:
        par.paragraph_format.left_indent = Cm(left)
    if align is not None:
        par.paragraph_format.alignment = align
    r = par.add_run(txt)
    r.bold = bold; r.italic = italic; r.font.size = Pt(size)
    if cor is not None:
        r.font.color.rgb = cor
    return par

def h1(txt):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(16); par.paragraph_format.space_after = Pt(6)
    r = par.add_run(txt); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = AZUL

def h2(txt):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(11); par.paragraph_format.space_after = Pt(4)
    r = par.add_run(txt); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = AZUL

def cit(txt, fonte=None):
    par = doc.add_paragraph()
    par.paragraph_format.left_indent = Cm(0.8)
    par.paragraph_format.right_indent = Cm(0.5)
    par.paragraph_format.space_after = Pt(3)
    par.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = par.add_run(txt); r.italic = True; r.font.size = Pt(9.5)
    if fonte:
        f = doc.add_paragraph()
        f.paragraph_format.left_indent = Cm(0.8)
        f.paragraph_format.space_after = Pt(8)
        rf = f.add_run(fonte); rf.font.size = Pt(8.5); rf.font.color.rgb = CINZA

def bullet(txt, nivel=0):
    par = doc.add_paragraph(style='List Bullet' if nivel == 0 else 'List Bullet 2')
    par.paragraph_format.space_after = Pt(3)
    par.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = par.add_run(txt); r.font.size = Pt(10.5)
    return par

def tabela(cabecalho, linhas, larguras=None):
    t = doc.add_table(rows=1, cols=len(cabecalho))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t.rows[0].cells
    for i, c in enumerate(cabecalho):
        hdr[i].text = ''
        par = hdr[i].paragraphs[0]
        par.paragraph_format.space_after = Pt(2)
        r = par.add_run(c); r.bold = True; r.font.size = Pt(9); r.font.color.rgb = AZUL
    for linha in linhas:
        cells = t.add_row().cells
        for i, c in enumerate(linha):
            cells[i].text = ''
            par = cells[i].paragraphs[0]
            par.paragraph_format.space_after = Pt(2)
            par.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            r = par.add_run(c); r.font.size = Pt(9)
    if larguras:
        for row in t.rows:
            for i, w in enumerate(larguras):
                row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return t

# ───────────────────────── Cabeçalho ─────────────────────────
p('DIREÇÃO-GERAL DE ALIMENTAÇÃO E VETERINÁRIA', bold=True, size=9.5, cor=CINZA, space=0,
  align=WD_ALIGN_PARAGRAPH.LEFT)
p('Direção de Serviços de Bem-Estar Animal', size=9.5, cor=CINZA, space=14,
  align=WD_ALIGN_PARAGRAPH.LEFT)

par = doc.add_paragraph(); par.paragraph_format.space_after = Pt(2)
r = par.add_run('CONTRIBUTO'); r.bold = True; r.font.size = Pt(16); r.font.color.rgb = AZUL
par.alignment = WD_ALIGN_PARAGRAPH.LEFT

p('Projeto de Decreto-Lei DL 405/XXV/2026 — Código do Licenciamento das Atividades Económicas (CLAE)',
  bold=True, size=12, space=2, align=WD_ALIGN_PARAGRAPH.LEFT)
p('O que o bem-estar dos animais de companhia pode acrescentar ao diploma', size=11, cor=CINZA,
  space=12, align=WD_ALIGN_PARAGRAPH.LEFT)

tabela(
    ['Campo', 'Elemento'],
    [
        ['Pedido', 'Mensagem de correio eletrónico da Diretora de Serviços de Bem-Estar Animal, de 25.9.2026: «Peço a tua análise tendo em conta a legislação em vigor no âmbito dos animais de companhia».'],
        ['Questão em aberto', 'Terceira questão suscitada na reunião de 24.9.2026 com a SA, CCDR e DGARD, remetida pela Chefe da Divisão de Identificação, Registo e Movimentação Animal: «Animais errantes. Alguém sugeriu a inclusão dos animais errantes na proposta do DL… se faz ou não sentido incluir neste diploma (para todos)».'],
        ['Versão analisada', '«DL 405 XXV 2026_PECUÁRIA_GSEA 25_09_v1.docx» (anexo à mensagem de 25.9.2026), com as alterações e comentários do Gabinete do MAGRIM/G-MECT.'],
        ['Fase do processo', 'Última semana antes da RSE; documento a submeter a consulta pública. Entrada em vigor prevista: 4 de janeiro de 2027 (art.º 19.º, n.º 1, do decreto-lei preambular).'],
        ['Data', '5 de outubro de 2026'],
    ],
    larguras=[3.2, 12.3],
)

# ───────────────────────── 1. Síntese ─────────────────────────
h1('1. Síntese')

p('O CLAE não revoga nem altera qualquer diploma do regime dos animais de companhia, mas revoga o '
  'Decreto-Lei n.º 10/2015, de 16 de janeiro — precisamente o diploma para o qual o n.º 1 do art.º 3.º do '
  'Decreto-Lei n.º 276/2001, de 17 de outubro, remete quanto aos estabelecimentos de comércio a retalho de '
  'animais de companhia. O projeto recolhe essa atividade (lojas de venda de animais vivos) e sujeita-a a '
  'comunicação prévia, com a câmara municipal como entidade coordenadora e a DGDCCS como entidade notificada, '
  'sem qualquer intervenção da DGAV. É o ponto mais sensível do diploma para esta Direção de Serviços.')

bullet('Quanto à questão dos animais errantes: o artigo proposto deve manter-se, mas circunscrito às espécies '
       'pecuárias, onde existe efetivamente um vazio legislativo. Não deve ser estendido aos animais de companhia, '
       'que dispõem de regime próprio e completo e cujo tratamento pelo CLAE geraria contradições materiais '
       '(prazos, destino do animal e proibição de abate como forma de controlo populacional).')
bullet('Quanto ao que o bem-estar dos animais de companhia pode acrescentar: nove contributos, listados no ponto 5 '
       'e resumidos no quadro do ponto 7, dos quais três são indispensáveis — reposição da DGAV no procedimento '
       'das lojas de venda de animais vivos, afastamento do deferimento tácito quando estejam em causa animais '
       'vivos e cláusula expressa de articulação com o regime dos animais de companhia e com o '
       'Regulamento (UE) 2026/1818.')

# ───────────────────────── 2. Nota metodológica ─────────────────────────
h1('2. Nota metodológica')

bullet('A análise parte da legislação vigente consolidada em matéria de animais de companhia — '
       'Decreto-Lei n.º 276/2001, de 17 de outubro, Decreto-Lei n.º 314/2003, de 17 de dezembro, '
       'Decreto-Lei n.º 315/2009, de 29 de outubro, Lei n.º 27/2016, de 23 de agosto, '
       'Lei n.º 8/2017, de 3 de março, Lei n.º 15/2018, de 27 de março, e '
       'Decreto-Lei n.º 82/2019, de 27 de junho — e confronta-a com o articulado do projeto.')
bullet('O Regulamento (UE) 2026/1818 do Parlamento Europeu e do Conselho, de 17 de junho de 2026, relativo ao '
       'bem-estar dos cães e dos gatos e à respetiva rastreabilidade (JO L, 2026/1818, de 10.8.2026), é citado a '
       'partir do texto publicado no Jornal Oficial, nas versões inglesa e portuguesa, ambas autênticas. '
       'É ato de aplicação direta: entrou em vigor no vigésimo dia seguinte ao da publicação e é aplicável, '
       'em regra, a partir de 31 de agosto de 2028, com as datas diferidas do seu art.º 33.º.')
bullet('O projeto de Regime Geral do Animal de Companhia (RGAC), em elaboração nesta Direção-Geral, é referido '
       'como trabalho em curso e nunca como legislação vigente. Serve aqui para demonstrar que as matérias em '
       'causa têm sede própria e para evitar que o CLAE e o RGAC venham a dispor em sentido divergente sobre '
       'o mesmo objeto.')
bullet('Nota sobre a numeração: no articulado do Anexo (CLAE), as epígrafes dos artigos são, em regra, numeradas '
       'automaticamente, mas o bloco da atividade pecuária que vai de «Detenção caseira» a «Sanções acessórias e '
       'apreensão cautelar» tem a numeração escrita manualmente (49.º a 60.º). Em consequência, a numeração '
       'automática retoma em 49.º logo após esse bloco e volta a correr em paralelo, pelo que o ficheiro '
       'apresenta artigos com o mesmo número em secções diferentes (p. ex., dois artigos 55.º — um na pecuária, '
       'outro nos empreendimentos turísticos) e um conjunto de artigos sem texto (49.º a 54.º) na Subsecção IV '
       'da Secção III. Sinaliza-se como lapso formal a corrigir antes da consulta pública. As referências '
       'seguintes indicam sempre a epígrafe, para evitar equívocos.')

# ───────────────────────── 3. Inventário ─────────────────────────
h1('3. O que o projeto já contém em matéria de animais')

p('Levantamento exaustivo das normas do projeto com incidência em animais de companhia ou com relevância para '
  'as atribuições desta Direção de Serviços:')

tabela(
    ['Norma do CLAE (Anexo)', 'Conteúdo', 'Observação'],
    [
        ['Art.º 38.º — «Acesso de animais de companhia»\n(Título I, Capítulo IV)',
         'Permanência de animais de companhia em espaços fechados, mediante dístico; trela curta; interdição da '
         'área de serviço e dos locais de exposição de alimentos; recusa de acesso; cães de assistência sempre '
         'admitidos.',
         'Reproduz, no essencial, o art.º 132.º-A do Decreto-Lei n.º 10/2015, aditado pela Lei n.º 15/2018, '
         'mas transfere-o para a parte geral, passando a abranger todas as atividades do CLAE e não apenas o '
         'comércio e a restauração. Alargamento positivo.'],
        ['Art.º 16.º, n.º 4 — comunicação prévia',
         '«A exploração de estabelecimentos de comércio a retalho de animais de companhia e respetivos alimentos, '
         'em estabelecimentos especializados» (CAE 47762, lista II do anexo I).',
         'Atividade que recebe, por sucessão, a disciplina do Decreto-Lei n.º 10/2015, ora revogado pela al. j) '
         'do n.º 1 do art.º 8.º do decreto-lei preambular. Ver ponto 5.1.'],
        ['Anexo II — entidades intervenientes',
         'Para a atividade anterior: entidade coordenadora — a câmara municipal territorialmente competente; '
         'entidades públicas consultadas — nenhuma; entidade notificada — a DGDCCS.',
         'A DGAV não é consultada nem notificada. É consultada, em contrapartida, no comércio de alimentos para '
         'animais de criação (al. f) do n.º 2 do art.º 16.º). Assimetria a corrigir.'],
        ['Art.º 48.º, al. b) — «Animal de espécie pecuária»',
         'Inclui «a produção pecuária de animais destinados a animais de companhia, de trabalho ou a atividades '
         'culturais ou desportivas».',
         'Reproduz o art.º 2.º do Decreto-Lei n.º 81/2013 (NREAP), acrescentando os insetos. Não é inovação, '
         'mas mantém em aberto a fronteira com o regime dos animais de companhia. Ver ponto 5.6.'],
        ['Art.º 48.º, al. l) — «Estabelecimento pecuário»',
         'Exclui «casas particulares onde sejam detidos animais de companhia e consultórios ou clínicas '
         'veterinárias».',
         'Exclusão correta e a manter. Note-se que o Regulamento (UE) 2026/1818 qualifica como estabelecimento, '
         'justamente, certas casas particulares onde se criam ou detêm cães e gatos para colocação no mercado.'],
        ['Art.º 49.º — «Detenção caseira»',
         'Capacidade instalada até 3 CN, com o máximo de 2 CN por espécie pecuária; isenta de licenciamento, '
         'mas sujeita a registo no SNIRA.',
         'Novidade relevante: o preâmbulo assume que «a detenção caseira passará a estar sujeita ao registo para '
         'efeitos de Sistema Nacional de Informação e Registo Animal (SNIRA)». Com impacto em espécies detidas '
         'como animais de companhia. Ver ponto 5.6.'],
        ['Art.º 59.º — «Recolha de animais errantes»\n(Subsecção IV, Secção III)',
         'Remoção do animal de espécie pecuária encontrado errante em via pública, espaço público ou '
         'infraestrutura de transporte; notificação do detentor; prazo de cinco dias úteis; despesas a cargo do '
         'detentor; destino determinado pelo município em articulação com a DGAV.',
         'Artigo novo, inserido na sequência da questão colocada na reunião de 24.9.2026. Ver ponto 4.'],
        ['Art.º 153.º, n.º 1 — atividade leiloeira',
         'Abrange a «venda de bens móveis e imóveis, corpóreos e incorpóreos ou de animais».',
         'Sem qualquer requisito de bem-estar, identificação ou rastreabilidade. Ver ponto 5.4.'],
        ['Art.º 133.º, n.º 2 — comércio não sedentário',
         'Elenco de produtos cuja venda a retalho não sedentária é proibida.',
         'Não inclui animais vivos. Ver ponto 5.4.'],
        ['Art.º 176.º, n.º 2 — restauração',
         'Proíbe «a entrada e permanência de animais vivos» nas zonas da área de serviço.',
         'Coerente com o art.º 38.º e com as regras de higiene dos géneros alimentícios.'],
        ['Art.º 183.º, al. c) — informação ao público',
         'Obriga a informar sobre «a permissão ou a não permissão de admissão de animais de companhia, caso seja '
         'aplicável, excetuando os cães de assistência».',
         'Adequado.'],
        ['Art.º 36.º, n.º 3 — condições de exercício',
         '«Os operadores económicos devem obedecer à legislação específica aplicável aos produtos que '
         'comercializam.»',
         'Cláusula de salvaguarda insuficiente: o animal não é um produto. A Lei n.º 8/2017, de 3 de março, '
         'reconhece-lhe estatuto jurídico próprio, de ser vivo dotado de sensibilidade. Ver ponto 5.3.'],
    ],
    larguras=[4.2, 5.6, 5.7],
)

p('Não há no projeto qualquer referência ao Decreto-Lei n.º 276/2001, de 17 de outubro, aos alojamentos de '
  'animais de companhia, aos centros de recolha oficial, ao SIAC ou ao Regulamento (UE) 2026/1818.',
  bold=True)

# ───────────────────────── 4. Errantes ─────────────────────────
h1('4. Resposta à questão dos animais errantes')

h2('4.1. O artigo proposto e o seu alcance')

p('O artigo inserido no projeto tem o seguinte teor, no seu n.º 1:')
cit('«1 – O animal de espécie pecuária encontrado errante, desacompanhado ou sem estar sob o controlo do '
    'respetivo detentor em via pública, espaço público ou em infraestrutura de transporte rodoviário ou '
    'ferroviário, é retirado pela entidade competente no local em causa, por iniciativa própria ou mediante '
    'intervenção das autoridades policiais, e impreterivelmente nas situações em que a presença dos animais '
    'constitua um perigo atual ou iminente para a circulação, para a segurança de pessoas e bens ou para o '
    'próprio animal.»',
    'n.º 1 do art.º 59.º («Recolha de animais errantes») do CLAE, na versão de 25.9.2026.')

p('O âmbito é, pois, o animal de espécie pecuária. O vazio legislativo assinalado na reunião de 24.9.2026 '
  'existe e é real — mas é do lado pecuário: a recolha de gado deambulante em via pública não tem hoje sede '
  'legal expressa, ao contrário do que sucede com cães e gatos. O artigo colmata essa lacuna e, nessa medida, '
  'merece acolhimento.')

h2('4.2. O artigo não deve ser estendido aos animais de companhia')

p('A inclusão dos animais de companhia neste diploma («para todos») não é aconselhável, por quatro ordens de '
  'razões:')

bullet('Existe regime próprio e vigente. A al. c) do n.º 1 do art.º 2.º do Decreto-Lei n.º 276/2001, de 17 de '
       'outubro, define «animal vadio ou errante» e o seu art.º 19.º atribui às câmaras municipais a recolha e a '
       'captura, prevendo o acolhimento em centro de recolha oficial, a entrega ao detentor contra pagamento das '
       'despesas de manutenção e a cedência dos animais não reclamados. O art.º 21.º comete às câmaras '
       'municipais o controlo da reprodução de cães e gatos vadios ou errantes. A Lei n.º 27/2016, de 23 de '
       'agosto, proíbe o abate como forma de controlo da população e cria a rede de centros de recolha oficial. '
       'O Decreto-Lei n.º 82/2019, de 27 de junho, assegura a identificação e o registo no SIAC, instrumento '
       'determinante para devolver o animal ao titular.')
bullet('O artigo proposto, aplicado a cães e gatos, contraria esse regime. O prazo de cinco dias úteis do seu '
       'n.º 3 é inferior ao período mínimo de permanência em centro de recolha oficial e aos prazos praticados '
       'para os animais não reclamados; e o n.º 5, ao remeter a determinação do destino para o município «em '
       'articulação com a DGAV», sem mais, abriria uma via paralela à que resulta da Lei n.º 27/2016 e das '
       'regras de esterilização e adoção. Qualquer leitura que fizesse prevalecer o CLAE equivaleria a uma '
       'revogação implícita de regras aprovadas pela Assembleia da República.')
bullet('A remissão para o regime das medidas administrativas é inaceitável quanto a animais de companhia. '
       'O n.º 4 do art.º 57.º («Medidas administrativas») determina que os animais apreendidos, não havendo '
       'condições de manutenção nem fiel depositário, sejam «conduzidos ao matadouro e abatidos, caso sejam '
       'aprovados para consumo» ou «destruídos nos termos da legislação em vigor». A solução faz sentido para '
       'efetivos pecuários; é contrária à lei vigente se aplicada a cães e gatos.')
bullet('A matéria está a ser objeto de revisão integrada. A recolha de animais errantes de companhia, a gestão '
       'dos centros de recolha oficial, os programas de captura, esterilização e devolução e o registo no SIAC '
       'estão a ser consolidados no projeto de RGAC, com o qual o CLAE deve articular-se e não concorrer.')

h2('4.3. O que deve, ainda assim, ser corrigido no próprio artigo')

p('Confirmando-se o artigo circunscrito às espécies pecuárias, subsistem três insuficiências que afetam '
  'diretamente as atribuições desta Direção de Serviços e os municípios:')

bullet('Onde é alojado o animal. O artigo não identifica a instalação de destino. Na prática, como foi '
       'assinalado na própria cadeia de correio eletrónico, muitos centros de recolha oficial de animais '
       'municipais já asseguram essa recolha e alojamento «por força das circunstâncias». Ora, o centro de '
       'recolha oficial é, por definição legal, alojamento oficial de animais de companhia — a al. t) do n.º 1 '
       'do art.º 2.º do Decreto-Lei n.º 276/2001 refere «nomeadamente os canis e os gatis municipais» — e não '
       'está dimensionado nem sanitariamente concebido para equídeos, bovinos ou ovinos. Propõe-se que o artigo '
       'identifique expressamente o alojamento adequado à espécie e que, quando recorra a instalação municipal, '
       'exija recinto próprio, separado e compatível com as normas sanitárias e de bem-estar aplicáveis à '
       'espécie, sem prejuízo das funções do centro de recolha oficial quanto aos animais de companhia.')
bullet('Quem suporta o custo quando o detentor não é identificado. O n.º 6 imputa as despesas ao detentor ou '
       'proprietário «quando identificada»; nos demais casos, o encargo recai sobre o município sem previsão de '
       'compensação, agravando a pressão sobre meios que a Lei n.º 27/2016 afetou aos animais de companhia.')
bullet('Articulação sanitária. A reintrodução do animal na exploração depende, nos termos do n.º 4, da '
       'regularização da identificação e do registo e do cumprimento das medidas sanitárias e de bem-estar '
       'determinadas pela autoridade competente, o que é correto; deve explicitar-se que essa autoridade é a '
       'DGAV e que o registo relevante é o SNIRA, por remissão para o Decreto-Lei n.º 142/2006, de 27 de julho, '
       'já referido na al. d) do art.º 2.º do CLAE.')

h2('4.4. Proposta de redação')

p('Sugere-se o aditamento de um número ao artigo, com a seguinte redação:')
cit('«[n.º] – O disposto no presente artigo não prejudica o regime aplicável aos animais de companhia '
    'encontrados errantes, designadamente o previsto no Decreto-Lei n.º 276/2001, de 17 de outubro, e na '
    'Lei n.º 27/2016, de 23 de agosto, nem o regime das medidas administrativas previsto nos artigos anteriores '
    'é aplicável a animais de companhia.»',
    'Proposta de aditamento ao art.º 59.º do CLAE.')

p('E, no n.º 2 do art.º 57.º e no n.º 4 do mesmo artigo, a inserção da expressão «de espécie pecuária» após '
  '«animais», de modo a tornar inequívoco que as medidas de abate ou destruição não alcançam animais de '
  'companhia eventualmente presentes no local.')

# ───────────────────────── 5. Contributos ─────────────────────────
h1('5. O que o bem-estar dos animais de companhia pode acrescentar')

h2('5.1. Lojas de venda de animais vivos: reposição da intervenção da DGAV (prioritário)')

p('O n.º 1 do art.º 3.º do Decreto-Lei n.º 276/2001, de 17 de outubro, começa por ressalvar: '
  '«Sem prejuízo do disposto no Decreto-Lei n.º 10/2015, de 16 de janeiro, quanto aos estabelecimentos de '
  'comércio a retalho de animais de companhia, o exercício da atividade de exploração de alojamentos, bem como '
  'a atividade de criação comercial de animais de companhia depende de: […]». A al. j) do n.º 1 do art.º 8.º do '
  'decreto-lei preambular revoga o Decreto-Lei n.º 10/2015. A remissão passa, assim, a dirigir-se a diploma '
  'revogado, operando a regra do n.º 4 do mesmo art.º 8.º («As remissões […] para normas ora revogadas '
  'consideram-se feitas, com as devidas adaptações, para o presente decreto-lei»). O resultado é que a '
  'disciplina do licenciamento das lojas de venda de animais vivos fica inteiramente no CLAE.')

p('No CLAE, porém, essa atividade é sujeita a comunicação prévia, tem a câmara municipal como entidade '
  'coordenadora, nenhuma entidade pública consultada e a DGDCCS como entidade notificada. Significa que a '
  'autoridade sanitária veterinária nacional — que a al. x) do n.º 1 do art.º 2.º do Decreto-Lei n.º 276/2001 '
  'identifica como autoridade competente — deixa de ter conhecimento da abertura de um estabelecimento que detém '
  'animais vivos para venda.')

p('A consequência é tanto mais relevante quanto, a partir de 31 de agosto de 2028, a loja de animais passa a '
  'ser, para o direito da União, um «estabelecimento de venda» sujeito a notificação e registo junto da '
  'autoridade competente:')

cit('«1. Operators shall notify the competent authorities of their activity, providing at least the following '
    'information for each of their establishments: (a) the name, address and contact details of the operator; '
    '(b) the location of the establishment; (c) the type of establishment: breeding establishment, selling '
    'establishment, shelter or foster home; […] 4. The competent authority shall keep a register of '
    'establishments.»',
    'art.º 9.º, n.ºs 1 e 4, do Regulamento (UE) 2026/1818 — versão inglesa (JO L, 2026/1818, de 10.8.2026).')
cit('«1. Os operadores notificam as autoridades competentes da sua atividade, facultando pelo menos as '
    'seguintes informações para cada um dos seus estabelecimentos: a) O nome, o endereço e dados de contacto do '
    'operador; b) A localização do estabelecimento; c) O tipo de estabelecimento: estabelecimento de criação, '
    'estabelecimento de venda, abrigo ou lar de acolhimento; […] 4. A autoridade competente deve manter um '
    'registo de estabelecimentos.»',
    'art.º 9.º, n.ºs 1 e 4, do Regulamento (UE) 2026/1818 — versão portuguesa (JO L, 2026/1818, de 10.8.2026).')

p('A al. q) do art.º 4.º do mesmo Regulamento define «estabelecimento de venda» como «qualquer instalação ou '
  'estrutura onde cães ou gatos são detidos para venda sem aí terem nascido, incluindo lojas de animais de '
  'companhia ou casas particulares», e o considerando 23 esclarece que, atenta a natureza exclusivamente '
  'comercial destes estabelecimentos, não se fixam limiares, aplicando-se os requisitos a todos eles, '
  'independentemente do número de cães ou gatos detidos.')

p('Propostas:', bold=True)
bullet('Aditar a DGAV à coluna «Entidades públicas consultadas» do Anexo II, na linha relativa à exploração de '
       'estabelecimentos de comércio a retalho de animais de companhia e respetivos alimentos, em '
       'estabelecimentos especializados; em alternativa mínima, à coluna «Entidades notificadas», a par da '
       'DGDCCS. Note-se que, para o comércio de alimentos para animais de criação, a DGAV já é consultada '
       '(al. f) do n.º 2 do art.º 16.º); não se compreende que o seja quanto à ração e não quanto ao animal.')
bullet('Prever que o título digital de atividade económica desta atividade não dispensa o cumprimento das '
       'obrigações relativas aos animais detidos, nem a comunicação à DGAV, e que a entidade coordenadora remete '
       'a esta os elementos relativos à espécie, número e capacidade máxima de animais a deter — informação '
       'que, de outro modo, nenhuma autoridade sanitária recolherá.')

h2('5.2. Deferimento tácito: afastamento quando estejam em causa animais vivos (prioritário)')

p('O preâmbulo do projeto assume «consagrar como regra o deferimento tácito, sustentado pela confiança e '
  'responsabilidade dos operadores económicos», concretizado no art.º 25.º do CLAE. A solução é incompatível '
  'com a verificação prévia que o direito da União impõe a certos estabelecimentos com animais vivos:')

cit('«1. Operators of breeding establishments that either produce or intend to produce more than five litters '
    'per calendar year or that keep more than a combined total of five bitches or queens at any given time '
    'shall place dogs or cats on the market only after their breeding establishment has been approved by the '
    'competent authority.»',
    'art.º 10.º, n.º 1, do Regulamento (UE) 2026/1818 — versão inglesa.')
cit('«1. Os operadores de estabelecimentos de criação que produzam ou tencionem produzir mais de cinco ninhadas '
    'por ano civil, ou que, a qualquer momento, detenham um total combinado de mais de cinco cadelas '
    'reprodutoras ou gatas reprodutoras, só podem colocar cães ou gatos no mercado após aprovação do seu '
    'estabelecimento de criação pela autoridade competente.»',
    'art.º 10.º, n.º 1, do Regulamento (UE) 2026/1818 — versão portuguesa.')

p('O n.º 2 do mesmo artigo exige inspeções no local e só permite a concessão de certificados de aprovação a '
  'estabelecimentos conformes. Em sentido convergente, o projeto de RGAC exclui expressamente o deferimento '
  'tácito no procedimento de permissão administrativa dos estabelecimentos. Propõe-se que o CLAE ressalve, no '
  'art.º 25.º, que não há deferimento tácito quando a atividade envolva a detenção, criação ou venda de animais '
  'vivos e dependa de ato permissivo da DGAV.')

h2('5.3. Cláusula expressa de articulação (prioritário)')

p('O art.º 2.º do CLAE enumera os regimes com que os procedimentos se articulam, incluindo já, na al. d), o '
  'Decreto-Lei n.º 142/2006, de 27 de julho. Propõe-se o aditamento de uma alínea com o regime de proteção dos '
  'animais de companhia, aprovado pelo Decreto-Lei n.º 276/2001, de 17 de outubro, e de referência ao '
  'Regulamento (UE) 2026/1818. Em paralelo, o n.º 3 do art.º 36.º deve deixar de tratar o animal como produto, '
  'aditando-se menção autónoma às obrigações aplicáveis aos animais vivos detidos ou comercializados, em '
  'coerência com o estatuto jurídico que lhes reconhece a Lei n.º 8/2017, de 3 de março.')

p('Recorde-se que o Regulamento admite expressamente normas nacionais mais exigentes:')
cit('«1. This Regulation shall not prevent Member States from maintaining or adopting stricter national rules '
    'aimed at providing more extensive protection of the welfare of dogs and cats kept in establishments, and a '
    'greater traceability of dogs and cats, provided that those rules are not inconsistent with this Regulation '
    'and do not interfere with the proper functioning of the internal market.»',
    'art.º 30.º, n.º 1, do Regulamento (UE) 2026/1818 — versão inglesa.')
cit('«1. O presente regulamento não obsta a que os Estados-Membros mantenham ou adotem regras nacionais mais '
    'restritivas que visem uma proteção mais ampla do bem-estar dos cães e gatos detidos em estabelecimentos e '
    'uma maior rastreabilidade dos cães e gatos, desde que essas regras não sejam incompatíveis com o presente '
    'regulamento e não interfiram com o correto funcionamento do mercado interno.»',
    'art.º 30.º, n.º 1, do Regulamento (UE) 2026/1818 — versão portuguesa.')

h2('5.4. Venda de animais em comércio não sedentário, feiras e leilões')

p('O n.º 2 do art.º 133.º do CLAE proíbe a venda a retalho não sedentária de produtos fitofarmacêuticos, '
  'medicamentos, aditivos para alimentos para animais, armas e munições, combustíveis, moedas e notas e '
  'veículos; não proíbe a venda de animais vivos. Acresce que o n.º 2 do art.º 2.º do Decreto-Lei n.º 276/2001 '
  'exclui do conceito de «alojamento» os locais de venda em feiras ou mercados, pelo que a venda de animais '
  'nesses locais não está sujeita aos requisitos de alojamento. O resultado conjugado é um regime mais '
  'permissivo para a modalidade de venda que oferece menores garantias de bem-estar e de rastreabilidade.')

p('De igual modo, o n.º 1 do art.º 153.º inclui na atividade leiloeira a venda «de animais», sem qualquer '
  'exigência de identificação, registo ou informação ao adquirente, quando o art.º 21.º, n.º 3, do '
  'Regulamento (UE) 2026/1818 obriga quem coloca um cão ou gato no mercado a facultar ao adquirente prova da '
  'identificação e do registo e as informações sobre espécie, sexo, data e país de nascimento e, se for o caso, '
  'raça.')

p('Propostas:', bold=True)
bullet('Aditar ao n.º 2 do art.º 133.º a proibição da venda a retalho não sedentária de animais de companhia, '
       'possibilidade que o art.º 30.º do Regulamento expressamente comporta, ou sujeitá-la a autorização '
       'prévia da DGAV.')
bullet('Excluir os animais vivos do objeto da atividade leiloeira ou, mantendo-se, subordinar expressamente a '
       'sua venda ao cumprimento do regime dos animais de companhia e, quanto a cães e gatos, das obrigações '
       'do art.º 21.º do Regulamento (UE) 2026/1818.')

h2('5.5. Venda e publicidade em linha')

p('O n.º 4 do art.º 1.º do CLAE estende os requisitos gerais de acesso e exercício às atividades exercidas por '
  'via eletrónica. O n.º 1 do art.º 1.º do Decreto-Lei n.º 276/2001 já abrange a venda de animais de companhia '
  '«presencialmente ou através de meios eletrónicos». O Regulamento (UE) 2026/1818 acrescenta, no seu '
  'art.º 21.º, a advertência obrigatória nos anúncios em linha, a ficha de verificação única e os deveres dos '
  'fornecedores de plataformas em linha, aplicáveis o n.º 3 a partir de 31 de agosto de 2030. Propõe-se que o '
  'CLAE remeta expressamente para esse regime quando a atividade de comércio a retalho de animais de companhia '
  'seja exercida por via eletrónica, evitando que o título digital de atividade económica seja lido como '
  'habilitação bastante.')

h2('5.6. Fronteira entre «detenção caseira» e animal de companhia')

p('A al. i) do art.º 48.º define «detenção caseira» como a detenção de um número reduzido de espécies pecuárias '
  'não cinegéticas cuja posse «tem o objetivo de lazer ou abastecimento do seu detentor», sujeitando-a a '
  'registo no SNIRA. Há espécies simultaneamente pecuárias e de companhia — leporídeos, aves, equídeos, '
  'pequenos roedores — detidas, em muitos casos, exclusivamente para fins de companhia. Para essas, cria-se '
  'uma dupla sujeição potencial: registo no SNIRA, por força do CLAE, e enquadramento como animal de companhia. '
  'Note-se que o n.º 2 do art.º 1.º do Decreto-Lei n.º 276/2001 exclui do seu âmbito «as espécies de pecuária», '
  'pelo que, hoje, um coelho detido como animal de companhia não beneficia das normas de alojamento e '
  'bem-estar daquele diploma — lacuna que o projeto de RGAC resolve por via de um critério finalista, '
  'qualificando como animais de companhia os das espécies da Parte B do Anexo I do Regulamento (UE) 2016/429 '
  '«quando detidos para fins de companhia».')

p('Propõe-se que o CLAE adote o mesmo critério finalista, esclarecendo que a detenção de animais das espécies '
  'pecuárias exclusivamente para fins de companhia, sem destino produtivo nem colocação no mercado, não '
  'constitui atividade pecuária para efeitos do Código, sem prejuízo das obrigações de identificação e registo '
  'e das medidas sanitárias determinadas pela DGAV. Trata-se de clarificação de legística, com ganho imediato '
  'de simplificação para o detentor — alinhada com o próprio objetivo do diploma.')

h2('5.7. Melhorias ao art.º 38.º (acesso de animais de companhia)')

bullet('O n.º 3 deve remeter expressamente para o Decreto-Lei n.º 74/2007, de 27 de março, relativo ao direito '
       'de acesso das pessoas com deficiência acompanhadas de cães de assistência, de modo a que a norma não '
       'seja lida como fonte autónoma do direito de acesso nem como permitindo a sua restrição pelo operador.')
bullet('A al. c) do n.º 1 deve ressalvar o disposto no Regulamento (CE) n.º 852/2004 quanto às zonas de '
       'manipulação de géneros alimentícios, para evitar divergência interpretativa com o n.º 2 do art.º 176.º.')
bullet('Deve clarificar-se que a faculdade reconhecida à entidade exploradora não prejudica a legislação sobre '
       'animais perigosos e potencialmente perigosos, aprovada pelo Decreto-Lei n.º 315/2009, de 29 de outubro, '
       'designadamente quanto ao uso de açaime funcional.')

h2('5.8. Cadastro setorial e bases de dados')

p('O capítulo relativo à base de dados setorial (art.ºs 198.º a 200.º) e o art.º 15.º do decreto-lei preambular '
  'enumeram os sistemas a articular, sem incluir o SIAC. Sendo o SIAC a base de dados oficial de identificação '
  'e registo dos animais de companhia, e devendo Portugal assegurar, nos termos do art.º 23.º do '
  'Regulamento (UE) 2026/1818, bases de dados nacionais interoperáveis, propõe-se que o SIAC seja referido como '
  'sistema a articular, pelo menos quanto às atividades que envolvam a detenção ou a venda de animais de '
  'companhia. O n.º 3 do art.º 30.º do CLAE, que já prevê a disponibilização da informação do título digital à '
  'ASAE e à DGAV, é a base adequada para essa articulação.')

h2('5.9. Fiscalização e medidas cautelares')

p('O art.º 190.º do CLAE permite a adoção de medidas cautelares quando exista «risco grave ou iminente para a '
  'saúde e a segurança das pessoas e da cadeia alimentar, bens, animais ou para o ambiente». Propõe-se que, '
  'nas atividades que envolvam animais de companhia, se preveja a comunicação imediata à DGAV e ao médico '
  'veterinário municipal e que o destino dos animais apreendidos siga o regime dos animais de companhia, e não '
  'o do n.º 3 do mesmo artigo, que remete para o abate ou destruição próprios do efetivo pecuário.')

# ───────────────────────── 6. Calendário ─────────────────────────
h1('6. Calendário a considerar')

tabela(
    ['Data', 'Evento', 'Relevância'],
    [
        ['4.1.2027', 'Entrada em vigor prevista do CLAE (art.º 19.º, n.º 1, do decreto-lei preambular).',
         'Anterior ao início de aplicação do Regulamento (UE) 2026/1818, mas o CLAE não pode desde já consagrar '
         'soluções que o contrariem, sob pena de ter de ser revisto logo em 2028.'],
        ['31.8.2028', 'Regra geral de aplicação do Regulamento (UE) 2026/1818 (art.º 33.º).',
         'Notificação e registo dos estabelecimentos (art.º 9.º), princípios e obrigações gerais de bem-estar, '
         'identificação e registo de cães e gatos (art.º 20.º). Prazo igualmente fixado para a comunicação à '
         'Comissão das regras nacionais mais restritivas a manter (art.º 30.º, n.º 2).'],
        ['31.8.2029', 'Art.º 16.º (saúde).', 'Requisitos aplicáveis aos estabelecimentos.'],
        ['31.8.2030', 'Art.º 21.º, n.º 3, e art.º 23.º, n.º 1; art.º 8.º, n.º 2, a 1.7.2030.',
         'Prova de identificação e registo na colocação no mercado, ficha de verificação em linha e bases de '
         'dados nacionais.'],
        ['31.8.2031', 'Art.ºs 15.º, 21.º, n.ºs 4 e 5, 22.º, n.º 1, als. a) a c), 23.º, n.ºs 3 e 4, e 26.º, n.ºs 1 a 3.',
         'Alojamento, plataformas em linha, formação e entrada de animais na União.'],
        ['31.8.2033 / 31.8.2034 / 1.7.2036 / 31.8.2036',
         'Art.º 12.º, n.ºs 2 e 3; art.º 10.º; art.º 8.º, n.º 1; art.º 26.º, n.º 4.',
         'Competências dos tratadores; aprovação dos estabelecimentos de criação; estratégia de criação; entrada '
         'na União.'],
    ],
    larguras=[2.6, 6.0, 6.9],
)

p('Sublinha-se a distinção: o Regulamento está em vigor, mas não é ainda aplicável. A circunstância não '
  'dispensa o legislador nacional de assegurar, desde já, a compatibilidade do CLAE com as obrigações que se '
  'tornarão aplicáveis — em especial a notificação e o registo dos estabelecimentos de venda, que o projeto, '
  'na redação atual, afasta da autoridade competente.')

# ───────────────────────── 7. Quadro-resumo ─────────────────────────
h1('7. Quadro-resumo das propostas')

tabela(
    ['#', 'Norma', 'Problema', 'Proposta', 'Prioridade'],
    [
        ['1', 'Anexo II (comércio a retalho de animais de companhia) e art.º 16.º, n.º 4',
         'A DGAV não é consultada nem notificada na abertura de lojas de venda de animais vivos; a remissão do '
         'art.º 3.º, n.º 1, do DL 276/2001 passa a apontar para diploma revogado.',
         'Aditar a DGAV às entidades públicas consultadas (ou, no mínimo, às notificadas) e prever a remessa dos '
         'elementos sobre espécies, número e capacidade máxima de animais.',
         'Indispensável'],
        ['2', 'Art.º 25.º (deferimento tácito)',
         'Incompatível com a aprovação prévia e as inspeções no local exigidas pelo art.º 10.º do '
         'Regulamento (UE) 2026/1818.',
         'Ressalvar a inexistência de deferimento tácito quando a atividade envolva detenção, criação ou venda de '
         'animais vivos e dependa de ato permissivo da DGAV.',
         'Indispensável'],
        ['3', 'Art.º 2.º e art.º 36.º, n.º 3',
         'Ausência de articulação com o regime dos animais de companhia; o animal é tratado como «produto».',
         'Aditar o DL 276/2001 ao art.º 2.º, referir o Regulamento (UE) 2026/1818 e autonomizar, no art.º 36.º, '
         'as obrigações relativas a animais vivos.',
         'Indispensável'],
        ['4', 'Art.º 59.º («Recolha de animais errantes») e art.º 57.º',
         'Risco de aplicação a animais de companhia; instalação de destino não identificada; regime de abate ou '
         'destruição.',
         'Manter o artigo circunscrito às espécies pecuárias, aditar cláusula de não prejuízo do regime dos '
         'animais de companhia, identificar o alojamento adequado à espécie e excluir os animais de companhia '
         'das medidas de abate.',
         'Elevada'],
        ['5', 'Art.º 133.º, n.º 2, e art.º 153.º, n.º 1',
         'Venda de animais vivos em comércio não sedentário e em leilão sem requisitos de bem-estar ou '
         'rastreabilidade.',
         'Proibir a venda não sedentária de animais de companhia ou sujeitá-la a autorização da DGAV; excluir os '
         'animais vivos da atividade leiloeira ou subordiná-la ao art.º 21.º do Regulamento.',
         'Elevada'],
        ['6', 'Art.º 48.º, al. i), e art.º 49.º («Detenção caseira»)',
         'Espécies pecuárias detidas exclusivamente para fins de companhia ficam sujeitas a registo no SNIRA e '
         'fora das normas de bem-estar dos animais de companhia.',
         'Adotar critério finalista: a detenção exclusivamente para fins de companhia, sem destino produtivo nem '
         'colocação no mercado, não constitui atividade pecuária para efeitos do Código.',
         'Média'],
        ['7', 'Art.º 1.º, n.º 4 (atividades por via eletrónica)',
         'Venda e publicidade de animais em linha sem remissão para as obrigações aplicáveis.',
         'Remeter expressamente para o regime dos animais de companhia e para o art.º 21.º do '
         'Regulamento (UE) 2026/1818.',
         'Média'],
        ['8', 'Art.º 38.º («Acesso de animais de companhia»)',
         'Falta de remissão para o DL 74/2007 e para o DL 315/2009; articulação com as regras de higiene '
         'alimentar.',
         'Aditar as remissões e ressalvar o Regulamento (CE) n.º 852/2004.',
         'Média'],
        ['9', 'Art.ºs 198.º a 200.º e art.º 15.º do decreto-lei preambular',
         'O SIAC não consta dos sistemas a articular com o cadastro setorial.',
         'Incluir o SIAC, pelo menos quanto às atividades que envolvam detenção ou venda de animais de companhia.',
         'Média'],
        ['10', 'Numeração do Anexo (Secção III)',
         'Numeração manual sobreposta à automática: artigos repetidos e artigos sem texto (49.º a 54.º).',
         'Correção formal antes da consulta pública.',
         'Formal'],
    ],
    larguras=[0.8, 3.1, 4.0, 4.6, 2.0],
)

# ───────────────────────── 8. Observações ─────────────────────────
h1('8. Observações')

p('As apreciações que seguem são deduções e juízos de oportunidade desta Direção de Serviços, distintas da '
  'análise descritiva que antecede.', italic=True)

bullet('A resposta curta à questão colocada é: o diploma não precisa de passar a regular os animais de '
       'companhia; precisa de deixar de os desregular. O risco principal do CLAE não está no que diz sobre '
       'animais de companhia, mas no que deixa de dizer ao revogar o Decreto-Lei n.º 10/2015 e ao recolher a '
       'atividade de venda de animais vivos num procedimento puramente municipal.')
bullet('Se apenas uma proposta puder ser acolhida, deve ser a inclusão da DGAV no procedimento das lojas de '
       'venda de animais vivos. É a alteração de menor custo administrativo — uma linha do Anexo II — e a de '
       'maior efeito prático, tanto para a fiscalização como para o cumprimento, a partir de 2028, do '
       'Regulamento (UE) 2026/1818.')
bullet('A inclusão dos animais errantes de companhia neste diploma, além de materialmente inadequada, '
       'antecipar-se-ia a opções que estão a ser tomadas na revisão integrada do regime dos animais de '
       'companhia, com risco de o CLAE ser revisto poucos meses depois de entrar em vigor.')
bullet('Recomenda-se que esta Direção de Serviços seja formalmente associada aos trabalhos, como aliás foi '
       'sugerido na própria cadeia de correio eletrónico, e que o contributo seja igualmente apresentado em '
       'sede de consulta pública, de modo a ficar documentado.')

doc.save('/home/user/Legislacao/DL 405_2026/Contributo_BEA_DL405_XXV_2026_CLAE.docx')
print('OK')
