# -*- coding: utf-8 -*-
from _memo_engine import *
from docx.shared import Cm


def construir(doc):
    capa(doc,
         'Anexo ao memorando técnico',
         'Articulação entre o Decreto-Lei n.º 314/2003 e o Decreto-Lei n.º 276/2001',
         'Análise da questão dos limites de alojamento por prédio e do seu efeito sobre os '
         'estabelecimentos de criação',
         'Direção-Geral de Alimentação e Veterinária   ·   setembro de 2026')

    # ------------------------------------------------------------------ 1
    h1(doc, '1.', 'Questão e método')
    para(doc,
         'Pergunta-se se os limites de animais por fogo fixados no artigo 3.º do Decreto-Lei n.º 314/2003 '
         'condicionam a capacidade dos estabelecimentos de criação de cães e gatos e, por essa via, o acesso '
         'à atividade regulada pelo Decreto-Lei n.º 276/2001.')
    para(doc,
         'A pergunta tem sido respondida nos dois sentidos, em regra sem demonstração. Este anexo não parte '
         'de uma resposta. Expõe primeiro os elementos que sustentam a tese da sobreposição, depois os que '
         'sustentam a tese da delimitação, pondera-os e só então formula a conclusão que os elementos '
         'consentem — que não coincide inteiramente com nenhuma das duas formulações correntes.')
    enquadramento(doc, [
        'A ordem de exposição é deliberada. Os elementos desfavoráveis à conclusão final são apresentados em '
        'primeiro lugar e sem atenuação, porque uma delimitação que só resista quando se omite o que a '
        'contraria não serve para fundamentar uma posição institucional nem para sustentar uma opção '
        'legislativa.'])

    # ------------------------------------------------------------------ 2
    h1(doc, '2.', 'Elementos que sustentam a leitura da sobreposição')

    h3(doc, '2.1  O artigo 3.º emprega a palavra «alojamento»')
    para(doc,
         'O primeiro obstáculo à tese da separação está no próprio texto. O artigo 3.º não fala de «detenção» '
         'no seu corpo dispositivo: fala de alojamento, que é precisamente o conceito que define o objeto do '
         'Decreto-Lei n.º 276/2001.')
    citacao(doc,
            ['1 — O alojamento de cães e gatos em prédios urbanos, rústicos ou mistos, fica sempre '
             'condicionado à existência de boas condições do mesmo e ausência de riscos hígio-sanitários '
             'relativamente à conspurcação ambiental e doenças transmissíveis ao homem.',
             '2 — Nos prédios urbanos podem ser alojados até três cães ou quatro gatos adultos por cada fogo '
             '[…]'],
            'N.ºs 1 e 2 do artigo 3.º do Decreto-Lei n.º 314/2003')
    para(doc,
         'A definição do Decreto-Lei n.º 276/2001 é, por seu turno, suficientemente ampla para abranger uma '
         'habitação.')
    citacao(doc,
            ['n) «Alojamento» qualquer instalação, edifício, grupo de edifícios ou outro local, podendo '
             'incluir zona não completamente fechada, onde os animais de companhia se encontram mantidos;'],
            'Al. n) do n.º 1 do artigo 2.º do Decreto-Lei n.º 276/2001')
    para(doc,
         'Qualquer argumento que assente numa alegada divergência de vocabulário entre os dois diplomas tem '
         'de ser construído sobre esta base, e não contra ela.')

    h3(doc, '2.2  O «detentor» do diploma sanitário abrange expressamente quem cria com fins comerciais')
    para(doc,
         'Este é o elemento mais forte contra a tese da separação de planos, e não pode ser contornado. O '
         'Decreto-Lei n.º 314/2003 define detentor por referência expressa à reprodução e à criação, com ou '
         'sem fins comerciais.')
    citacao(doc,
            ["d) 'Detentor' qualquer pessoa, singular ou colectiva, responsável pelos animais de companhia "
             "para efeitos de reprodução, criação, manutenção, acomodação ou utilização, com ou sem fins "
             "comerciais;"],
            'Al. d) do artigo 2.º do Decreto-Lei n.º 314/2003')
    para(doc,
         'A definição do Decreto-Lei n.º 276/2001 é praticamente a mesma, com substituição de «comerciais» '
         'por «lucrativos».')
    citacao(doc,
            ['v) «Detentor» qualquer pessoa, singular ou coletiva, responsável pelos animais de companhia '
             'para efeitos de reprodução, criação, manutenção, acomodação ou utilização, com ou sem fins '
             'lucrativos;'],
            'Al. v) do n.º 1 do artigo 2.º do Decreto-Lei n.º 276/2001')
    destaque(doc, [
        'Daqui resulta uma conclusão que deve ser afirmada sem rodeios: **é incorreto sustentar que o '
        'Decreto-Lei n.º 314/2003 não se aplica a quem cria.** Aplica-se. Quem cria é detentor para efeitos '
        'do diploma sanitário, e o artigo 3.º dirige-se-lhe. A questão em aberto não é essa; é apenas a de '
        'saber se os números do artigo 3.º funcionam como teto de lotação do estabelecimento.'])

    h3(doc, '2.3  O n.º 4 do artigo 3.º tem estrutura de norma de capacidade')
    para(doc,
         'O artigo 3.º não se limita a impor condições higiossanitárias. No n.º 4 gradua o número admissível '
         'em função da área disponível, que é a lógica própria das normas de lotação.')
    citacao(doc,
            ['4 — Nos prédios rústicos ou mistos podem ser alojados até seis animais adultos, podendo tal '
             'número ser excedido se a dimensão do terreno o permitir e desde que as condições de alojamento '
             'obedeçam aos requisitos estabelecidos no n.º 1.'],
            'N.º 4 do artigo 3.º do Decreto-Lei n.º 314/2003')
    para(doc,
         'A jurisprudência administrativa leu a norma exatamente nesses termos, impondo à Administração o '
         'dever de aferir, caso a caso, se a dimensão do prédio permite exceder os seis animais.')
    citacao(doc,
            ['I — A posse de animais [cães ou gatos] em qualquer número em prédios urbanos, rústicos ou '
             'mistos, nos termos do n.º 1 do artigo 3.º do DL n.º 314/2003, de 17/12, depende da existência '
             'de uma situação de salubridade ambiental, com vista a evitar um perigo para a saúde pública.',
             'II — Porém, o n.º 4 do preceito em causa prevê que «nos prédios rústicos ou mistos podem ser '
             'alojados até seis animais adultos, podendo tal número ser excedido se a dimensão do terreno o '
             'permitir […]», o que significa que incumbe à Administração aferir sempre se o prédio onde se '
             'encontram alojados animais [cães e gatos] permite ou não o enquadramento na situação especial '
             'contida na norma […]'],
            'Acórdão do Tribunal Central Administrativo Sul de 4 de fevereiro de 2010, processo n.º 04784/09')

    h3(doc, '2.4  A existência da exceção da al. p) pressupõe sobreposição')
    para(doc,
         'O argumento que se costuma extrair da alteração introduzida pelo Decreto-Lei n.º 315/2003 funciona, '
         'na verdade, nos dois sentidos, e o sentido desfavorável merece ser explicitado. Se os dois regimes '
         'não se tocassem, não teria sido necessária exceção nenhuma. A inserção de uma ressalva na definição '
         'de hospedagem sem fins lucrativos demonstra que o legislador reconheceu que, sem ela, situações de '
         'detenção doméstica ficariam abrangidas pelo conceito de alojamento do Decreto-Lei n.º 276/2001.')
    citacao(doc,
            ['p) «Hospedagem sem fins lucrativos» o alojamento, permanente ou temporário, de animais de '
             'companhia que não vise a obtenção de rendimentos, com exceção das referidas no n.º 3 do artigo '
             '3.º do diploma que aprova o Plano Nacional de Luta e Vigilância da Raiva Animal e outras '
             'Zoonoses;'],
            'Al. p) do n.º 1 do artigo 2.º do Decreto-Lei n.º 276/2001, na redação em vigor')
    para(doc,
         'E a exceção é estreita: «das referidas» é feminino plural e só pode reportar-se às fracções '
         'autónomas mencionadas no n.º 3 do artigo 3.º. Quem detém animais em moradia ou em prédio rústico '
         'não está abrangido pela ressalva. Lido literalmente, o preceito conduz a que a generalidade da '
         'detenção doméstica caia na definição de hospedagem sem fins lucrativos — e, por via da al. a) do '
         'n.º 1 do artigo 3.º, fique sujeita a mera comunicação prévia. Um argumento a contrario construído '
         'sobre a al. p) pode, por isso, voltar-se contra quem o invoca.')

    h3(doc, '2.5  Não há prova de que a articulação tenha sido deliberada')
    para(doc,
         'Sustentou-se por vezes que, tendo os dois diplomas a mesma data, o legislador teria conscientemente '
         'delimitado os regimes. A afirmação não resiste à consulta do preâmbulo do Decreto-Lei n.º 315/2003, '
         'que enuncia como finalidades a autonomização do regime dos animais potencialmente perigosos, a '
         'correção de inexatidões do texto anterior e o reforço de normas de bem-estar, e que **não faz '
         'qualquer referência ao Decreto-Lei n.º 314/2003 nem ao programa da raiva**.')
    para(doc,
         'A ressalva da al. p) apresenta-se, assim, com maior verosimilhança como uma das «correções de '
         'inexatidões» do que como um ato de delimitação pensado. O seu valor interpretativo é, nessa medida, '
         'limitado, e não deve ser apresentado como demonstração.')

    h3(doc, '2.6  Os tribunais dão ao artigo 3.º efeitos fora do plano sanitário')
    para(doc,
         'A doutrina que adiante se cita sustenta que os limites do artigo 3.º valem apenas para efeitos de '
         'prevenção de zoonoses. A jurisprudência civil não tem seguido essa contenção. O Tribunal da Relação '
         'de Guimarães integrou o artigo 3.º no elenco das regras de higiene, sossego e boa vizinhança cuja '
         'violação releva para a resolução do contrato de arrendamento, a par do Regulamento Geral do Ruído e '
         'das restrições de vizinhança do Código Civil.')
    citacao(doc,
            ['[…] o DL n.º 314/2003, de 17 de Dezembro, que aprova o Programa Nacional de Luta e Vigilância '
             'Epidemiológica da Raiva e que em cuja art.º 3º n.º 2 dispõe que nos prédios urbanos podem ser '
             'alojados até três cães ou quatro gatos adultos por cada fogo, não podendo no total ser excedido '
             'o número de quatro animais […]'],
            'Acórdão do Tribunal da Relação de Guimarães de 19 de maio de 2022, processo n.º '
            '119/20.1T8FAF.G1, a propósito da al. a) do n.º 2 do artigo 1083.º do Código Civil')
    para(doc,
         'O acórdão mostra que os limites do artigo 3.º são mobilizados como padrão geral de conduta, fora do '
         'domínio da polícia sanitária. Quem sustente que a norma tem alcance estritamente sanitário tem de '
         'contar com este elemento.')

    h3(doc, '2.7  Os tribunais aplicam o artigo 3.º a canis de facto')
    para(doc,
         'Também não é exato que o artigo 3.º só seja convocado em situações de detenção familiar. Foi ao '
         'abrigo do seu n.º 1 — e não da falta de título de acesso — que se ordenou a remoção dos animais de '
         'um canil instalado no logradouro de um prédio urbano.')
    citacao(doc,
            ['I — Deve ser deferida a providência que visa a remoção de animais alojados num canil '
             'clandestino, instalado no logradouro de um prédio urbano, de onde emana um cheiro nauseabundo, '
             'ladrando os 30 canídeos dia e noite o que traduz violação do disposto no artigo 3.º/1 do '
             'Decreto-Lei n.º 314/2003, de 17 de Dezembro.'],
            'Acórdão do Tribunal da Relação de Lisboa de 28 de junho de 2007, processo n.º 1692/2007-8')
    para(doc,
         'O caso envolvia mais de cinquenta cães de grande porte num logradouro residencial. O Decreto-Lei '
         'n.º 276/2001 não é sequer mencionado. A leitura mais natural do aresto não é a de que o diploma dos '
         'alojamentos não se aplicava, mas a de que a via sanitária foi a escolhida por ser a eficaz.')

    # ------------------------------------------------------------------ 3
    h1(doc, '3.', 'Elementos que sustentam a leitura da delimitação')

    h3(doc, '3.1  Objeto e finalidade dos diplomas')
    para(doc,
         'O Decreto-Lei n.º 314/2003 aprova o Programa Nacional de Luta e Vigilância Epidemiológica da Raiva '
         'Animal e Outras Zoonoses. O bem jurídico do artigo 3.º é enunciado no seu n.º 1 e é a salubridade: '
         'ausência de riscos relativamente à conspurcação ambiental e a doenças transmissíveis ao homem. O '
         'Decreto-Lei n.º 276/2001 executa a Convenção Europeia para a Proteção dos Animais de Companhia e '
         'regula, nos termos do seu artigo 1.º, o exercício da atividade de exploração de alojamentos e de '
         'venda. Um protege a vizinhança e a saúde pública; o outro protege o animal na atividade económica.')

    h3(doc, '3.2  O tipo contraordenacional qualifica o objeto do artigo 3.º')
    para(doc,
         'Quando teve de nomear a realidade que o artigo 3.º disciplina, o legislador não empregou '
         '«alojamento», «estabelecimento» nem «canil». Empregou «habitações e terrenos anexos».')
    citacao(doc,
            ['c) A permanência de cães e gatos em habitações e terrenos anexos em desrespeito pelas condições '
             'previstas no artigo 3.º;'],
            'Al. c), do n.º 3, do artigo 14.º do Decreto-Lei n.º 314/2003')
    para(doc,
         'O elemento é relevante porque provém da norma sancionatória, que delimita condutas puníveis e, por '
         'isso, exige precisão. Não existe no Decreto-Lei n.º 314/2003 qualquer tipo que puna o exercício de '
         'atividade em estabelecimento acima de determinada lotação.')

    h3(doc, '3.3  O diploma sanitário sabe distinguir estabelecimento de habitação')
    para(doc,
         'O Decreto-Lei n.º 314/2003 conhece e regula estabelecimentos — mas fá-lo em artigo próprio, '
         'distinto do artigo 3.º e com alínea sancionatória distinta.')
    citacao(doc,
            ['1 — Os cães e gatos que se encontrem em estabelecimentos destinados ao seu comércio devem estar '
             'acompanhados do respectivo boletim sanitário de cães e gatos […]'],
            'N.º 1 do artigo 5.º do Decreto-Lei n.º 314/2003')
    para(doc,
         'A arrumação interna do diploma é, pois, a seguinte: artigo 3.º para as habitações e terrenos '
         'anexos, punido pela al. c); artigo 5.º para os estabelecimentos de comércio, punido pela al. f). A '
         'distinção é do próprio legislador sanitário. O que não existe é um artigo do Decreto-Lei '
         'n.º 314/2003 dedicado aos estabelecimentos de criação.')

    h3(doc, '3.4  Autoridade competente e procedimento não coincidem')
    tabela(doc,
           ['', 'Decreto-Lei n.º 314/2003, artigo 3.º', 'Decreto-Lei n.º 276/2001'],
           [
            ['Facto regulado', 'Condições de alojamento num prédio',
             'Exercício da atividade de exploração de alojamentos e de criação comercial'],
            ['Intervenção prévia', 'Parecer vinculativo do médico veterinário municipal e do delegado de '
             'saúde, a pedido do detentor',
             'Mera comunicação prévia à DGAV; permissão administrativa nos casos do art.º 3.º, n.º 1, al. b)'],
            ['Reação ao incumprimento', 'Notificação camarária para remoção dos animais; contraordenação da '
             'al. c) do n.º 3 do art.º 14.º',
             'Regime sancionatório próprio dirigido ao titular da exploração, com suspensão e encerramento'],
            ['Fixação da lotação', 'Não estabelece procedimento de fixação',
             'Declarada na mera comunicação prévia (art.º 3.º-A, n.º 1, al. h)) e limitada pelas dimensões '
             'mínimas do anexo III (art.º 27.º, n.º 1)'],
           ],
           [Cm(3.2), Cm(6.6), Cm(6.8)])

    h3(doc, '3.5  O Decreto-Lei n.º 276/2001 admite expressamente alojamentos em casas de habitação')
    para(doc,
         'Se a classificação do prédio fosse determinante para o acesso à atividade, o diploma dos '
         'alojamentos não teria de prever o acesso das autoridades a casas de habitação para controlar o '
         'alojamento e o seu titular.')
    citacao(doc,
            ['2 — Caso o titular da exploração do alojamento se recuse a facultar o acesso ao alojamento, '
             'pode ser solicitado mandado judicial para permitir às autoridades competentes o acesso aos '
             'locais onde os animais se encontrem, nomeadamente casas de habitação e terrenos privados.'],
            'N.º 2 do artigo 67.º-A do Decreto-Lei n.º 276/2001')
    para(doc,
         'A norma pressupõe que um alojamento com titular de exploração possa situar-se numa casa de '
         'habitação. É a mesma opção que o Regulamento (UE) 2026/1818 viria a consagrar ao incluir as casas '
         'particulares no conceito de estabelecimento.')

    h3(doc, '3.6  A capacidade tem regime próprio no diploma dos alojamentos')
    para(doc,
         'O Decreto-Lei n.º 276/2001 dispõe de mecanismo completo de fixação e de controlo da lotação: é '
         'declarada pelo interessado no título de acesso e materialmente limitada pelos parâmetros mínimos de '
         'espaço. Havendo regime especial completo, não há lacuna que justifique ir buscar a norma de '
         'capacidade a diploma com outro objeto.')
    citacao(doc,
            ['h) A capacidade máxima de animais e respetivas espécies a alojar;'],
            'Al. h) do n.º 1 do artigo 3.º-A do Decreto-Lei n.º 276/2001')

    h3(doc, '3.7  Doutrina')
    para(doc,
         'A doutrina que se debruçou sobre o artigo 3.º recusou que os seus limites valham fora do domínio '
         'sanitário, a propósito da tentativa de deles extrair uma limitação geral aos poderes do '
         'proprietário de fracção autónoma.')
    citacao(doc,
            ['Seria no mínimo abusivo pretender retirar daqui uma limitação geral em termos de detenção de '
             'animais numa fracção autónoma, numa limitação matreira aos poderes conferidos pelo código civil '
             'aos proprietários.',
             'A limitação prevista nesta norma vale para efeito de prevenção de zoonoses. […]',
             'O limite máximo aqui estabelecido releva para efeitos de luta e vigilância epidemiológica, '
             'indiciando riscos higío-sanitários, não pretende regular relações de vizinhança, nem tutelar '
             'direitos de personalidade dos outros conviventes no prédio.'],
            'Sandra Passinhas, «Os animais e o regime português da propriedade horizontal», Revista da Ordem '
            'dos Advogados, Ano 66, Vol. II, setembro de 2006')
    nota(doc, [
        'Registe-se que esta posição doutrinária **não foi acolhida** pelo acórdão do Tribunal da Relação de '
        'Guimarães referido em 2.6, que mobilizou o artigo 3.º precisamente como regra de vizinhança. A '
        'doutrina é, neste ponto, elemento de peso mas não pacífico.'])

    h3(doc, '3.8  A prática administrativa não cruza os dois planos')
    para(doc,
         'A prática seguida pelas autoridades competentes é convergente e verificável em fontes públicas '
         'atuais.')
    bullets(doc, [
        'As perguntas frequentes da DGAV para alojamentos de criação, na versão de julho de 2025, descrevem '
        'o título de acesso, os documentos exigidos e os requisitos das instalações por remissão para o '
        'Decreto-Lei n.º 276/2001, e **não invocam em momento algum o Decreto-Lei n.º 314/2003, os limites '
        'por fogo ou a classificação do prédio**.',
        'O serviço municipal de «autorização de alojamento de animais em n.º superior ao previsto na lei» '
        'dirige-se a detentores em prédios urbanos e distingue-o expressamente das situações de alojamento '
        'de animais, com ou sem fins comerciais, sujeitas a título próprio.',
        'Os regulamentos municipais recentes reproduzem o artigo 3.º e acrescentam-lhe apenas o procedimento '
        'de vistoria e a taxa devida, sem o ligarem ao licenciamento de alojamentos — assim, o artigo 13.º do '
        'Regulamento n.º 181/2025, de 31 de janeiro, do Município do Cartaxo.',
    ])

    # ------------------------------------------------------------------ 4
    h1(doc, '4.', 'Ponderação')
    para(doc,
         'Os elementos do ponto 2 provam que os dois diplomas se tocam: partilham o conceito de detentor, '
         'partilham o vocábulo alojamento, e o artigo 3.º é efetivamente aplicado a quem detém muitos animais '
         'numa habitação, incluindo quando a situação é materialmente um canil. Não provam, porém, aquilo '
         'que seria necessário para a tese da sobreposição: que os números do artigo 3.º operem como limite '
         'de lotação de um estabelecimento titulado.')
    para(doc,
         'Os elementos do ponto 3 provam que o artigo 3.º não foi construído como norma de acesso a '
         'atividade: não tipifica o exercício sem título, não fixa lotação de estabelecimento, é executado '
         'por autoridades diferentes e convive com um regime de capacidade completo no diploma dos '
         'alojamentos. Não provam, porém, que o artigo 3.º deixe de se aplicar a quem cria.')
    destaque(doc, [
        'As duas séries de elementos são compatíveis entre si, e a incompatibilidade só surge se se insistir '
        'em formular a questão como exclusão recíproca. **Os regimes são cumulativos.** Quem cria cães na sua '
        'habitação é, simultaneamente, detentor para efeitos do diploma sanitário e — se a atividade for de '
        'criação comercial — operador para efeitos do diploma dos alojamentos. Cumular não é sobrepor: '
        'nenhum dos regimes fixa o limiar do outro.'])

    # ------------------------------------------------------------------ 5
    h1(doc, '5.', 'O ponto de fricção real')
    para(doc,
         'Assente a cumulação, a questão prática reduz-se muito, e convém enunciá-la com exatidão, porque é '
         'mais estreita do que o debate público sugere.')
    para(doc,
         'Nos prédios rústicos e mistos **não existe teto**: o n.º 4 admite exceder os seis animais sempre que '
         'a dimensão do terreno o permita e se verifiquem as condições do n.º 1. Nestes prédios, portanto, o '
         'artigo 3.º não constitui obstáculo à existência de um estabelecimento de criação de qualquer '
         'dimensão, desde que salubre. É neles que se situa a esmagadora maioria dos estabelecimentos.')
    para(doc,
         'Nos prédios urbanos existe um máximo absoluto de seis animais adultos, alcançável apenas mediante '
         'parecer vinculativo do médico veterinário municipal e do delegado de saúde. Aqui, e só aqui, há '
         'colisão possível entre o que o artigo 3.º consente ao detentor e o que a mera comunicação prévia '
         'permitiria declarar ao operador.')
    tabela(doc,
           ['Situação', 'Artigo 3.º do DL n.º 314/2003', 'Efeito prático'],
           [
            ['Prédio rústico ou misto', 'Sem teto; depende da dimensão do terreno e da salubridade (n.º 4)',
             'Não limita a lotação do estabelecimento'],
            ['Prédio urbano, até 4 animais', 'Admitido sem formalidade (n.º 2, 1.ª parte)',
             'Não limita a lotação do estabelecimento'],
            ['Prédio urbano, 5 ou 6 animais', 'Admitido mediante parecer vinculativo (n.º 2, parte final)',
             'Exigência sanitária cumulativa, não título de acesso'],
            ['Prédio urbano, mais de 6 animais', 'Não admitido pela letra do n.º 2',
             'Ponto de fricção — ver texto'],
           ],
           [Cm(3.9), Cm(6.4), Cm(6.3)],
           shades=[None, None, None, {0: NO_BG, 1: NO_BG, 2: NO_BG}])
    para(doc,
         'Sobre a última linha, a posição que os elementos consentem é a seguinte. O n.º 2 não proíbe o '
         'exercício da atividade nem revoga o título de acesso; impõe uma condição higiossanitária ao '
         'alojamento naquele prédio. Um estabelecimento de criação em prédio urbano com mais de seis adultos '
         'encontra-se, à face da letra da lei, em incumprimento do artigo 3.º, com a consequência prevista no '
         'seu n.º 5 e a contraordenação da al. c) do n.º 3 do artigo 14.º — e não com a consequência de o '
         'título de acesso ser inválido. É matéria de conformidade sanitária, não de acesso à atividade.')
    nota(doc, [
        'Este é o único ponto em que a resposta não é inteiramente segura e em que a interpretação contrária '
        'é sustentável. Não se conhece decisão judicial nem parecer publicado que o tenha resolvido. É '
        'também o ponto que o futuro regime deve resolver por via expressa, em vez de o deixar à '
        'interpretação.'])

    # ------------------------------------------------------------------ 6
    h1(doc, '6.', 'O que a prática revela — dedução a partir da aplicação')
    para(doc,
         'Vale a pena olhar para o que efetivamente acontece, e não apenas para o que os textos consentem.')
    para(doc,
         'Na pesquisa realizada na base de dados de jurisprudência das relações, do Supremo Tribunal de '
         'Justiça, dos tribunais centrais administrativos e do Supremo Tribunal Administrativo, foram '
         'identificadas e lidas trinta e duas decisões que citam o Decreto-Lei n.º 314/2003 e trinta e seis '
         'que citam o Decreto-Lei n.º 276/2001. Em nenhuma delas alguém foi sancionado por criar ou alojar '
         'animais de companhia sem o título de acesso do Decreto-Lei n.º 276/2001. As situações de detenção '
         'em massa que chegaram aos tribunais — incluindo um canil de facto com mais de cinquenta cães em '
         'logradouro urbano — foram tratadas pela via sanitária municipal ou pela via dos direitos de '
         'personalidade.')
    para(doc,
         'Acrescente-se um elemento sistemático. A única hipótese em que a lei tipifica autonomamente a '
         'criação sem título é a dos cães potencialmente perigosos, na al. j) do artigo 38.º do Decreto-Lei '
         'n.º 315/2009. Para as restantes raças não existe tipo equivalente.')
    destaque(doc, [
        'A dedução que daqui se retira é relevante para o debate em curso: **o chamado «criador informal» não '
        'existe por falta de norma, mas por ausência de aplicação da que existe.** A criação comercial já '
        'depende de mera comunicação prévia desde 2001, e a ausência de casuística mostra que o incumprimento '
        'desse dever não tem sido objeto de reação. Transferir a discussão para os limites de detenção por '
        'prédio desloca o problema do plano em que ele efetivamente se coloca.'])
    para(doc,
         'A isto acresce um segundo fator, que o exame dos requisitos exigidos torna evidente. As condições '
         'que a DGAV enuncia para os alojamentos de criação — instalações individualizadas para maternidade e '
         'criação até à idade adulta, enfermaria, quarentena, zonas separadas de armazenagem e manuseamento '
         'de alimentos, sistema de proteção contra incêndios com alarme de avaria, área de recreio coberta e '
         'descoberta — não são cumpríveis numa habitação corrente. O obstáculo ao cumprimento não está na '
         'classificação do prédio nem no número de animais: está na calibração dos requisitos, concebidos '
         'para estabelecimentos de dimensão industrial e aplicados sem graduação a quem tem uma ninhada por '
         'ano.')

    # ------------------------------------------------------------------ 7
    h1(doc, '7.', 'A incidência do Regulamento (UE) 2026/1818')
    para(doc,
         'O Regulamento aplica-se aos estabelecimentos de criação independentemente do local em que se '
         'situem, incluindo casas particulares, e prevê para os criadores de pequena dimensão um regime '
         'aligeirado. A partir de 31 de agosto de 2028 a questão nacional passa a colocar-se num quadro '
         'diferente.')
    bullets(doc, [
        'Se Portugal quiser manter os limites de detenção por prédio como restrição oponível a '
        'estabelecimentos abrangidos pelo Regulamento, está a manter uma regra nacional mais restritiva, '
        'sujeita ao artigo 30.º e ao dever de notificação à Comissão **até 31 de agosto de 2028**.',
        'Se entender, como aqui se conclui, que os limites operam no plano sanitário da detenção e não no '
        'plano do acesso à atividade, nada há a notificar quanto a este ponto — mas a clarificação deve '
        'ficar expressa no diploma nacional, para que a questão não continue a ser decidida caso a caso.',
    ])
    nota(doc, [
        'A escolha entre as duas vias não é técnica; é uma opção de política legislativa com prazo. Não a '
        'fazer é, na prática, fazer a primeira sem a notificar.'])

    # ------------------------------------------------------------------ 8
    h1(doc, '8.', 'Nota sobre a estabilidade do artigo 3.º')
    para(doc,
         'O artigo 3.º nunca foi alterado. A verificação é direta: o seu texto é idêntico, palavra por '
         'palavra, nas três versões oficiais do Decreto-Lei n.º 314/2003 — a redação originária de 17 de '
         'dezembro de 2003, a resultante do Decreto-Lei n.º 20/2019, de 30 de janeiro, e a versão em vigor. '
         'As duas alterações sofridas pelo diploma incidiram sobre o n.º 2 do artigo 4.º e sobre o artigo '
         '14.º, e a Resolução da Assembleia da República n.º 138/2019, de 8 de agosto, fez cessar a vigência '
         'das normas alteradas, repristinando nessa parte a redação de 2003.')
    para(doc,
         'Em consequência, o n.º 3 para que remete a al. p) do n.º 1 do artigo 2.º do Decreto-Lei '
         'n.º 276/2001 é hoje o mesmo que era em 2003 — a regra do regulamento do condomínio. A remissão não '
         'está desatualizada por efeito de renumeração; está apenas mal calibrada quanto ao seu alcance, pelas '
         'razões expostas em 2.4.')

    # ------------------------------------------------------------------ 9
    h1(doc, '9.', 'Limites desta análise')
    bullets(doc, [
        'Não se localizou decisão judicial, parecer publicado nem orientação administrativa que resolva '
        'expressamente a questão do prédio urbano com mais de seis animais em estabelecimento titulado. A '
        'conclusão formulada em 5. é, nesse ponto, interpretativa.',
        'A pesquisa jurisprudencial foi feita na base de dados pública dos tribunais superiores. Não cobre a '
        'primeira instância, onde se decide a maior parte das impugnações de atos municipais, nem os '
        'processos de contraordenação decididos administrativamente. A inexistência de casuística publicada '
        'não equivale, por isso, a inexistência de casos.',
        'O motor de pesquisa dessa base devolve zero resultados quando se combina o operador AND com termos '
        'que contenham barra ou acentuação, ainda que existam documentos que satisfazem a consulta. As '
        'pesquisas foram por isso feitas com termos simples e o cruzamento realizado sobre o texto integral '
        'das decisões descarregadas.',
        'Não foi consultado o texto original do Diário da República de 17 de dezembro de 2003 em suporte '
        'oficial, nem o processo legislativo do Decreto-Lei n.º 315/2003, que poderiam esclarecer a génese da '
        'ressalva da al. p).',
    ])

    # ------------------------------------------------------------------ 10
    h1(doc, '10.', 'Conclusões')
    numlist(doc, [
        'O Decreto-Lei n.º 314/2003 **aplica-se** a quem cria cães ou gatos: o criador é detentor nos termos '
        'da al. d) do seu artigo 2.º. Afirmar o contrário é insustentável.',
        'O artigo 3.º **não é norma de acesso à atividade** e os seus números não constituem a lotação dos '
        'estabelecimentos, que é declarada no título de acesso e aferida pelos parâmetros de espaço do '
        'Decreto-Lei n.º 276/2001.',
        'Os dois regimes são **cumulativos**. Em prédios rústicos e mistos não há teto legal de animais; em '
        'prédios urbanos há um máximo de seis adultos, que constitui exigência sanitária e não condição de '
        'validade do título.',
        'A situação do estabelecimento de criação em prédio urbano com mais de seis adultos é o único ponto '
        'genuinamente duvidoso e deve ser resolvido por norma expressa no futuro regime.',
        'A ausência de casuística sobre criação sem título indica que a questão prática do «criador informal» '
        'é de fiscalização e de calibração dos requisitos, e não de insuficiência normativa.',
        'Qualquer opção que mantenha os limites por prédio como restrição a estabelecimentos abrangidos pelo '
        'Regulamento tem de ser notificada à Comissão ao abrigo do artigo 30.º até 31 de agosto de 2028.',
    ])

    h1(doc, '11.', 'Recomendações')
    numlist(doc, [
        'Explicitar no futuro regime que os limites de detenção previstos na legislação sanitária não '
        'constituem limiar de capacidade dos estabelecimentos, e regular expressamente a situação do '
        'estabelecimento em prédio urbano.',
        'Reformular a ressalva da al. p) do n.º 1 do artigo 2.º do Decreto-Lei n.º 276/2001, excecionando '
        'diretamente a detenção doméstica sem remissão e sem a assimetria atual entre fracção autónoma, '
        'moradia e prédio rústico.',
        'Graduar os requisitos das instalações em função da escala da criação, à semelhança do que o '
        'Regulamento faz, em vez de manter um padrão único calibrado para estabelecimentos de grande '
        'dimensão.',
        'Decidir, e fundamentar, a opção quanto ao artigo 30.º do Regulamento dentro do prazo de notificação.',
    ])
