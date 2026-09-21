# -*- coding: utf-8 -*-
from _memo_engine import *
from docx.shared import Cm


def construir(doc):
    capa(doc,
         'Anexo de jurisprudência e doutrina',
         'Delimitação entre o Decreto-Lei n.º 314/2003 e o Decreto-Lei n.º 276/2001',
         'Elementos jurisprudenciais, doutrinais e de prática administrativa recolhidos em apoio da '
         'interpretação exposta no anexo de delimitação',
         'Direção-Geral de Alimentação e Veterinária   ·   setembro de 2026')

    enquadramento(doc, [
        'Este anexo reúne os elementos externos que sustentam a conclusão do anexo de delimitação: os '
        'limites de alojamento por prédio do artigo 3.º do Decreto-Lei n.º 314/2003 não constituem '
        'limiar de capacidade dos estabelecimentos de criação. A pesquisa cobriu a base de dados do '
        'Instituto de Gestão Financeira e Equipamentos da Justiça (dgsi.pt) em todas as bases '
        'disponíveis, a jurisprudência do Tribunal Constitucional, doutrina publicada e prática '
        'administrativa. Os limites da pesquisa constam do ponto 11.'])

    # ------------------------------------------------------------------ 1
    h1(doc, '1.', 'Genealogia da norma')
    para(doc,
         'O artigo 3.º do Decreto-Lei n.º 314/2003 não é norma inovadora. Descende do artigo 10.º do '
         'Decreto-Lei n.º 317/85, de 2 de agosto, inserido no capítulo respeitante aos cães, secção do '
         'alojamento, do então Programa Nacional de Luta e Vigilância Epidemiológica da Raiva Animal. '
         'A epígrafe do preceito era, e é elucidativa: «Remoção dos animais por decisão camarária; '
         'processo aplicável».')
    citacao(doc,
            ['1 — A permanência de cães em habitações situadas em zonas urbanas fica condicionada à '
             'existência de boas condições de alojamento dos mesmos, ausência de riscos sob o aspecto '
             'sanitário e inexistência nestes animais de doenças transmissíveis ao homem.',
             '2 — As câmaras municipais, sempre que razões de salubridade ou tranquilidade da '
             'vizinhança o imponham, poderão determinar a remoção de quaisquer cães ou outros animais '
             'de companhia.',
             '3 — A câmara municipal competente, confirmada a existência de situações referidas no '
             'número anterior, notificará o dono ou detentor dos animais para a remoção dos mesmos no '
             'prazo de 8 dias.'],
            'N.os 1 a 3 do artigo 10.º do Decreto-Lei n.º 317/85, de 2 de agosto, transcritos no '
            'Acórdão do Tribunal Constitucional n.º 158/95')
    para(doc,
         'A unidade de referência era a **habitação**. O Decreto-Lei n.º 314/2003 substituiu-a por '
         '«prédios urbanos, rústicos ou mistos» e acrescentou os limites numéricos, sem alterar a '
         'natureza da norma nem a sua inserção sistemática. O Tribunal Constitucional situou o '
         'preceito no diploma que visou «englobar num único diploma as normas a que deve submeter-se a '
         'profilaxia médica da raiva e as medidas de polícia sanitária».')

    # ------------------------------------------------------------------ 2
    h1(doc, '2.', 'Tribunal Constitucional')
    para(doc,
         'A qualificação da decisão camarária de remoção está fixada há quarenta anos, e uma das '
         'decisões tem força obrigatória geral.')
    tabela(doc,
           ['Acórdão', 'Objeto e sentido'],
           [
            ['N.º 158/95\n2.ª Secção\nRel. Guilherme da Fonseca',
             'Inconstitucionalidade orgânica do n.º 4 do artigo 10.º do Decreto-Lei n.º 317/85, na '
             'parte em que atribuía ao tribunal judicial a competência para conhecer do recurso. '
             'Qualifica a decisão camarária como ato administrativo.'],
            ['N.os 190/95 e 193/95', 'Remetem integralmente para o Acórdão n.º 158/95.'],
            ['N.º 579/95\nPlenário\nRel. Maria Fernanda Palma',
             '**Declaração de inconstitucionalidade com força obrigatória geral** da mesma norma.'],
            ['N.º 229/2007\n2.ª Secção\nRel. Maria Fernanda Palma',
             'Mesma solução quanto ao n.º 6 do artigo 3.º do Decreto-Lei n.º 314/2003.'],
           ],
           [Cm(4.4), Cm(12.2)])
    para(doc,
         'O fundamento é constante e respeita ao bem jurídico protegido.')
    citacao(doc,
            ['A decisão camarária é caracterizável como acto administrativo na medida em que há aí um '
             'comando de um órgão autárquico, prosseguindo e realizando interesses públicos '
             'relativamente à remoção de um animal de raça canina, com efeitos jurídicos sobre uma '
             'situação individual e num caso concreto.'],
            'Acórdão do Tribunal Constitucional n.º 158/95, transcrito no Acórdão n.º 229/2007')
    citacao(doc,
            ['[A norma] ao prever que «as razões de salubridade ou tranquilidade da vizinhança» (…) são '
             'fundamento da decisão camarária de remoção dos animais em causa, integra uma tal decisão '
             'no âmbito (…) das atribuições cometidas às câmaras (…). A tranquilidade da vizinhança ou '
             'a qualidade de vida em que pode interferir a instalação de animais em habitações sem as '
             'devidas condições (…)'],
            'Acórdão do Tribunal Constitucional n.º 579/95, transcrito no Acórdão n.º 229/2007')
    para(doc,
         'O que está em causa é polícia sanitária municipal sobre a detenção doméstica. Em nenhuma das '
         'decisões o preceito é associado ao acesso a uma atividade económica, ao licenciamento de '
         'estabelecimentos ou à competência da autoridade veterinária nacional.')

    # ------------------------------------------------------------------ 3
    h1(doc, '3.', 'Jurisprudência administrativa')

    h2(doc, '3.1', 'O caso dos quarenta e cinco cães')
    para(doc,
         'O acórdão do Tribunal Central Administrativo Sul de 4 de fevereiro de 2010, processo n.º '
         '04784/09, relatado por Rui Pereira, é o mais próximo da questão. Fixa a natureza da norma.')
    citacao(doc,
            ['I – A posse de animais [cães ou gatos] em qualquer número em prédios urbanos, rústicos ou '
             'mistos, nos termos do n.º 1 do artigo 3.º do DL n.º 314/2003, de 17/12, depende da '
             'existência de uma situação de salubridade ambiental, com vista a evitar um perigo para a '
             'saúde pública.'],
            'Sumário do Acórdão do TCA Sul de 4 de fevereiro de 2010, processo n.º 04784/09')
    para(doc,
         'O caso tem valor demonstrativo próprio. Estava em causa uma detentora que mantinha cerca de '
         'quarenta e cinco cães no quintal da sua residência. A Administração atuou exclusivamente ao '
         'abrigo do artigo 3.º do diploma da raiva.')
    citacao(doc,
            ['Considerando: — Que M…, residente no lote …, possui ilegalmente no quintal da sua '
             'residência aproximadamente 45 cães; — Que foram realizadas vistorias pelo Delegado de '
             'Saúde e pelo Médico Veterinário Municipal; — Que, no dia 16 de Setembro de 2005, se '
             'realizou uma vistoria conjunta (…) que concluíram existir uma situação de insalubridade '
             'ambiental, causadora de maus cheiros e proliferação de insectos vectores de doenças, '
             'constituindo tal facto um perigo para a saúde pública; (…) Ordeno, nos termos do n.º 5 do '
             'artigo 3.º do Decreto-Lei n.º 314/2003, de 17 de Dezembro, (…) que M… proceda à remoção '
             'para o canil municipal ou para outro destino que reúna as condições estabelecidas neste '
             'diploma legal (…) de todos os cães que se encontrem na sua residência, para além do '
             'limite imposto por lei [seis cães].'],
            'Despacho do Presidente da Câmara Municipal de 2 de janeiro de 2006, transcrito no Acórdão '
            'do TCA Sul, processo n.º 04784/09')
    destaque(doc, [
        'Em todo o processo — despacho municipal, decisão de primeira instância e acórdão — **o '
        'Decreto-Lei n.º 276/2001 não é mencionado uma única vez**. Perante quarenta e cinco cães, nem '
        'a Administração nem os tribunais equacionaram a existência de um alojamento sujeito a título '
        'de acesso. O caso foi tratado, do princípio ao fim, como detenção doméstica insalubre.'])

    h2(doc, '3.2', 'A unicidade do meio de reação')
    para(doc,
         'O acórdão do Tribunal da Relação de Évora de 18 de abril de 2013, processo n.º 78/12, '
         'relatado por Elisabete Valente, respeitava a uma detentora com dez cães na habitação e '
         'quintal anexo. O Ministério Público intentara ação cível pedindo que se abstivesse de deter '
         'mais de três.')
    citacao(doc,
            ['– Deve recorrer-se aos mecanismos previstos no Decreto-Lei n.º 314/2003, de 17 de '
             'Dezembro, para pôr fim à situação em que um particular detenha na sua habitação e quintal '
             'anexo mais do que 3 canídeos, sem as condições de mínimas de higiene e salubridade para '
             'tal.',
             '– É competente o Tribunal Administrativo para conhecer de recurso no âmbito desse DL, '
             'pois a decisão para a remoção de animais, tendo em conta a saúde pública, é um acto '
             'administrativo.'],
            'Sumário do Acórdão do TRE de 18 de abril de 2013, processo n.º 78/12')
    para(doc,
         'No corpo da decisão o tribunal é ainda mais assertivo quanto ao caráter fechado do '
         'mecanismo: «A situação está legalmente prevista no DL e o meio de reacção é só um, aquele que '
         'a lei prevê e que supra descrevemos.» O regime do artigo 3.º tem via própria, exclusiva e '
         'administrativa: vistoria conjunta do delegado de saúde e do médico veterinário municipal, '
         'notificação do detentor, remoção para o canil municipal, sindicância nos tribunais '
         'administrativos.')

    h2(doc, '3.3', 'Taxonomia judicial dos diplomas')
    para(doc,
         'O acórdão do Tribunal da Relação de Guimarães de 1 de fevereiro de 2022, processo n.º '
         '4718/18.3T8GMR.G1, relatado por José Amaral, arruma expressamente os diplomas por matéria.')
    citacao(doc,
            ['(…) não é regulada pelo Código da Estrada nem pelos diplomas legais (Decretos-Lei n.º '
             '314/2003, de 17 de Dezembro, n.º 82/2019, de 27 de Junho, e n.º 315/2009, de 29 de '
             'Outubro) que tratam das suas condições sanitárias (combate à raiva), do seu rastreio, '
             'registo e licenciamento (animais de companhia) ou da criação, reprodução e detenção '
             '(animais perigosos).'],
            'Acórdão do TRG de 1 de fevereiro de 2022, processo n.º 4718/18.3T8GMR.G1')
    para(doc,
         'O Decreto-Lei n.º 314/2003 é aí identificado, sem hesitação, como o diploma das condições '
         'sanitárias de combate à raiva.')

    # ------------------------------------------------------------------ 4
    h1(doc, '4.', 'Contextos de aplicação do artigo 3.º na jurisprudência comum')
    para(doc,
         'Recolheram-se trinta e três acórdãos das Relações que citam o Decreto-Lei n.º 314/2003. '
         'Quando o artigo 3.º é convocado, é sempre em contexto de detenção doméstica, vizinhança ou '
         'salubridade. Nenhum o aplica como limiar de capacidade de estabelecimento autorizado.')
    tabela(doc,
           ['Decisão', 'Contexto de aplicação'],
           [
            ['TRL, 18.12.2025, proc. 31180/22.3T8LSB.L1-6',
             'Resolução de contrato de arrendamento por violação de regras de higiene e de boa '
             'vizinhança. Arrendatária com três cães e um gato no locado.'],
            ['TRC, 13.12.2022, proc. 856/22.6T8GRD.C1',
             'Tutela da personalidade. Direito ao sossego, à tranquilidade, à saúde e ao sono do '
             'vizinho. Ordenada a retirada dos animais.'],
            ['TRP, 30.4.2026, proc. 6599/24.9T8MAI.P1',
             'Direitos de personalidade. Ruído provocado por animal doméstico.'],
            ['TRP, 21.11.2016, proc. 3091/15.6T8GDM.P1',
             'Arrendamento para habitação. Proibição de cães no locado.'],
            ['TRG, 19.2.2026, proc. 585/08.3TBPVL.G1',
             'Ação executiva para prestação de facto. Remoção de canídeos de imóvel adjudicado.'],
            ['TRE, 18.4.2013, proc. 78/12', 'Competência em razão da matéria. Remoção de animais.'],
            ['TCA Sul, 10.10.2013, proc. 10348/13',
             'Forma processual do mandado judicial para remoção de animais.'],
           ],
           [Cm(5.4), Cm(11.2)])

    # ------------------------------------------------------------------ 5
    h1(doc, '5.', 'O plano do estabelecimento')
    para(doc,
         'Quando o litígio respeita a um estabelecimento, os tribunais convocam outro conjunto de '
         'normas. O artigo 3.º do diploma da raiva não aparece.')
    tabela(doc,
           ['Decisão', 'Enquadramento convocado'],
           [
            ['STA, 7.3.2006, proc. 0794/05\nCanil com capacidade para cem cães',
             'Plano Director Municipal, licenciamento de construção, artigo 103.º do Decreto-Lei n.º '
             '380/99. A capacidade do canil é aferida em sede urbanística; os limites do artigo 3.º não '
             'são convocados nem discutidos.'],
            ['TCA Norte, 21.4.2023, proc. 01571/22.6BEPRT\nEncerramento de alojamento de associação '
             'sem fins lucrativos',
             'Regime do Decreto-Lei n.º 276/2001. Providência cautelar contra ato de encerramento do '
             'alojamento.'],
           ],
           [Cm(5.6), Cm(11.0)])
    para(doc,
         'O contraste é eloquente. Um canil para cem cães discute-se em sede de instrumento de gestão '
         'territorial e de licenciamento; quarenta e cinco cães no quintal de uma residência '
         'discutem-se em sede de salubridade e remoção camarária. São dois circuitos jurídicos que não '
         'se cruzam.')

    # ------------------------------------------------------------------ 6
    h1(doc, '6.', 'O intervalo de 2001 a 2003')
    para(doc,
         'Este é o elemento de maior peso, e resulta apenas da sequência dos diplomas.')
    numlist(doc, [
        'O Decreto-Lei n.º 317/85 fixava, no artigo 10.º, a regra da permanência de cães em habitações '
        'e o poder camarário de remoção.',

        'O **Decreto-Lei n.º 91/2001, de 23 de março**, revogou-o expressamente e **não reproduziu '
        'qualquer limite de animais por fogo nem qualquer poder camarário de remoção**. A palavra '
        '«alojamento» não ocorre uma única vez no seu articulado.',

        'O **Decreto-Lei n.º 276/2001, de 17 de outubro** — todo o regime dos alojamentos de '
        'reprodução, criação, manutenção e venda, o procedimento de acesso, a figura da criação '
        'comercial e o anexo I — foi aprovado **dentro desse intervalo**.',

        'O **Decreto-Lei n.º 314/2003, de 17 de dezembro**, revogou o Decreto-Lei n.º 91/2001 e '
        'reintroduziu os limites, agora por referência a prédios urbanos, rústicos ou mistos.',
    ])
    citacao(doc,
            ['1 — É revogado o Decreto-Lei n.º 317/85, de 2 de Agosto.'],
            'N.º 1 do artigo 9.º do Decreto-Lei n.º 91/2001, de 23 de março')
    citacao(doc,
            ['É revogado o Decreto-Lei n.º 91/2001, de 23 de Março (…)'],
            'Artigo 19.º do Decreto-Lei n.º 314/2003, de 17 de dezembro')
    destaque(doc, [
        'Durante **dois anos e nove meses**, entre 23 de março de 2001 e 17 de dezembro de 2003, o '
        'ordenamento português não conheceu qualquer limite de animais por fogo. Foi exatamente nesse '
        'período que se aprovou e entrou em vigor o regime dos alojamentos do Decreto-Lei n.º '
        '276/2001. Um regime construído na ausência de qualquer limite de detenção **não pode tê-lo '
        'pressuposto**, e a sua reposição posterior, em diploma de polícia sanitária, não o converte '
        'retroativamente em teto de lotação dos estabelecimentos.'])

    # ------------------------------------------------------------------ 7
    h1(doc, '7.', 'O anexo I do Decreto-Lei n.º 276/2001')
    para(doc,
         'O argumento anterior confirma-se pelo modo como o próprio diploma dos alojamentos dimensiona '
         'a capacidade: por superfície disponível por animal, e não por contagem de cabeças.')
    citacao(doc,
            ['Num canil, cada animal deverá dispor de uma superfície de base de, pelo menos, 1,22 m × '
             '1,22 m;',
             'Um recinto com as dimensões 1,50 m × 3 m não poderá alojar mais de dois cães de raça '
             'média ou grande, ou três cães de raça pequena.',
             'A superfície mínima do chão do recinto para uma cadela e respectiva ninhada deve estar '
             'compreendida entre 4 m² e 6 m².'],
            'Anexo I do Decreto-Lei n.º 276/2001, para que remete o n.º 6 do artigo 25.º')
    para(doc,
         'Se o teto de quatro ou de seis animais valesse para os alojamentos, todo este sistema de '
         'dimensionamento seria inútil: nenhum estabelecimento chegaria alguma vez ao ponto em que as '
         'medidas do anexo se tornam operativas. A existência do anexo pressupõe, necessariamente, '
         'alojamentos com mais animais do que os limites do diploma da raiva admitem por fogo.')

    # ------------------------------------------------------------------ 8
    h1(doc, '8.', 'Doutrina')
    para(doc,
         'A doutrina que se ocupou do artigo 3.º recusou, pelas mesmas razões, que os seus limites '
         'valham fora do domínio sanitário.')
    citacao(doc,
            ['Seria no mínimo abusivo pretender retirar daqui uma limitação geral em termos de detenção '
             'de animais numa fracção autónoma, numa limitação matreira aos poderes conferidos pelo '
             'código civil aos proprietários.',
             'A limitação prevista nesta norma vale para efeito de prevenção de zoonoses. Mal se '
             'compreenderia, num diploma desta natureza, uma limitação geral, feita em abstracto (sem '
             'qualquer atenção, por exemplo, à dimensão da fracção autónoma) aos poderes conferidos ao '
             'proprietário pelo Direito Civil.',
             'O limite máximo aqui estabelecido releva para efeitos de luta e vigilância '
             'epidemiológica, indiciando riscos higío-sanitários, não pretende regular relações de '
             'vizinhança, nem tutelar direitos de personalidade dos outros conviventes no prédio.'],
            'Sandra Passinhas, «Os animais e o regime português da propriedade horizontal», Revista da '
            'Ordem dos Advogados, Ano 66, Vol. II, setembro de 2006')
    para(doc,
         'A análise do quadro contraordenacional aponta no mesmo sentido, ao autonomizar a infração '
         'por excesso de animais **por fogo urbano**, sancionada pela al. c) do n.º 3 do artigo 14.º do '
         'Decreto-Lei n.º 314/2003, das infrações de atividade do artigo 68.º do Decreto-Lei n.º '
         '276/2001. São tipos distintos, com pressupostos distintos.')
    bullets(doc, [
        'Bruno Filipe Salvador da Silva Branco, «A detenção de animais de companhia — uma análise do '
        'ponto de vista contraordenacional», Revista Jurídica Lusófona Brasileira, Ano 5 (2019), n.º '
        '2, pp. 229-260.',
        'Associação Portuguesa de Médicos Veterinários Especialistas em Animais de Companhia, revisão '
        'crítica legislativa, que lê o artigo 3.º como fixando o «número de animais de companhia que '
        'legalmente é possível **deter**».',
    ], marker='·')

    # ------------------------------------------------------------------ 9
    h1(doc, '9.', 'Prática administrativa')
    para(doc,
         'A prática das autoridades acompanha a separação. A página institucional da Direção-Geral de '
         'Alimentação e Veterinária sobre autorização e requisitos de funcionamento dos alojamentos de '
         'animais de companhia invoca o Decreto-Lei n.º 276/2001 e o Decreto-Lei n.º 260/2012, e '
         'remete para os anexos por espécie. **Não menciona o Decreto-Lei n.º 314/2003 nem qualquer '
         'limite de animais por fogo.**')
    para(doc,
         'Também a repartição de competências contraordenacionais separa os dois planos: as infrações '
         'do artigo 14.º do Decreto-Lei n.º 314/2003 distribuem-se por juntas de freguesia e '
         'municípios, ao passo que as infrações do artigo 68.º do Decreto-Lei n.º 276/2001 são '
         'instruídas pela autoridade veterinária nacional. Diferentes entidades instrutórias para '
         'diferentes domínios materiais.')

    # ------------------------------------------------------------------ 10
    h1(doc, '10.', 'Elemento em sentido aparentemente contrário')
    para(doc,
         'Por dever de rigor assinala-se a única decisão recolhida que aplica o artigo 3.º a uma '
         'instalação descrita como canil.')
    citacao(doc,
            ['I – Deve ser deferida a providência que visa a remoção de animais alojados num canil '
             'clandestino, instalado no logradouro de um prédio urbano, de onde emana um cheiro '
             'nauseabundo, ladrando os 30 canídeos dia e noite o que traduz violação do disposto no '
             'artigo 3.º/1 do Decreto-lei n.º 314/2003, de 17 de Dezembro.'],
            'Sumário do Acórdão do TRL de 28 de junho de 2007, processo n.º 1692/2007-8')
    para(doc,
         'A decisão não infirma a conclusão deste anexo, por três razões cumulativas.')
    numlist(doc, [
        'Aplicou o **n.º 1** do artigo 3.º, que é cláusula geral de salubridade de alcance universal, e '
        'não os limites numéricos dos n.os 2 e 4.',
        'A instalação era **clandestina**, isto é, não titulada ao abrigo do Decreto-Lei n.º 276/2001. '
        'Não estava em causa a capacidade de um alojamento autorizado, mas a existência de uma '
        'situação de facto insalubre.',
        'A causa de pedir era de **tutela da personalidade** — direitos à tranquilidade, à qualidade de '
        'vida, à habitação e ao ambiente —, e não de acesso a atividade.',
    ])
    para(doc,
         'Retira-se daqui uma precisão útil: o n.º 1 do artigo 3.º pode alcançar qualquer situação de '
         'alojamento insalubre, incluindo a de um estabelecimento não titulado. O que não faz, em caso '
         'algum, é fixar a lotação de um estabelecimento regularmente autorizado, matéria que o '
         'Decreto-Lei n.º 276/2001 regula por declaração na comunicação prévia e pelos parâmetros do '
         'seu anexo I.')

    # ------------------------------------------------------------------ 11
    h1(doc, '11.', 'Método e limites da pesquisa')
    para(doc,
         'Consultaram-se as bases do Supremo Tribunal de Justiça, das Relações de Lisboa, Porto, '
         'Coimbra, Évora e Guimarães, do Supremo Tribunal Administrativo e dos Tribunais Centrais '
         'Administrativos Sul e Norte, bem como a jurisprudência do Tribunal Constitucional. Foram '
         'descarregados e lidos trinta e três acórdãos que citam o Decreto-Lei n.º 314/2003.')
    nota(doc, [
        'Três reservas devem acompanhar a leitura deste anexo.',
        '**Primeira.** O texto do Decreto-Lei n.º 314/2003 tal como publicado no Diário da República de '
        '17 de dezembro de 2003 não foi obtido. A redação originária do artigo 3.º foi confirmada por '
        'duas vias indiretas convergentes: a versão consolidada não regista alterações a esse artigo, e '
        'a doutrina de 2006 transcreve-o com a numeração atual.',
        '**Segunda.** Não se obteve o articulado de regulamentos municipais com cláusula expressa de '
        'exclusão dos alojamentos licenciados.',
        '**Terceira.** A pesquisa combinada na base do dgsi.pt, associando a referência do diploma a '
        'outro termo, produz resultados nulos para combinações que existem no acervo. As conclusões dos '
        'pontos 4 e 5 assentam na leitura dos acórdãos efetivamente descarregados, e não em contagens '
        'dessa pesquisa combinada.'])

    # ------------------------------------------------------------------ 12
    h1(doc, '12.', 'Síntese')
    destaque(doc, [
        'A interpretação segundo a qual os limites do artigo 3.º do Decreto-Lei n.º 314/2003 não fixam '
        'a capacidade dos estabelecimentos de criação encontra apoio convergente em quatro planos: na '
        '**genealogia** da norma, que remonta a 1985 e sempre teve por objeto a permanência de animais '
        'em habitações; na **jurisprudência constitucional**, que há quarenta anos a qualifica como '
        'polícia sanitária municipal, com uma declaração de inconstitucionalidade com força '
        'obrigatória geral; na **jurisprudência administrativa e comum**, que a aplica exclusivamente a '
        'situações de detenção doméstica, mesmo perante quarenta e cinco cães, e que remete os '
        'estabelecimentos para o licenciamento; e na **doutrina**, que recusa extrair do preceito '
        'qualquer limitação geral. A tudo acresce o dado decisivo de o regime dos alojamentos ter sido '
        'aprovado num período em que nenhum limite de detenção vigorava.'])

    h1(doc, '13.', 'Elementos citados')
    bullets(doc, [
        'Acórdãos do Tribunal Constitucional n.os 158/95, 190/95, 193/95, 579/95 (Plenário) e 229/2007.',
        'Acórdão do STA de 7 de março de 2006, processo n.º 0794/05.',
        'Acórdãos do TCA Sul de 4 de fevereiro de 2010, processo n.º 04784/09, e de 10 de outubro de '
        '2013, processo n.º 10348/13.',
        'Acórdão do TCA Norte de 21 de abril de 2023, processo n.º 01571/22.6BEPRT.',
        'Acórdão do TRE de 18 de abril de 2013, processo n.º 78/12.',
        'Acórdãos do TRL de 28 de junho de 2007, processo n.º 1692/2007-8, e de 18 de dezembro de 2025, '
        'processo n.º 31180/22.3T8LSB.L1-6.',
        'Acórdão do TRC de 13 de dezembro de 2022, processo n.º 856/22.6T8GRD.C1.',
        'Acórdãos do TRP de 21 de novembro de 2016, processo n.º 3091/15.6T8GDM.P1, e de 30 de abril de '
        '2026, processo n.º 6599/24.9T8MAI.P1.',
        'Acórdãos do TRG de 1 de fevereiro de 2022, processo n.º 4718/18.3T8GMR.G1, e de 19 de '
        'fevereiro de 2026, processo n.º 585/08.3TBPVL.G1.',
        'Decreto-Lei n.º 317/85, de 2 de agosto; Decreto-Lei n.º 91/2001, de 23 de março; Decreto-Lei '
        'n.º 276/2001, de 17 de outubro; Decreto-Lei n.º 314/2003, de 17 de dezembro; Decreto-Lei n.º '
        '315/2003, de 17 de dezembro.',
        'Sandra Passinhas, Revista da Ordem dos Advogados, Ano 66, Vol. II, setembro de 2006.',
        'Bruno Branco, Revista Jurídica Lusófona Brasileira, Ano 5 (2019), n.º 2.',
    ], marker='·')
