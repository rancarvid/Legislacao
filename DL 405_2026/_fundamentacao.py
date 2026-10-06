# -*- coding: utf-8 -*-
"""Fundamentação detalhada das observações ao DL das atividades económicas (DL 405/XXV/2026)."""
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


def p(txt='', bold=False, italic=False, size=10.5, cor=None, space=6, left=0):
    par = doc.add_paragraph()
    par.paragraph_format.space_after = Pt(space)
    if left:
        par.paragraph_format.left_indent = Cm(left)
    r = par.add_run(txt)
    r.bold = bold; r.italic = italic; r.font.size = Pt(size)
    if cor is not None:
        r.font.color.rgb = cor
    return par


def h1(txt):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(18); par.paragraph_format.space_after = Pt(6)
    r = par.add_run(txt); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = AZUL


def h2(txt):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(12); par.paragraph_format.space_after = Pt(4)
    r = par.add_run(txt); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = AZUL


def cit(txt, fonte):
    par = doc.add_paragraph()
    par.paragraph_format.left_indent = Cm(0.8)
    par.paragraph_format.right_indent = Cm(0.4)
    par.paragraph_format.space_after = Pt(2)
    r = par.add_run(txt); r.italic = True; r.font.size = Pt(9.5)
    f = doc.add_paragraph()
    f.paragraph_format.left_indent = Cm(0.8)
    f.paragraph_format.space_after = Pt(8)
    rf = f.add_run(fonte); rf.font.size = Pt(8.5); rf.font.color.rgb = CINZA


def bullet(txt):
    par = doc.add_paragraph(style='List Bullet')
    par.paragraph_format.space_after = Pt(3)
    par.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = par.add_run(txt); r.font.size = Pt(10.5)


def tabela(cab, linhas, larguras=None):
    t = doc.add_table(rows=1, cols=len(cab))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, c in enumerate(cab):
        cell = t.rows[0].cells[i]; cell.text = ''
        par = cell.paragraphs[0]; par.paragraph_format.space_after = Pt(2)
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


# ───────────────────────────── Capa ─────────────────────────────
p('DIREÇÃO-GERAL DE ALIMENTAÇÃO E VETERINÁRIA', bold=True, size=9.5, cor=CINZA, space=0)
p('Direção de Serviços de Bem-Estar Animal', size=9.5, cor=CINZA, space=14)

par = doc.add_paragraph(); par.paragraph_format.space_after = Pt(2)
r = par.add_run('FUNDAMENTAÇÃO DAS OBSERVAÇÕES'); r.bold = True; r.font.size = Pt(16); r.font.color.rgb = AZUL

p('Projeto de DL das atividades económicas — DL 405/XXV/2026', bold=True, size=12, space=2)
p('Análise técnica de suporte à pronúncia da Direção de Serviços de Bem-Estar Animal.',
  size=10.5, cor=CINZA, space=14)

h1('Temas em análise')
p('A numeração é a dos temas analisados e não a do diploma.')

tabela(
    ['N.º', 'Tema', 'Norma principal'],
    [
        ['01', 'A DGAV no procedimento das lojas de venda de animais de companhia e a articulação com o regime '
                'dos animais de companhia e com a Lei da Saúde Animal',
         'Art.º 16.º, n.º 4, e Anexo II; art.ºs 2.º e 36.º, n.º 3'],
        ['02', 'Animais de companhia na definição de atividade pecuária: qual a norma de bem-estar aplicável',
         'Art.º 48.º, als. b) e c)'],
        ['03', 'Deferimento tácito em atividades com animais vivos', 'Art.º 25.º, n.º 3'],
        ['04', 'Animais errantes e articulação com os centros de recolha oficial',
         'Art.ºs 57.º e 59.º'],
        ['05', 'Acesso de animais de companhia a estabelecimentos', 'Art.º 38.º'],
    ],
    larguras=[1.0, 7.3, 5.2],
)

# ───────────────────────────── Ponto 01 ─────────────────────────────
h1('Ponto 01 — Estabelecimentos de comércio a retalho de animais de companhia')

h2('1.1. A norma no projeto')
p('A atividade está prevista no n.º 4 do artigo 16.º do anexo, entre as sujeitas a comunicação prévia, com a '
  'designação «A exploração de estabelecimentos de comércio a retalho de animais de companhia e respetivos '
  'alimentos, em estabelecimentos especializados». Corresponde ao CAE 47762, «Comércio a retalho de animais de '
  'companhia e respetivos alimentos», constante da lista II do anexo I.')
p('Advertência quanto à referência: as alíneas do n.º 4 do artigo 16.º estão com a numeração automática '
  'danificada no ficheiro, aparecendo quase todas como «a)». O Anexo II remete para este caso como «alínea f)», '
  'mas essa letra não é verificável no articulado tal como está. Por isso, nas observações enviadas, a norma é '
  'identificada apenas pelo número, sem a alínea.')

h2('1.2. O que o Anexo II estabelece')
p('A linha correspondente do Anexo II, que identifica as entidades intervenientes em cada procedimento, tem o '
  'seguinte conteúdo:')
tabela(
    ['Atividade económica', 'Entidade coordenadora', 'Entidades públicas consultadas', 'Entidades notificadas'],
    [['Exploração de estabelecimentos de comércio a retalho de animais de companhia e respetivos alimentos, '
      'em estabelecimentos especializados (cf. alínea f)',
      'A câmara municipal territorialmente competente', '(em branco)', 'A DGDCCS']],
    larguras=[5.6, 3.3, 3.3, 2.4],
)
p('A comparação com as linhas vizinhas é o que torna o ponto demonstrável. Para a exploração de '
  'estabelecimentos de comércio por grosso e a retalho e de armazéns de alimentos para animais de criação, '
  'constante da al. f) do n.º 2 do mesmo artigo 16.º, o Anexo II indica a câmara municipal como coordenadora e '
  '«A DGAV» como entidade pública consultada. Para a atividade pecuária de classe 1 e de classe 2, a DGAV '
  'figura igualmente entre as consultadas. A DGAV é, portanto, chamada a pronunciar-se sobre a ração e sobre o '
  'efetivo pecuário, e não sobre o estabelecimento que detém animais de companhia vivos para venda.')

h2('1.3. Por que razão a atividade passa a estar aqui')
p('O n.º 1 do artigo 3.º do Decreto-Lei n.º 276/2001, de 17 de outubro, abre com uma ressalva:')
cit('«1 - Sem prejuízo do disposto no Decreto-Lei n.º 10/2015, de 16 de janeiro, quanto aos estabelecimentos '
    'de comércio a retalho de animais de companhia, o exercício da atividade de exploração de alojamentos, bem '
    'como a atividade de criação comercial de animais de companhia depende de: [...]»',
    'n.º 1 do art.º 3.º do Decreto-Lei n.º 276/2001, de 17 de outubro, na redação consolidada.')
p('A al. j) do n.º 1 do artigo 8.º do decreto-lei preambular revoga o Decreto-Lei n.º 10/2015, de 16 de '
  'janeiro. O n.º 4 do mesmo artigo 8.º determina que «As remissões, legais e regulamentares, para normas ora '
  'revogadas consideram-se feitas, com as devidas adaptações, para o presente decreto-lei, salvo se a '
  'interpretação daquelas impuser solução diferente». A ressalva do Decreto-Lei n.º 276/2001 passa, assim, a '
  'apontar para o novo diploma.')
p('Importa delimitar o efeito: o que transita é o título de acesso à atividade, não as normas materiais. Os '
  'requisitos de detenção dos animais à venda continuam no Decreto-Lei n.º 276/2001, que não é revogado — '
  'designadamente o seu Capítulo III, «Normas para os alojamentos de reprodução, criação, manutenção e venda de '
  'animais de companhia», com o art.º 26.º para pequenos roedores e coelhos, o art.º 27.º e o Anexo III para '
  'cães e gatos, o art.º 32.º quanto às instalações para venda, os art.ºs 36.º e 37.º quanto a animais doentes, '
  'fêmeas prenhes e ninhadas, e o art.º 38.º quanto a pessoal auxiliar e assistência médico-veterinária. O '
  'problema não é de normas materiais: é de quem fica a saber que o estabelecimento abriu.')

h2('1.4. A consequência procedimental')
p('O procedimento de comunicação prévia não tem fase de consulta. O n.º 3 do artigo 21.º do anexo descreve-o '
  'em três fases, a apresentação da comunicação prévia na Plataforma dos Licenciamentos, a decisão e a emissão '
  'do título. E o n.º 3 do artigo 29.º dispõe que, nesse procedimento, «o título digital de atividade económica '
  'é automaticamente emitido com o pagamento da taxa devida ou, não sendo devida taxa, com a apresentação da '
  'comunicação prévia».')
p('Daqui decorre a conclusão técnica que sustenta a proposta: a inclusão da DGAV entre as entidades '
  'consultadas é incompatível com a manutenção da atividade no n.º 4 do artigo 16.º, porque não existe aí fase '
  'em que uma entidade consultada possa pronunciar-se. Para haver pronúncia prévia, a atividade tem de passar '
  'ao n.º 3, que é o procedimento de comunicação com prazo. O custo dessa passagem é o prazo de pronúncia, que '
  'no Anexo III corresponde à linha residual «Outras consultas — 20 dias», com deferimento tácito favorável ao '
  'requerente nos termos do n.º 3 do artigo 25.º.')
p('Existe, dentro do próprio diploma, uma formulação aproveitável para dar peso à pronúncia:')
cit('«2 - Sem prejuízo da competência da entidade coordenadora, são vinculativas as pronúncias da DGAV em '
    'matéria de saúde e bem-estar animal, biossegurança, aprovação sanitária de estabelecimentos e validação do '
    'plano de produção»',
    'n.º 2 do art.º 54.º do anexo (condições gerais para o exercício da atividade pecuária), na versão de '
    '25.9.2026.')

h2('1.5. O que o Regulamento (UE) 2026/1818 passa a impor')
p('A loja de animais é, para o Regulamento, um estabelecimento de venda:')
cit('«(q) ‘selling establishment’ means any premises or structure where dogs or cats are kept for sale without '
    'being born there, including pet shops or private homes, as well as any premises or structures for assembly '
    'operations in which dogs or cats from more than one establishment are assembled;»',
    'al. q) do art.º 4.º do Regulamento (UE) 2026/1818 — versão inglesa, JO L, 2026/1818, de 10.8.2026.')
cit('«q) «Estabelecimento de venda», qualquer instalação ou estrutura onde cães ou gatos são detidos para '
    'venda sem aí terem nascido, incluindo lojas de animais de companhia ou casas particulares, bem como '
    'quaisquer instalações ou estruturas destinadas a operações de agrupamento nas quais sejam agrupados cães '
    'ou gatos a partir de mais do que um estabelecimento;»',
    'al. q) do art.º 4.º do Regulamento (UE) 2026/1818 — versão portuguesa, JO L, 2026/1818, de 10.8.2026.')
p('E sobre esse estabelecimento recai uma obrigação de notificação, com um registo a cargo da autoridade '
  'competente:')
cit('«1. Operators shall notify the competent authorities of their activity, providing at least the following '
    'information for each of their establishments: (a) the name, address and contact details of the operator; '
    '(b) the location of the establishment; (c) the type of establishment: breeding establishment, selling '
    'establishment, shelter or foster home; (d) the species and, for breeding establishments, the breeds of the '
    'dogs or cats kept in the establishment; (e) the capacity of the establishment, expressed as the maximum '
    'number of dogs and cats which can be kept in the establishment; (f) for breeding establishments, the '
    'estimated number of litters to be placed on the market per year. [...] 4. The competent authority shall '
    'keep a register of establishments. The competent authority may, for that purpose, use the register '
    'established pursuant to Article 101(1), point (a), of Regulation (EU) 2016/429.»',
    'art.º 9.º, n.ºs 1 e 4, do Regulamento (UE) 2026/1818 — versão inglesa.')
cit('«1. Os operadores notificam as autoridades competentes da sua atividade, facultando pelo menos as '
    'seguintes informações para cada um dos seus estabelecimentos: a) O nome, o endereço e dados de contacto do '
    'operador; b) A localização do estabelecimento; c) O tipo de estabelecimento: estabelecimento de criação, '
    'estabelecimento de venda, abrigo ou lar de acolhimento; d) A espécie e, para os estabelecimentos de '
    'criação, as raças dos cães ou gatos detidos no estabelecimento; e) A capacidade do estabelecimento, '
    'expressa em termos de número máximo de cães e gatos que podem ser detidos no estabelecimento; f) No caso '
    'dos estabelecimentos de criação, o número estimado de ninhadas a colocar no mercado por ano. [...] 4. A '
    'autoridade competente deve manter um registo de estabelecimentos. A autoridade competente pode utilizar, '
    'para esse efeito, o registo criado nos termos do artigo 101.º, n.º 1, alínea a), do Regulamento (UE) '
    '2016/429.»',
    'art.º 9.º, n.ºs 1 e 4, do Regulamento (UE) 2026/1818 — versão portuguesa.')
p('Dois elementos completam o quadro. Primeiro, não há limiares: o considerando 23 esclarece que, «atenta a '
  'natureza exclusivamente comercial dos estabelecimentos de venda, não é necessário fixar limiares», pelo que '
  'os requisitos se aplicam a todos, independentemente do número de cães ou gatos detidos. Segundo, o artigo '
  '9.º é aplicável a partir de 31 de agosto de 2028, data da regra geral do artigo 33.º, ou seja, menos de dois '
  'anos depois da entrada em vigor prevista para o diploma nacional, fixada em 4 de janeiro de 2027 pelo n.º 1 '
  'do artigo 19.º do decreto-lei preambular.')
p('Nota de delimitação: o Regulamento não exige aprovação prévia dos estabelecimentos de venda. A aprovação, '
  'com inspeção no local, está no artigo 10.º e dirige-se aos estabelecimentos de criação acima de cinco '
  'ninhadas por ano civil ou cinco fêmeas reprodutoras, sendo aplicável apenas a partir de 31 de agosto de '
  '2034. Exigir vistoria prévia às lojas seria uma regra nacional mais restritiva, admissível nos termos do '
  'n.º 1 do artigo 30.º mas sujeita à comunicação à Comissão prevista no n.º 2 do mesmo artigo. Foi por isso '
  'que a proposta enviada se ficou pela pronúncia e pela notificação.')

h2('1.6. Fontes do ponto 01')
bullet('Projeto: «DL 405 XXV 2026_PECUÁRIA_GSEA 25_09_v1.docx», anexo à mensagem de 25.9.2026 — art.ºs 16.º, '
       '21.º, 25.º, 29.º e 54.º do anexo; Anexos I, II e III; art.ºs 8.º e 19.º do decreto-lei preambular.')
bullet('Decreto-Lei n.º 276/2001, de 17 de outubro, versão consolidada — art.ºs 1.º, 2.º, 3.º, 3.º-A, 24.º a '
       '27.º, 32.º, 36.º a 38.º e Anexos II e III.')
bullet('Decreto-Lei n.º 10/2015, de 16 de janeiro — diploma revogado pela al. j) do n.º 1 do art.º 8.º do '
       'decreto-lei preambular.')
bullet('Regulamento (UE) 2026/1818 do Parlamento Europeu e do Conselho, de 17 de junho de 2026, JO L, '
       '2026/1818, de 10.8.2026, ELI http://data.europa.eu/eli/reg/2026/1818/oj — considerando 23, art.ºs 4.º, '
       '9.º, 10.º, 30.º e 33.º, nas versões inglesa e portuguesa, ambas autênticas.')

# ───────────────────────────── Ponto 02 ─────────────────────────────
h1('Ponto 02 — Animais de companhia na definição de atividade pecuária')

h2('2.1. A alteração registada no ficheiro')
p('A alínea c) do artigo 48.º do anexo define «atividade pecuária». No ficheiro de 25.9.2026 o seu início '
  'apresenta-se assim, com a alteração registada visível:')
cit('«Atividade pecuária», todas as atividades de reprodução, produção, detenção, comercialização, exposição '
    'e outras relativas a animais das espécies pecuárias, com exceção da apicultura e [eliminado: «animais de '
    'companhia»] em: [...]',
    'al. c) do art.º 48.º do anexo. Eliminação registada em nome de Nádia Silvestre, com data de 21.9.2026.')
p('O texto que hoje se lê no ficheiro, com as alterações aceites, é «com exceção da apicultura eem:». A '
  'sequência «eem» resulta da justaposição do «e» da conjunção, que antecedia a expressão eliminada, ao «em» '
  'que a seguia. É indício de que a frase não foi relida depois da eliminação.')
p('A eliminação integra-se numa revisão de grande amplitude da Secção III. Nessa mesma data e em nome da '
  'mesma pessoa foram registadas 224 inserções e 140 eliminações, que reescreveram a secção da atividade '
  'pecuária, criaram subsecções e introduziram artigos que antes não existiam, entre os quais os artigos '
  '«Detenção caseira», «Regulamentação» e «Registo de estabelecimentos não sujeitos».')

h2('2.2. A exclusão existe no regime em vigor')
p('O que foi eliminado reproduzia uma delimitação do Novo Regime do Exercício da Atividade Pecuária. A al. a) '
  'do n.º 3 do artigo 1.º do Decreto-Lei n.º 81/2013, de 14 de junho, exclui do âmbito do regime, por código '
  'de atividade económica, a apicultura, CAE 01491, e os animais de companhia, CAE 01493. O projeto comprimiu '
  'essa exclusão de âmbito para dentro de uma definição e, nessa passagem, perdeu metade dela.')
p('Verificação complementar: pesquisaram-se no projeto os códigos 01491 e 01493 e nenhum consta. O diploma '
  'não tem lista de códigos de atividade económica para a pecuária, cuja delimitação é feita por limiares de '
  'cabeças normais no artigo 16.º, pelo que a exclusão não reaparece por outra via.')

h2('2.3. A cláusula que permanece, e de onde vem')
p('A alínea b) do mesmo artigo 48.º define «animal de espécie pecuária» e mantém a referência que suscita a '
  'dúvida. Confrontada com a definição do regime em vigor, a redação é igual palavra por palavra, com uma única '
  'diferença, o acrescento dos insetos:')
cit('«c) «Animal de espécie pecuária» qualquer espécimen vivo bovino, suíno, ovino, caprino, equídeo, ave, '
    'leporídeo (coelhos e lebres) ou outra espécie que seja explorada com destino à sua reprodução ou produção '
    'de carne, leite, ovos, lã, seda, pelo, pele ou repovoamento cinegético, bem como a produção pecuária de '
    'animais destinados a animais de companhia, de trabalho ou a atividades culturais ou desportivas;»',
    'al. c) do art.º 2.º do Decreto-Lei n.º 81/2013, de 14 de junho. A redação da al. b) do art.º 48.º do '
    'projeto é idêntica, com o acrescento de «insetos» após «leporídeo (coelhos e lebres)».')
p('Quanto ao sentido da expressão, a leitura é finalística e não de espécie. O paralelo das três hipóteses, '
  'animais destinados a animais de companhia, de trabalho ou a atividades culturais ou desportivas, indica que '
  'o critério é o destino do animal e não aquilo que ele alimenta. A cláusula serve para que a produção de '
  'espécies pecuárias com destino diferente do alimentar, designadamente leporídeos e aves para o mercado dos '
  'animais de companhia, ou equídeos para trabalho ou desporto, não escape ao regime. A redação admite, porém, '
  'a leitura alternativa de animais destinados a alimentar animais de companhia, e essa ambiguidade subsiste '
  'desde 2013.')
p('A origem foi confirmada até à versão original do Decreto-Lei n.º 81/2013, publicada em 14 de junho de 2013. '
  'Não foi possível confirmar, nas fontes consultadas, se a formulação já constava do Decreto-Lei n.º 214/2008, '
  'que aquele revogou. Fica como verificação pendente.')

h2('2.4. Os comentários do ficheiro no mesmo lugar')
p('O parágrafo da definição de «animal de espécie pecuária» tem três comentários, todos sobre o acrescento dos '
  'insetos e nenhum sobre os animais de companhia:')
tabela(
    ['Marca', 'Autor', 'Teor'],
    [['PO54.1', 'Paulo Meireles de Oliveira', '«Confirma-se os insectos na pecuária?»'],
     ['GMECT54.2', 'G-MECT', '«@Pecuária»'],
     ['NS54.3', 'Nádia Silvestre', '«Confirmamos a sua inserção»']],
    larguras=[2.2, 4.5, 8.8],
)
p('O parágrafo onde a eliminação ocorreu, o da definição de «atividade pecuária», tem um único comentário, '
  'também de Nádia Silvestre, e igualmente alheio à questão: «ver com dgadr a sua proposta: Atividade pecuária '
  'em explorações pecuárias, entrepostos e centros de agrupamentos e atividades complementares de gestão de EP, '
  'anexas e autónomas». Não há, no ficheiro, qualquer justificação registada para a eliminação.')

h2('2.5. Leitura sobre o motivo (inferência)')
p('O que segue é inferência desta Direção de Serviços, e não facto documentado. Apresenta-se como tal.',
  italic=True)
p('A eliminação parece estar ligada ao artigo que foi criado na mesma revisão. A «detenção caseira» é definida '
  'como a detenção de um número reduzido de espécies pecuárias não cinegéticas em que «a posse desses animais '
  'tem o objetivo de lazer ou abastecimento do seu detentor», isenta de licenciamento mas sujeita a registo no '
  'SNIRA. Se os animais de companhia continuassem excluídos da definição de atividade pecuária, o universo que '
  'esse artigo visa, o detentor de algumas galinhas, coelhos ou de um equídeo mantidos por lazer, sairia pela '
  'porta das exceções antes de entrar pela porta do registo. A apicultura não colide com esse objetivo e por '
  'isso subsistiu.')
p('Corrobora esta leitura a alteração do preâmbulo registada no mesmo dia e em nome da mesma pessoa. O texto '
  'anterior descrevia a eliminação do controlo prévio da classe 3 e afirmava que essas atividades e a detenção '
  'caseira «continuam sujeitas» ao registo no SNIRA, traduzindo-se isso «na flexibilização do regime jurídico '
  'aplicável aos pequenos detentores, eliminando barreiras burocráticas desajustadas à dimensão da sua '
  'atividade, sem, no entanto, comprometer as exigências de rastreabilidade». O texto resultante diz que «a '
  'detenção caseira passará a estar sujeita ao registo para efeitos de Sistema Nacional de Informação e Registo '
  'Animal (SNIRA)» e que a integração plena «traduz-se na clarificação do regime jurídico aplicável aos '
  'pequenos detentores, salvaguardando as exigências de rastreabilidade em matéria de saúde pública e animal». '
  'Passou-se de uma afirmação de continuidade e de desregulação para a afirmação de uma obrigação nova.')
p('Consequência prática desta leitura: não se pode pedir a reposição da exclusão como se fosse um lapso de '
  'transcrição, porque isso equivaleria a pedir a revogação de um objetivo deliberado e legítimo, que é a '
  'rastreabilidade dos pequenos detentores. O que se pode propor é um critério que preserve esse objetivo sem '
  'arrastar os animais detidos exclusivamente para fins de companhia. Foi essa a formulação escolhida para o '
  'texto enviado.')

h2('2.5-A. O que a alteração resolve, e que a lei atual não resolve')
p('A eliminação da exclusão não é só perda. Fecha um vazio que é, ele próprio, um problema nosso, e isso tem '
  'de ser dito para que a observação seja equilibrada.')
p('Hoje o coelho, a galinha ou o pónei detidos em casa por gosto não estão com segurança em nenhum dos dois '
  'regimes: o n.º 2 do art.º 1.º do Decreto-Lei n.º 276/2001 exclui «as espécies de pecuária» e a al. a) do '
  'n.º 3 do art.º 1.º do Decreto-Lei n.º 81/2013 excluía os animais de companhia. Que o art.º 26.º do '
  'primeiro fixe medidas de caixa para coelhos e pequenos roedores resolve a contradição por interpretação e '
  'não por texto, o que é frágil: basta invocar a natureza pecuária da espécie para discutir a aplicação do '
  'diploma.')
p('Resolve ainda dois problemas concretos. O primeiro é o criador informal de coelhos, roedores ou aves para '
  'o mercado dos animais de companhia: a al. aa) do n.º 1 do art.º 2.º do Decreto-Lei n.º 276/2001 define '
  'criação comercial como possuir «uma ou mais fêmeas reprodutoras cujas crias sejam destinadas ao comércio», '
  'o que o apanharia, mas a exclusão das espécies de pecuária dá-lhe argumento para sair. Sem a exclusão do '
  'lado pecuário, a cláusula da al. b) do art.º 48.º apanha-o. O segundo é a visibilidade do pequeno detentor, '
  'hoje inexistente, de que dependem a fiscalização, o controlo de zoonoses e a identificação do detentor do '
  'animal encontrado errante.')
p('O problema não é, por isso, o fecho do vazio: é o parâmetro com que se fecha. Pela via pecuária, a '
  'referência de bem-estar daquele coelho passa a ser a cabeça normal e a capacidade instalada, grandezas '
  'concebidas para medir densidade produtiva e efluentes. O vazio fecha-se, a proteção não melhora.')
p('Daqui resulta o erro de técnica que sustenta a observação, e que é mais sólido do que a discussão da '
  'exclusão: a redação usa uma única qualificação, ser ou não atividade pecuária, para decidir duas questões '
  'independentes, quem fica registado e qual o padrão de bem-estar aplicável. A Lei da Saúde Animal separa-as, '
  'ao registar animais de companhia para efeitos de circulação sem os tratar como efetivo. Por isso a '
  'formulação pedida não é a reposição da exclusão, que devolveria estes animais à terra de ninguém, mas a '
  'adoção do critério finalista com ressalva expressa das obrigações de identificação e registo.')

h2('2.5-B. A norma de bem-estar aplicável: os fios já abertos no ficheiro')
p('A observação enviada na quarta versão abandona a proposta de redação e passa a colocar uma dúvida de '
  'aplicação: a detenção caseira de coelhos ou de pequenos roedores por lazer fica sujeita a que normas de '
  'bem-estar? A escolha tem três fundamentos.')
p('O primeiro é que a questão já está aberta no documento, e foi aberta do lado do Gabinete. No parágrafo que '
  'hoje é o n.º 1 do art.º 54.º, que manda o operador agir «no respeito pelas normas de bem-estar animal», '
  'está um comentário de Paulo Meireles de Oliveira a observar que essas normas «parecem decorrer dos regimes '
  'complementares e não revogados» e a enumerá-las: o Decreto-Lei n.º 64/2000, o n.º 48/2001 relativo a '
  'vitelos, o n.º 72-F/2003 relativo a galinhas poedeiras e o n.º 135/2003 relativo a suínos. O Gabinete '
  'encaminhou com «@Pecuária» e a resposta registada foi «Ponderar junto da DGAV e DGADR». Há dois '
  'encaminhamentos equivalentes: na linha dos leporídeos do art.º 50.º, «Ver com DGAV e DGADR», e na epígrafe '
  'do art.º 51.º, «Verificar com DGAV e DGADR». A observação responde a um fio aberto, não abre um novo.')
p('Note-se o que falta na enumeração do revisor: leporídeos e roedores. Não por omissão, mas porque para essas '
  'espécies as normas estão em portaria.')
p('O segundo fundamento é que o diploma dá pistas de resposta e nenhuma é conclusiva. O art.º 2.º enumera os '
  'regimes a articular e não inclui o Decreto-Lei n.º 276/2001. O art.º 36.º, n.º 1, manda cumprir requisitos '
  'de higiene e de saúde pública, e o seu n.º 3 refere a legislação aplicável aos «produtos». O art.º 50.º, '
  'n.º 1, al. e), habilita portaria sobre a «detenção e produção pecuária» de leporídeos e outras espécies. O '
  'art.º 51.º remete para o Decreto-Lei n.º 142/2006. E o art.º 54.º manda respeitar «as normas de bem-estar '
  'animal» e «as normas de funcionamento previstas para as espécies», sem as identificar.')
p('O terceiro é a delimitação correta do vazio, que obriga a corrigir uma afirmação feita antes nesta análise. '
  'Não é exato que as únicas normas específicas para coelhos e pequenos roedores estejam no art.º 26.º e no '
  'Anexo II do Decreto-Lei n.º 276/2001. A Portaria n.º 635/2009, de 9 de junho, estabelece as normas '
  'regulamentares da detenção e produção pecuária de leporídeos em explorações e núcleos de produção cunícula, '
  'armazéns e centros de agrupamento, identifica três sistemas de produção, entre eles o de animais de '
  'companhia, e fixa requisitos de instalações e medidas sanitárias. A cláusula da al. b) do art.º 48.º tem, '
  'por isso, contrapartida regulamentar desde 2009.')
p('O vazio é, então, outro e mais estreito. Aquela portaria assenta nas classes do regime pecuário e a '
  'detenção caseira criada pelo projeto situa-se abaixo da classe 3, que subsiste no n.º 4 do art.º 16.º para '
  'capacidades até 15 CN, e é expressamente isenta de licenciamento. A pergunta é se uma detenção isenta de '
  'licenciamento é alcançada por regulamentação construída sobre as classes de licenciamento. Se for, '
  'aplicam-se a um animal de estimação requisitos de isolamento térmico, de lavabilidade de paredes e '
  'pavimentos e de vazio sanitário entre lotes, que são parâmetros de produção. Se não for, não se aplica '
  'norma alguma.')
p('Risco a antecipar: a resposta pode ser «aplica-se a Portaria n.º 635/2009». O contra-argumento é o do '
  'parágrafo anterior, e foi deliberadamente deixado fora da observação enviada, para que esta se mantenha '
  'como dúvida e não se transforme em alegação.')

h2('2.6. O efeito cruzado com o regime dos animais de companhia')
p('O n.º 2 do artigo 1.º do Decreto-Lei n.º 276/2001 exclui do seu âmbito «as espécies da fauna selvagem '
  'autóctone e exótica e os seus descendentes criados em cativeiro, objeto de regulamentação específica, e os '
  'touros de lide e as espécies de pecuária». Lido à letra, o coelho estaria fora daquele diploma. Mas o mesmo '
  'diploma regula-o expressamente: o art.º 26.º, «Condições particulares para a manutenção de pequenos roedores '
  'e coelhos», exige material de cama adequado e remete as medidas das caixas para o Anexo II, que tem quadros '
  'próprios para pequenos roedores, para pequenos roedores em reprodução e para coelhos em reprodução. A '
  'contradição aparente resolve-se pelo fim da detenção e não pela espécie: o coelho mantido como animal de '
  'companhia é animal de companhia, o coelho de uma cunicultura não é. É esse critério implícito que a '
  'eliminação põe em causa, porque o projeto passa a puxar pela espécie e pela atividade.')
p('A isso acresce o artigo criado na mesma revisão, «Registo de estabelecimentos não sujeitos», que remete a '
  'atividade não sujeita a título apenas para as normas sanitárias, de bem-estar animal, identificação e '
  'registo do Decreto-Lei n.º 142/2006, de 27 de julho, sem qualquer referência ao Decreto-Lei n.º 276/2001.')

h2('2.7. A ordem de grandeza dos limiares')
p('A «detenção caseira» admite capacidade instalada até 3 CN, não podendo ser excedido o limite de 2 CN por '
  'espécie pecuária. O projeto não permite, porém, converter esses limiares em número de animais: o seu Anexo '
  'V tem o título «Equivalências em cabeças normais (CN)», uma remissão para a «alínea e) do Artigo 46.º», que '
  'não corresponde à norma que invoca a tabela, e uma nota de pé que define cabeça normal, mas não tem tabela '
  'alguma.')
p('Recorrendo à tabela do regime que substitui, o Anexo II do Decreto-Lei n.º 81/2013, obtêm-se as seguintes '
  'ordens de grandeza para o limite de 2 CN por espécie:')
tabela(
    ['Espécie e tipo de animal', 'CN por animal', 'Animais correspondentes a 2 CN'],
    [['Coelho ou lebre, de recria ou acabamento', '0,009', 'cerca de 222'],
     ['Coelha ou lebre reprodutora, em aleitamento', '0,04', '50'],
     ['Galinha poedeira', '0,013', 'cerca de 153'],
     ['Frango ou pintada', '0,006', 'cerca de 333']],
    larguras=[7.0, 3.0, 5.5],
)
p('Significa que a detenção de algumas centenas de coelhos «para lazer» cabe, em cabeças normais, dentro da '
  'detenção caseira, ficando isenta de licenciamento e com o único dever de registo no SNIRA. Fica ainda '
  'disponível o argumento de que, tratando-se de atividade pecuária, as medidas mínimas do Anexo II do '
  'Decreto-Lei n.º 276/2001 não lhe são oponíveis. Em matéria de bem-estar, é o resultado inverso do '
  'pretendido.')

h2('2.8. O critério que o RGAC adota')
p('O projeto de Regime Geral do Animal de Companhia, em elaboração nesta Direção-Geral e que é trabalho em '
  'curso e não legislação vigente, resolve a fronteira por critério finalista, abandonando a exclusão das '
  'espécies de pecuária:')
cit('«2 - Para efeitos do presente decreto-lei, são animais de companhia os animais das espécies constantes da '
    'Parte A do Anexo I do Regulamento (UE) 2016/429 do Parlamento Europeu e do Conselho, de 9 de março de '
    '2016, e, quando detidos para fins de companhia, os das espécies constantes da Parte B do mesmo anexo.»',
    'n.º 2 do art.º 2.º do projeto de RGAC, versão de trabalho de 30.6.2026, 18h00.')
p('Na Parte A do Anexo I daquele regulamento estão o cão, o gato e o furão; na Parte B, entre outros, os '
  'coelhos e os pequenos roedores. O critério do RGAC qualifica, portanto, as três primeiras espécies como '
  'animais de companhia sem condição, e as restantes quando a detenção tenha esse fim. É este o critério '
  'equivalente a que o texto enviado alude, sem o nomear, por o RGAC não ser ainda diploma publicado.')

h2('2.9. Efeito por espécie, no estado atual do projeto')
tabela(
    ['Espécie', 'Risco de ser lida como atividade pecuária', 'Normas de bem-estar aplicáveis hoje'],
    [['Cães e gatos',
      'Baixo. Não constam da lista nominativa. A cláusula «produção pecuária de animais destinados a animais '
      'de companhia» descreve, à letra, a criação para venda, e a barreira textual que a afastava era a '
      'exclusão eliminada.',
      'Art.ºs 7.º a 18.º e 27.º do DL 276/2001 e Anexo III, com as dimensões mínimas, a proibição de exposição '
      'à venda antes da 8.ª semana, o limite de 15 dias em gaiola e o exercício diário. DL 315/2009 para raças '
      'potencialmente perigosas. Identificação pelo DL 82/2019, no SIAC. A partir de 2028, Regulamento (UE) '
      '2026/1818; o art.º 15.º e o ponto 2 do Anexo I, sobre alojamento, a partir de 31.8.2031.'],
     ['Furões',
      'Baixo, pela mesma via dos cães e gatos.',
      'Nenhuma norma específica. A pesquisa das palavras «furão» e «furões» no DL 276/2001 não devolve '
      'ocorrências; aplicam-se só as normas gerais. Subsiste dúvida de âmbito, por o n.º 2 do art.º 1.º excluir '
      'a fauna selvagem autóctone e os seus descendentes criados em cativeiro. Identificação obrigatória pelo '
      'DL 82/2019. Fora do Regulamento (UE) 2026/1818, que abrange apenas cães e gatos.'],
     ['Coelhos',
      'Elevado. «Leporídeo (coelhos e lebres)» consta da lista nominativa, e a detenção por lazer é o próprio '
      'critério da detenção caseira.',
      'Art.º 26.º do DL 276/2001 e Anexo II, com medidas mínimas de caixa, incluindo quadro para coelhos em '
      'reprodução. Fora do Regulamento (UE) 2026/1818.'],
     ['Hamsters e porquinhos-da-índia',
      'Intermédio. Não constam da lista nominativa, mas cabem em «outra espécie» conjugada com a cláusula '
      'finalista.',
      'Art.º 26.º do DL 276/2001 e Anexo II, als. a) e b), com medidas mínimas para outros pequenos roedores e '
      'para pequenos roedores em reprodução. Fora do Regulamento (UE) 2026/1818.']],
    larguras=[2.6, 5.6, 7.3],
)

h2('2.10. Fontes do ponto 02')
bullet('Projeto: «DL 405 XXV 2026_PECUÁRIA_GSEA 25_09_v1.docx» — preâmbulo; art.ºs 16.º, 48.º, als. b), c) e '
       'i), 49.º e 51.º do anexo; Anexo V. Alterações e comentários registados no próprio ficheiro, com autor e '
       'data, lidos a partir do respetivo XML.')
bullet('Decreto-Lei n.º 81/2013, de 14 de junho, Novo Regime do Exercício da Atividade Pecuária — art.º 1.º, '
       'n.º 3, al. a), art.º 2.º, al. c), e Anexo II, «Equivalências em cabeças normais (CN)». Anexo verificado '
       'no Diário da República, 1.ª série, n.º 113, de 14 de junho de 2013, pp. 3324 e 3325.')
bullet('Decreto-Lei n.º 276/2001, de 17 de outubro, versão consolidada — art.ºs 1.º, n.º 2, 2.º, 26.º e Anexo '
       'II; e, para a comparação por espécie, art.ºs 7.º a 18.º, 27.º e Anexo III.')
bullet('Decreto-Lei n.º 82/2019, de 27 de junho — identificação obrigatória de cães, gatos e furões.')
bullet('Decreto-Lei n.º 142/2006, de 27 de julho — regime de identificação, registo e circulação de animais, '
       'para que remete o artigo «Registo de estabelecimentos não sujeitos» do projeto.')
bullet('Regulamento (UE) 2016/429 do Parlamento Europeu e do Conselho, de 9 de março de 2016, Anexo I, Partes '
       'A e B.')
bullet('Projeto de RGAC, «RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO - Revisto 30-06-2026 18h00 Grupo.docx» — '
       'art.º 2.º, n.º 2. Trabalho em curso, citado como tal.')

h2('2.11. Verificações pendentes')
bullet('Confirmar se a formulação «produção pecuária de animais destinados a animais de companhia» já constava '
       'do Decreto-Lei n.º 214/2008, de 10 de novembro, que o Decreto-Lei n.º 81/2013 revogou.')
bullet('Confirmar se o Anexo V do projeto virá a reproduzir a tabela do Anexo II do Decreto-Lei n.º 81/2013 ou '
       'se terá valores próprios, e corrigir a remissão para a «alínea e) do Artigo 46.º».')
bullet('Quantificar o universo afetado: número de estabelecimentos do CAE 47762 e, destes, quantos detêm '
       'animais vivos. Sem este dado não é possível avaliar a exequibilidade de procedimentos mais exigentes.')

h2('2.5-C. A ligação à lista positiva de animais de companhia')
p('A questão do ponto 02 é, no fundo, de classificação: a lei decide o regime de bem-estar nomeando espécies, '
  'e a mesma espécie acaba em dois regimes. A Lei da Saúde Animal dá o critério da finalidade mas não diz quais '
  'as espécies que podem ser detidas como animais de companhia. O instrumento que fecha essa questão é a lista '
  'positiva, e o projeto de RGAC já a prevê.')
cit('«3 - Sem prejuízo do disposto nos n.ºs anteriores, serão considerados animais de companhia aqueles que '
    'vierem a integrar a lista positiva de animais de companhia (ou lista nacional de animais de companhia), a '
    'publicar em Portaria dos membros do Governo responsáveis pelas áreas da agricultura e do ambiente.»',
    'n.º 3 do art.º 4.º do projeto de RGAC, versão de trabalho de 30.6.2026. O n.º 4 do mesmo artigo exclui a '
    'fauna selvagem indígena e não indígena, as espécies da Lista Nacional de Espécies Invasoras, as inscritas '
    'na CITES e as perigosas e exóticas sujeitas a legislação especial; o n.º 5 permite à DGAV a exclusão '
    'cautelar imediata de uma espécie.')
p('A figura vem do RGBEAC de junho de 2025, onde é apresentada como uma das principais inovações, com '
  'referência comparada à Bélgica, aos Países Baixos, à Finlândia, à França e a Chipre.')

p('Daqui resulta um argumento de legística, concreto e verificável: há duas habilitações regulamentares '
  'concorrentes sobre o mesmo ato, a detenção, relativamente à mesma espécie.', bold=True)
tabela(
    ['Instrumento', 'Objeto', 'Portaria de quem'],
    [['Art.º 4.º, n.º 3, do projeto de RGAC',
      'Lista positiva de animais de companhia, que determina quais as espécies qualificadas como animais de '
      'companhia',
      'Membros do Governo responsáveis pela agricultura e pelo ambiente'],
     ['Art.º 50.º, n.º 1, al. e), do anexo do projeto de DL das atividades económicas',
      'Normas regulamentares aplicáveis à «detenção e produção pecuária» de «Leporídeos e outras espécies»',
      'Membro do Governo responsável pela agricultura e pelo desenvolvimento rural']],
    larguras=[5.0, 6.5, 4.0],
)
p('Mesma espécie, mesmo ato, duas portarias, conjuntos de signatários diferentes e nenhuma regra de '
  'articulação entre elas. A que for publicada primeiro fixa, por omissão, o regime do coelho ou do roedor '
  'detido por companhia.')
p('E há um argumento substantivo que decorre deste. A lista positiva só tem efeito útil se a qualificação '
  'tiver consequências. Se uma espécie puder constar da lista positiva de animais de companhia e ser, '
  'simultaneamente e sem distinção, espécie pecuária na mesma situação de detenção, a lista passa a ser um '
  'rótulo sem regime associado. A alteração assinalada no ponto 02 não afeta, por isso, apenas o Decreto-Lei '
  'n.º 276/2001: afeta o instrumento central do regime que estamos a preparar.')
p('Ressalva: o Regulamento (UE) 2026/1818 não prevê listas positivas. A pesquisa das expressões «lista '
  'positiva» e «positive list» nas versões portuguesa e inglesa do texto publicado não devolve ocorrências. A '
  'âncora desta figura é nacional e comparada, não europeia.')
p('Incoerência interna do RGAC que esta análise expõe, e que deve seguir para o memorando de acompanhamento: '
  'o n.º 2 do art.º 2.º qualifica as espécies da Parte B do Anexo I do Regulamento (UE) 2016/429 como animais '
  'de companhia «quando detidos para fins de companhia», enquanto o n.º 2 do art.º 4.º diz que essas espécies '
  '«são também considerados animais de companhia», sem o critério finalista. Sem esse critério, todo o coelho '
  'seria animal de companhia, incluindo o da cunicultura. É o lapso simétrico do que se assinala ao Gabinete.')
p('Nota de oportunidade: este argumento foi deliberadamente deixado fora da observação 02 enviada. Serve '
  'melhor como resposta de segunda volta, caso a resposta à dúvida de aplicação venha a ser a de que se aplica '
  'a portaria da pecuária. Jogado antes, permite que a articulação seja resolvida contra nós no próprio texto.')

# ───────────────────────────── Ponto 03 ─────────────────────────────
h1('Ponto 03 — Deferimento tácito em atividades com animais vivos')

h2('3.1. A regra no projeto')
p('O preâmbulo declara a intenção: o regime é consonante com a ação governativa no sentido de «consagrar como '
  'regra o deferimento tácito, sustentado pela confiança e responsabilidade dos operadores económicos». A '
  'concretização está no artigo 25.º do anexo.')
cit('«3 - Caso não seja emitida pronúncia no prazo definido no n.º 1, considera-se que a mesma é favorável à '
    'pretensão do requerente.»',
    'n.º 3 do art.º 25.º («Pronúncia das entidades públicas consultadas e deferimento tácito») do anexo, na '
    'versão de 25.9.2026. O n.º 4 prevê a emissão de certidão com menção expressa ao deferimento, sem taxa.')
p('Os prazos são os do Anexo III. Para as consultas sem prazo próprio aplica-se a linha residual «Outras '
  'consultas — 20 dias»; para os regimes em matéria de segurança da cadeia alimentar, 30 dias.')
p('Importa delimitar o alcance. O deferimento tácito do art.º 25.º opera no procedimento de comunicação com '
  'prazo e no de comunicação com prazo e vistoria, que são os que têm fase de pronúncia. No procedimento de '
  'comunicação prévia não há deferimento tácito porque não há decisão a diferir: o n.º 3 do art.º 29.º '
  'determina que o título é emitido automaticamente com a apresentação. São duas insuficiências distintas, e '
  'esta observação respeita à primeira.')

h2('3.2. A legislação vigente afasta-o expressamente neste domínio')
p('Quando a decisão respeita à detenção de animais, o legislador nacional excluiu o deferimento tácito em '
  'termos inequívocos:')
cit('«2 - Caso não seja proferida a decisão referida no número anterior no prazo de 60 dias contados da data '
    'de receção do pedido de permissão administrativa devidamente instruído, independentemente da realização de '
    'visita de controlo, não há lugar a deferimento tácito, podendo o interessado obter a tutela adequada junto '
    'dos tribunais administrativos.»',
    'n.º 2 do art.º 3.º-D do Decreto-Lei n.º 276/2001, de 17 de outubro, na redação dada pelo Decreto-Lei '
    'n.º 20/2019, de 30 de janeiro. Norma vigente.')
p('A norma respeita à permissão administrativa dos alojamentos destinados à reprodução e criação de animais '
  'potencialmente perigosos, o caso em que o regime dos animais de companhia exige decisão expressa. O projeto '
  'de RGAC reproduz a solução no n.º 2 do seu art.º 47.º. Não se trata, portanto, de uma pretensão nova desta '
  'Direção de Serviços: é a solução que o ordenamento já consagra para decisões desta natureza.')

h2('3.3. E o direito da União vai no mesmo sentido')
cit('«1. Operators of breeding establishments that either produce or intend to produce more than five litters '
    'per calendar year or that keep more than a combined total of five bitches or queens at any given time '
    'shall place dogs or cats on the market only after their breeding establishment has been approved by the '
    'competent authority. 2. The competent authority shall perform on-site inspections to verify that the '
    'breeding establishment meets the requirements of this Regulation. [...] The competent authority shall '
    'grant certificates of approval only to breeding establishments that meet the requirements of this '
    'Regulation.»',
    'art.º 10.º, n.ºs 1 e 2, do Regulamento (UE) 2026/1818 — versão inglesa, JO L, 2026/1818, de 10.8.2026.')
cit('«1. Os operadores de estabelecimentos de criação que produzam ou tencionem produzir mais de cinco '
    'ninhadas por ano civil, ou que, a qualquer momento, detenham um total combinado de mais de cinco cadelas '
    'reprodutoras ou gatas reprodutoras, só podem colocar cães ou gatos no mercado após aprovação do seu '
    'estabelecimento de criação pela autoridade competente. 2. A autoridade competente efetua inspeções no '
    'local para verificar se o estabelecimento de criação cumpre os requisitos do presente regulamento. [...] A '
    'autoridade competente só deve conceder certificados de aprovação a estabelecimentos de criação que cumpram '
    'os requisitos do presente regulamento.»',
    'art.º 10.º, n.ºs 1 e 2, do Regulamento (UE) 2026/1818 — versão portuguesa.')
p('O art.º 10.º é aplicável a partir de 31 de agosto de 2034, nos termos da al. f) do art.º 33.º. Note-se a '
  'natureza da exigência: a colocação no mercado depende de aprovação, e a aprovação depende de inspeção no '
  'local, não podendo o certificado ser concedido a estabelecimento que não cumpra. Uma aprovação obtida por '
  'silêncio administrativo é incompatível com esta construção.')

h2('3.4. O que o artigo 31.º revela')
p('O art.º 31.º enumera as causas de indeferimento e de não emissão do título. Entre as dezenas de '
  'circunstâncias previstas, a única referência à DGAV é a da al. f), relativa à «Decisão desfavorável quanto à '
  'atribuição do NCV ou NII», isto é, matéria de segurança da cadeia alimentar e de subprodutos. Não há '
  'qualquer causa de indeferimento fundada em pronúncia desfavorável em matéria de saúde ou de bem-estar '
  'animal, o que é coerente com a ausência da DGAV no procedimento das atividades que detêm animais de '
  'companhia, assinalada no ponto 01.')

h2('3.5. Efeito sobre a aprovação sanitária de estabelecimentos')
p('O n.º 1 do art.º 14.º do anexo determina que os estabelecimentos abrangidos pelo n.º 2 do art.º 4.º do '
  'Regulamento (CE) n.º 853/2004, pelo art.º 10.º do Regulamento (CE) n.º 183/2005 e pelo art.º 44.º do '
  'Regulamento (CE) n.º 1069/2009 «só podem iniciar a atividade após realização de vistoria e aprovação pela '
  'DGAV». Conjugado com o n.º 3 do art.º 25.º e com a linha de 30 dias do Anexo III, coloca-se a questão de '
  'saber se o silêncio da DGAV pode valer como aprovação sanitária para efeitos daqueles regulamentos. A '
  'matéria é da competência dos serviços de segurança alimentar e de subprodutos, não desta Direção de '
  'Serviços, mas deve ser-lhes sinalizada.')

h2('3.6. Fontes do ponto 03')
bullet('Projeto: preâmbulo; art.ºs 14.º, 21.º, 25.º, 29.º e 31.º do anexo; Anexo III.')
bullet('Decreto-Lei n.º 276/2001, de 17 de outubro — art.ºs 3.º, 3.º-B, 3.º-C e 3.º-D, n.º 2, na redação do '
       'Decreto-Lei n.º 20/2019, de 30 de janeiro.')
bullet('Regulamento (UE) 2026/1818 — art.º 10.º, n.ºs 1 e 2, e al. f) do art.º 33.º, nas versões inglesa e '
       'portuguesa.')
bullet('Projeto de RGAC — n.º 2 do art.º 47.º. Trabalho em curso, citado como tal.')

h2('3.7. Verificações pendentes')
bullet('Confirmar se o regime geral do Código do Procedimento Administrativo e a legislação de segurança '
       'alimentar admitem, ou não, aprovação sanitária por deferimento tácito, para fundamentar o ponto 3.5.')
bullet('Confirmar se existe prática ou orientação da DGAV sobre prazos de pronúncia no SIR e no SI REAP que '
       'permita estimar o risco real de o prazo de 20 dias ser excedido.')

# ───────────────────────────── Ponto 04 ─────────────────────────────
h1('Ponto 04 — Animais errantes e articulação com os centros de recolha oficial')

h2('4.1. O regime vigente dos centros de recolha oficial')
p('O centro de recolha oficial é, juridicamente, um alojamento de animais de companhia. A al. t) do n.º 1 do '
  'art.º 2.º do Decreto-Lei n.º 276/2001 define «centro de recolha» como «qualquer alojamento oficial onde um '
  'animal é hospedado por um período determinado pela autoridade competente, nomeadamente os canis e os gatis '
  'municipais», e a al. a) do n.º 1 do art.º 3.º do mesmo diploma inclui expressamente os centros de recolha '
  'entre as atividades dependentes de mera comunicação prévia à DGAV. É, por isso, um estabelecimento '
  'registado na DGAV, com médico-veterinário responsável e sujeito às normas do seu Capítulo III.')
p('A obrigação de o manter está no art.º 11.º do Decreto-Lei n.º 314/2003: as câmaras municipais, isoladamente '
  'ou em associação, «são obrigadas a possuir e manter instalações destinadas a canis e gatis, de acordo com as '
  'necessidades da zona», com pelo menos duas celas semicirculares para isolamento e quarentena de suspeitos '
  'de raiva, podendo celebrar protocolos com municípios vizinhos, e com a direção a cargo do '
  'médico-veterinário municipal. A rede resulta do n.º 4 do art.º 2.º da Lei n.º 27/2016.')

h2('4.2. Funções e prazos')
tabela(
    ['Função', 'Norma', 'Elemento relevante'],
    [['Captura e recolha', 'Art.º 19.º do DL 276/2001 e art.º 8.º do DL 314/2003',
      'Competência das câmaras municipais; os animais são recolhidos ao canil ou gatil municipal'],
     ['Exame clínico e destino', 'Art.º 9.º, n.º 1, do DL 314/2003',
      'Exame pelo médico-veterinário municipal, que decide o destino; permanência mínima de oito dias'],
     ['Presunção de abandono', 'Art.º 3.º, n.º 1, da Lei n.º 27/2016',
      'Decorridos quinze dias sobre a recolha sem reclamação, presumem-se abandonados e são obrigatoriamente '
      'esterilizados e encaminhados para adoção'],
     ['Esterilização e CED', 'Art.º 4.º da Lei n.º 27/2016 e Portaria n.º 146/2017',
      'Captura, vacinação e esterilização de errantes e execução dos programas de captura, esterilização e '
      'devolução'],
     ['Despesas', 'Art.º 9.º, n.º 2, do DL 314/2003', 'Alimentação e alojamento a cargo do detentor'],
     ['Cadáveres', 'Art.º 12.º do DL 314/2003', 'Destruição assegurada pelas câmaras municipais'],
     ['Relato', 'Art.º 3.º, n.ºs 9 e 10, da Lei n.º 27/2016',
      'Relatório de gestão anual publicitado no primeiro mês do ano; relatório nacional da DGAV até ao fim do '
      'primeiro trimestre'],
     ['Prazo do projeto', 'Art.º 59.º, n.º 3, do anexo', 'Cinco dias úteis para a recolha pelo detentor'],
    ],
    larguras=[3.4, 5.0, 7.1],
)
p('Os prazos são, portanto, quatro e não coincidem: oito dias de permanência mínima, quinze dias para a '
  'presunção de abandono, dez dias no mínimo proposto pelo projeto de RGAC e cinco dias úteis no artigo do '
  'projeto em análise.')

h2('4.3. A sede da matéria no diploma')
p('O artigo está no Título II, «Requisitos de exercício», Capítulo '
  'II, «Requisitos especiais de exercício», Secção III, «Atividade pecuária», Subsecção IV, «Medidas '
  'Administrativas», entre o artigo das medidas administrativas e o das sanções acessórias. Foi aí colocado '
  'como medida de polícia do licenciamento pecuário: o animal errante é sintoma de incumprimento do dever de '
  'contenção, que é condição de exercício pela al. j) do n.º 1 do art.º 54.º, e o n.º 4 do art.º 59.º '
  'condiciona a devolução à verificação de que a exploração dispõe de condições que previnam nova fuga.')
p('O artigo foi inserido por inteiro em 23 de setembro de 2026, em nome de «Utilizador Convidado», no conjunto '
  'de cerca de noventa inserções dessa data, na véspera da reunião de 24 de setembro. O seu próprio autor '
  'deixou-lhe um comentário ancorado ao n.º 1: «Qual é a entidade competente?».')

h2('4.4. Onde o projeto toca os centros de recolha oficial')
bullet('Pela omissão. O art.º 59.º não identifica instalação alguma, mas refere despesas de «alojamento» no '
       'n.º 3 e atribui ao município a determinação do destino no n.º 5. O município dispõe de uma única '
       'instalação de alojamento de animais, que é o centro de recolha oficial.')
bullet('Pela terminologia. A subal. i) da al. c) do art.º 48.º define «Centro de Agrupamento» como «os locais, '
       'como centros de recolha, feiras e mercados […] onde são agrupados animais provenientes de diferentes '
       'explorações». A expressão «centros de recolha» é a mesma que o Decreto-Lei n.º 276/2001 usa para o '
       'canil e o gatil municipais. A definição é herdada do art.º 2.º do Decreto-Lei n.º 81/2013, pelo que a '
       'coincidência não é nova; novo é o contacto, porque nada mandava, até agora, animais pecuários para a '
       'mão do município. Na pronúncia, basta a nota de que não são a mesma realidade.')
bullet('Pela capacidade e pelos meios. A Lei n.º 27/2016 afetou aos centros de recolha oficial uma missão '
       'determinada, e é sobre ela que se construíram os apoios públicos. Uma função adicional sem meios, com '
       'o encargo a recair no município sempre que o detentor não seja identificado, que é a regra no gado '
       'deambulante, compromete a missão existente.')

h2('4.5. A base legal não é restritiva: a restrição está na portaria')
p('A lei habilitante é espécie-neutra. A Lei n.º 27/2016, de 23 de agosto, intitula-se «Aprova medidas para a '
  'criação de uma rede de centros de recolha oficial de animais» e o seu art.º 1.º dispõe que «A presente lei '
  'aprova medidas para a criação de uma rede de centros de recolha oficial de animais e para a modernização '
  'dos serviços municipais de veterinária, e estabelece a proibição do abate de animais errantes como forma de '
  'controlo da população, privilegiando a esterilização». Em nenhum dos dois lugares a lei escreve «animais de '
  'companhia»: escreve «animais».')
p('A restrição é introduzida pelo diploma de execução. O art.º 1.º da Portaria n.º 146/2017, de 26 de abril, '
  'define o objeto como a regulamentação da «criação de uma rede efetiva de centros de recolha oficial de '
  'animais de companhia», e o art.º 2.º fixa o âmbito:')
cit('«A presente portaria aplica-se aos centros de recolha oficial (CRO) de animais de companhia e controlo '
    'das populações errantes desses animais, considerando-se como tais as espécies previstas na Parte A do '
    'Anexo I do Regulamento (UE) 2016/429, do Parlamento Europeu e do Conselho, de 9 de março.»',
    'art.º 2.º da Portaria n.º 146/2017, de 26 de abril.')
p('A delimitação opera, portanto, por remissão para a Parte A do Anexo I da Lei da Saúde Animal, que abrange '
  'o cão, o gato e o furão. Ficam fora as espécies da Parte B, entre elas os coelhos, os roedores e as aves, e '
  'ficam fora os equídeos e as demais espécies pecuárias.')
p('Consequência relevante para a pronúncia: o estreitamento do âmbito dos centros de recolha oficial às três '
  'espécies da Parte A é obra de portaria, e não da lei. A sede da eventual ampliação é, por isso, '
  'regulamentar, e a competência de proposta cabe à área do bem-estar animal. Não depende deste diploma.')

h2('4.6. Os Avisos de financiamento, de 2018 a 2026')
p('O alojamento de espécies diferentes do cão e do gato nos centros de recolha oficial não é uma hipótese '
  'teórica: foi requisito mínimo de construção e item financiado, de forma contínua, durante oito anos e sob '
  'duas entidades gestoras sucessivas.')
p('O programa foi aprovado pelo Despacho n.º 3321/2018, publicado no Diário da República, ao abrigo do n.º 4 '
  'do art.º 2.º da Lei n.º 27/2016 e do art.º 227.º da Lei n.º 114/2017, de 29 de dezembro. O ponto 1 do seu '
  'anexo estabelecia:')
cit('«a) Um CRO municipal deve possuir a capacidade mínima de alojamento para 15 cães/gatos e uma cela de '
    'isolamento, uma boxe para outros animais, bem como uma sala que permita realizar a esterilização e/ou '
    'tratamentos.»',
    'al. a) do n.º 1 do anexo «Valores de referência e limites» ao Despacho n.º 3321/2018, publicado no '
    'Diário da República, 2.ª série, n.º 66, de 4 de abril de 2018.')
p('A mesma formulação, e o correspondente item da tabela de apoios, mantiveram-se nos Avisos seguintes, com '
  'atualização apenas dos valores:')

tabela(
    ['Aviso', 'Entidade', 'Requisito mínimo', 'Valor do apoio'],
    [['Despacho n.º 3321/2018', 'DGAL, DGAV e CCDR',
      '«uma boxe para outros animais»', '1.300 € (3 m²)'],
     ['Aviso 1/2021', 'ICNF-DBEAC', '«uma boxe para outros animais»', '1.300 € (3 m²)'],
     ['Aviso 1/2022', 'ICNF-DBEAC', '«uma boxe para outros animais»', '1.430 € (3 m²/animal)'],
     ['Aviso 1/2023', 'ICNF-DBEAC', '«uma boxe para outros animais»', '1.430 € (3 m²/animal)'],
     ['Aviso 1/2025', 'DGAV-DBEA', '«um compartimento para outras espécies»', '1 537,02 € (3 m²/animal)'],
     ['Aviso 1/2026', 'DGAV-DBEA', 'ausente', 'ausente']],
    larguras=[3.0, 2.6, 5.4, 2.5],
)

p('A redação de 2025, na al. b) do n.º 1 do Capítulo XV, é a seguinte:')
cit('«Um CRO municipal deve possuir, no mínimo, duas celas de isolamento, um compartimento para outras '
    'espécies, bem como uma sala que permita realizar a esterilização, tratamento e/ou occisão»',
    'al. b) do n.º 1 do Capítulo XV do Aviso n.º 1/2025 DGAV-DBEA.')
p('E a al. c), iii), do mesmo número fixava o apoio em «Compartimento para outras espécies (área mínima '
  'coberta de 3 m²/animal) – 1 537,02 €».')
p('O Aviso n.º 1/2026, que é o Aviso em vigor, não contém uma única ocorrência da palavra «espécie». O item '
  'desapareceu dos requisitos técnicos e desapareceu da tabela de apoios. A verificação foi feita por pesquisa '
  'sistemática do termo no texto integral dos dois Avisos.')
p('Leitura (inferência): o requisito não foi substituído por outro, nem acompanhado de norma transitória. '
  'Trata-se, pela aparência, de uma simplificação do Aviso e não de uma decisão de política, mas o efeito é o '
  'de retirar do quadro de financiamento a única infraestrutura que permitia aos centros de recolha oficial '
  'acolher espécies diferentes do cão e do gato.', italic=True)
p('Nota de precisão a observar na pronúncia: a expressão literal «sala multiespécie» não consta dos Avisos. '
  'Consta do documento da Direção-Geral de Veterinária n.º 01/DSSPA/M//2010, de dezembro de 2010, sobre '
  'requisitos dos centros de recolha, que classifica as «Instalações por espécie» como obrigatórias e a «sala '
  'multiespécie» como recomendável, admitindo em alternativa «protocolos com outros centros de recolha ou '
  'outras entidades». Nos Avisos, a designação é «boxe para outros animais» e, a partir de 2025, '
  '«compartimento para outras espécies». É esta a expressão a citar.', size=9.5, cor=CINZA)

h2('4.7. A atividade existe e a própria DGAV a registou')
p('O Relatório de Atividades dos Centros de Recolha Oficial relativo a 2025 contém a seguinte advertência '
  'metodológica:')
cit('«Para efeitos do presente relatório, são considerados os dados referentes somente a cães e gatos. Alguns '
    'CRO têm ações realizadas com outras espécies, contudo esses dados, apesar de se encontrarem explanados na '
    'tabela, não foram considerados para os totais.»',
    'DGAV, Relatório de Atividades dos Centros de Recolha Oficial de Animais de Companhia, 2025.')
p('O enunciado é duplamente útil. Documenta, por fonte própria da DGAV, que há centros de recolha oficial a '
  'intervir sobre outras espécies; e documenta que essa atividade não é medida, porque os dados declarados '
  'pelos municípios são excluídos dos totais. A prática antecede, pois, o enquadramento.')

h2('4.8. O recinto multiespécie no projeto de RGAC')
p('O projeto de RGAC prevê que os centros de recolha possam dispor de, pelo menos, um recinto multiespécie '
  'adequado a espécies pecuárias, cumprindo a legislação específica. A previsão é coerente com a base legal '
  'identificada no ponto 4.5 e com a série de Avisos do ponto 4.6, e é o lugar próprio para a matéria.')

h2('4.9. Os modelos europeus')
p('Três modelos, quanto à relação entre a instalação destinada a animais de companhia e o alojamento de '
  'animais de espécie pecuária encontrados sem detentor.')
bullet('Modelo dualista, em França, Espanha e Itália ao nível nacional. Duas figuras jurídicas distintas, uma '
       'para os animais de companhia e outra para o gado. Em França, a «fourrière» dos art.ºs L211-24 e '
       'seguintes do Code rural et de la pêche maritime cobre cães e gatos, e o gado tem a figura autónoma do '
       '«lieu de dépôt». Em Espanha, a al. b) do n.º 3 do art.º 1.º da Ley 7/2023 exclui expressamente do seu '
       'âmbito os animais de produção, que ficam sob o regime das «reses mostrencas».')
bullet('Modelo unitário espécie-neutro, nos Países Baixos e na Bélgica. Há uma só obrigação de recolha e '
       'guarda, redigida para «um animal», qualquer que seja a espécie, com encaminhamento diferenciado na '
       'execução. O lid 3 do art.º 5:8 do Burgerlijk Wetboek neerlandês dispõe que «Indien een dier wordt '
       'gevonden» — se for encontrado um animal — o burgomestre é competente, decorridas duas semanas, para o '
       'transmitir a terceiro. A doutrina administrativa municipal confirma que o dever de acolhimento não se '
       'limita a cães e gatos e abrange todos os animais detidos.')
bullet('Modelo intermédio, no nível regional italiano. A Lei Regional da Calábria n.º 45, de 3 de outubro de '
       '2023, é o único diploma identificado que positiva a instalação de companhia aberta a outras espécies '
       'com padrão de separação. A al. b) do n.º 2 do seu art.º 28.º admite no canil sanitário «altri animali '
       'rinvenuti senza proprietario […] compatibilmente con la recettività e le caratteristiche della '
       'struttura»; a al. c) do n.º 1 do art.º 29.º exige que, «in caso di ricovero di specie diverse tra loro '
       'incompatibili», sejam usados meios que impeçam que os animais «possano vedersi, annusarsi o udirsi '
       'reciprocamente»; e o art.º 32.º admite a coexistência de estruturas diversas «purché siano separate, '
       'fisicamente e funzionalmente», com «uso in comune delle strutture di servizio e sanitarie».')
p('Duas notas de delimitação, para que o argumento comparado não seja sobre-estendido. Primeira: nenhum dos '
  'ordenamentos analisados impõe uma instalação multiespécie, pelo que a solução portuguesa, se avançar, é '
  'inovadora e não transposta. Segunda: o diploma calabrês define «animale d\'affezione» como o animal detido '
  '«senza fini produttivi o alimentari», pelo que o gado permanece formalmente fora do seu âmbito; a abertura '
  'do art.º 28.º tem finalidade de profilaxia antirrábica.', size=9.5, cor=CINZA)

p('Nas Ilhas Britânicas há duas peças de interesse direto, uma de modelo e outra de advertência.')
p('A peça de modelo é galesa. O Code of Best Practice for Animal Welfare Establishments, do Governo do País '
  'de Gales, de 2020, é o único documento oficial identificado que inclui no seu âmbito as instalações '
  'municipais de recolha de animais errantes e as trata como instalações multiespécie. O âmbito declarado '
  'abrange «rehabilitation centres, rescue centres, and stray animal facilities (local authority or '
  'contractor)» e a definição é a seguinte:')
cit('«A person, organisation or establishment who holds themselves out to receive vulnerable animals on a '
    'regular basis, whether companion, farmed, wild, protected or other animals, with a view to rehabilitating '
    'and either rehoming or releasing (back to the wild), or providing long-term care.»',
    'Code of Best Practice for Animal Welfare Establishments, Welsh Government, 2020, definição de Animal '
    'Welfare Establishment.')
p('O código fixa, para os recintos interiores e exteriores, o requisito de «Separation from other species if '
  'appropriate» e «Separation from other species as appropriate», prevê expressamente a coexistência de '
  'estábulos e canis na mesma instalação, e faz depender a lotação máxima dos recursos efetivos do '
  'estabelecimento, incluindo a necessidade de manter animais de espécies diferentes separados e fora da vista '
  'e do olfato dos restantes. É o molde técnico mais completo encontrado.')
p('A peça de advertência é irlandesa, e deve ser retida com igual atenção. O n.º 1 do art.º 2.º do Pounds '
  '(Provision and Maintenance) Act, 1935, impõe às autoridades locais o dever de prover instalação, com '
  'certificação prévia de adequação por entidade externa ao município. A instalação é multiespécie por '
  'definição legal. Sucede que o poder de fixar padrões técnicos, previsto na al. h) do n.º 3 do art.º 5.º do '
  'Animals Act, 1985, nunca foi exercido, e a revisão governamental de 2017 concluiu que as instalações, '
  'sobretudo as privadas com fim lucrativo, estão «inadequately regulated».')
p('A conclusão a extrair da comparação não é, por isso, que a instalação multiespécie seja boa ou má em si. É '
  'que a figura sem norma técnica produz maus-tratos, e que a norma técnica é precisamente o contributo que '
  'esta área tem para dar. O caso irlandês mostra também o inverso quando o investimento é feito a montante: '
  'segundo os dados abertos do Department of Agriculture, Food and the Marine, as occisões de equídeos '
  'apreendidos passaram de 4 231, em 2014, para 14, em 2022, e a proporção de animais realojados subiu de '
  'cerca de 10 % para 76 %.')
p('Reserva quanto a estes números: provêm do conjunto de dados aberto A0020 do Department of Agriculture, '
  'Food and the Marine, com uma divergência não explicada, no ano de 2019, entre a ficha do próprio '
  'departamento, que indica 885 apreensões, e o conjunto de dados, que indica 1 050. Os valores posteriores a '
  '2022 não foram confirmados.', size=9.5, cor=CINZA)

h2('4.10. Fontes do ponto 04')
bullet('Projeto: art.ºs 48.º, al. c), 54.º, 55.º, 57.º, 58.º e 59.º do anexo; estrutura do Título II; ficha de '
       'avaliação legislativa, quadro das audições obrigatórias.')
bullet('Decreto-Lei n.º 276/2001 — art.ºs 2.º, n.º 1, als. c) e t), 3.º, n.º 1, al. a), e 19.º.')
bullet('Decreto-Lei n.º 314/2003 — art.ºs 2.º, al. n), 8.º, 9.º, 10.º, 11.º e 12.º.')
bullet('Lei n.º 27/2016 — art.ºs 1.º a 5.º, em especial o n.º 1 do art.º 3.º e os n.ºs 9 e 10 do mesmo artigo.')
bullet('Portaria n.º 146/2017 — normas técnicas dos programas de captura, esterilização e devolução.')
bullet('Código Civil, art.º 1323.º, na redação da Lei n.º 8/2017 — regime do animal achado, aplicável a '
       'qualquer espécie.')
bullet('Código da Estrada, art.º 92.º — condução de animais na via pública. A norma que sanciona o '
       'proprietário que deixe o animal vaguear não foi confirmada quanto ao número do artigo.')
bullet('Portaria n.º 1112/2009 — Rede Nacional de Centros de Recuperação de Fauna, coordenada pelo ICNF em '
       'articulação com a DGAV, para animais selvagens.')
bullet('Projeto de RGAC — artigo relativo aos centros de recolha, quanto ao recinto multiespécie. Trabalho em '
       'curso, citado como tal.')
bullet('Despacho n.º 3321/2018, publicado no Diário da República, 2.ª série, n.º 66, de 4 de abril de 2018 — '
       'programa de apoio à construção e modernização de centros de recolha oficial; anexo «Valores de '
       'referência e limites».')
bullet('Avisos n.ºs 1/2021, 1/2022 e 1/2023 do ICNF-DBEAC e n.ºs 1/2025 e 1/2026 da DGAV-DBEA — requisitos '
       'mínimos de construção e tabelas de apoio. Os Avisos de 2020 e 2024 não foram consultados.')
bullet('Documento da Direção-Geral de Veterinária n.º 01/DSSPA/M//2010, de dezembro de 2010 — requisitos dos '
       'centros de recolha; origem da expressão «sala multiespécie».')
bullet('DGAV, Relatório de Atividades dos Centros de Recolha Oficial de Animais de Companhia, 2025.')
bullet('Code rural et de la pêche maritime (França), art.ºs L211-19-1 e L211-23 e seguintes; Ley 7/2023, de 28 '
       'de marzo (Espanha), n.º 3 do art.º 1.º; Burgerlijk Wetboek (Países Baixos), art.º 5:8; Code wallon du '
       'Bien-être animal e Vlaamse Codex Dierenwelzijn (Bélgica); Legge 14 agosto 1991, n. 281, e Lei Regional '
       'da Calábria n.º 45, de 3 de outubro de 2023 (Itália), art.ºs 2.º, 28.º, 29.º e 32.º.')
bullet('Animals Act 1971 (Inglaterra e País de Gales), art.º 7.º; Control of Horses (Wales) Act 2014; Code of '
       'Best Practice for Animal Welfare Establishments, Governo do País de Gales, 2020; Code of Practice for '
       'the Welfare of Horses, País de Gales, 2018.')
bullet('Pounds (Provision and Maintenance) Act, 1935 (Irlanda), art.º 2.º; Animals Act, 1985, al. h) do n.º 3 '
       'do art.º 5.º; Control of Horses Act, 1996; conjunto de dados aberto A0020 do Department of '
       'Agriculture, Food and the Marine.')
bullet('Projeto de Resolução n.º 82/XIV/1.ª — documenta a ausência de infraestrutura para fiel depositário de '
       'equídeos apreendidos e a exigência de registo como exploração pecuária para constituir santuário.')
bullet('Resolução do Conselho de Ministros n.º 78/2021, de 25 de junho, e Estratégia Nacional para os Animais '
       'Errantes, do ICNF — ambas circunscritas aos animais de companhia.')

# ──────────────── Resíduos do ponto eliminado sobre comércio não sedentário ────────────────
h1('Secção complementar — Venda em comércio não sedentário, feiras e leilões')

h2('C.1. A omissão dos animais vivos no elenco de proibições')
p('A questão de partida era a omissão dos animais vivos no elenco de proibições do n.º 2 do art.º 133.º do '
  'anexo. A análise conclui que não houve decisão neste projeto nem regressão face ao regime vigente.')
bullet('No ficheiro não há qualquer eliminação de texto relativa a animais no art.º 133.º, nem comentário '
       'ancorado ao artigo. A única alteração registada em todo o artigo é a eliminação da expressão «, na sua '
       'redação atual» na al. a) do n.º 2, em nome de Maria João Torres, com data de 1.9.2026.')
bullet('O n.º 2 do art.º 133.º reproduz literalmente o n.º 2 do art.º 75.º do Decreto-Lei n.º 10/2015, de 16 '
       'de janeiro: as mesmas sete alíneas, na mesma ordem e com a mesma redação. A omissão é herdada de 2015.')
bullet('Em 2015 a matéria já tinha sede própria. O n.º 6 do art.º 35.º do Decreto-Lei n.º 276/2001, na redação '
       'do Decreto-Lei n.º 315/2003, de 17 de dezembro, dispõe que «não é permitida a venda ambulante de '
       'animais de companhia», no mesmo artigo que fixa as condições da venda em feiras e mercados.')
bullet('O critério do elenco é coerente: fitofarmacêuticos, medicamentos, aditivos para alimentação animal, '
       'armas e explosivos, combustíveis, moedas e notas e veículos são produtos cuja venda fora de '
       'estabelecimento envolve risco de segurança ou de saúde pública. O animal não é um produto e o '
       'fundamento da proibição é o bem-estar, matéria de outro diploma.')

h2('C.2. Os leilões de animais')
p('O n.º 1 do art.º 153.º do anexo define a atividade leiloeira como a venda «de bens móveis e imóveis, '
  'corpóreos e incorpóreos ou de animais», sujeita a comunicação prévia, com a DGDCCS como entidade '
  'coordenadora e sem requisito algum de identificação, registo ou informação ao adquirente. A pesquisa das '
  'expressões «leilão» e «leiloeira» no Decreto-Lei n.º 276/2001 não devolve ocorrências: o leilão de animais '
  'de companhia não está regulado do lado do bem-estar. A partir de 31 de agosto de 2030 o n.º 3 do art.º 21.º '
  'do Regulamento (UE) 2026/1818 obriga quem coloca um cão ou gato no mercado a facultar ao adquirente prova '
  'da identificação e do registo, bem como a espécie, o sexo, a data e o país de nascimento e, se for o caso, '
  'a raça.')
p('Verificação pendente: se os Decretos-Leis n.ºs 155/2015 e 160/2015, que este projeto revoga e que regulavam '
  'a atividade leiloeira e a prestamista, continham disposição sobre animais. Se continham, há regressão; se '
  'não, o vazio é antigo e apenas se consolida.')

h2('C.3. A remissão do projeto de RGAC para o Decreto-Lei n.º 10/2015')
p('O n.º 2 do art.º 11.º do projeto de RGAC vai além da lei vigente, ao proibir a transmissão de animais de '
  'companhia «fora dos locais autorizados para o efeito, nomeadamente na via pública ou no âmbito da atividade '
  'de comércio a retalho não sedentária, designadamente em feiras, mercados ou de modo ambulante, tal como '
  'definida no Decreto-Lei n.º 10/2015, de 16 de janeiro». A proibição é ancorada por remissão a um diploma '
  'que este projeto revoga. Se o RGAC for publicado nestes termos, nasce com remissão para norma revogada. '
  'É matéria a corrigir no nosso texto, e segue para o memorando de acompanhamento, não para a pronúncia.')

h2('C.4. Hipótese não confirmada')
p('Antes do Decreto-Lei n.º 10/2015, a venda ambulante regia-se pelo Decreto-Lei n.º 122/79, de 8 de maio, '
  'cujo art.º 7.º não enumerava os produtos no corpo da lei, remetendo para lista anexa alterável por '
  'despacho. Há indicação de que essa lista, e os regulamentos municipais que nela se apoiavam, abrangiam aves '
  'e outros animais de criação. Sendo assim, o elenco de 2015 poderá ter deixado cair a proibição quanto às '
  'espécies pecuárias, que o Decreto-Lei n.º 276/2001 não alcança por excluir do seu âmbito «as espécies de '
  'pecuária». Não foi possível confirmar: o acesso à fonte foi recusado com erro 403. A confirmar-se, o tema '
  'ligar-se-ia ao ponto 02 e justificaria a sua reabertura.')

# ──────────────────── Secção transversal: Lei da Saúde Animal ────────────────────
h1('Secção transversal — A Lei da Saúde Animal como pano de fundo')

p('Esta secção serve os pontos 01, 02 e 09 e explica por que razão o Regulamento (UE) 2016/429, Lei da Saúde '
  'Animal, é o enquadramento que decide as duas questões já fechadas.')

h2('T.1. O registo de 2028 é o registo da Lei da Saúde Animal')
p('A obrigação de notificação dos estabelecimentos do artigo 9.º do Regulamento (UE) 2026/1818 não cria '
  'sistema novo: encaixa no da Lei da Saúde Animal, e di-lo expressamente.')
cit('«3. Member States shall use the information provided for in accordance with Article 84 of Regulation (EU) '
    '2016/429. Operators shall not be required to notify the information already submitted in accordance with '
    'that Article again. 4. The competent authority shall keep a register of establishments. The competent '
    'authority may, for that purpose, use the register established pursuant to Article 101(1), point (a), of '
    'Regulation (EU) 2016/429.»',
    'art.º 9.º, n.ºs 3 e 4, do Regulamento (UE) 2026/1818 — versão inglesa, JO L, 2026/1818, de 10.8.2026.')
cit('«3. Os Estados-Membros devem utilizar as informações facultadas em conformidade com o artigo 84.º do '
    'Regulamento (UE) 2016/429. Os operadores não são obrigados a notificar novamente as informações já '
    'comunicadas em conformidade com o referido artigo. 4. A autoridade competente deve manter um registo de '
    'estabelecimentos. A autoridade competente pode utilizar, para esse efeito, o registo criado nos termos do '
    'artigo 101.º, n.º 1, alínea a), do Regulamento (UE) 2016/429.»',
    'art.º 9.º, n.ºs 3 e 4, do Regulamento (UE) 2026/1818 — versão portuguesa.')
p('Daqui decorre que a obrigação de registo destes estabelecimentos não nasce em 31 de agosto de 2028. O '
  'artigo 84.º da Lei da Saúde Animal, aplicável desde 21 de abril de 2021, impõe aos operadores de '
  'estabelecimentos que detêm animais terrestres o dever de informar a autoridade competente antes de iniciar '
  'a atividade, para que o estabelecimento seja registado; e o artigo 101.º impõe à autoridade competente a '
  'constituição e manutenção dos registos correspondentes. Nenhum dos dois está limitado às espécies '
  'pecuárias, pelo que o criador e a loja de cães e gatos são, nessa aceção, estabelecimentos. O que o '
  'Regulamento de 2026 acrescenta é conteúdo e publicidade, não a obrigação de base.')

h2('T.2. A fronteira que se pede ao diploma nacional já é europeia')
p('A Lei da Saúde Animal distingue animal de companhia de animal detido em estabelecimento, e distingue-o '
  'pela finalidade da detenção:')
cit('«11) «Animal de companhia», um animal detido das espécies listadas no anexo I, que é detido para fins '
    'privados não comerciais;»',
    'art.º 4.º, ponto 11, do Regulamento (UE) 2016/429.')
p('É o mesmo critério que o projeto de RGAC adota no n.º 2 do seu artigo 2.º, com a distinção entre as '
  'espécies da Parte A do Anexo I, que são sempre animais de companhia, e as da Parte B, que o são quando '
  'detidas para fins de companhia. O critério que as observações 02 pedem não é, por isso, uma invenção '
  'nacional: é o critério do direito da União, de aplicação direta, que o próprio projeto já invoca ao '
  'referir, na al. d) do art.º 2.º do anexo, o regime de identificação, registo e circulação dos animais.')

h2('T.3. A «detenção caseira» funde duas categorias que a Lei da Saúde Animal separa')
p('A al. i) do art.º 48.º do anexo define a detenção caseira pela posse de animais cujo objetivo é «de lazer '
  'ou abastecimento do seu detentor». São duas realidades distintas à luz da Lei da Saúde Animal. A detenção '
  'por lazer, sem comércio, corresponde à detenção de animais de companhia na aceção do art.º 4.º, ponto 11, '
  'e não constitui estabelecimento. A detenção para abastecimento do próprio detentor é produção primária e '
  'cai no âmbito do art.º 84.º, com as derrogações que este e o Regulamento Delegado (UE) 2019/2035 admitem '
  'para estabelecimentos de pequena dimensão.')
p('Sujeitar ambas, indistintamente, ao registo no SNIRA trata como exploração pecuária aquilo que o direito '
  'europeu classifica como detenção de animais de companhia. É esta a observação de fundo do ponto 02, e é '
  'por esta via, e não pela reposição da exclusão eliminada, que ela melhor se sustenta: preserva o objetivo '
  'de rastreabilidade de quem produz e deixa de fora quem detém apenas por companhia.')

h2('T.4. O veículo nacional do registo')
p('Em Portugal, o registo que materializa o art.º 101.º da Lei da Saúde Animal quanto a estabelecimentos de '
  'animais de companhia é, hoje, a lista da DGAV das meras comunicações prévias do art.º 3.º-A do Decreto-Lei '
  'n.º 276/2001, divulgada nos termos do n.º 12 do seu art.º 3.º. O projeto de RGAC consolida essa função no '
  'SIAC, que passa a ser a base de dados oficial de identificação e registo dos animais de companhia, do RNAZ '
  'e dos estabelecimentos, e monta no artigo da divulgação dos estabelecimentos a lista pública com número '
  'único de aprovação, exigida também pelo n.º 3 do art.º 10.º do Regulamento (UE) 2026/1818.')
p('É esta a ligação ao ponto 01: encaminhada a loja de animais para um procedimento puramente municipal, sem '
  'pronúncia nem notificação da DGAV, nada do que o procedimento recolhe alimenta o registo que a autoridade '
  'competente tem de manter. E é esta a ligação ao ponto 09: o cadastro setorial e a base de dados setorial do '
  'anexo não incluem o SIAC entre os sistemas a articular.')

h2('T.5. Fontes e verificações pendentes desta secção')
bullet('Regulamento (UE) 2026/1818 — art.º 9.º, n.ºs 3 e 4, e art.º 10.º, n.º 3, nas versões inglesa e '
       'portuguesa do texto publicado no Jornal Oficial. Confirmado.')
bullet('Regulamento (UE) 2016/429 — art.º 4.º, ponto 11. Confirmado.')
bullet('Regulamento (UE) 2016/429 — art.ºs 84.º, 93.º e 101.º. O teor foi apurado por fonte secundária: o '
       'acesso ao EUR-Lex foi recusado a partir deste ambiente, pelo que o texto não foi lido no Jornal '
       'Oficial. A descrição acima não deve ser usada como citação verbatim sem essa confirmação.')
bullet('Regulamento Delegado (UE) 2019/2035 da Comissão — referido pelo projeto de RGAC, inclusive quanto ao '
       'art.º 71.º-A, em matéria de rastreabilidade de cães, gatos e furões. Não verificado nesta sessão.')
bullet('Verificação pendente: se os estabelecimentos de animais de companhia estão hoje efetivamente '
       'registados ao abrigo do art.º 84.º da Lei da Saúde Animal e em que sistema. É a pergunta que determina '
       'se existe já um incumprimento a corrigir ou apenas um risco a prevenir.')

# ───────────────────────────── Registo ─────────────────────────────
doc.save('/home/user/Legislacao/DL 405_2026/Fundamentacao_das_Observacoes.docx')
print('OK')
