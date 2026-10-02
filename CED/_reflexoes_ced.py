# -*- coding: utf-8 -*-
"""Conteudo do documento Reflexoes sobre o CED."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'criador informal'))
from _memo_engine import *
from docx.shared import Cm


def construir(doc):
    capa(doc,
         'Documento de reflexão',
         'Reflexões sobre os programas de captura, esterilização e devolução',
         'Zonas cinzentas do regime jurídico do CED — lacunas reconhecidas, controvérsias '
         'em aberto e posições das partes interessadas',
         'Direção-Geral de Alimentação e Veterinária   ·   setembro de 2026')

    # ================================================================= 1
    h1(doc, '1.', 'Objeto, método e advertência')
    para(doc,
         'Este documento reúne e organiza as questões que o regime jurídico dos programas de captura, '
         'esterilização e devolução deixa por resolver. Não é uma tomada de posição institucional. É um '
         'levantamento destinado a suportar decisão — seja na resposta a pedidos de esclarecimento '
         'concretos, seja na preparação de uma revisão normativa.')
    para(doc,
         'O método foi o seguinte. Partiu-se do texto em vigor — a Lei n.º 27/2016, de 23 de agosto, e a '
         'Portaria n.º 146/2017, de 26 de abril — e confrontou-se com quatro tipos de fonte: documentos '
         'oficiais de diagnóstico, pareceres de organizações profissionais, posições partidárias e '
         'regulamentos e manuais municipais. Sempre que a fonte é citada, é-o verbatim.')
    enquadramento(doc, [
        'Duas fontes estruturam todo o documento e merecem ser identificadas desde já. A **Estratégia '
        'Nacional para os Animais Errantes**, elaborada pelo Departamento de Bem-Estar dos Animais de '
        'Companhia do ICNF e submetida a consulta pública entre 19 de julho e 30 de agosto de 2023, e o '
        '**Relatório Final do Grupo de Trabalho para o Bem-Estar Animal** sobre a avaliação da '
        'implementação da Lei n.º 27/2016, publicado pela DGAV em 2021. Ambos são documentos do próprio '
        'Estado e ambos **reconhecem por escrito** a maior parte das lacunas inventariadas adiante. Não se '
        'está, portanto, a inferir a existência dos problemas: a Administração já os declarou.'])
    nota(doc, [
        '**Advertência quanto ao estatuto das fontes.** A Estratégia Nacional para os Animais Errantes é '
        'uma proposta submetida a consulta pública; não foi localizado ato que a aprove com força '
        'normativa. O projeto de revisão da Portaria n.º 146/2017 referido no ponto 4 nunca foi publicado. '
        'Um e outro valem como elementos de diagnóstico e de intenção da Administração, não como direito '
        'vigente. As posições de organizações profissionais e de partidos valem como o que são: opiniões '
        'de partes interessadas.'])

    # ================================================================= 2
    h1(doc, '2.', 'Sumário — as vinte e uma zonas cinzentas')
    para(doc,
         'O inventário que se segue está organizado em seis grupos. Os quatro primeiros pontos são lacunas '
         'que a Administração já reconheceu por escrito; os restantes resultam do confronto entre o texto '
         'da Portaria e a sua aplicação.')
    tabela(doc,
           ['#', 'Questão', 'Estado'],
           [
            ['1', 'O estatuto de cuidador de colónia não está definido', 'Reconhecido pela ENAE'],
            ['2', 'As famílias de acolhimento temporário não estão reguladas', 'Reconhecido pela ENAE'],
            ['3', 'Não se sabe quantas colónias existem nem onde', 'Reconhecido pela ENAE'],
            ['4', 'Não existe guia nacional de boas práticas para o CED', 'Reconhecido pela ENAE'],
            ['5', 'O CED não está implementado em todo o território', 'Reconhecido pela ENAE'],
            ['6', 'Regulamentos municipais proíbem alimentar errantes', 'Reconhecido pela ENAE'],
            ['7', 'Faculdade ou dever do município?', 'Zona cinzenta de regime'],
            ['8', 'Quem é a «entidade responsável pelo CED»?', 'Zona cinzenta de regime'],
            ['9', 'Em nome de quem se registam os animais no SIAC?', 'Zona cinzenta de regime'],
            ['10', 'Responsabilidade civil por danos causados pelos animais', 'Zona cinzenta de regime'],
            ['11', 'O critério feral / sociável: quem decide e como', 'Zona cinzenta de regime'],
            ['12', 'Crias: quatro prazos que não se articulam', 'Zona cinzenta de regime'],
            ['13', 'Colónias em propriedade privada: silêncio total', 'Zona cinzenta de regime'],
            ['14', 'Devolução a local que não garante segurança', 'Zona cinzenta de regime'],
            ['15', 'Suspensão e recolha sem garantias procedimentais', 'Zona cinzenta de regime'],
            ['16', 'CED e conservação da natureza: rota de colisão', 'Conflito de políticas'],
            ['17', 'Dispersão e reversão da tutela', 'Conflito de políticas'],
            ['18', 'A legislação como parte do problema', 'Conflito de políticas'],
            ['19', 'A extensão do CED a cães', 'Controvérsia ativa'],
            ['20', 'Falta de médicos veterinários municipais', 'Capacidade institucional'],
            ['21', 'A figura do animal comunitário não existe', 'Proposta pendente'],
           ],
           [Cm(1.0), Cm(9.6), Cm(6.0)])

    # ================================================================= 3
    pagebreak(doc)
    h1(doc, '3.', 'O quadro normativo em vigor')

    h3(doc, '3.1  O dever do Estado')
    para(doc,
         'A base legal do CED é uma norma de uma só frase, que enuncia um dever e não uma faculdade.')
    citacao(doc,
            ['O Estado, por razões de saúde pública, assegura, por intermédio dos centros de recolha '
             'oficial de animais, a captura, vacinação e esterilização dos animais errantes sempre que '
             'necessário, assim como a concretização de programas captura, esterilização, devolução (CED) '
             'para gatos.'],
            'Artigo 4.º da Lei n.º 27/2016, de 23 de agosto')

    h3(doc, '3.2  A regulamentação')
    para(doc,
         'Todo o regime operativo consta de um único artigo da Portaria n.º 146/2017, com dez números. '
         'Transcreve-se na íntegra, por ser a peça central de tudo o que se segue.')
    citacao(doc,
            ['1 — Como forma de gestão da população de gatos errantes e nos casos em que tal se justifique, '
             'podem as câmaras municipais, sob parecer do médico veterinário municipal, autorizar a '
             'manutenção, em locais especialmente designados para o efeito, de colónias de gatos, no âmbito '
             'de programas de captura, esterilização e devolução (CED) ao local de origem.',
             '2 — Os programas CED podem realizar-se por iniciativa das câmaras municipais ou mediante '
             'proposta de organização de proteção animal a quem a câmara municipal atribua a gestão do '
             'programa CED.',
             '3 — Deve ser evitada a implementação de programas CED nos parques públicos, nos refúgios de '
             'vida selvagem ou outros locais públicos que sirvam de habitat à vida selvagem.',
             '4 — A entidade responsável pelo CED deve assegurar: a) A existência de um plano de gestão da '
             'colónia, do qual conste a identificação do médico veterinário assistente e das pessoas que na '
             'entidade são responsáveis pela execução do programa; b) Que os animais que compõem a colónia '
             'são avaliados periodicamente do ponto de vista clínico, de forma a despistar doenças '
             'transmissíveis que, casuisticamente, sejam consideradas importantes; c) Que os animais '
             'portadores de doenças transmissíveis a outros animais ou a seres humanos são retirados da '
             'colónia; d) Que os animais capturados, antes de integrarem a colónia, são entregues nos CRO '
             'para verificação da sua aptidão; e) Que os animais capturados são esterilizados e marcados '
             'com um pequeno corte na orelha esquerda, registados e identificados eletronicamente, e '
             'desparasitados e vacinados contra a raiva ou outras medidas profiláticas obrigatórias ou '
             'consideradas no plano de gestão da colónia.',
             '5 — A colónia intervencionada será supervisionada pelo médico veterinário municipal, devendo '
             'a entidade responsável pelo programa assegurar que são prestados os cuidados de saúde e '
             'alimentação adequados aos animais, controlando as saídas ou entradas de novos animais, ou '
             'quaisquer outros fatores que perturbem a estabilidade da colónia, a segurança e a '
             'tranquilidade pública e da vizinhança, de tudo mantendo registo.',
             '6 — A dimensão da colónia de gatos não pode pôr em causa a salubridade, a saúde pública e a '
             'segurança de pessoas, animais e bens.',
             '7 — Os alojamentos e espaços utilizados pela colónia são mantidos livres de resíduos ou '
             'restos de comida, de forma a evitar a proliferação de pragas.',
             '8 — As despesas relacionadas com a manutenção de colónias de gatos são da responsabilidade da '
             'entidade promotora.',
             '9 — Sempre que a câmara municipal verifique que não está cumprido qualquer dos requisitos '
             'referidos no n.º 4, pode determinar medidas corretivas ou a suspensão do programa CED em '
             'curso e proceder à recolha dos animais para o CRO.',
             '10 — O programa a que se refere o presente artigo não é aplicável a cães.'],
            'Artigo 9.º da Portaria n.º 146/2017, de 26 de abril, na redação em vigor')
    nota(doc, [
        'A Portaria **mantém-se na redação originária de 2017**. Não regista qualquer diploma alterante. '
        'Dez números e cinco alíneas são todo o regime nacional de um programa que a Estratégia Nacional '
        'assume como o destino de toda a população errante até 2030.'])

    # ================================================================= 4
    pagebreak(doc)
    h1(doc, '4.', 'A revisão que não aconteceu')
    para(doc,
         'Em dezembro de 2021 circulou na Associação Nacional de Municípios Portugueses um projeto de '
         'portaria que alterava os artigos 3.º, 5.º, 7.º, 8.º, 9.º, 10.º e 11.º da Portaria n.º 146/2017. '
         'O seu preâmbulo enunciava a razão da intervenção.')
    citacao(doc,
            ['O período de aplicação desta Portaria já decorrido, bem como as questões que têm vindo a ser '
             'colocadas recorrentemente pelas autarquias locais e pelo movimento associativo, vieram '
             'demonstrar a necessidade de atualizar diversas normas para a melhor operacionalização das '
             'ações previstas neste âmbito.'],
            'Preâmbulo do projeto de revisão da Portaria n.º 146/2017, dezembro de 2021')
    para(doc,
         'O que propunha para o artigo 9.º resolvia quase todas as questões inventariadas neste documento.')
    tabela(doc,
           ['Matéria', 'Projeto de 2021', 'Texto em vigor'],
           [
            ['Natureza',
             '«as câmaras municipais […] **devem executar** programas de captura, esterilização e devolução '
             'à origem (CED) em colónias de gatos»',
             '«**podem** as câmaras municipais […] **autorizar** a manutenção […] de colónias de gatos»'],
            ['Promotores',
             '«**devem realizar-se** por iniciativa das câmaras municipais ou mediante proposta de '
             'associações zoófilas legalmente constituídas e de organizações não governamentais de '
             'ambiente que visem a proteção animal»',
             '«podem realizar-se por iniciativa das câmaras municipais ou mediante proposta de organização '
             'de proteção animal»'],
            ['Entidade responsável',
             '«A entidade responsável pelo programa CED **é a câmara municipal, através do respetivo Centro '
             'de Recolha Oficial**»',
             'Não identificada — «A entidade responsável pelo CED deve assegurar»'],
            ['Plano de gestão',
             'Passaria a incluir a identificação **dos cuidadores** e o registo dos animais capturados, '
             'libertados, realojados, adotados, eutanasiados, tratados ou encontrados mortos, com causa de '
             'morte',
             'Só identifica o médico veterinário assistente e os responsáveis pela execução'],
            ['Verificação de aptidão',
             'Al. d) **revogada**',
             'Al. d) — entrega no CRO para verificação da aptidão'],
            ['Registo SIAC',
             '«registados **em nome da câmara municipal** responsável pelo programa CED»',
             '«registados e identificados eletronicamente» — sem indicar o titular'],
            ['Habitats de vida selvagem',
             'Programas nesses locais «devem ser **articulados com o ICNF I.P.**»',
             '«Deve ser evitada a implementação»'],
            ['Cães',
             'Admitia esterilização «excecional e transitoriamente, por falta de capacidade de alojamento '
             'no CRO» de cães errantes; n.º 10 revogado',
             'N.º 10 — «não é aplicável a cães»'],
           ],
           [Cm(2.9), Cm(6.9), Cm(6.8)])
    destaque(doc, [
        '**O projeto nunca foi publicado.** Cinco anos depois, o texto em vigor é o de 2017. A leitura da '
        'tabela acima permite uma conclusão incómoda: as lacunas apontadas neste documento não são '
        'descobertas recentes nem construções da doutrina. **Foram identificadas pela própria Administração '
        'e a correção ficou por fazer.**'])

    # ================================================================= 5
    pagebreak(doc)
    h1(doc, '5.', 'Lacunas reconhecidas pela Administração')

    h2(doc, '5.1', 'O estatuto de cuidador de colónia não está definido')
    para(doc,
         'A Portaria impõe deveres a uma figura que não define. O n.º 5 do artigo 9.º manda assegurar «os '
         'cuidados de saúde e alimentação adequados aos animais» — obrigação que, na prática, recai sobre o '
         'cuidador. A Estratégia Nacional assinala o problema sem rodeios.')
    citacao(doc,
            ['A Portaria n.º 146/2017, de 26 de abril, refere expressamente que os cuidadores têm de '
             'prestar "os cuidados de saúde e alimentação adequados aos animais". Acontece que não está '
             'definido o conceito de "cuidador da colónia" nem existem recomendações sobre as boas práticas '
             'nas atividades desempenhadas por este.'],
            'Estratégia Nacional para os Animais Errantes, p. 35')
    para(doc,
         'Não se define quem é, como se designa, que direitos tem, perante quem responde, nem o que '
         'sucede quando cessa funções. Alguns municípios criaram, sem base habilitante que o preveja, '
         'cartões de identificação de cuidador.')
    citacao(doc,
            ['1 — É proibida a alimentação de animais vadios ou errantes em quaisquer espaços públicos ou '
             'em espaços privados confinantes com a via pública, exceto nas colónias de gatos '
             'intervencionadas pelos programas CED, por parte de cidadãos nomeados para o efeito '
             '(portadores de um cartão de identificação de cuidador), desde que nos locais se cumpram as '
             'medidas de higiene, nomeadamente para prevenir a chamada de animais oportunistas.'],
            'N.º 1 do artigo 8.º do Regulamento de Saúde e Bem-Estar Animal do Município de Setúbal')
    nota(doc, [
        '**Observação.** Impor deveres a uma categoria indefinida de pessoas, e fazer depender delas o '
        'cumprimento de uma obrigação legal do município, é construção frágil. O cartão de cuidador é uma '
        'solução administrativa sensata para um problema que a lei não resolveu — mas nada diz que direitos '
        'confere ao seu portador, nem o protege se a colónia for suspensa.'])

    h2(doc, '5.2', 'As famílias de acolhimento temporário não estão reguladas')
    citacao(doc,
            ['Importa criar mecanismos para uma participação mais ativa da comunidade que não passe '
             'somente pelo voluntariado nos abrigos ou ações das organizações não-governamentais (ONG). As '
             'famílias de acolhimento temporário de animais de companhia (FAT), os cuidadores informais de '
             'animais ou o apadrinhamento de animais dos abrigos constituem soluções, não só de promoção do '
             'bem-estar animal, mas também de envolvimento e sensibilização da população. Contudo, não se '
             'encontram regulados o conceito de "família de acolhimento temporário" de animais de '
             'companhia ou o estatuto de cuidador por forma a resultar clara a articulação entre estes e as '
             'entidades competentes. Estas figuras, apesar de não serem entidades formais, terão de ser '
             'consideradas na rede de resposta, atendendo ao seu papel na gestão de animais errantes, desde '
             'logo pelos seus conhecimentos do terreno e das realidades locais mas também pelo seu '
             'inquestionável contributo.'],
            'Estratégia Nacional para os Animais Errantes, pp. 30-31')
    para(doc,
         'A mesma Estratégia inscreve como prioridades de investimento a «Criação de uma rede de Famílias '
         'de Acolhimento Temporário» e a «Elaboração de um manual das normas e procedimentos para o '
         'alojamento temporário de animais (FAT)». Em 26 de agosto de 2024 o PAN apresentou iniciativa '
         'parlamentar para criar o estatuto, assente no reconhecimento formal do contributo das FAT, na '
         'criação de uma rede e em apoio material, financeiro e veterinário.')
    destaque(doc, [
        'Esta é a lacuna com consequências mais imediatas para o cidadão. Manuais municipais recomendam '
        'expressamente o recurso a famílias de acolhimento temporário — «que podem ser pessoas físicas ou '
        'colectivas» — para os animais que devem ser encaminhados para adoção. **Recomenda-se uma figura '
        'que a lei não reconhece, não define e não protege.** Quem a pratica arrisca ser tratado, pela '
        'aplicação do conceito legal de detentor, como responsável definitivo pelos animais que acolheu.'])

    h2(doc, '5.3', 'Não se sabe quantas colónias existem nem onde')
    citacao(doc,
            ['Até à data, os programas CED para gatos encontram-se previstos na Lei n.º 27/2016, de 23 de '
             'agosto, regulamentada pela Portaria n.º 146/2017, de 26 de abril. Apesar de ser obrigatória a '
             'identificação eletrónica dos gatos inseridos em programas CED, não é possível aferir o número '
             'de animais nem o número e localização das colónias intervencionadas ao abrigo destes '
             'programas. Importará também associar cada colónia ao seu cuidador para garantir a alimentação '
             'e abeberamento destes animais de acordo com as boas práticas, bem como realizar a '
             'georreferenciação das mesmas para garantir a proteção destes animais em cenários de acidente '
             'grave ou catástrofe.'],
            'Estratégia Nacional para os Animais Errantes, p. 35')
    nota(doc, [
        '**Observação.** Sem cadastro não há avaliação de eficácia possível. A meta que a própria '
        'Estratégia fixa — que em 2030 a população de animais errantes «se resuma aos gatos integrados em '
        'programas de Capturar-Esterilizar-Devolver» — não é verificável com os instrumentos existentes. '
        'E a obrigação de registo da al. e) do n.º 4 do artigo 9.º, cumprida individualmente, não gera '
        'informação agregada sobre colónias porque o SIAC não tem campo para tal.'])

    h2(doc, '5.4', 'Não existe guia nacional de boas práticas, e o programa não cobre o território')
    citacao(doc,
            ['A elaboração de um guia de boas práticas para estes programas, que inclua um plano sanitário '
             'e um registo individual e da colónia adequado ao contexto específico, permitirá uniformizar '
             'procedimentos e garantir a salvaguarda da sanidade e do bem-estar dos animais que os '
             'integram. Os programas CED não estão instituídos em todo o território, o que limita a sua '
             'eficácia.'],
            'Estratégia Nacional para os Animais Errantes, p. 35')
    para(doc,
         'Na ausência de guia nacional, cada município constrói o seu instrumento. O Município de Setúbal '
         'aprovou em 2020 um Manual de Gestão de Colónias Felinas; o Município do Porto executa o programa '
         'desde 2019 com prática própria; o Município de Salvaterra de Magos aprovou um regulamento '
         'autónomo do programa CED. As soluções divergem em pontos essenciais, designadamente no critério '
         'de aptidão e no titular do registo.')

    h2(doc, '5.5', 'Regulamentos municipais que proíbem alimentar errantes')
    citacao(doc,
            ['Alguns membros da sociedade alimentam cães e gatos de rua e tal deve ser considerado no '
             'planeamento das ações. Um requisito essencial para programas CED é a garantia de fontes de '
             'alimento. Existem regulamentos ou posturas camarárias que proíbem alimentar animais '
             'errantes. Contudo, para os gatos de rua, assilvestrados ou errantes está prevista a '
             'implementação de programas CED pelos municípios, nos termos do art.º 4.º da Lei n.º 27/2016, '
             'de 23 de agosto […]'],
            'Estratégia Nacional para os Animais Errantes, p. 35')
    nota(doc, [
        '**Observação.** A Estratégia está a sinalizar, com contenção diplomática, que há regulamentos '
        'municipais cuja legalidade é duvidosa à luz do artigo 4.º da Lei. O ponto não é académico: casos '
        'de cidadãos processados por alimentar gatos de rua têm chegado à imprensa nacional, e a '
        'articulação entre a proibição regulamentar e o dever legal de assegurar o CED nunca foi resolvida '
        'por norma nem por decisão conhecida.'])

    # ================================================================= 6
    pagebreak(doc)
    h1(doc, '6.', 'Zonas cinzentas de regime')

    h2(doc, '6.1', 'Faculdade ou dever?')
    para(doc,
         'O artigo 4.º da Lei diz que o Estado «assegura» a concretização de programas CED. O artigo 9.º da '
         'Portaria diz que as câmaras «podem […] autorizar». O projeto de 2021 dizia «devem executar». A '
         'contradição entre a lei habilitante e o regulamento nunca foi resolvida.')
    nota(doc, [
        '**Observação.** É a fratura central de todo o regime. Enquanto for faculdade municipal, não há '
        'direito do cidadão nem dever exigível, e a autoridade nacional pode declarar ilegal um critério de '
        'exclusão sem poder impor a execução do programa. É também a origem do ponto 5.4: um programa '
        'facultativo não cobre o território.'])

    h2(doc, '6.2', 'Quem é a «entidade responsável pelo CED»?')
    para(doc,
         'O n.º 4 do artigo 9.º impõe cinco deveres à «entidade responsável pelo CED» sem a identificar. O '
         'n.º 2 admite dois promotores possíveis. O n.º 8 atribui as despesas à «entidade promotora» — '
         'termo distinto, não definido, e que pode ou não coincidir com a anterior.')
    para(doc,
         'O Município de Setúbal antecipou a solução do projeto de 2021, assumindo-se como entidade '
         'responsável e suprimindo a alternativa da proposta por organização de proteção animal.')
    citacao(doc,
            ['5 — O programa CED realiza-se por iniciativa do Município.',
             '7 — O Município assegura: […] d) Que os animais capturados, antes de integrarem a colónia, '
             'são recolhidos no CROAC para verificação da sua aptidão;'],
            'N.ºs 5 e 7 do artigo 59.º do Regulamento de Saúde e Bem-Estar Animal do Município de Setúbal')
    para(doc,
         'Na prática instalou-se um terceiro modelo, que nenhuma norma prevê, descrito no manual municipal '
         'de Setúbal.')
    citacao(doc,
            ['Pode também ocorrer a gestão partilhada das colónias em que algumas tarefas estão a cargo das '
             'associações (como a captura, devolução e manutenção da colónia) e outras da Câmara (como a '
             'esterilização, vacinação, identificação e controlo de saúde dos gatos).'],
            'Manual de Gestão de Colónias Felinas do Município de Setúbal, 2020')

    h2(doc, '6.3', 'Em nome de quem se registam os animais no SIAC?')
    para(doc,
         'A al. e) do n.º 4 do artigo 9.º exige que os animais capturados sejam «registados e identificados '
         'eletronicamente». Não diz em nome de quem. O projeto de 2021 di-lo-ia: «em nome da câmara '
         'municipal responsável pelo programa CED».')
    para(doc,
         'A prática consolidou-se nesse sentido. O Município do Porto declarou, em verificação jornalística '
         'sobre a titularidade dos gatos de colónia, que os microchips são «registados em nome da CMP com a '
         'observação da identificação da colónia e da associação zoófila responsável pela sua gestão», '
         'acrescentando-se que «as colónias legalmente reconhecidas são geridas pelas associações de '
         'proteção animal que as acompanham e que garantem a alimentação e cuidados dos animais».')
    nota(doc, [
        '**Observação.** Há aqui uma incongruência conceptual que merece ser enfrentada. O SIAC regista '
        '**titulares**, e a al. f) do artigo 3.º do Decreto-Lei n.º 82/2019 define titular como «o '
        'proprietário ou o possuidor […] cuja posse faça presumir a propriedade». Registar um gato feral em '
        'nome da câmara significa fazer a autarquia presumida proprietária de um animal que vive na rua e '
        'que não controla. É uma ficção operacional útil — resolve a rastreabilidade e a isenção de taxa do '
        'n.º 2 do artigo 17.º — mas sem apoio na definição legal, e com consequências não estudadas no '
        'plano da responsabilidade civil.'])

    h2(doc, '6.4', 'Responsabilidade civil por danos causados pelos animais da colónia')
    para(doc,
         'A Portaria é omissa. Aplica-se o regime geral, cuja jurisprudência fixa que o dever de vigilância '
         'decorre do controlo de facto sobre o animal — podendo recair sobre o comodatário, o depositário '
         'ou o cuidador, e não necessariamente sobre o proprietário. Há presunção de culpa.')
    para(doc,
         'A questão foi invocada no debate político como razão de prudência.')
    citacao(doc,
            ['Temos vindo a acompanhar questões práticas e de responsabilidade civil que recomendam '
             'prudência no alargamento dos programas CED a cães.'],
            'Resposta da CDU ao questionário da Maratona pelos Animais, março de 2024')
    nota(doc, [
        '**Observação.** Se o registo no SIAC é em nome da câmara e a guarda de facto pertence ao cuidador, '
        'quem responde pelos danos? Não se conhece decisão sobre o ponto. O risco recai previsivelmente '
        'sobre a pessoa singular que alimenta e vigia a colónia — precisamente aquela cujo estatuto a lei '
        'não define e que não dispõe de seguro nem de cobertura institucional.'])

    h2(doc, '6.5', 'O critério feral ou sociável: quem decide, com que método')
    para(doc,
         'A única norma é a al. d) do n.º 4 do artigo 9.º: entrega no CRO «para verificação da sua '
         'aptidão». Sem critério, sem escala de avaliação, sem prazo, sem fundamentação exigível e sem '
         'impugnação. A doutrina administrativa preenche o vazio, e fá-lo de forma exigente.')
    citacao(doc,
            ['Avaliar se um gato é ou não silvestre é muito importante para perceber qual a melhor solução '
             'para garantir o seu bem-estar. Se for silvestre, permitir-lhe viver no seu próprio território '
             'com os seus companheiros de colónia será a melhor solução. […] Sempre que possível, os '
             'animais adultos dóceis e as crias que ainda estejam em idade de socialização são retirados '
             'das colónias e encaminhados para adoção.'],
            'Estratégia Nacional para os Animais Errantes, p. 34')
    citacao(doc,
            ['Em todos os modelos, desde logo, há que assumir que uma colónia felina não é um repositório '
             'de qualquer tipo de gato errante, nem serve para colmatar a inexistência de gatil municipal '
             'ou de abrigo privado, mas antes é o habitat de - e exclusivamente - gatos ferais.'],
            'Manual de Gestão de Colónias Felinas do Município de Setúbal, 2020')
    destaque(doc, [
        'Trata-se de uma decisão que determina se um animal vive numa casa ou na rua, tomada sem '
        'procedimento regulado e sem fundamentação exigível. **É, materialmente, o ato mais gravoso de '
        'todo o programa — e é o menos regulado.**'])

    h2(doc, '6.6', 'Crias: quatro prazos que não se articulam')
    tabela(doc,
           ['Marco', 'Fonte', 'Consequência'],
           [
            ['Idade de socialização', 'Estratégia Nacional, p. 34 — sem definição normativa',
             'As crias «são retiradas das colónias e encaminhadas para adoção»'],
            ['120 dias', 'N.º 1 do art.º 5.º do DL n.º 82/2019',
             'Prazo para identificação e registo no SIAC'],
            ['Menos de 6 meses', 'N.º 6 do art.º 8.º da Portaria n.º 146/2017',
             'Podem ser encaminhados para adoção antes de esterilizados'],
            ['8 meses', 'N.º 6 do art.º 8.º da Portaria n.º 146/2017',
             'Prazo-limite para a esterilização, a assegurar pelo novo detentor'],
           ],
           [Cm(3.2), Cm(6.4), Cm(6.9)])
    nota(doc, [
        '**Observação.** Os prazos não conversam entre si. Um animal de cinco meses está fora do prazo de '
        'registo, dentro da janela de adoção sem esterilização e a três meses do prazo de esterilização. '
        'Nenhuma norma diz quem assegura o quê em cada janela, nem o que sucede quando o animal permanece '
        'sob guarda de terceiro que não é o seu titular registado.'])

    h2(doc, '6.7', 'Colónias em propriedade privada')
    para(doc,
         'O n.º 3 do artigo 9.º só afasta «parques públicos, refúgios de vida selvagem ou outros locais '
         'públicos que sirvam de habitat à vida selvagem». Sobre terrenos privados a Portaria é '
         'inteiramente omissa — não permite nem proíbe. Os manuais municipais admitem-nos.')
    citacao(doc,
            ['Para colmatar a inexistência de espaço físico da entidade promotora, pública ou privada, ou a '
             'sobrelotação desse espaço, e assim acolherem-se os gatos que devem ser encaminhados para '
             'adopção, há que recorrer a soluções alternativas nomeadamente a Famílias de Acolhimento '
             'Temporário (FAT), que podem ser pessoas físicas ou colectivas, a santuários ou refúgios, '
             'instalados em espaços privados ou camarários.'],
            'Manual de Gestão de Colónias Felinas do Município de Setúbal, 2020')
    nota(doc, [
        '**Observação.** Falta regular a colónia em terreno privado com consentimento do proprietário, e '
        'faltam os direitos do vizinho que a não quer. É o terreno onde nascem os conflitos que chegam '
        'regularmente à imprensa e, por vezes, aos tribunais.'])

    h2(doc, '6.8', 'Devolução a local que não garante segurança')
    para(doc,
         'O n.º 1 do artigo 9.º manda devolver «ao local de origem», sem qualquer juízo sobre a idoneidade '
         'desse local. O manual municipal de Setúbal descreve as consequências.')
    citacao(doc,
            ['E surgem denúncias […] de dizimação de colónias cujos gatos esterilizados terminam mortos por '
             'atropelamento ou por envenenamento, porque devolvidos a um local que não garantia a sua '
             'integridade física ou vida.'],
            'Manual de Gestão de Colónias Felinas do Município de Setúbal, 2020')

    h2(doc, '6.9', 'Suspensão e recolha sem garantias procedimentais')
    para(doc,
         'O n.º 9 do artigo 9.º permite à câmara «determinar medidas corretivas ou a suspensão do programa '
         'CED em curso e proceder à recolha dos animais para o CRO» sempre que verifique incumprimento de '
         'qualquer dos requisitos do n.º 4. Não se prevê audiência prévia, prazo de sanação, nem destino '
         'assegurado aos animais recolhidos, que entram no regime dos quinze dias e da esterilização '
         'obrigatória.')

    # ================================================================= 7
    pagebreak(doc)
    h1(doc, '7.', 'Conflitos entre políticas públicas')

    h2(doc, '7.1', 'CED e conservação da natureza')
    para(doc,
         'A Estratégia Nacional assume simultaneamente o problema e a ignorância sobre a sua dimensão.')
    citacao(doc,
            ['Desconhece-se qual o real impacto dos cães e gatos na biodiversidade. Contudo, atendendo a '
             'que são conhecidas as tipologias desse impacto nomeadamente a predação e a hibridização, '
             'deverão ser elaboradas […]'],
            'Estratégia Nacional para os Animais Errantes, capítulo sobre redução do impacto na '
            'biodiversidade')
    para(doc,
         'Do lado da conservação, a Sociedade Portuguesa para o Estudo das Aves documenta a predação por '
         'gatos como ameaça às aves marinhas e instalou emissores ultrassónicos em colónias de cagarra na '
         'ilha do Corvo para afastar gatos, identificando a predação como uma das principais causas de '
         'mortalidade das crias.')
    nota(doc, [
        '**Observação.** O único ponto de contacto normativo entre as duas políticas é o n.º 3 do artigo '
        '9.º, que se limita a dizer que o CED «deve ser evitado» em habitats de vida selvagem. O projeto de '
        '2021 era mais exigente — mandava articular com o ICNF — e não foi publicado. Nas ilhas, onde o '
        'conflito é agudo, não existe regra específica.'])

    h2(doc, '7.2', 'Dispersão e reversão da tutela')
    tabela(doc,
           ['Data', 'Ato', 'Efeito'],
           [
            ['2020-2021', 'DL n.º 27-A/2020 e DL n.º 54/2021; RCM n.º 78/2021',
             'Bem-estar dos animais de companhia, incluindo errantes, transita para o ICNF, sob o '
             'Ministério do Ambiente'],
            ['25.6.2021', 'Decreto Regulamentar n.º 3/2021', 'Cria o Provedor do Animal'],
            ['2023', 'Estratégia Nacional para os Animais Errantes',
             'Elaborada pelo ICNF; consulta pública de 19.7 a 30.8.2023'],
            ['7.4.2025', 'Decreto-Lei n.º 63/2025',
             'Competências regressam à DGAV, com efeitos a **1 de julho de 2025**'],
           ],
           [Cm(2.2), Cm(5.6), Cm(8.7)])
    para(doc,
         'A Associação Portuguesa de Médicos Veterinários Especialistas em Animais de Companhia pronunciou-se '
         'com dureza sobre a dispersão.')
    citacao(doc,
            ['Como já manifestámos em comunicados públicos anteriores, a APMVEAC discordou da retirada de '
             'competências no que concerne à proteção e bem-estar animal da Direção Geral de Alimentação e '
             'Veterinária (DGAV). De resto, manifestamos o nosso total desacordo de qualquer proposta que '
             'disperse a tutela das questões relacionadas com os animais domésticos. Essa dispersão só '
             'fragiliza a proteção dos animais já que a saúde física e o bem-estar e, por consequência a '
             'sua proteção, são indissociáveis. Somos da opinião de que a separação da sua tutela levará '
             'inevitavelmente a graves danos para os animais.'],
            'Parecer da APMVEAC sobre a proposta de Estratégia Nacional para os Animais Errantes, '
            'setembro de 2023')
    nota(doc, [
        '**Observação.** Cinco anos de instabilidade orgânica explicam, em boa medida, por que a revisão da '
        'Portaria ficou por publicar e por que a Estratégia não teve seguimento normativo. A competência '
        'mudou de ministério duas vezes no período em que a revisão estava pronta.'])

    h2(doc, '7.3', 'A legislação como parte do problema')
    citacao(doc,
            ['O presente enquadramento legal é parte integrante do problema dos animais errantes, com '
             'diplomas dispersos, falta de fiscalização e medidas de difícil implementação. Nenhuma '
             'estratégia que vise abordar a problemática dos animais errantes pode ser eficaz sem uma '
             'revisão profunda do quadro normativo da proteção animal em Portugal.'],
            'Parecer da APMVEAC, setembro de 2023')
    para(doc,
         'A APMVEAC acrescentou que as organizações profissionais da medicina veterinária não foram '
         'consultadas na elaboração da proposta, considerando «incompreensível que a tutela não as tenha '
         'consultado diretamente em tão importante proposta», e solicitou ser ouvida em conjunto com a '
         'Ordem dos Médicos Veterinários, o Sindicato Nacional dos Médicos Veterinários, a ANVETEM e a '
         'SPCV.')
    para(doc,
         'O diagnóstico oficial anterior tinha ido no mesmo sentido. O Grupo de Trabalho para o Bem-Estar '
         'Animal, ao avaliar a implementação da Lei n.º 27/2016, registou que a lei «além de supressão de '
         'algumas das lacunas geradas pela Lei n.º 69/2014, de 29 de agosto, adicionou outras», e apurou, '
         'por inquérito às entidades, que a principal dificuldade associada à captura de animais errantes é '
         'a dificuldade de alojamento e que o principal constrangimento na gestão e construção de '
         'alojamentos é o financiamento. Entre as recomendações constam «Reforçar a implementação do '
         'programa CED», «Alargar a implementação de programas CED», «Rever as normas associadas ao '
         'programa CED» e «Clarificar e uniformizar conceitos».')

    # ================================================================= 8
    pagebreak(doc)
    h1(doc, '8.', 'A controvérsia ativa: a extensão do CED a cães')
    para(doc,
         'É hoje o eixo de fratura mais visível, e opõe o movimento de proteção animal e parte do espetro '
         'político às organizações profissionais da medicina veterinária.')

    h3(doc, 'Posições favoráveis')
    bullets(doc, [
        '**Estratégia Nacional para os Animais Errantes**: «Atualmente, nos termos da lei, os programas CED '
        'não se aplicam a cães. Tal facto restringe a possibilidade de travar a reprodução das matilhas de '
        'cães, enquanto permanecem nas ruas por incapacidade de alojamento nos CRO. Importa avaliar a '
        'possibilidade da aplicação do programa CED aos cães de matilha, para os quais o tempo de '
        'permanência no local de origem seria apenas o suficiente até ser encontrada uma outra solução.»',
        '**Projeto de revisão de 2021**: admitia que as câmaras promovessem, «excecional e '
        'transitoriamente, por falta de capacidade de alojamento no CRO, a esterilização de cães errantes '
        'quando não seja possível proceder à sua recolha imediata, a fim de evitar a sua reprodução e '
        'agravar a proliferação de animais errantes e formação de matilhas».',
        '**PAN**: obteve na al. a) do n.º 1 do artigo 200.º da Lei n.º 82/2023, de 29 de dezembro '
        '(Orçamento do Estado para 2024), verba de 4 900 000 € para centros de recolha oficial, abrigos '
        'CED e, pela primeira vez, parques de matilhas. Aprovou na generalidade o Projeto de Lei n.º '
        '662/XV/1.ª, caducado com a dissolução, que reconhecia a figura do animal comunitário. Mantém no '
        'programa «o alargamento da aplicação do método CED a cães e a criação de parques de matilhas».',
        '**Bloco de Esquerda**: «Entendemos que a esterilização e devolução de cães errantes pode ser '
        'considerada como uma medida eficaz, numa estratégia a definir em colaboração com as autoridades '
        'veterinárias competentes e o movimento social de proteção animal.»',
        '**Chega**: «o CHEGA concorda com o sistema CED para cães desde que estes se encontrem num local '
        'circunscrito e tenham cuidadores designados».',
    ])

    h3(doc, 'Posições contrárias')
    para(doc,
         'A Ordem dos Médicos Veterinários pronunciou-se em 25 de novembro de 2025, reafirmando «total '
         'apoio ao programa CED aplicado a gatos, cuja eficácia depende das particularidades próprias da '
         'espécie felina», e qualificando a transposição do modelo para cães como «tecnicamente infundada» '
         'e «socialmente perigosa». Os argumentos invocados foram a segurança pública, o bem-estar animal '
         '— devolver cães à rua seria «condená-los a sofrimento contínuo» —, a abdicação de '
         'responsabilidade pelas autoridades locais, o risco sanitário e a deseducação social.')
    para(doc, 'A APMVEAC foi no mesmo sentido, e mais longe quanto às causas.')
    citacao(doc,
            ['Também consideramos que estender a estratégia de CED aos cães não é de todo a medida mais '
             'responsável e eficaz para lidar com as populações caninas errantes, mesmo como medida '
             'provisória. Da mesma forma, a construção de parques de realojamento de cães com '
             'comportamento assilvestrado comporta questões de alocação de recursos e de bem-estar animal '
             'que necessitam ser investigadas antes de se avançar para a sua disseminação. As matilhas de '
             'cães são, em grande medida, um produto da legislação deficiente, em particular da já referida '
             '"Lei do fim do abate".'],
            'Parecer da APMVEAC, setembro de 2023')
    para(doc,
         'A CDU manifestou prudência, invocando «questões práticas e de responsabilidade civil». A AD '
         'declarou-se disponível para refletir sobre o controlo de matilhas mas considerou que «a '
         'prioridade deve ser uma campanha massiva de esterilização para combater o problema na sua raiz». '
         'O PS e a Iniciativa Liberal não responderam ao questionário.')

    h3(doc, 'O ponto adjacente: eutanásia e autonomia clínica')
    citacao(doc,
            ['A eutanásia deve ser encarada como um ato clínico, responsabilidade exclusiva do médico '
             'veterinário a quem compete determinar as circunstâncias concretas em que é realizada.'],
            'Parecer da APMVEAC, setembro de 2023')
    nota(doc, [
        '**Observação.** Esta posição colide frontalmente com o regime em vigor. O n.º 5 do artigo 3.º da '
        'Lei n.º 27/2016 e o artigo 11.º da Portaria n.º 146/2017 fixam um elenco taxativo de situações em '
        'que o abate ou occisão pode ser praticado. O vice-presidente do Conselho Profissional e '
        'Deontológico da Ordem dos Médicos Veterinários sintetizou a tensão observando que os veterinários '
        'municipais não podem decidir segundo critério próprio como os veterinários privados, sentindo-se '
        'por isso «muito pressionados».'])

    # ================================================================= 9
    pagebreak(doc)
    h1(doc, '9.', 'Capacidade institucional')

    h2(doc, '9.1', 'Médicos veterinários municipais')
    para(doc,
         'O regime do CED depende, em dois momentos essenciais, de uma figura que nem todos os municípios '
         'possuem: o parecer prévio do n.º 1 do artigo 9.º e a supervisão da colónia do n.º 5. A mesma '
         'figura é pressuposto do parecer vinculativo do n.º 2 do artigo 3.º do Decreto-Lei n.º 314/2003.')
    para(doc,
         'A Câmara Municipal de Setúbal declarou publicamente não existir no município o cargo de médico '
         'veterinário municipal, dispondo de dois técnicos superiores com licenciatura em medicina '
         'veterinária. A ANVETEM — Associação dos Veterinários dos Municípios — tem por objeto, entre '
         'outros, «defender a sua integração nos municípios e o exercício das suas competências».')
    nota(doc, [
        '**Observação.** Se a figura não existe no município, o parecer que a lei exige não pode ser '
        'emitido nos termos em que é exigido. Não é irregularidade menor: é pressuposto de legalidade do '
        'ato de autorização da colónia. O ponto merece levantamento nacional.'])

    h2(doc, '9.2', 'As dificuldades reportadas pelos municípios')
    para(doc,
         'O Grupo de Trabalho para o Bem-Estar Animal inquiriu as entidades envolvidas e sistematizou as '
         'categorias de dificuldade reportadas: na captura, a falta de alojamento; na gestão e construção '
         'de alojamentos, o financiamento; e, transversalmente, «dificuldades de pessoal sem [formação]», '
         '«requisitos» e «quadro legal».')
    citacao(doc,
            ['Percebe-se assim que o investimento no alargamento e a modernização da rede de alojamento de '
             'animais errantes não pode deixar de ser considerado como objetivo estratégico na definição da '
             'estratégia para os animais errantes.'],
            'Relatório Final do Grupo de Trabalho para o Bem-Estar Animal, DGAV, 2021')

    # ================================================================= 10
    h1(doc, '10.', 'Uma figura proposta que resolveria muito')
    para(doc,
         'O direito vigente só conhece dois estados para um gato: errante, nos termos da al. c) do n.º 1 do '
         'artigo 2.º do Decreto-Lei n.º 276/2001, ou com detentor. Não há terceira categoria. Toda a '
         'situação real tem de ser forçada para dentro de uma das duas.')
    para(doc,
         'O PAN aprovou na generalidade o Projeto de Lei n.º 662/XV/1.ª, que «assegurava o reconhecimento '
         'legal da figura do animal comunitário» e que caducou com a dissolução do Parlamento. Mantém o '
         'compromisso de «rever a lei e os regulamentos vigentes para que seja instituída a figura do '
         'animal comunitário, garantida a esterilização, e a alimentação e o abeberamento dos animais '
         'comunitários ou errantes que se encontrem na via pública, incluindo as colónias de gatos ou '
         'matilhas de cães».')
    destaque(doc, [
        'É a figura em falta. Um animal que **não é errante**, porque tem cuidador identificado, plano de '
        'gestão e registo, e que **não tem detentor-proprietário**, porque ninguém o detém. Sem ela, '
        'qualquer situação intermédia — designadamente o acolhimento temporário de crias de colónia — é '
        'resolvida por reconduzir o cidadão à categoria de detentor, com todas as consequências que daí '
        'decorrem.'])

    # ================================================================= 11
    pagebreak(doc)
    h1(doc, '11.', 'Síntese: o que uma revisão tem de resolver')
    numlist(doc, [
        'Definir se o CED é **faculdade ou dever** do município, conformando o artigo 9.º da Portaria com '
        'o artigo 4.º da Lei.',
        'Identificar expressamente a **entidade responsável** e distingui-la, ou não, da entidade '
        'promotora que suporta as despesas.',
        'Criar o **estatuto do cuidador de colónia**: designação, requisitos, direitos, deveres, cessação '
        'e regime de responsabilidade.',
        'Criar o **estatuto da família de acolhimento temporário**, esclarecendo que o acolhimento não '
        'converte o acolhedor em titular.',
        'Fixar **em nome de quem** se registam os animais de colónia no SIAC e criar campo próprio para a '
        'colónia, permitindo o cadastro e a georreferenciação.',
        'Regular o **procedimento de verificação de aptidão**: critério, quem decide, fundamentação e '
        'impugnação.',
        'Articular os **prazos aplicáveis às crias** — socialização, registo, adoção e esterilização.',
        'Regular a **colónia em propriedade privada** e os direitos de terceiros afetados.',
        'Introduzir **garantias procedimentais** na suspensão do programa e na recolha dos animais.',
        'Resolver a articulação com a **conservação da natureza**, designadamente em território insular.',
        'Decidir, com fundamento técnico, a questão da **extensão a cães**.',
        'Aprovar o **guia nacional de boas práticas** que a Estratégia prevê.',
    ])

    # ================================================================= 12
    h1(doc, '12.', 'Limites desta análise')
    bullets(doc, [
        'Não foi localizada **jurisprudência** sobre nenhuma das questões inventariadas. A pesquisa na base '
        'de dados dos tribunais superiores não devolveu decisões sobre elegibilidade para CED, estatuto do '
        'cuidador ou responsabilidade por danos causados por animais de colónia.',
        'Não foi localizada **posição pública da ANVETEM** sobre a maioria destas questões, nem parecer da '
        'Ordem dos Médicos Veterinários sobre o CED aplicado a gatos para além do apoio genérico expresso '
        'em novembro de 2025.',
        'A **Estratégia Nacional para os Animais Errantes** é citada na versão submetida a consulta '
        'pública. Não foi localizado ato que a aprove; as citações valem como diagnóstico da Administração, '
        'não como direito vigente.',
        'O **projeto de revisão da Portaria** é citado na versão circulada à ANMP em dezembro de 2021. Não '
        'foi publicado e não se conhece a razão pela qual o processo não prosseguiu.',
        'Não foram consultados os **contributos individuais** submetidos na consulta pública da Estratégia, '
        'que poderão conter posições relevantes de associações e de municípios.',
        'A dimensão **científica** do debate sobre a eficácia do CED — taxas mínimas de esterilização, '
        'condição de população fechada, modelos de projeção — não foi objeto de revisão sistemática neste '
        'documento.',
    ])

    # ================================================================= Anexo
    pagebreak(doc)
    h1(doc, 'Anexo A', 'Elenco de fontes')
    tabela(doc,
           ['Fonte', 'Natureza', 'Data'],
           [
            ['Lei n.º 27/2016, de 23 de agosto', 'Lei da Assembleia da República', '2016'],
            ['Portaria n.º 146/2017, de 26 de abril', 'Regulamento — redação originária, sem alterações',
             '2017'],
            ['Decreto-Lei n.º 276/2001, de 17 de outubro', 'Regime dos alojamentos e proteção',
             'Consolidado'],
            ['Decreto-Lei n.º 314/2003, de 17 de dezembro', 'PNLVERAZ', 'Consolidado'],
            ['Decreto-Lei n.º 82/2019, de 27 de junho', 'SIAC — identificação e registo', 'Consolidado'],
            ['Decreto Regulamentar n.º 3/2021, de 25 de junho', 'Cria o Provedor do Animal', '2021'],
            ['RCM n.º 78/2021, de 25 de junho', 'Programa Nacional para os Animais de Companhia', '2021'],
            ['Decreto-Lei n.º 63/2025, de 7 de abril',
             'Competências regressam à DGAV, com efeitos a 1.7.2025', '2025'],
            ['Estratégia Nacional para os Animais Errantes', 'Proposta do ICNF em consulta pública',
             '2023'],
            ['Projeto de revisão da Portaria n.º 146/2017', 'Projeto circulado à ANMP, não publicado',
             'dez. 2021'],
            ['Relatório Final do Grupo de Trabalho para o Bem-Estar Animal',
             'Avaliação da implementação da Lei n.º 27/2016, DGAV', '2021'],
            ['Parecer da APMVEAC sobre a ENAE', 'Parecer de associação profissional', 'set. 2023'],
            ['Posição da Ordem dos Médicos Veterinários sobre o CED em cães', 'Comunicado',
             '25.11.2025'],
            ['Respostas dos partidos — Maratona pelos Animais', 'Questionário eleitoral', 'mar. 2024'],
            ['Regulamento de Saúde e Bem-Estar Animal do Município de Setúbal', 'Regulamento municipal',
             '2020'],
            ['Manual de Gestão de Colónias Felinas do Município de Setúbal', 'Manual municipal', '2020'],
            ['Relatório anual dos centros de recolha oficial', 'Relatório da DGAV, dados de 2025',
             '31.3.2026'],
           ],
           [Cm(7.4), Cm(6.2), Cm(2.9)])

    h1(doc, 'Anexo B', 'Quadro de normas citadas')
    tabela(doc,
           ['Norma', 'Diploma', 'Matéria'],
           [
            ['art.º 3.º, n.os 9 e 10', 'Lei n.º 27/2016', 'Relatórios anuais dos CRO e relatório nacional'],
            ['art.º 4.º', 'Lei n.º 27/2016', 'Dever do Estado — captura, vacinação, esterilização e CED'],
            ['art.º 3.º, n.º 5', 'Lei n.º 27/2016', 'Condições do abate ou occisão'],
            ['art.º 7.º, n.os 1 e 2', 'Portaria n.º 146/2017', 'Competência de captura e dever de entrega'],
            ['art.º 8.º, n.º 6', 'Portaria n.º 146/2017', 'Adoção antes da esterilização; prazo dos 8 meses'],
            ['art.º 9.º, n.os 1 a 10', 'Portaria n.º 146/2017', 'Programas CED'],
            ['art.º 11.º', 'Portaria n.º 146/2017', 'Abate e eutanásia — elenco taxativo'],
            ['art.º 2.º, n.º 1, al. c)', 'DL n.º 276/2001', 'Definição de animal vadio ou errante'],
            ['art.º 6.º-A', 'DL n.º 276/2001', 'Abandono'],
            ['art.º 3.º, al. a) e f)', 'DL n.º 82/2019', 'Detentor e titular'],
            ['art.º 5.º, n.º 1', 'DL n.º 82/2019', 'Prazo de 120 dias para identificação e registo'],
            ['art.º 11.º, n.º 5', 'DL n.º 82/2019', 'Registo dos animais de CRO não reclamados'],
            ['art.º 17.º, n.º 2', 'DL n.º 82/2019', 'Isenção de taxa para CRO e associações zoófilas'],
            ['art.º 3.º, n.º 2', 'DL n.º 314/2003', 'Parecer vinculativo do médico veterinário municipal'],
            ['art.º 493.º', 'Código Civil', 'Danos causados por animais — dever de vigilância'],
            ['art.º 8.º, n.º 1', 'RSBEAMS de Setúbal', 'Proibição de alimentar errantes; cartão de cuidador'],
            ['art.º 59.º', 'RSBEAMS de Setúbal', 'Programa CED municipal'],
            ['art.º 57.º, n.º 5', 'RSBEAMS de Setúbal', 'CROAC não aceita ninhadas sem autonomia'],
           ],
           [Cm(4.3), Cm(4.6), Cm(7.6)])
