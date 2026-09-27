# -*- coding: utf-8 -*-
"""Estudo: limites por fogo do art. 3.o do DL 314/2003 vs lotacao dos alojamentos registados."""
from _memo_engine import *
from docx.shared import Cm


def construir(doc):
    capa(doc,
         'Estudo jurídico',
         'Os limites de detenção por fogo e a lotação dos alojamentos registados',
         'Artigo 3.º do Decreto-Lei n.º 314/2003 e artigo 3.º-A do Decreto-Lei n.º 276/2001 — '
         'delimitação recíproca',
         'Direção-Geral de Alimentação e Veterinária   ·   setembro de 2026')

    # ------------------------------------------------------------------ 1
    h1(doc, '1.', 'Questão, delimitação do objeto e método')
    para(doc,
         'Pergunta-se se os limites de animais fixados para prédios urbanos no n.º 2 do artigo 3.º do '
         'Decreto-Lei n.º 314/2003 condicionam a lotação de um alojamento registado por mera comunicação '
         'prévia nos termos do artigo 3.º-A do Decreto-Lei n.º 276/2001.')
    enquadramento(doc, [
        '**Delimitação do objeto.** Trata-se de questão de direito interno vigente. O Regulamento (UE) '
        '2026/1818 e o projeto de diploma consolidado ficam expressamente fora deste estudo. A ponte '
        'entre eles, se houver lugar a ela, faz-se noutro documento e depois.'])
    para(doc,
         'O método foi o seguinte. Partiu-se do texto de ambos os diplomas e confrontou-se com quatro '
         'ordens de elemento: os argumentos que sustentam a aplicação dos limites ao estabelecimento, os '
         'que a afastam, a jurisprudência dos tribunais superiores e a prática administrativa. Os '
         'elementos desfavoráveis à conclusão final são apresentados em primeiro lugar e sem atenuação. '
         'Todas as citações são verbatim.')

    # ------------------------------------------------------------------ 2
    h1(doc, '2.', 'Conclusões')
    destaque(doc, [
        'Os limites do n.º 2 do artigo 3.º do Decreto-Lei n.º 314/2003 **não fixam a lotação de um '
        'alojamento registado** — mas por uma razão precisa, e com um caso residual em que a resposta é '
        'afirmativa.'])
    numlist(doc, [
        'A unidade de contagem do n.º 2 é o **fogo**, não o prédio. Onde não há fogo, a norma não tem '
        'campo operativo.',
        'Um alojamento registado não é um fogo: o artigo 25.º do Decreto-Lei n.º 276/2001 obriga-o a '
        'possuir **instalações individualizadas**, o que o diferencia necessariamente da habitação.',
        'O **n.º 1** do artigo 3.º — dever geral de salubridade — **aplica-se sempre**, incluindo ao '
        'alojamento registado. Registar não isenta; a al. j) do n.º 1 do artigo 3.º-A obriga o '
        'interessado a declarar o cumprimento de toda a legislação aplicável em matéria de higiene.',
        '**Caso residual.** Quem tem o alojamento registado mas mantém os animais integrados na casa, '
        'como animais do agregado, continua sujeito ao n.º 2. O registo não cria, por si, caminho acima '
        'de seis animais dentro do fogo.',
    ])
    nota(doc, [
        'Não se localizou decisão judicial, parecer publicado nem orientação administrativa que resolva '
        'expressamente a questão. A conclusão é interpretativa e o ponto 15 declara os seus limites.'])

    # ------------------------------------------------------------------ 3
    pagebreak(doc)
    h1(doc, '3.', 'Os dois regimes')
    para(doc,
         'Antes do confronto dos textos, importa fixar o que cada diploma regula, a quem se dirige, que '
         'autoridade o executa e por que procedimento.')
    tabela(doc,
           ['', 'Decreto-Lei n.º 314/2003, artigo 3.º', 'Decreto-Lei n.º 276/2001'],
           [
            ['Objeto do diploma',
             'Programa Nacional de Luta e Vigilância Epidemiológica da Raiva Animal e Outras Zoonoses; '
             'regras relativas à posse e detenção, comércio, exposições e entrada em território nacional',
             'Medidas complementares da Convenção Europeia para a Proteção dos Animais de Companhia; '
             'exercício da atividade de exploração de alojamentos, independentemente do seu fim, e de '
             'venda'],
            ['Facto regulado', 'Condições de alojamento de animais num prédio',
             'Exercício da atividade de exploração de alojamentos e de criação comercial'],
            ['Unidade de referência', 'O **fogo**, nos prédios urbanos; o **terreno**, nos rústicos e '
             'mistos', 'O **alojamento**, com capacidade máxima declarada'],
            ['Intervenção prévia',
             'Parecer vinculativo do médico veterinário municipal e do delegado de saúde, a pedido do '
             'detentor, para exceder quatro animais',
             'Mera comunicação prévia dirigida à DGAV; permissão administrativa nos casos da al. b) do '
             'n.º 1 do artigo 3.º'],
            ['Reação ao incumprimento',
             'Notificação camarária para remoção dos animais para o canil ou gatil municipal (n.º 5); '
             'contraordenação da al. c) do n.º 3 do artigo 14.º, punível pelo diretor-geral',
             'Regime sancionatório próprio dirigido ao titular da exploração, com suspensão e '
             'encerramento; instrução e decisão pela DGAV (artigo 70.º)'],
            ['Fixação da lotação', 'Não estabelece procedimento de fixação',
             'Declarada na mera comunicação prévia (al. h) do n.º 1 do artigo 3.º-A) e limitada pelas '
             'dimensões mínimas do anexo III (n.º 1 do artigo 27.º)'],
           ],
           [Cm(3.0), Cm(6.6), Cm(6.8)])
    nota(doc, [
        '**Nota institucional.** Os n.ºs 2 a 10 do artigo 3.º do Decreto-Lei n.º 276/2001 foram revogados '
        'pelo Decreto-Lei n.º 260/2012, de 12 de dezembro. Com eles desapareceu o antigo regime de licença '
        'de funcionamento, que exigia licenças camarárias e parecer do médico veterinário municipal. '
        '**Desde 2012 o município deixou de intervir no título de acesso do alojamento.** Não existe hoje '
        'nenhum momento procedimental em que as duas autoridades se encontrem: a contradição, quando '
        'surge, só aflora em inspeção.'])

    # ------------------------------------------------------------------ 4
    pagebreak(doc)
    h1(doc, '4.', 'Os textos em confronto')

    h2(doc, '4.1', 'Decreto-Lei n.º 314/2003, de 17 de dezembro')
    para(doc,
         'O artigo 3.º transcreve-se na íntegra, por ser a peça central da questão. O ponto 16 demonstra '
         'que nunca foi alterado.')
    citacao(doc,
            ['1 - O alojamento de cães e gatos em prédios urbanos, rústicos ou mistos, fica sempre '
             'condicionado à existência de boas condições do mesmo e ausência de riscos hígio-sanitários '
             'relativamente à conspurcação ambiental e doenças transmissíveis ao homem.',
             '2 - Nos prédios urbanos podem ser alojados até três cães ou quatro gatos adultos por cada '
             'fogo, não podendo no total ser excedido o número de quatro animais, excepto se, a pedido do '
             'detentor, e mediante parecer vinculativo do médico veterinário municipal e do delegado de '
             'saúde, for autorizado alojamento até ao máximo de seis animais adultos, desde que se '
             'verifiquem todos os requisitos hígio-sanitários e de bem-estar animal legalmente exigidos.',
             '3 - No caso de fracções autónomas em regime de propriedade horizontal, o regulamento do '
             'condomínio pode estabelecer um limite de animais inferior ao previsto no número anterior.',
             '4 - Nos prédios rústicos ou mistos podem ser alojados até seis animais adultos, podendo tal '
             'número ser excedido se a dimensão do terreno o permitir e desde que as condições de '
             'alojamento obedeçam aos requisitos estabelecidos no n.º 1.',
             '5 - Em caso de não cumprimento do disposto nos números anteriores, as câmaras municipais, '
             'após vistoria conjunta do delegado de saúde e do médico veterinário municipal, notificam o '
             'detentor para retirar os animais para o canil ou gatil municipal no prazo estabelecido por '
             'aquelas entidades, caso o detentor não opte por outro destino que reúna as condições '
             'estabelecidas pelo presente diploma.',
             '6 - No caso de criação de obstáculos ou impedimentos à remoção de animais que se encontrem '
             'em desrespeito ao previsto no presente artigo, o presidente da câmara municipal pode '
             'solicitar a emissão de mandado judicial que lhe permita aceder ao local onde estes se '
             'encontram e à sua remoção.'],
            'Artigo 3.º do Decreto-Lei n.º 314/2003, epígrafe «Detenção de cães e gatos»')
    para(doc, 'Três outras normas do mesmo diploma relevam para a questão.')
    citacao(doc,
            ["d) 'Detentor' qualquer pessoa, singular ou colectiva, responsável pelos animais de "
             "companhia para efeitos de reprodução, criação, manutenção, acomodação ou utilização, com ou "
             "sem fins comerciais;"],
            'Al. d) do artigo 2.º do Decreto-Lei n.º 314/2003')
    citacao(doc,
            ['1 - Os cães e gatos que se encontrem em estabelecimentos destinados ao seu comércio devem '
             'estar acompanhados do respectivo boletim sanitário de cães e gatos […]'],
            'N.º 1 do artigo 5.º do Decreto-Lei n.º 314/2003, epígrafe «Comércio de cães e gatos»')
    citacao(doc,
            ['c) A permanência de cães e gatos em habitações e terrenos anexos em desrespeito pelas '
             'condições previstas no artigo 3.º;',
             'f) O comércio de cães e gatos em desrespeito das condições previstas no artigo 5.º;'],
            'Als. c) e f) do n.º 3 do artigo 14.º do Decreto-Lei n.º 314/2003')

    h2(doc, '4.2', 'Decreto-Lei n.º 276/2001, de 17 de outubro')
    para(doc,
         'Este diploma **nunca usa a palavra «fogo»**. Verificado por pesquisa ao texto integral da versão '
         'consolidada. A sua unidade é o alojamento.')
    citacao(doc,
            ['1 - O presente diploma estabelece as medidas complementares das disposições da Convenção '
             'Europeia para a Proteção dos Animais de Companhia […] regulando o exercício da atividade de '
             'exploração de alojamentos, independentemente do seu fim, e de venda de animais de '
             'companhia, presencialmente ou através de meios eletrónicos.'],
            'N.º 1 do artigo 1.º do Decreto-Lei n.º 276/2001')
    citacao(doc,
            ['n) «Alojamento» qualquer instalação, edifício, grupo de edifícios ou outro local, podendo '
             'incluir zona não completamente fechada, onde os animais de companhia se encontram mantidos;',
             'p) «Hospedagem sem fins lucrativos» o alojamento, permanente ou temporário, de animais de '
             'companhia que não vise a obtenção de rendimentos, com exceção das referidas no n.º 3 do '
             'artigo 3.º do diploma que aprova o Plano Nacional de Luta e Vigilância da Raiva Animal e '
             'outras Zoonoses;',
             'q) «Hospedagem com fins lucrativos» o alojamento para reprodução, criação, manutenção e '
             'venda de animais de companhia que vise interesses comerciais ou lucrativos, incluindo-se no '
             'alojamento para manutenção os hotéis e os centros de treino de cães com alojamento;',
             'v) «Detentor» qualquer pessoa, singular ou coletiva, responsável pelos animais de companhia '
             'para efeitos de reprodução, criação, manutenção, acomodação ou utilização, com ou sem fins '
             'lucrativos;'],
            'Als. n), p), q) e v) do n.º 1 do artigo 2.º do Decreto-Lei n.º 276/2001')
    nota(doc, [
        'Registe-se desde já que a definição de detentor da al. v) é **praticamente idêntica** à da al. d) '
        'do artigo 2.º do Decreto-Lei n.º 314/2003, mudando apenas «lucrativos» por «comerciais». Os dois '
        'diplomas partilham o conceito de detentor. O que os separa não é a pessoa; é o facto regulado.'])
    citacao(doc,
            ['1 - A mera comunicação prévia a que se refere a alínea a) do n.º 1 do artigo anterior é '
             'dirigida à DGAV e deve conter os seguintes elementos, quando aplicáveis: […] h) A capacidade '
             'máxima de animais e respetivas espécies a alojar; i) O número de animais detidos, espécies e '
             'raças; j) Declaração de responsabilidade, subscrita pelo interessado, relativa ao '
             'cumprimento da legislação aplicável aos animais de companhia, nomeadamente em matéria de '
             'instalações, equipamentos, higiene, saúde e bem-estar dos animais.'],
            'Als. h), i) e j) do n.º 1 do artigo 3.º-A do Decreto-Lei n.º 276/2001')
    citacao(doc,
            ['Os detentores de animais de companhia que se dediquem à sua reprodução, criação, manutenção '
             'ou venda devem cumprir as condições previstas no presente capítulo, sem prejuízo das demais '
             'disposições aplicáveis, nomeadamente as constantes do Decreto-Lei n.º 315/2009, de 29 de '
             'outubro.'],
            'Artigo 24.º do Decreto-Lei n.º 276/2001')
    citacao(doc,
            ['1 - Os alojamentos no âmbito deste capítulo devem possuir instalações individualizadas '
             'destinadas à armazenagem de alimentos e equipamento limpo e à lavagem e recolha de material.',
             '2 - Os alojamentos para a reprodução/criação, para além do disposto no número anterior, '
             'devem possuir instalações individualizadas destinadas à maternidade e à criação até à idade '
             'adulta, a quarentena, a enfermaria, o manuseamento de alimentos e à higienização dos '
             'animais.',
             '4 - Os hotéis para animais, para além do disposto no n.º 1, devem possuir instalações '
             'individualizadas para enfermaria, manuseamento de alimentos e higienização dos animais.',
             '5 - […] os alojamentos destinados a cães e gatos devem também possuir área de recreio, '
             'coberta ou descoberta.'],
            'N.ºs 1, 2, 4 e 5 do artigo 25.º do Decreto-Lei n.º 276/2001')
    citacao(doc,
            ['1 - O alojamento de cães e gatos deve obedecer às dimensões mínimas indicadas no anexo iii '
             'do presente diploma, do qual faz parte integrante.'],
            'N.º 1 do artigo 27.º do Decreto-Lei n.º 276/2001')
    citacao(doc,
            ['2 - Caso o titular da exploração do alojamento se recuse a facultar o acesso ao alojamento, '
             'pode ser solicitado mandado judicial para permitir às autoridades competentes o acesso aos '
             'locais onde os animais se encontrem, nomeadamente casas de habitação e terrenos privados.'],
            'N.º 2 do artigo 67.º-A do Decreto-Lei n.º 276/2001')

    # ------------------------------------------------------------------ 5
    pagebreak(doc)
    h1(doc, '5.', 'O conceito de fogo e as suas consequências operativas')
    para(doc,
         'O Decreto-Lei n.º 314/2003 não define «fogo». Aplica-se o sentido corrente e urbanístico. No '
         'Regulamento Geral das Edificações Urbanas, aprovado pelo Decreto-Lei n.º 38 382, de 7 de agosto '
         'de 1951, as noções de «habitação» e de «fogo» são usadas como sinónimos, definindo-se «área '
         'bruta da habitação» como a superfície total do fogo. Em estatística e na Ficha Técnica da '
         'Habitação, o fogo integra-se no conceito de alojamento familiar, abrangendo a habitação o fogo e '
         'as suas dependências — varandas, arrecadações, logradouros pavimentados, telheiros e alpendres.')
    para(doc, 'Daqui decorrem três consequências operativas, e são decisivas.')
    numlist(doc, [
        '**A unidade de contagem do n.º 2 é doméstica, não predial.** Um prédio urbano com dez fogos '
        'comporta dez vezes a dotação. O limite não é do prédio; é de cada fogo.',
        '**Um prédio urbano sem fogo não tem unidade a que aplicar o n.º 2.** A norma não tem, aí, campo '
        'operativo — não porque se afaste, mas porque lhe falta o termo de referência.',
        '**O Decreto-Lei n.º 276/2001 nunca usa a palavra.** A sua unidade é o alojamento, cuja capacidade '
        'é declarada pelo interessado e aferida por superfície.',
    ])

    # ------------------------------------------------------------------ 6
    pagebreak(doc)
    h1(doc, '6.', 'Elementos que sustentam a aplicação')
    para(doc,
         'Expõem-se primeiro, e sem atenuação, os argumentos que militam no sentido de os limites do '
         'artigo 3.º condicionarem a lotação do estabelecimento. Uma conclusão que só resista quando se '
         'omite o que a contraria não serve para fundamentar posição institucional.')

    h3(doc, '6.1  O artigo 3.º emprega a palavra «alojamento»')
    para(doc,
         'O n.º 1 não fala de «detenção» no seu corpo dispositivo: fala de alojamento. E os n.ºs 2 e 4 '
         'dizem «podem ser alojados». É o mesmo vocábulo que define o objeto do Decreto-Lei n.º 276/2001, '
         'cuja al. n) do n.º 1 do artigo 2.º o define de forma amplíssima — «qualquer instalação, '
         'edifício, grupo de edifícios ou outro local». Qualquer argumento que assente numa alegada '
         'divergência de vocabulário tem de ser construído sobre esta base, e não contra ela.')

    h3(doc, '6.2  O detentor do diploma sanitário abrange quem cria com fins comerciais')
    para(doc,
         'É o elemento mais forte contra a conclusão, e não pode ser contornado. A al. d) do artigo 2.º do '
         'Decreto-Lei n.º 314/2003 define detentor por referência expressa à reprodução e à criação, com '
         'ou sem fins comerciais.')
    destaque(doc, [
        '**É incorreto sustentar que o Decreto-Lei n.º 314/2003 não se aplica a quem cria.** Aplica-se. '
        'Quem cria é detentor para efeitos do diploma sanitário, e o artigo 3.º dirige-se-lhe. A questão '
        'em aberto não é essa; é apenas a de saber se os números do artigo 3.º funcionam como teto de '
        'lotação do estabelecimento.'])

    h3(doc, '6.3  O n.º 4 tem estrutura de norma de capacidade')
    para(doc,
         'O artigo 3.º não se limita a impor condições higiossanitárias. No n.º 4 gradua o número '
         'admissível em função da área disponível — «podendo tal número ser excedido se a dimensão do '
         'terreno o permitir» —, que é a lógica própria das normas de lotação.')

    h3(doc, '6.4  Nenhum dos diplomas contém norma de articulação')
    para(doc,
         'Não existe preceito que isente o alojamento titulado do artigo 3.º, nem preceito que declare os '
         'limites aplicáveis aos estabelecimentos. O silêncio é recíproco e total.')

    h3(doc, '6.5  A ressalva da al. p) pressupõe sobreposição')
    para(doc,
         'O argumento que se costuma extrair da alteração introduzida pelo Decreto-Lei n.º 315/2003 '
         'funciona nos dois sentidos, e o sentido desfavorável merece ser explicitado. **Se os dois '
         'regimes não se tocassem, não teria sido necessária exceção nenhuma.** A inserção de uma ressalva '
         'na definição de hospedagem sem fins lucrativos demonstra que o legislador reconheceu que, sem '
         'ela, situações de detenção doméstica ficariam abrangidas pelo conceito de alojamento.')
    para(doc,
         'E a exceção é estreita. «Das referidas» é feminino plural e só pode reportar-se às fracções '
         'autónomas mencionadas no n.º 3 do artigo 3.º. Quem detém animais em moradia ou em prédio rústico '
         'não está abrangido pela ressalva. Lido literalmente, o preceito conduz a que a generalidade da '
         'detenção doméstica caia na definição de hospedagem sem fins lucrativos e fique sujeita a mera '
         'comunicação prévia. Um argumento *a contrario* construído sobre a al. p) pode, por isso, '
         'voltar-se contra quem o invoca.')

    h3(doc, '6.6  A norma sancionatória alcança o terreno anexo')
    para(doc,
         'A al. c) do n.º 3 do artigo 14.º tipifica a conduta como «permanência de cães e gatos em '
         'habitações **e terrenos anexos**». O «terreno anexo» alcança literalmente o quintal, e com ele '
         'as instalações que aí sejam construídas.')

    h3(doc, '6.7  Não há prova de que a articulação tenha sido deliberada')
    para(doc,
         'Sustentou-se por vezes que, tendo os dois diplomas a mesma data — 17 de dezembro de 2003 —, o '
         'legislador teria conscientemente delimitado os regimes. A afirmação não resiste à consulta do '
         'preâmbulo do Decreto-Lei n.º 315/2003, que enuncia como finalidades a autonomização do regime '
         'dos animais potencialmente perigosos, a correção de inexatidões do texto anterior e o reforço de '
         'normas de bem-estar, e que **não faz qualquer referência ao Decreto-Lei n.º 314/2003 nem ao '
         'programa da raiva**. A ressalva da al. p) apresenta-se, assim, com maior verosimilhança como uma '
         'das «correções de inexatidões» do que como ato de delimitação pensado.')

    # ------------------------------------------------------------------ 7
    pagebreak(doc)
    h1(doc, '7.', 'Elementos que sustentam a não aplicação')

    h3(doc, '7.1  A unidade do n.º 2 é o fogo')
    para(doc,
         'Desenvolvido no ponto 5. É o elemento decisivo: a norma conta animais por fogo, e onde não há '
         'fogo falta-lhe o termo de referência.')

    h3(doc, '7.2  O alojamento registado é, por imposição legal, um conjunto de instalações individualizadas')
    para(doc,
         'Este é o segundo elemento decisivo, e é interno ao Decreto-Lei n.º 276/2001. Cumprir o artigo '
         '25.º é, por definição, constituir um conjunto diferenciado da habitação: instalações '
         'individualizadas para armazenagem de alimentos e equipamento limpo, para lavagem e recolha de '
         'material e, tratando-se de reprodução ou criação, para maternidade, criação até à idade adulta, '
         'quarentena, enfermaria, manuseamento de alimentos e higienização, mais área de recreio coberta e '
         'descoberta.')
    destaque(doc, [
        'Um fogo que cumpra o artigo 25.º deixou de ser apenas um fogo naquilo em que o cumpre. **A lei '
        'não admite que o alojamento registado se confunda com a habitação: obriga a que dela se '
        'diferencie.**'])

    h3(doc, '7.3  A capacidade tem regime próprio e completo')
    para(doc,
         'A lotação é declarada pelo interessado no título de acesso — al. h) do n.º 1 do artigo 3.º-A — e '
         'materialmente limitada pelas dimensões mínimas do anexo III, por força do n.º 1 do artigo 27.º. '
         'Havendo regime especial completo, não há lacuna que justifique ir buscar a norma de capacidade a '
         'diploma com objeto diverso. A regra da especialidade impõe a prevalência do Decreto-Lei '
         'n.º 276/2001 nesta matéria.')

    h3(doc, '7.4  A norma sancionatória qualifica o objeto do artigo 3.º')
    para(doc,
         'Quando teve de nomear, na norma sancionatória, a realidade que o artigo 3.º disciplina, o '
         'legislador não empregou «alojamento», «estabelecimento» nem «canil». Empregou «habitações e '
         'terrenos anexos». O elemento é relevante porque provém da norma que delimita condutas puníveis '
         'e, por isso, exige precisão. **Não existe no Decreto-Lei n.º 314/2003 qualquer tipo que puna o '
         'exercício de atividade em estabelecimento acima de determinada lotação.**')

    h3(doc, '7.5  O diploma sanitário sabe distinguir estabelecimento de habitação')
    para(doc,
         'O Decreto-Lei n.º 314/2003 conhece e regula estabelecimentos — mas fá-lo em artigo próprio, '
         'distinto do artigo 3.º e com alínea sancionatória distinta. A arrumação interna é esta: artigo '
         '3.º para as habitações e terrenos anexos, punido pela al. c); artigo 5.º para os estabelecimentos '
         'de comércio, punido pela al. f). A distinção é do próprio legislador sanitário. O que não existe '
         'é artigo do mesmo diploma dedicado aos estabelecimentos de criação.')

    h3(doc, '7.6  O diploma dos alojamentos admite expressamente alojamentos em casas de habitação')
    para(doc,
         'Se a classificação do prédio fosse determinante para o acesso à atividade, o diploma dos '
         'alojamentos não teria de prever o acesso das autoridades a casas de habitação para controlar o '
         'alojamento e o seu titular. O n.º 2 do artigo 67.º-A pressupõe que um alojamento com titular de '
         'exploração possa situar-se numa casa de habitação.')

    h3(doc, '7.7  Autoridades e procedimentos não coincidem')
    para(doc,
         'O artigo 3.º do Decreto-Lei n.º 314/2003 é executado pela câmara municipal, com o delegado de '
         'saúde e o médico veterinário municipal, e sancionado pelo diretor-geral. O Decreto-Lei '
         'n.º 276/2001 assenta na mera comunicação prévia à DGAV. Desde a revogação dos n.ºs 2 a 10 do seu '
         'artigo 3.º pelo Decreto-Lei n.º 260/2012 não existe momento procedimental em que as duas '
         'autoridades se encontrem.')

    h3(doc, '7.8  Cláusula expressa de cumulação')
    para(doc,
         'O artigo 24.º manda cumprir as condições do capítulo III «sem prejuízo das demais disposições '
         'aplicáveis». É cláusula expressa de cumulação, e o seu destinatário é o **detentor** que se '
         'dedica à reprodução, criação, manutenção ou venda — não o «titular da exploração». Cumular não é '
         'sobrepor.')

    h3(doc, '7.9  O registo pressupõe a conformidade; não a dispensa')
    para(doc,
         'A al. j) do n.º 1 do artigo 3.º-A faz o interessado declarar o cumprimento da legislação '
         'aplicável aos animais de companhia, «nomeadamente em matéria de instalações, equipamentos, '
         '**higiene**, saúde e bem-estar dos animais». Registar não isenta: obriga a declarar que se '
         'cumpre tudo o resto, incluindo o n.º 1 do artigo 3.º.')

    # ------------------------------------------------------------------ 8
    pagebreak(doc)
    h1(doc, '8.', 'O teste da absurdidade')
    para(doc,
         'Se o n.º 2 fosse teto de prédio urbano, seguir-se-iam estas consequências.')
    bullets(doc, [
        'Nenhum **hotel para animais** — al. q) do n.º 1 do artigo 2.º e n.º 4 do artigo 25.º — instalado '
        'em prédio urbano poderia ter mais de seis animais adultos.',
        'Nenhum **centro de atendimento médico-veterinário** poderia internar mais de seis.',
        'Nenhuma **loja de venda** poderia expor mais de seis.',
        'Nenhum **centro de recolha oficial** instalado em prédio urbano seria legal — e o anexo III tem '
        'alínea dedicada a centros de recolha, que pressupõe alojamento em grupo em canil.',
        'O próprio n.º 5 do artigo 3.º manda remover os animais em excesso «para o canil ou gatil '
        'municipal», que teria assim de receber mais animais do que a lei lhe permitiria alojar.',
    ])
    destaque(doc, [
        'Nenhuma destas consequências é sustentada por ninguém. **E a razão pela qual não se verificam é '
        'sempre a mesma: nenhum destes locais é um fogo.** O teste não é retórico — confirma, por via '
        'independente, a leitura exposta no ponto 5.'])

    # ------------------------------------------------------------------ 9
    h1(doc, '9.', 'Ponderação')
    para(doc,
         'Os elementos do ponto 6 provam que os dois diplomas se tocam: partilham o conceito de detentor, '
         'partilham o vocábulo alojamento, e o artigo 3.º é efetivamente aplicável a quem cria. Não provam, '
         'porém, aquilo que seria necessário para a tese da sobreposição — que os números do artigo 3.º '
         'operem como limite de lotação de um estabelecimento titulado.')
    para(doc,
         'Os elementos do ponto 7 provam que o artigo 3.º não foi construído como norma de acesso a '
         'atividade: não tipifica o exercício sem título, não fixa lotação de estabelecimento, é executado '
         'por autoridades diferentes e convive com um regime de capacidade completo no diploma dos '
         'alojamentos. Não provam, porém, que o artigo 3.º deixe de se aplicar a quem cria.')
    destaque(doc, [
        'As duas séries são compatíveis, e a incompatibilidade só surge se se insistir em formular a '
        'questão como exclusão recíproca. **Os regimes são cumulativos.** Quem cria na sua habitação é, '
        'simultaneamente, detentor para efeitos sanitários e operador para efeitos do diploma dos '
        'alojamentos. Cumular não é sobrepor: nenhum dos regimes fixa o limiar do outro.'])

    # ------------------------------------------------------------------ 10
    pagebreak(doc)
    h1(doc, '10.', 'Aplicação a casos-tipo')
    para(doc,
         'Assente a cumulação, o critério deixa de ser a classificação matricial e passa a ser **onde '
         'estão os animais**.')
    tabela(doc,
           ['Situação de facto', 'Enquadramento', 'Limite aplicável'],
           [
            ['Moradia em prédio urbano; animais a viver dentro da casa, como animais do agregado',
             'Estão no **fogo**',
             '**N.º 2 aplica-se**: quatro animais; até seis mediante parecer vinculativo do médico '
             'veterinário municipal e do delegado de saúde'],
            ['Moradia em prédio urbano; animais em instalações do artigo 25.º construídas no quintal',
             'Estão no **alojamento**',
             'O n.º 2 **não** fixa a lotação; fixam-na a capacidade declarada e o anexo III'],
            ['Prédio rústico ou misto, com ou sem estabelecimento',
             'N.º 4 do artigo 3.º',
             '**Sem teto**: seis animais, excedíveis se a dimensão do terreno o permitir'],
            ['Fracção autónoma em propriedade horizontal',
             'Acresce o n.º 3 do artigo 3.º e o regime da propriedade horizontal',
             'Hipótese **não analisada** neste estudo — ver ponto 15'],
            ['Qualquer das anteriores', '—',
             '**N.º 1 aplica-se sempre**: boas condições e ausência de riscos hígio-sanitários'],
           ],
           [Cm(5.0), Cm(4.0), Cm(7.6)])
    nota(doc, [
        '**Precisão quanto ao logradouro.** O logradouro de uma moradia integra o prédio urbano, entrando '
        'na avaliação como área de terreno livre. Não converte o conjunto em prédio misto: o artigo 5.º do '
        'Código do Imposto Municipal sobre Imóveis exige, para essa qualificação, que nenhuma das partes '
        'seja a principal. A área do quintal é, por isso, juridicamente irrelevante para o n.º 2 — o que é '
        'precisamente o que o ponto 13 problematiza.'])

    # ------------------------------------------------------------------ 11
    pagebreak(doc)
    h1(doc, '11.', 'Jurisprudência')
    para(doc,
         'Nenhuma decisão resolve a questão. Três aproximam-se, e a terceira contraria a doutrina que '
         'adiante se cita.')

    h3(doc, '11.1  Acórdão do Tribunal Central Administrativo Sul de 4 de fevereiro de 2010')
    citacao(doc,
            ['I – A posse de animais [cães ou gatos] em qualquer número em prédios urbanos, rústicos ou '
             'mistos, nos termos do n.º 1 do artigo 3.º do DL n.º 314/2003, de 17/12, depende da '
             'existência de uma situação de salubridade ambiental, com vista a evitar um perigo para a '
             'saúde pública.',
             'II – Porém, o n.º 4 do preceito em causa prevê que «nos prédios rústicos ou mistos podem ser '
             'alojados até seis animais adultos, podendo tal número ser excedido se a dimensão do terreno '
             'o permitir […]», o que significa que incumbe à Administração aferir sempre se o prédio onde '
             'se encontram alojados animais [cães e gatos] permite ou não o enquadramento na situação '
             'especial contida na norma […]'],
            'Sumário do acórdão do TCA Sul de 4.2.2010, processo n.º 04784/09, relator Rui Pereira; '
            'descritores «alojamento de animais» e «prédio misto»')
    para(doc,
         'O caso teve origem em despacho do presidente de câmara, de 2 de janeiro de 2006, ordenando a '
         'remoção dos cães existentes na residência «para além do limite imposto». Confirma que o n.º 4 '
         'não tem teto e que a Administração tem de aferir caso a caso. Nada diz sobre estabelecimentos.')

    h3(doc, '11.2  Acórdão do Tribunal da Relação de Lisboa de 28 de junho de 2007')
    citacao(doc,
            ['I – Deve ser deferida a providência que visa a remoção de animais alojados num canil '
             'clandestino, instalado no logradouro de um prédio urbano, de onde emana um cheiro '
             'nauseabundo, ladrando os 30 canídeos dia e noite o que traduz violação do disposto no artigo '
             '3.º/1 do Decreto-lei n.º 314/2003, de 17 de Dezembro.'],
            'Sumário do acórdão do TRL de 28.6.2007, processo n.º 1692/2007-8, relator Salazar Casanova')
    para(doc,
         'O caso envolvia mais de cinquenta cães de grande porte no logradouro de uma vivenda geminada. '
         'Foi resolvido pelo n.º 1 do artigo 3.º e pela tutela dos direitos de personalidade. **O '
         'Decreto-Lei n.º 276/2001 não é sequer mencionado**, apesar de estar em causa instalação que, com '
         'cinquenta cães, seria manifestamente um alojamento não titulado.')
    nota(doc, [
        '**Duplo sentido.** Mostra que o artigo 3.º é efetivamente mobilizado contra instalações que são, '
        'de facto, canis, e não apenas contra a detenção familiar — o que milita no sentido do ponto 6. '
        'Mas o caso era de instalação **não titulada**, e não de lotação de alojamento registado. A '
        'leitura mais natural do silêncio sobre o Decreto-Lei n.º 276/2001 não é a de que o diploma não se '
        'aplicava, mas a de que a via sanitária e a tutela da personalidade foram as escolhidas por serem '
        'as eficazes.'])

    h3(doc, '11.3  Acórdão do Tribunal da Relação de Guimarães de 19 de maio de 2022')
    para(doc,
         'A doutrina que se debruçou sobre o artigo 3.º sustentou que os seus limites valem apenas para '
         'efeitos de prevenção de zoonoses e que seria abusivo deles extrair uma limitação geral aos '
         'poderes do proprietário de fracção autónoma. Essa posição não foi acolhida.')
    citacao(doc,
            ['[…] o DL n.º 314/2003, de 17 de Dezembro, que aprova o Programa Nacional de Luta e '
             'Vigilância Epidemiológica da Raiva e que em cuja art.º 3º n.º 2 dispõe que nos prédios '
             'urbanos podem ser alojados até três cães ou quatro gatos adultos por cada fogo, não podendo '
             'no total ser excedido o número de quatro animais […] e cujo n.º 3 dispõe que [n]o caso de '
             'fracções autónomas em regime de propriedade horizontal, o regulamento do condomínio pode '
             'estabelecer um limite de animais inferior ao previsto no número anterior;'],
            'Acórdão do TRG de 19.5.2022, processo n.º 119/20.1T8FAF.G1, relator José Carlos Duarte, a '
            'propósito da al. a) do n.º 2 do artigo 1083.º do Código Civil')
    para(doc,
         'O tribunal integrou o artigo 3.º no elenco das regras de higiene, sossego e boa vizinhança '
         'relevantes para a resolução do contrato de arrendamento, a par do Regulamento Geral do Ruído e '
         'das restrições de vizinhança do Código Civil. É elemento de peso: mostra que os limites são '
         'mobilizados como padrão de conduta fora do domínio da polícia sanitária. Não respeita, ainda '
         'assim, à capacidade de estabelecimentos.')

    h3(doc, '11.4  Resultado negativo')
    destaque(doc, [
        'Foram descarregados e lidos na íntegra **trinta e dois acórdãos que citam o Decreto-Lei '
        'n.º 314/2003 e trinta e seis que citam o Decreto-Lei n.º 276/2001**, nas nove bases dos tribunais '
        'superiores. Em nenhum deles alguém foi sancionado por criar ou alojar animais sem o título de '
        'acesso, e em nenhum a lotação de um estabelecimento foi fixada a partir do artigo 3.º.'])

    # ------------------------------------------------------------------ 12
    pagebreak(doc)
    h1(doc, '12.', 'Prática administrativa')
    bullets(doc, [
        '**DGAV — «FAQ\'s para alojamentos de criação»**, versão de julho de 2025. Descreve o título de '
        'acesso, os documentos exigidos, o destinatário, a ausência de taxa e de vistoria de abertura, e '
        'os requisitos das instalações por remissão para o Decreto-Lei n.º 276/2001. **Não invoca em '
        'momento algum o Decreto-Lei n.º 314/2003, os limites por fogo ou a classificação do prédio.** '
        'Entre as exigências enumeradas contam-se instalações individualizadas para maternidade e criação '
        'até à idade adulta, quarentena e enfermaria; zonas separadas de armazenagem e manuseamento de '
        'alimentos; sistema de proteção contra incêndios com alarme de avaria; área de recreio coberta e '
        'descoberta; e inspeção diária.',
        '**Município do Porto** — serviço «Autorização de alojamento de animais em n.º superior ao '
        'previsto na lei». Dirige-se a proprietários de habitações em prédios urbanos e distingue '
        'expressamente as «situações de alojamento de animais, com ou sem fins comerciais», que carecem de '
        'título próprio.',
        '**Município do Cartaxo** — Regulamento n.º 181/2025, de 31 de janeiro, publicado no Diário da '
        'República, 2.ª série, n.º 22. O artigo 13.º reproduz o artigo 3.º e acrescenta-lhe apenas o '
        'procedimento — requerimento ao presidente da câmara e vistoria conjunta — e a sujeição a taxas. '
        '**Não o liga ao licenciamento de alojamentos.**',
        '**CIM do Alto Minho** — perguntas frequentes sobre animais de companhia. A questão é formulada '
        'como «Qual o número máximo de animais que é possível alojar **numa habitação**?». Nunca associa o '
        'limite à criação.',
    ])
    nota(doc, [
        '**Observação.** A prática administrativa é convergente e não cruza os dois planos. Não vale como '
        'fonte de direito, mas vale como prática reiterada da autoridade competente e dos municípios, e é '
        'elemento a ponderar na interpretação.'])

    # ------------------------------------------------------------------ 13
    h1(doc, '13.', 'A assimetria entre os n.ºs 2 e 4 e o critério matricial')
    para(doc,
         'O n.º 4 usa como critério a dimensão do terreno. O n.º 2 ignora o terreno por completo. Lido '
         'como teto predial, o n.º 2 faria a licitude depender da **inscrição matricial** — categorias dos '
         'artigos 2.º a 6.º do Código do Imposto Municipal sobre Imóveis, de natureza fiscal, sem qualquer '
         'conexão material com o bem jurídico protegido pelo n.º 1, que é a salubridade e a prevenção de '
         'doenças transmissíveis ao homem. Duas situações fisicamente idênticas — a mesma moradia, o mesmo '
         'quintal, os mesmos animais, as mesmas condições — teriam tratamento distinto consoante a '
         'inscrição na matriz.')
    destaque(doc, [
        'A leitura pelo fogo dissolve a assimetria. **O n.º 2 não é norma de capacidade do terreno; é '
        'norma sobre detenção doméstica.** Não compete com o n.º 4 porque regulam coisas diferentes — e a '
        'razão de o legislador ter usado critérios distintos é simples: o prédio rústico não tem, por '
        'definição, fogo. Para um estabelecimento, nenhum dos dois é a norma de lotação; é o anexo III.'])

    # ------------------------------------------------------------------ 14
    h1(doc, '14.', 'O caso residual')
    para(doc,
         'Resta a situação do titular de alojamento registado que mantém os animais integrados na casa, '
         'como animais do agregado, e não em instalações diferenciadas.')
    destaque(doc, [
        'Nessa hipótese **o n.º 2 aplica-se**, e o registo não o afasta. Acima de seis animais adultos '
        'dentro do fogo, a letra da lei não oferece caminho: a via do parecer vinculativo até seis é a '
        'única que o texto dá. O que desencadeia o n.º 2 é a habitação, não o registo.'])
    nota(doc, [
        'É o único ponto em que a resposta não é inteiramente segura e em que a interpretação contrária é '
        'sustentável. Não se conhece decisão judicial nem parecer publicado que o tenha resolvido. É '
        'também o ponto que uma revisão legislativa deve resolver por via expressa, em vez de o deixar à '
        'interpretação.'])

    # ------------------------------------------------------------------ 15
    pagebreak(doc)
    h1(doc, '15.', 'Pontos em aberto e limites da análise')
    numlist(doc, [
        'Não há decisão judicial, parecer publicado nem orientação administrativa que resolva '
        'expressamente a questão. A conclusão é interpretativa.',
        'O elemento textual mais incómodo é a al. c) do n.º 3 do artigo 14.º — «habitações **e terrenos '
        'anexos**». A resposta proposta é que essa alínea delimita o âmbito do artigo 3.º no seu conjunto, '
        'e que o n.º 1 alcança efetivamente o quintal; o que não faz é converter o «fogo» do n.º 2 em '
        '«prédio».',
        'Não se obtiveram as **tabelas do anexo III**, que as versões eletrónicas apresentam como «ver '
        'documento original». Seriam necessárias para demonstrar numericamente a lotação por superfície.',
        'Não foi consultado o **texto original do Diário da República de 17 de dezembro de 2003** em '
        'suporte oficial, nem o processo legislativo do Decreto-Lei n.º 315/2003, que poderia esclarecer a '
        'génese da ressalva da al. p).',
        'A pesquisa jurisprudencial cobre apenas os tribunais superiores. **Não cobre a primeira '
        'instância**, onde se decide a maior parte das impugnações de atos municipais, nem os processos de '
        'contraordenação decididos administrativamente. Ausência de casuística publicada não equivale a '
        'ausência de casos.',
        'Não se testou a hipótese de o alojamento estar em **fracção autónoma**, caso em que acrescem o '
        'n.º 3 do artigo 3.º e o regime da propriedade horizontal. Fica por analisar.',
    ])

    # ------------------------------------------------------------------ 16
    h1(doc, '16.', 'Nota metodológica')
    para(doc,
         'Os textos legais foram obtidos das versões consolidadas e confrontados com as cópias do '
         'repositório. A pesquisa de jurisprudência foi feita na base de dados pública dos tribunais '
         'superiores, nas bases das Relações de Lisboa, Porto, Guimarães, Évora e Coimbra, do Supremo '
         'Tribunal de Justiça, do Supremo Tribunal Administrativo e dos Tribunais Centrais Administrativos '
         'Sul e Norte.')
    nota(doc, [
        '**Armadilha do motor de pesquisa.** O motor daquela base devolve **zero resultados** quando se '
        'combina o operador «AND» com termos que contenham barra ou acentuação, ainda que existam '
        'documentos que satisfazem a consulta. Exemplo verificado: a pesquisa de «276/2001» combinada com '
        '«licença» devolveu zero, quando «276/2001» isolado devolveu trinta e seis. As pesquisas foram por '
        'isso feitas com termos simples e o cruzamento realizado sobre o texto integral das decisões '
        'descarregadas. Esta reserva é relevante para quem repita o trabalho.'])

    # ------------------------------------------------------------------ Anexo A
    pagebreak(doc)
    h1(doc, 'Anexo A', 'O artigo 3.º nunca foi alterado — verificação')
    para(doc,
         'A afirmação é verificável nas três versões oficiais do Decreto-Lei n.º 314/2003. O texto do '
         'artigo 3.º é idêntico, palavra por palavra, na redação originária de 17 de dezembro de 2003, na '
         'resultante do Decreto-Lei n.º 20/2019, de 30 de janeiro, e na versão em vigor.')
    tabela(doc,
           ['Versão', 'Diploma', 'Artigo 3.º'],
           [
            ['1.ª', 'Decreto-Lei n.º 314/2003, de 17 de dezembro', 'Redação originária'],
            ['2.ª', 'Decreto-Lei n.º 20/2019, de 30 de janeiro',
             '**Idêntico** — as alterações incidiram no n.º 2 do artigo 4.º e no artigo 14.º'],
            ['3.ª (em vigor)', 'Resolução da AR n.º 138/2019, de 8 de agosto',
             '**Idêntico** — fez cessar a vigência das normas alteradas pelo DL n.º 20/2019, '
             'repristinando a redação de 2003'],
           ],
           [Cm(2.6), Cm(6.4), Cm(7.6)])
    nota(doc, [
        'A verificação foi feita por extração do texto das três versões, isolamento do artigo 3.º e '
        'comparação: a assinatura MD5 do artigo é **idêntica nas três** — '
        '`745db9eaca77368cb870a4e84ae56b6c`. O artigo 3.º não figura em nenhum dos blocos de alteração '
        'do diploma.'])
    para(doc,
         'Em consequência, o n.º 3 para que remete a al. p) do n.º 1 do artigo 2.º do Decreto-Lei '
         'n.º 276/2001 é hoje o mesmo que era em 2003 — a regra do regulamento do condomínio. **A remissão '
         'não está desatualizada por efeito de renumeração**; está mal calibrada quanto ao seu alcance, '
         'pelas razões expostas no ponto 6.5.')

    # ------------------------------------------------------------------ Anexo B
    h1(doc, 'Anexo B', 'Quadro das normas citadas')
    tabela(doc,
           ['Norma', 'Diploma', 'Matéria'],
           [
            ['art.º 1.º', 'DL n.º 314/2003', 'Objeto — PNLVERAZ'],
            ['al. d) do art.º 2.º', 'DL n.º 314/2003',
             'Detentor — inclui reprodução e criação, com ou sem fins comerciais'],
            ['al. e) do art.º 2.º', 'DL n.º 314/2003', 'Animal de companhia — «no seu lar»'],
            ['n.ºs 1 a 6 do art.º 3.º', 'DL n.º 314/2003', 'Detenção de cães e gatos — limites por fogo'],
            ['n.º 1 do art.º 5.º', 'DL n.º 314/2003', 'Comércio — estabelecimentos'],
            ['al. c) do n.º 3 do art.º 14.º', 'DL n.º 314/2003',
             'Contraordenação — «habitações e terrenos anexos»'],
            ['al. f) do n.º 3 do art.º 14.º', 'DL n.º 314/2003',
             'Contraordenação — estabelecimentos de comércio'],
            ['n.º 1 do art.º 1.º', 'DL n.º 276/2001',
             'Âmbito — exploração de alojamentos, independentemente do fim'],
            ['al. n) do n.º 1 do art.º 2.º', 'DL n.º 276/2001', 'Alojamento'],
            ['al. p) do n.º 1 do art.º 2.º', 'DL n.º 276/2001', 'Hospedagem sem fins lucrativos — ressalva'],
            ['al. q) do n.º 1 do art.º 2.º', 'DL n.º 276/2001', 'Hospedagem com fins lucrativos'],
            ['al. v) do n.º 1 do art.º 2.º', 'DL n.º 276/2001', 'Detentor'],
            ['n.º 1 do art.º 3.º', 'DL n.º 276/2001', 'Títulos de acesso'],
            ['als. h) e j) do n.º 1 do art.º 3.º-A', 'DL n.º 276/2001',
             'Capacidade máxima declarada; declaração de cumprimento'],
            ['art.º 24.º', 'DL n.º 276/2001',
             'Destinatário do Cap. III; «sem prejuízo das demais disposições aplicáveis»'],
            ['n.ºs 1 a 5 do art.º 25.º', 'DL n.º 276/2001', 'Instalações individualizadas'],
            ['n.º 1 do art.º 27.º', 'DL n.º 276/2001', 'Dimensões mínimas — anexo III'],
            ['n.º 2 do art.º 67.º-A', 'DL n.º 276/2001', 'Acesso — «casas de habitação e terrenos privados»'],
            ['art.º 70.º', 'DL n.º 276/2001', 'Instrução e decisão dos processos de contraordenação'],
            ['arts. 2.º a 6.º', 'CIMI', 'Classificação predial — critério fiscal'],
            ['al. a) do n.º 2 do art.º 1083.º', 'Código Civil',
             'Resolução do arrendamento — higiene e vizinhança'],
           ],
           [Cm(4.6), Cm(3.4), Cm(8.2)])
