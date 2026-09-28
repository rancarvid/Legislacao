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
    para(doc,
         'Esta síntese é o resumo de leitura rápida do estudo. Cada ponto é autónomo e cabe num '
         'parágrafo, com remissão para o capítulo que o desenvolve. É atualizada sempre que uma das '
         'questões do capítulo 17 recebe resposta.')
    destaque(doc, [
        'Os limites do n.º 2 do artigo 3.º do Decreto-Lei n.º 314/2003 **não fixam a lotação de um '
        'alojamento registado** — mas por uma razão precisa, e com um caso residual em que a resposta é '
        'afirmativa.'])
    numlist(doc, [
        'A unidade de contagem do n.º 2 é o **fogo**, não o prédio. Onde não há fogo, a norma não tem '
        'campo operativo. Capítulo 5.',
        '«Fogo» é a **unidade de utilização destinada a habitação**, e não o agregado doméstico nem a '
        'fração autónoma. O Regime Jurídico da Urbanização e Edificação, em vigor, opõe «o número de '
        'fogos **e outras unidades de utilização**»: uma unidade cuja utilização não seja a habitação '
        'não é um fogo. Capítulo 5.',
        'Um alojamento registado não é um fogo: o artigo 25.º do Decreto-Lei n.º 276/2001 obriga-o a '
        'possuir **instalações individualizadas**, o que o diferencia necessariamente da habitação. '
        'Capítulo 7.',
        'O próprio Decreto-Lei n.º 276/2001 **prevê e regula os hotéis para animais** — al. q) do n.º 1 '
        'do artigo 2.º e n.º 4 do artigo 25.º —, exigindo-lhes instalações individualizadas. A licitude '
        'da hospedagem remunerada não depende, por isso, de um argumento de absurdidade: está na letra '
        'do diploma. Capítulo 8.',
        'Os **títulos de acesso** às atividades com animais deixaram de ser municipais. A guarda '
        'remunerada e a criação comercial passaram a mera comunicação prévia à DGAV; o comércio a '
        'retalho passou ao regime do Decreto-Lei n.º 10/2015. A autorização municipal do artigo 2.º da '
        'Lei n.º 92/95 subsiste apenas quanto a atividades que não são de alojar, pelo que não é via de '
        'entrada dos limites do artigo 3.º. Capítulo 13.',
        'A **única ponte expressa** entre os dois diplomas é a al. p) do n.º 1 do artigo 2.º do '
        'Decreto-Lei n.º 276/2001, acrescentada pelo Decreto-Lei n.º 315/2003 no mesmo Diário da '
        'República em que saiu o Decreto-Lei n.º 314/2003. Exclui do conceito de hospedagem sem fins '
        'lucrativos o alojamento em fração autónoma — o único espaço onde a diferenciação material é '
        'impossível. Tendo o legislador cruzado os dois diplomas uma única vez e para efeito tão '
        'estreito, o silêncio quanto à lotação é qualificado. Capítulo 14.',
        'O **n.º 4** do artigo 3.º, para prédios rústicos e mistos, não fixa número: seis animais, «podendo '
        'tal número ser excedido se a dimensão do terreno o permitir», sem teto e sem autorização '
        'prévia. Uma norma que não fixa número não pode ser a norma de lotação de um estabelecimento. '
        'O artigo 3.º gradua densidade doméstica; a capacidade dos alojamentos mede-se pelo anexo III. '
        'Capítulo 15.',
        'No artigo 3.º, «alojamento» é o **facto de alojar**, não o estabelecimento: sete das nove '
        'ocorrências no diploma têm esse sentido, e a decisiva está na própria norma dos limites — '
        '«for autorizado alojamento até ao máximo de seis animais adultos». Daqui resulta que o artigo '
        'alcança quem quer que aloje, incluindo o titular de alojamento registado; o que o mantém fora '
        'dos números é a unidade de contagem, não a palavra. Capítulo 9.',
        'A **coima** do artigo 3.º só existe dentro de casa: a al. c) do n.º 3 do artigo 14.º tipifica '
        'a permanência de animais «em habitações e terrenos anexos», e o tipo não pode ser alargado. '
        'Fora daí resta o remédio administrativo do n.º 5. Capítulo 9.',
        'O **n.º 1** do artigo 3.º — dever geral de salubridade — **aplica-se sempre**, incluindo ao '
        'alojamento registado. Registar não isenta; a al. j) do n.º 1 do artigo 3.º-A obriga o '
        'interessado a declarar o cumprimento de toda a legislação aplicável em matéria de higiene.',
        '**Caso residual.** Quem tem o alojamento registado mas mantém os animais integrados na casa, '
        'como animais do agregado, continua sujeito ao n.º 2. O registo não cria, por si, caminho acima '
        'de seis animais dentro do fogo. Capítulo 16.',
    ])
    nota(doc, [
        'Não se localizou decisão judicial, parecer publicado nem orientação administrativa que resolva '
        'expressamente a questão. A conclusão é interpretativa e o capítulo 17 declara os seus limites e '
        'enumera as questões ainda por responder.'])

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
         'O artigo 3.º transcreve-se na íntegra, por ser a peça central da questão. O ponto 18 demonstra '
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

    h2(doc, '4.3', 'Lei n.º 92/95, de 12 de setembro, e Decreto-Lei n.º 10/2015, de 16 de janeiro')
    citacao(doc,
            ['Sem prejuízo do disposto no capítulo III quanto aos animais de companhia, qualquer pessoa '
             'física ou colectiva que explore o comércio de animais, que guarde animais mediante uma '
             'remuneração, que os crie para fins comerciais, que os alugue, que se sirva de animais para '
             'fins de transporte, que os exponha ou que os exiba com um fim comercial só poderá fazê-lo '
             'mediante autorização municipal, a qual só poderá ser concedida desde que os serviços '
             'municipais verifiquem que as condições previstas na lei destinadas a assegurar o bem-estar '
             'e a sanidade dos animais serão cumpridas.'],
            'Artigo 2.º da Lei n.º 92/95, sob a epígrafe «Licença municipal»')
    para(doc,
         'O artigo 4.º do Decreto-Lei n.º 10/2015 enumera as atividades sujeitas a mera comunicação '
         'prévia. Entre elas, na al. c) do seu n.º 1:')
    citacao(doc,
            ['c) A exploração de estabelecimentos de comércio a retalho de animais de companhia e '
             'respetivos alimentos, em estabelecimentos especializados;'],
            'Al. c) do n.º 1 do artigo 4.º do Decreto-Lei n.º 10/2015')
    citacao(doc,
            ['1 - As meras comunicações prévias referidas nas alíneas a) a c) e g) a m) do artigo 4.º, '
             'são apresentadas ao município territorialmente competente através do «Balcão do '
             'empreendedor», nos termos do artigo 20.º, devendo, para efeitos de reporte estatístico, ser '
             'remetidas de imediato para a Direção-Geral das Atividades Económicas (DGAE).'],
            'N.º 1 do artigo 7.º do Decreto-Lei n.º 10/2015')

    # ------------------------------------------------------------------ 5
    pagebreak(doc)
    h1(doc, '5.', 'O conceito de «fogo»')
    destaque(doc, [
        '«Fogo» é a **unidade de utilização destinada a habitação**. Não é o agregado doméstico nem a '
        'fração autónoma. E o apoio mais seguro desta noção já não é o Regulamento Geral das Edificações '
        'Urbanas, de 1951, mas o Regime Jurídico da Urbanização e Edificação, na redação em vigor.'])

    h2(doc, '5.1', 'O que o diploma não diz')
    para(doc,
         'O Decreto-Lei n.º 314/2003 não define «fogo». Mais: a palavra aparece **uma única vez em todo o '
         'diploma**, no n.º 2 do artigo 3.º. Não há remissão para outro regime, nem norma interpretativa. '
         'O conceito tem de ser colhido fora.')

    h2(doc, '5.2', 'A âncora histórica: o Regulamento Geral das Edificações Urbanas')
    citacao(doc,
            ['5. O tipo de fogo é definido pelo número de quartos de dormir, e para a sua identificação '
             'utiliza-se o símbolo Tx, em que x representa o número de quartos de dormir.'],
            'N.º 5 do artigo 66.º do RGEU, na redação do Decreto-Lei n.º 650/75, de 18 de novembro')
    citacao(doc,
            ['a) Área bruta (Ab) é a superfície total do fogo, medida pelo perímetro exterior das paredes '
             'exteriores e eixos das paredes separadoras dos fogos, e inclui varandas privativas, locais '
             'acessórios e a quota-parte que lhe corresponda nas circulações comuns do edifício;',
             'b) Área útil (Au) é a soma das áreas de todos os compartimentos da habitação, incluindo […]'],
            'Als. a) e b) do n.º 2 do artigo 67.º do RGEU')
    para(doc,
         'A sinonímia entre «fogo» e «habitação» não é afirmada: é demonstrada pelo próprio texto. A al. '
         'a) mede «o fogo»; a al. b), imediatamente a seguir e para o mesmo objeto, mede «a habitação». '
         'São a mesma coisa.')

    h2(doc, '5.3', 'A âncora vigente: o Regime Jurídico da Urbanização e Edificação')
    para(doc,
         'O Regime Jurídico da Urbanização e Edificação, aprovado pelo Decreto-Lei n.º 555/99, de 16 de '
         'dezembro, na redação dada pelo Decreto-Lei n.º 108/2026, de 29 de maio, usa a palavra com '
         'sentido firme e atual. Dois lugares bastam.')
    citacao(doc,
            ['a) Na parcela destacada só seja construído edifício que se destine exclusivamente a fins '
             'habitacionais e que não tenha mais de dois fogos;'],
            'Al. a) do n.º 5 do artigo 6.º do RJUE')
    citacao(doc,
            ['c) Programa de utilização das edificações, incluindo a área total de construção a afetar aos '
             'diversos usos e o número de fogos e outras unidades de utilização, com identificação das '
             'áreas acessórias, técnicas e de serviço;'],
            'Al. c) do n.º 2 do artigo 14.º do RJUE')
    destaque(doc, [
        'A expressão «o número de fogos **e outras unidades de utilização**» é decisiva. O fogo é a '
        'espécie habitacional do género «unidade de utilização». Uma unidade cuja utilização não seja a '
        'habitação **não é um fogo** — é uma das «outras unidades de utilização».'])

    h2(doc, '5.4', 'O RGEU está em vigor, mas por um fio')
    para(doc,
         'O artigo 25.º do Decreto-Lei n.º 10/2024, de 8 de janeiro, na sua redação originária, dispunha '
         'que «o RGEU é revogado com efeitos reportados a 1 de junho de 2026». Na véspera dessa data o '
         'Governo travou a revogação.')
    citacao(doc,
            ['1 — O RGEU é revogado com efeitos reportados à data de entrada em vigor do diploma que '
             'definir as normas técnicas aplicáveis à edificação.',
             '2 — A regulamentação prevista no número anterior deve contar com a colaboração das ordens '
             'profissionais competentes na definição das regras de ordem técnica que considerem adequadas '
             'para a preparação dos projetos relativos às edificações urbanas.'],
            'Artigo 25.º do Decreto-Lei n.º 10/2024, na redação do Decreto-Lei n.º 108/2026, de 29 de maio')
    nota(doc, [
        '**Cronologia.** O Decreto-Lei n.º 108/2026 foi publicado em 29 de maio de 2026, sexta-feira, e o '
        'seu artigo final determina que «as alterações ao Decreto-Lei n.º 10/2024, de 8 de janeiro, '
        'entram em vigor no primeiro dia útil seguinte ao da publicação do presente decreto-lei» — isto '
        'é, 1 de junho de 2026, o próprio dia em que a revogação produziria efeitos. **O RGEU está, '
        'pois, em vigor**, e a sua revogação passou a depender de um diploma futuro, ainda não publicado.'])
    destaque(doc, [
        'Consequência metodológica: uma análise que assente exclusivamente no RGEU fica refém de um '
        'diploma que pode sair a qualquer momento. Por isso o peso da demonstração desloca-se para o '
        'RJUE, que está em vigor e foi revisto há meses.'])

    h2(doc, '5.5', 'As três leituras, e qual se sustenta')
    tabela(doc,
           ['Leitura', 'Conteúdo', 'Apreciação'],
           [['Unidade de utilização habitacional',
             'Critério físico-edificado, colhido no RGEU e no RJUE: o fogo é a unidade de utilização '
             'destinada a habitação.',
             '**Procede.** É a única com apoio em direito positivo vigente'],
            ['Fração autónoma',
             'O n.º 3 do artigo 3.º pressupõe que cada fração tem limite próprio, ao permitir que o '
             'regulamento do condomínio o reduza.',
             'Improcede como definição: uma fração autónoma pode ser uma loja, uma garagem ou um '
             'escritório. Toda a fração habitacional é um fogo; nem todo o fogo é uma fração'],
            ['Agregado doméstico',
             'Economia comum, independentemente do edificado.',
             'Improcede: nenhum texto legal o sustenta, e havendo critério objetivo edificado não há '
             'razão para preferir um critério pessoal']],
           [Cm(3.6), Cm(6.4), Cm(6.6)])

    h2(doc, '5.6', 'Quatro consequências operativas')
    numlist(doc, [
        '**A unidade de contagem do n.º 2 é doméstica, não predial.** Um prédio urbano com dez fogos '
        'comporta dez vezes a dotação. O limite não é do prédio; é de cada fogo.',
        '**Um prédio urbano sem fogo não tem unidade a que aplicar o n.º 2.** A norma não tem, aí, campo '
        'operativo — não porque se afaste, mas porque lhe falta o termo de referência.',
        '**É o título de utilização que decide.** A autorização de utilização diz a que se destina cada '
        'unidade. Uma unidade licenciada para outro uso que não a habitação é, na linguagem do RJUE, uma '
        '«outra unidade de utilização», e não um fogo.',
        '**O Decreto-Lei n.º 276/2001 nunca usa a palavra.** A sua unidade é o alojamento, cuja '
        'capacidade é declarada pelo interessado e aferida por superfície.',
    ])
    nota(doc, [
        '**Nota de pesquisa.** Não se localizou qualquer iniciativa legislativa parlamentar que tenha '
        'incidido sobre o artigo 3.º do Decreto-Lei n.º 314/2003. As iniciativas que alteram esse diploma '
        '— designadamente as do PAN sobre animais comunitários e esterilização — versam sobre os artigos '
        '8.º e 11.º, relativos a animais errantes. Em mais de vinte anos, o artigo 3.º nunca foi objeto '
        'de debate parlamentar, o que ajuda a explicar a ausência de doutrina e de jurisprudência.'])

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
    h1(doc, '9.', 'Ponderação: o sentido de «alojamento» e o peso dos elementos')

    h2(doc, '9.1', 'O que a palavra «alojamento» significa no artigo 3.º')
    para(doc,
         'O ponto 6.1 registou, entre os elementos favoráveis à aplicação, que o artigo 3.º emprega a '
         'mesma palavra que define o objeto do Decreto-Lei n.º 276/2001. O argumento merece resposta '
         'direta, e a resposta obtém-se contando. A palavra e os seus derivados ocorrem **nove vezes** em '
         'todo o Decreto-Lei n.º 314/2003.')
    tabela(doc,
           ['Onde', 'Texto', 'Sentido'],
           [['N.º 1 do art.º 3.º', '«O alojamento de cães e gatos em prédios urbanos, rústicos ou mistos»',
             'Contestado'],
            ['N.º 2 do art.º 3.º', '«podem ser alojados até três cães ou quatro gatos adultos»', 'Facto'],
            ['N.º 2 do art.º 3.º', '«for autorizado alojamento até ao máximo de seis animais adultos»',
             '**Facto**'],
            ['N.º 4 do art.º 3.º', '«podem ser alojados até seis animais adultos»', 'Facto'],
            ['N.º 4 do art.º 3.º', '«as condições de alojamento»', 'Facto'],
            ['Art.º 6.º', '«ficam obrigados a quarentena em alojamento autorizado para o efeito»',
             '**Lugar**'],
            ['Art.º 6.º', '«ou pelo alojamento em canil ou gatil, preferencialmente oficial»', 'Facto'],
            ['N.º 2 do art.º 9.º', '«todas as despesas de alimentação e alojamento»', 'Facto'],
            ['N.º 3 do art.º 9.º',
             '«as condições exigidas pelo presente diploma para o seu alojamento»', 'Facto']],
           [Cm(3.4), Cm(9.4), Cm(3.8)])
    para(doc,
         'Sete das nove ocorrências são o facto de alojar. Uma — a quarentena do artigo 6.º — é '
         'inequivocamente o lugar. E a contestada é a do n.º 1.')
    destaque(doc, [
        'A ocorrência decisiva está **dentro da própria norma dos limites**: o n.º 2 prevê que «for '
        'autorizado alojamento até ao máximo de seis animais adultos». Não se autoriza um edifício «até '
        'ao máximo de seis animais»; autoriza-se o **alojar** de até seis. No artigo 3.º, a palavra é o '
        'facto.'])
    bullets(doc, [
        '**A epígrafe confirma-o.** O artigo 3.º intitula-se «Detenção de cães e gatos» — uma conduta. '
        'Compare-se com os capítulos do Decreto-Lei n.º 276/2001, que se intitulam «Normas para os '
        'alojamentos de...». Quando o legislador quer regular estabelecimentos, di-lo na epígrafe.',
        '**A norma sancionatória usa outro vocábulo ainda.** A al. c) do n.º 3 do artigo 14.º tipifica «a '
        'permanência de cães e gatos em habitações e terrenos anexos» — um estado, situado em habitações.',
        '**E o diploma nunca chama «alojamento» a uma instalação de acolhimento.** Quando se refere a '
        'uma, diz «canil ou gatil municipal», «canis e gatis», «instalações» ou «estabelecimentos».',
    ])
    para(doc,
         'Quanto ao argumento do vocabulário comum, ele cai por inteiro: o próprio Decreto-Lei n.º '
         '276/2001 usa a palavra nos dois sentidos, e em alíneas consecutivas. A al. n) do n.º 1 do artigo '
         '2.º define «alojamento» como «qualquer instalação, edifício, grupo de edifícios ou outro local»; '
         'a al. o), imediatamente a seguir, define «hospedagem» como «o alojamento, permanente ou '
         'temporário, de um animal de companhia». Lugar numa linha, facto na seguinte.')

    h2(doc, '9.2', 'O que esta resposta entrega, e o que não entrega')
    destaque(doc, [
        'A questão 5 resolve-se **contra** este estudo num ponto e a favor noutro, e é preciso dizê-lo '
        'com clareza. Se o artigo 3.º regula o facto de alojar, então regula-o **seja quem for quem '
        'aloja** — incluindo o titular de um alojamento registado. A palavra não afasta o '
        'estabelecimento.'])
    para(doc,
         'O que mantém o estabelecimento fora dos números não é o vocábulo: é a **unidade de contagem**. '
         'O n.º 2 conta por fogo, e um alojamento não é um fogo, pelas razões do capítulo 5. O n.º 1, '
         'esse, aplica-se a toda a gente, incluindo ao alojamento registado — e é exatamente isso que '
         'este estudo afirma desde as conclusões.')
    destaque(doc, [
        'Toda a conclusão repousa, portanto, na **questão 4** — no conceito de fogo —, e não na palavra '
        '«alojamento». Quem quiser atacar a tese deste estudo deve atacar ali, e não aqui.'])

    h2(doc, '9.3', 'O alcance da norma sancionatória')
    para(doc,
         'Das sete alíneas do n.º 3 do artigo 14.º, só uma remete para o artigo 3.º, e é o único lugar do '
         'diploma onde o objeto desse artigo é nomeado.')
    citacao(doc,
            ['c) A permanência de cães e gatos em habitações e terrenos anexos em desrespeito pelas '
             'condições previstas no artigo 3.º;'],
            'Al. c) do n.º 3 do artigo 14.º do Decreto-Lei n.º 314/2003')

    h3(doc, 'A redação é a original, e sobreviveu a uma intervenção parlamentar')
    para(doc,
         'O artigo 14.º foi alterado pelo Decreto-Lei n.º 20/2019, de 30 de janeiro, que transferiu '
         'competências para os órgãos municipais no domínio da proteção animal, e pela Resolução da '
         'Assembleia da República n.º 138/2019, de 8 de agosto, que fez **cessar a vigência** daquele '
         'decreto-lei. Impunha-se verificar qual o texto hoje aplicável.')
    destaque(doc, [
        'Conferida no Diário da República n.º 290, I série-A, de 17 de dezembro de 2003, a al. c) tem '
        'hoje **exatamente a redação originária**. Nunca foi alterada, e o seu teor atravessou incólume a '
        'única intervenção parlamentar que o artigo conheceu. Não é texto descuidado: é texto deliberado '
        'e reconfirmado.'])

    h3(doc, 'O tipo não pode ser alargado')
    citacao(doc,
            ['Só será punido como contra-ordenação o facto descrito e declarado passível de coima por lei '
             'anterior ao momento da sua prática.'],
            'Artigo 2.º do Regime Geral das Contra-Ordenações, aprovado pelo Decreto-Lei n.º 433/82, de '
            '27 de outubro, conferido no Diário da República n.º 249, I série, a páginas 3553')
    para(doc,
         'Seja qual for o âmbito da norma de conduta, o âmbito do **tipo** é o que a al. c) descreve. Não '
         'há punição por analogia nem extensão do tipo a espaços que ele não nomeia.')

    h3(doc, 'Duas palavras que decidem: «anexos» e «permanência»')
    bullets(doc, [
        '**«Anexos» é relacional.** Anexo pressupõe um principal, e o principal que a norma nomeia é a '
        'habitação. Um alojamento dotado das instalações individualizadas que o artigo 25.º do '
        'Decreto-Lei n.º 276/2001 exige não é «terreno anexo» a uma habitação: é coisa distinta dela. O '
        'texto mais incómodo para este estudo, lido com atenção, situa o objeto sancionado na casa e no '
        'seu redor imediato.',
        '**«Permanência» é um estado, não uma atividade.** O legislador não tipificou «a exploração», «o '
        'funcionamento» ou «o alojamento» — tipificou o facto de os animais lá estarem.',
    ])

    h3(doc, 'As duas leituras conciliam-se')
    tabela(doc,
           ['Leitura', 'Consequência'],
           [['O tipo é mais estreito do que a norma de conduta',
             'Fora das habitações o artigo 3.º seria norma imperfeita, sem sanção'],
            ['O tipo revela o âmbito da norma de conduta',
             'O artigo 3.º só alcançaria habitações e terrenos anexos']],
           [Cm(6.4), Cm(10.2)])
    destaque(doc, [
        'A conciliação está no **n.º 5 do artigo 3.º**, que dá um remédio administrativo — vistoria '
        'conjunta e notificação para remoção — **sem o limitar a habitações**. O legislador usou '
        'deliberadamente dois alcances: remédio administrativo em todo o campo da norma, coima apenas na '
        'habitação e no seu anexo. Não é lapso; é arquitetura.'])
    nota(doc, [
        '**Observação, sem atenuação.** Isto confirma que o artigo 3.º foi pensado a partir da casa, mas '
        '**não** exclui que a norma de conduta alcance mais — como o ponto 9.1 demonstrou, ela alcança '
        'quem quer que aloje. O que a al. c) revela é onde o legislador entendeu que valia a pena punir, '
        'não onde entendeu que a norma se aplica. A consequência prática desta assimetria está tratada '
        'nos pontos 15.5 e 15.7.'])

    h2(doc, '9.4', 'O peso das duas séries de elementos')
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
             'Hipótese **não analisada** neste estudo — ver ponto 17'],
            ['Qualquer das anteriores', '—',
             '**N.º 1 aplica-se sempre**: boas condições e ausência de riscos hígio-sanitários'],
           ],
           [Cm(5.0), Cm(4.0), Cm(7.6)])
    nota(doc, [
        '**Precisão quanto ao logradouro.** O logradouro de uma moradia integra o prédio urbano e não '
        'converte o conjunto em prédio misto, pelo que a área do quintal é juridicamente irrelevante para '
        'o n.º 2. O ponto 15.4 desenvolve-o.'])

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
    pagebreak(doc)
    h1(doc, '13.', 'Os títulos de acesso às atividades e a autorização municipal')
    para(doc,
         'A Lei n.º 92/95 sujeitou, em 1995, sete atividades a um único título municipal de controlo '
         'prévio: explorar o comércio de animais, guardá-los mediante remuneração, criá-los para fins '
         'comerciais, alugá-los, servir-se deles para transporte, expô-los ou exibi-los com fim '
         'comercial. Interessa saber o que resta dessa norma, porque uma autorização municipal cujo '
         'pressuposto é a verificação das «condições previstas na lei destinadas a assegurar o bem-estar '
         'e a sanidade dos animais» seria via possível de entrada dos limites do artigo 3.º no regime dos '
         'alojamentos.')

    h2(doc, '13.1', 'Três deslocamentos sucessivos')
    numlist(doc, [
        '**A guarda remunerada e a criação comercial passaram para a DGAV.** A al. a) do n.º 1 do artigo '
        '3.º do Decreto-Lei n.º 276/2001, na redação do Decreto-Lei n.º 260/2012, sujeita a mera '
        'comunicação prévia os centros de recolha, os alojamentos para hospedagem e a criação comercial '
        'de animais de companhia; a al. b) sujeita a permissão administrativa a criação de animais '
        'potencialmente perigosos. A comunicação é dirigida à DGAV através do balcão único eletrónico. O '
        'município saiu do procedimento.',
        '**O comércio a retalho passou para o regime das atividades económicas.** A al. c) do n.º 1 do '
        'artigo 4.º do Decreto-Lei n.º 10/2015 sujeita a exploração de estabelecimentos de comércio a '
        'retalho de animais de companhia a mera comunicação prévia, dirigida ao município através do '
        '«Balcão do empreendedor», nos termos do n.º 1 do artigo 7.º. O município continua destinatário, '
        'mas deixou de autorizar: passou a ser notificado. A diferença não é de forma — o controlo '
        'prévio desapareceu.',
        '**Os dois regimes foram encaixados, não sobrepostos.** A al. a) do n.º 1 do artigo 3.º do '
        'Decreto-Lei n.º 276/2001 exclui expressamente da comunicação à DGAV os alojamentos destinados '
        'exclusivamente à venda, precisamente porque estes caem no regime anterior.',
    ])
    citacao(doc,
            ['O funcionamento das lojas de animais não depende de mera comunicação prévia junto da DGAV, '
             'estando aquele sujeito às normas previstas no regime jurídico de acesso e exercício de '
             'atividades de comércio, serviços e restauração.'],
            'DGAV, Esclarecimento n.º 4/2018 sobre a Lei n.º 95/2017, junho de 2018')

    h2(doc, '13.2', 'O que subsiste do artigo 2.º')
    para(doc,
         'Três das sete atividades: o aluguer de animais, o servir-se deles para fins de transporte e a '
         'sua exposição ou exibição com fim comercial. Nenhuma tem outro título de acesso, e aí o artigo '
         '2.º opera sozinho. Nenhuma delas é, porém, uma atividade de **alojar** — o artigo 3.º do '
         'Decreto-Lei n.º 314/2003 não tem aí objeto sobre que incidir.')

    h2(doc, '13.3', 'Vigência formal e revogação tácita parcial')
    para(doc,
         'A construção assenta em duas normas, e não em argumento próprio. Quanto à paridade de valor, o '
         'n.º 2 do artigo 112.º da Constituição, na redação da Lei Constitucional n.º 1/2005, dispõe que '
         '«as leis e os decretos-leis têm igual valor, '
         'sem prejuízo da subordinação às correspondentes leis dos decretos-leis publicados no uso de '
         'autorização legislativa e dos que desenvolvam as bases gerais dos regimes jurídicos». A Lei n.º '
         '92/95 foi aprovada ao abrigo da competência legislativa comum — o preâmbulo invoca os artigos '
         '164.º, alínea d), e 169.º, n.º 3, da Constituição na numeração anterior à revisão de 1997 — e '
         'não é lei de valor reforçado. Um decreto-lei posterior pode, pois, derrogá-la.')
    citacao(doc,
            ['2 - A revogação pode resultar de declaração expressa, da incompatibilidade entre as novas '
             'disposições e as regras precedentes ou da circunstância de a nova lei regular toda a '
             'matéria da lei anterior.'],
            'N.º 2 do artigo 7.º do Código Civil, conferido no Diário do Governo n.º 274, I série, de '
            '25 de novembro de 1966, a páginas 1886')
    para(doc,
         'São as duas últimas hipóteses que relevam: substituir o controlo prévio municipal por mera '
         'comunicação prévia é incompatível com a exigência de autorização, e o Decreto-Lei n.º 10/2015 '
         'regula toda a matéria do acesso àquela atividade. O artigo 2.º nunca foi expressamente '
         'revogado, e a Assembleia da República voltou ao diploma em 2002, 2014, 2020 e 2022 sem lhe '
         'tocar.')
    destaque(doc, [
        'A construção defensável é a de **revogação tácita parcial por incompatibilidade**: a norma '
        'subsiste, mas o seu objeto foi sendo ocupado por regimes especiais posteriores, restando-lhe o '
        'que estes não ocuparam. Não sendo o título dos alojamentos municipal, a autorização do artigo '
        '2.º não é via por onde os limites do artigo 3.º possam entrar no regime dos alojamentos '
        'registados. **Efeito na questão central: neutro.**'])
    nota(doc, [
        '**Ressalva.** O município não desapareceu do regime. Continua a ser autoridade competente para '
        'efeitos do Decreto-Lei n.º 276/2001, nos termos da al. x) do n.º 1 do artigo 2.º, e detém o '
        'poder do n.º 5 do artigo 3.º do Decreto-Lei n.º 314/2003. Mas isso é fiscalização, não '
        'titulação. **Por confirmar:** se algum município ainda pratica autorizações ao abrigo do artigo '
        '2.º, e se existe jurisprudência sobre esta derrogação. Nada foi localizado. Não se localizou '
        'doutrina que trate especificamente desta derrogação; o raciocínio é próprio, embora as premissas '
        'normativas sejam as citadas.'])

    # ------------------------------------------------------------------ 14
    pagebreak(doc)
    h1(doc, '14.', 'A remissão da al. p) do n.º 1 do artigo 2.º do Decreto-Lei n.º 276/2001')
    destaque(doc, [
        'A remissão é **coerente e deliberada**, e não um lapso. O seu efeito é o inverso do que aparenta: '
        'reforça a conclusão de que os limites por fogo não fixam a lotação dos alojamentos registados.'])

    h2(doc, '14.1', 'A génese, documentada')
    para(doc,
         'A remissão não existia em 2001. No Diário da República n.º 241, de 17 de outubro de 2001, a '
         'alínea lia-se apenas:')
    citacao(doc,
            ['p) «Hospedagem sem fins lucrativos» alojamento, permanente ou temporário, de animais de '
             'companhia que não vise a obtenção de rendimentos;'],
            'Al. p) do artigo 2.º do Decreto-Lei n.º 276/2001, texto original de 17.10.2001')
    para(doc,
         'A ressalva foi acrescentada pelo **Decreto-Lei n.º 315/2003, de 17 de dezembro**, que alterou o '
         'artigo 2.º do Decreto-Lei n.º 276/2001. Esse diploma foi publicado no **Diário da República '
         'n.º 290, de 17 de dezembro de 2003 — o mesmo número em que foi publicado o Decreto-Lei n.º '
         '314/2003**. São diplomas gémeos, saídos juntos.')
    citacao(doc,
            ['p) «Hospedagem sem fins lucrativos», alojamento, permanente ou temporário, de animais de '
             'companhia que não vise a obtenção de rendimentos, com excepção das referidas no n.º 3 do '
             'artigo 3.º do diploma que aprova o Plano Nacional de Luta e Vigilância da Raiva Animal e '
             'outras Zoonoses;'],
            'Al. p) do n.º 1 do artigo 2.º do Decreto-Lei n.º 276/2001, na redação do Decreto-Lei '
            'n.º 315/2003')
    para(doc,
         'O referente só pode ser o Decreto-Lei n.º 314/2003. O Decreto-Lei n.º 91/2001, de 23 de março, '
         'que aquele revogou, tem no artigo 3.º uma norma de definições com alíneas e sem números, pelo '
         'que não tem n.º 3; e a Portaria n.º 81/2002, de 24 de janeiro, tem no artigo 3.º a vacinação '
         'anti-rábica em regime de campanha, com dois números apenas. Nenhum dos dois comporta a '
         'remissão.')
    nota(doc, [
        '**Designação usada.** A alínea fala em «Plano Nacional de Luta e Vigilância da Raiva Animal e '
        'outras Zoonoses». O Decreto-Lei n.º 314/2003 chama-lhe «Programa Nacional de Luta e Vigilância '
        '**Epidemiológica** da Raiva Animal e Outras Zoonoses». A designação da alínea é a do vocabulário '
        'de 2001, que oscilava entre «Plano» e «Programa» dentro do próprio Decreto-Lei n.º 91/2001. É '
        'desleixo de redação, não vício de remissão.'])

    h2(doc, '14.2', 'As duas leituras possíveis')
    para(doc,
         'O n.º 3 do artigo 3.º do Decreto-Lei n.º 314/2003 dispõe: «No caso de fracções autónomas em '
         'regime de propriedade horizontal, o regulamento do condomínio pode estabelecer um limite de '
         'animais inferior ao previsto no número anterior.»')
    tabela(doc,
           ['Leitura', 'Conteúdo', 'Efeito'],
           [['Gramatical',
             '«As referidas» são as **fracções autónomas** — único plural feminino da norma remetida. A '
             'al. p) exclui do conceito de hospedagem sem fins lucrativos o alojamento em fração '
             'autónoma.',
             'Aplica'],
            ['Lapso de numeração',
             'Pretendia-se remeter para o n.º 2, excluindo do conceito a detenção doméstica dentro dos '
             'limites. Teleologicamente atraente, mas sem antecedente feminino plural.',
             'Não aplica']],
           [Cm(2.6), Cm(10.4), Cm(3.0)])
    destaque(doc, [
        'A conclusão resiste às duas leituras. Na primeira, a remissão é uma exclusão cirúrgica de um '
        'tipo de espaço. Na segunda, a al. p) afirma que abaixo do limite há lar e acima há hospedagem — '
        'o que também afasta a aplicação dos números à lotação.'])

    h2(doc, '14.3', 'Por que razão só a hospedagem sem fins lucrativos')
    para(doc,
         'O Decreto-Lei n.º 315/2003 alterou a al. p) e deixou a al. q) intacta. A assimetria tem '
         'explicação, e não é o favorecimento do comércio.')
    bullets(doc, [
        'A al. q) define-se **pela positiva** e é auto-limitada: exige que o alojamento «vise interesses '
        'comerciais ou lucrativos», o que uma casa particular nunca satisfaz.',
        'A al. p) define-se **pela negativa** — «que não vise a obtenção de rendimentos» — e, sem '
        'ressalva, abrange literalmente todos os lares: manter animais em casa, em permanência, sem '
        'auferir rendimento, é exatamente isso. Era esta definição, e só ela, que estava sem chão.',
        'O chão dado não foi «a habitação» em geral, foi a **fração autónoma** — precisamente o espaço '
        'onde a diferenciação material é impossível. Numa moradia com logradouro podem construir-se as '
        'instalações individualizadas do artigo 25.º; num apartamento não podem. O critério da exclusão '
        'acompanha a possibilidade de separação física, que é o critério do próprio artigo 25.º.',
    ])
    para(doc,
         'Quanto à função, a al. p) fecha uma via de fuga. Sem ela, quem tivesse vinte cães num '
         'apartamento poderia sustentar que não é detentor doméstico sujeito ao n.º 2 do artigo 3.º do '
         'Decreto-Lei n.º 314/2003, mas titular de um alojamento de hospedagem sem fins lucrativos ao '
         'abrigo do Decreto-Lei n.º 276/2001, e reclamar licença nessa qualidade. O legislador de 17 de '
         'dezembro de 2003 tapou essa via no mesmo dia em que publicou os limites por fogo. Para a '
         'hospedagem lucrativa nada havia a tapar: a licença de funcionamento, com parecer da DRA, e os '
         'requisitos do artigo 25.º já filtravam os apartamentos.')
    nota(doc, [
        '**Observação.** O preâmbulo do Decreto-Lei n.º 315/2003 nada diz sobre este ponto. Declara três '
        'propósitos: retirar do Decreto-Lei n.º 276/2001 as normas sobre animais potencialmente '
        'perigosos, «proceder a rectificações ao seu texto, o qual foi publicado com algumas '
        'inexactidões», e «acrescentar aspectos que reforçam as normas de bem-estar dos animais de '
        'companhia». O que fica dito em 14.3 é inferência a partir do texto e do contexto, não intenção '
        'documentada.'])

    h2(doc, '14.4', 'O argumento decisivo')
    destaque(doc, [
        'A remissão prova que o legislador **sabia cruzar os dois diplomas e sabia como se faz**. Fê-lo '
        'expressamente uma única vez, para um efeito estreitíssimo, e não o fez para aquilo que '
        'verdadeiramente importaria — mandar os números do n.º 2 valerem como lotação dos alojamentos. '
        'Onde o legislador falou uma vez e calou no resto, o silêncio é qualificado.'])
    nota(doc, [
        'Não se localizou doutrina, jurisprudência nem parecer que se debruce sobre esta remissão. A '
        'revisão crítica legislativa da Associação Portuguesa de Médicos Veterinários Especialistas em '
        'Animais de Companhia, de abril de 2021, percorre ambos os diplomas e trata do artigo 3.º do '
        'Decreto-Lei n.º 314/2003 e das definições do Decreto-Lei n.º 276/2001, mas não a menciona.'])

    # ------------------------------------------------------------------ 15
    h1(doc, '15.', 'Os prédios rústicos e mistos: a assimetria dos n.ºs 2 e 4')
    destaque(doc, [
        'O n.º 4 é, à primeira vista, o melhor argumento a favor da aplicação dos limites aos '
        'estabelecimentos — gradua o número pelo espaço, que é a lógica das normas de lotação. Mas é '
        'também o que a destrói: **uma norma que não fixa número nenhum não pode ser a norma de lotação '
        'de coisa alguma.**'])

    h2(doc, '15.1', 'Duas unidades de contagem dentro do mesmo artigo')
    para(doc,
         'O n.º 2 conta por **fogo**; o n.º 4 conta por **prédio**. O mesmo artigo usa duas unidades '
         'diferentes, e a razão é simples: o prédio rústico não tem, por definição, fogo. Esta é a '
         'primeira consequência a extrair, e vale contra a leitura predial do n.º 2 — se o legislador '
         'quisesse contar por prédio no n.º 2, tinha a palavra à mão e usou-a três números adiante.')

    h2(doc, '15.2', 'O n.º 4 não fixa número, e não tem controlo prévio')
    para(doc,
         'O n.º 2 fixa quatro animais, elevável a seis, e exige para isso parecer vinculativo do médico '
         'veterinário municipal e do delegado de saúde. O n.º 4 fixa seis, «podendo tal número ser '
         'excedido se a dimensão do terreno o permitir», e não exige parecer, autorização ou comunicação '
         'de espécie alguma. O único travão é o n.º 1 — boas condições e ausência de riscos '
         'hígio-sanitários. Não há teto e não há porteiro.')
    para(doc,
         'O Tribunal Central Administrativo Sul confirmou-o: incumbe à Administração «aferir sempre se o '
         'prédio onde se encontram alojados animais permite ou não o enquadramento na situação especial '
         'contida na norma» — acórdão de 4 de fevereiro de 2010, transcrito no ponto 11.1.')

    h2(doc, '15.3', 'A consequência decisiva')
    para(doc,
         'O ponto 6.3 registou, entre os elementos favoráveis à aplicação, que o n.º 4 tem estrutura de '
         'norma de capacidade. É verdade quanto à forma e falso quanto ao efeito. Uma norma de lotação '
         'diz quantos cabem; o n.º 4 diz que cabem seis, ou mais, consoante o terreno, sem limite '
         'superior e sem quem o verifique antes. Se o artigo 3.º fosse a norma de lotação dos '
         'alojamentos, um alojamento registado num prédio urbano teria lotação de quatro animais e um '
         'alojamento registado num prédio rústico teria lotação ilimitada.')
    destaque(doc, [
        'Nenhum regime de capacidade de estabelecimentos funciona assim. A lotação dos alojamentos tem '
        'regime próprio e mensurável — o n.º 1 do artigo 27.º do Decreto-Lei n.º 276/2001 e as tabelas do '
        'anexo III, que fixam superfícies mínimas por animal. O artigo 3.º gradua densidade doméstica; o '
        'anexo III mede capacidade. São operações diferentes.'])

    h2(doc, '15.4', 'A fronteira é fiscal, e isso agrava o problema')
    para(doc,
         'Lido como teto predial, o n.º 2 faria a licitude depender da **inscrição matricial** — '
         'categorias dos artigos 2.º a 6.º do Código do Imposto Municipal sobre Imóveis, de natureza '
         'fiscal, sem qualquer conexão material com o bem jurídico protegido pelo n.º 1, que é a '
         'salubridade e a prevenção de doenças transmissíveis ao homem. Duas situações fisicamente '
         'idênticas — a mesma moradia, o mesmo quintal, os mesmos animais, as mesmas condições — teriam '
         'tratamento distinto consoante a inscrição na matriz: quatro animais se o prédio for urbano, '
         'seis ou mais se for misto.')
    nota(doc, [
        '**Precisão quanto ao logradouro.** O logradouro de uma moradia integra o prédio urbano, entrando '
        'na avaliação como área de terreno livre. Não converte o conjunto em prédio misto: o artigo 5.º '
        'do Código do Imposto Municipal sobre Imóveis exige, para essa qualificação, que nenhuma das '
        'partes seja a principal. A área do quintal é, por isso, juridicamente irrelevante para o n.º 2.'])

    h2(doc, '15.5', 'A lacuna sancionatória no prédio rústico')
    para(doc,
         'Das sete alíneas do n.º 3 do artigo 14.º, só a al. c) remete para o artigo 3.º, e o seu objeto '
         'é «a permanência de cães e gatos em **habitações e terrenos anexos** em desrespeito pelas '
         'condições previstas no artigo 3.º». Num prédio rústico sem habitação não há habitação, nem '
         'terreno anexo a habitação alguma.')
    destaque(doc, [
        'Nessa hipótese o n.º 4 é **norma sem sanção**. O incumprimento aciona o n.º 5 — vistoria '
        'conjunta e notificação para remoção —, mas não é contraordenação. É mais um indício de que o '
        'artigo 3.º foi pensado a partir da casa, e que o n.º 4 é a sua extensão ao meio rural, não uma '
        'norma sobre estabelecimentos.'])

    h2(doc, '15.6', 'Resposta à questão 3')
    numlist(doc, [
        'O n.º 4 aplica-se a quem detém animais em prédio rústico ou misto, e o limite de seis é '
        'indicativo: cede perante a dimensão do terreno, sem teto e sem autorização prévia.',
        'A elasticidade não é defeito de redação: é a marca de uma norma de **densidade**, que mede '
        'animais contra espaço disponível, e não de uma norma de **capacidade**, que fixa um número.',
        'Por isso o n.º 4 não fixa a lotação de um alojamento registado instalado em prédio rústico — '
        'não fixa lotação nenhuma. A capacidade desse alojamento resulta do n.º 1 do artigo 27.º do '
        'Decreto-Lei n.º 276/2001 e do anexo III.',
        'A assimetria entre os n.ºs 2 e 4 dissolve-se pela leitura do fogo. Mantida a leitura predial, a '
        'assimetria torna-se arbitrária, porque passa a depender da matriz fiscal.',
    ])

    h2(doc, '15.7', 'O detentor não declarado, em prédio rústico ou misto')
    para(doc,
         'A questão 3 tem uma face prática que a sua formulação não revela: quem detém um número muito '
         'elevado de animais em prédio rústico ou misto, sem declarar atividade e sem registar '
         'alojamento, está sujeito a quê, e quem o controla?')

    h3(doc, 'O gatilho do regime é a atividade, nunca o número')
    para(doc,
         'O que faz nascer a obrigação de comunicação prévia é o exercício de uma atividade — hospedagem, '
         'criação comercial, venda —, nos termos da al. a) do n.º 1 do artigo 3.º do Decreto-Lei n.º '
         '276/2001. A al. q) do n.º 1 do artigo 2.º exige, para a hospedagem com fins lucrativos, que o '
         'alojamento «vise interesses comerciais ou lucrativos». Quem acumula sem fim lucrativo nunca tem '
         'alojamento a comunicar, tenha dez animais ou duzentos.')
    destaque(doc, [
        '**O número, por si, não desencadeia obrigação nenhuma de registo.** É a peça estrutural do '
        'problema, e vale igualmente para prédios rústicos e mistos.'])
    para(doc,
         'Não declarar não isenta quem efetivamente exerce a atividade: a falta da mera comunicação '
         'prévia é contraordenação económica grave, nos termos da al. a) do n.º 1 do artigo 68.º. Mas se '
         'não há fim lucrativo, não há infração nesse plano, e a fiscalização fica sem porta de entrada.')

    h3(doc, 'O que se aplica mesmo sem registo, e o que não se aplica')
    para(doc,
         'O Decreto-Lei n.º 276/2001 tem dois andares, e a distinção é decisiva. O **Capítulo II**, sob a '
         'epígrafe «Normas gerais de detenção, alojamento, maneio, intervenções cirúrgicas, captura e '
         'abate», vincula qualquer detentor: o artigo 6.º impõe o dever especial de cuidado a «o detentor '
         'do animal», e o artigo 8.º, sob a epígrafe «Condições dos alojamentos», dispõe que «os animais '
         'devem dispor do espaço adequado às suas necessidades fisiológicas e etológicas». Os **Capítulos '
         'III a VI** dependem da atividade — o artigo 24.º abre precisamente com «os detentores de '
         'animais de companhia que se dediquem à sua reprodução, criação, manutenção ou venda devem '
         'cumprir as condições previstas no presente capítulo».')
    nota(doc, [
        '**Consequência a reter.** As tabelas do anexo III, para que remete o n.º 1 do artigo 27.º, estão '
        'no Capítulo III e **não vinculam o detentor doméstico**. Podem servir de referência técnica numa '
        'vistoria, não de norma aplicável. E o artigo 8.º, esse sim de aplicação geral, é puramente '
        'qualitativo: não contém número algum.'])
    destaque(doc, [
        'Em parte alguma do sistema existe um número para o detentor não comercial em prédio rústico ou '
        'misto. O artigo 8.º é qualitativo, o anexo III não lhe é aplicável, e o n.º 4 do artigo 3.º do '
        'Decreto-Lei n.º 314/2003 é elástico. **O limite é o n.º 1 do artigo 3.º, aferido por vistoria.**'])

    h3(doc, 'Os instrumentos de controlo existentes')
    tabela(doc,
           ['Instrumento', 'Norma', 'Natureza'],
           [['Vistoria conjunta do delegado de saúde e do médico veterinário municipal, com notificação '
             'para remoção dos animais',
             'N.º 5 do artigo 3.º do Decreto-Lei n.º 314/2003', 'Reativo — depende de queixa'],
            ['Mandado judicial, em caso de obstrução à remoção',
             'N.º 6 do artigo 3.º do Decreto-Lei n.º 314/2003', 'Reativo'],
            ['Identificação e registo obrigatórios de cães, gatos e furões no SIAC',
             'Decreto-Lei n.º 82/2019, de 27 de junho',
             'O único com aptidão preventiva: liga cada animal a um titular'],
            ['Alojamento em desrespeito das condições do diploma — por via do Capítulo II',
             'Al. f) do n.º 1 do artigo 68.º do Decreto-Lei n.º 276/2001',
             'Aplica-se a qualquer detentor'],
            ['Falta de comunicação prévia, havendo atividade',
             'Al. a) do n.º 1 do artigo 68.º do Decreto-Lei n.º 276/2001',
             'Só se houver fim lucrativo'],
            ['Vacinação antirrábica, cães perigosos, ordenamento e ruído', 'Vários', 'Laterais']],
           [Cm(6.4), Cm(5.4), Cm(4.8)])
    para(doc,
         'O SIAC é o único mecanismo com aptidão verdadeiramente preventiva, porque cada animal '
         'identificado fica ligado a um titular e a base permite contar. Mas só vê os animais '
         'identificados, e quem não declara atividade tende também a não identificar.')

    h3(doc, 'Rústico e misto não são o mesmo caso')
    tabela(doc,
           ['', 'Prédio rústico sem habitação', 'Prédio misto'],
           [['Limite numérico',
             'N.º 4 do artigo 3.º — seis, excedíveis conforme o terreno',
             'N.º 4 quanto ao prédio; o n.º 2 tem campo quanto ao fogo da parte urbana'],
            ['Contraordenação pela al. c) do n.º 3 do artigo 14.º',
             '**Não há tipo.** A norma exige «habitações e terrenos anexos», e não há habitação',
             'Há tipo, pelo menos quanto aos animais na habitação e no terreno anexo a ela'],
            ['Remédio disponível',
             'Apenas a remoção administrativa do n.º 5',
             'Remoção administrativa e coima']],
           [Cm(3.4), Cm(6.6), Cm(6.6)])
    nota(doc, [
        '**Ponto por resolver.** No prédio misto, os animais que se encontrem na parte rústica, afastados '
        'da habitação, dificilmente cabem em «habitações e terrenos anexos». A cobertura sancionatória do '
        'prédio misto é, por isso, parcial, e a fronteira depende da distância à casa — critério que '
        'nenhuma norma fixa.'])

    h3(doc, 'A inibição prática da fiscalização')
    destaque(doc, [
        'O n.º 5 do artigo 3.º manda notificar o detentor para retirar os animais «para o canil ou gatil '
        'municipal». Executar a remoção significa, para o município, **acolher os animais a suas '
        'expensas**. Um município sem capacidade instalada tem incentivo direto a não agir. O regime '
        'confia a fiscalização a quem suporta o custo de a exercer.'])
    nota(doc, [
        '**Observação.** É a lacuna mais séria identificada neste estudo, e é de política legislativa, '
        'não de interpretação. O sistema é inteiramente reativo; a acumulação em meio rural pode crescer '
        'sem qualquer controlo até que alguém se queixe; e no prédio rústico sem habitação nem sequer há '
        'tipo contraordenacional. Uma revisão legislativa que queira resolver a questão central deve '
        'resolver também esta, sob pena de fixar limites que ninguém verifica.'])

    # ------------------------------------------------------------------ 16
    h1(doc, '16.', 'O caso residual')
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

    # ------------------------------------------------------------------ 17
    pagebreak(doc)
    h1(doc, '17.', 'Questões em aberto e limites da análise')
    para(doc,
         'Registo das questões cuja resposta condiciona a conclusão. São tratadas uma a uma; à medida que '
         'cada uma recebe resposta, o capítulo 2 é atualizado. As questões 1 a 3 foram enumeradas pelo '
         'grupo; as 4 a 9 resultaram da análise.')
    tabela(doc,
           ['N.º', 'Questão', 'Estado'],
           [['1',
             'Como se articula a licença ou autorização municipal do artigo 2.º da Lei n.º 92/95 com o '
             'registo dos alojamentos do Decreto-Lei n.º 276/2001 e com o limite por fogo do artigo 3.º '
             'do Decreto-Lei n.º 314/2003?',
             'Respondida — capítulo 13'],
            ['2',
             'Como tratar a remissão da al. p) do n.º 1 do artigo 2.º do Decreto-Lei n.º 276/2001 para o '
             'n.º 3 do artigo 3.º do Decreto-Lei n.º 314/2003?',
             'Respondida — capítulo 14'],
            ['3',
             'Como tratar a aplicação que o n.º 4 do artigo 3.º do Decreto-Lei n.º 314/2003 faz aos '
             'prédios rústicos e mistos, incluindo a possibilidade de o número ser excedido em função da '
             'dimensão do terreno?',
             'Respondida — capítulo 15'],
            ['4',
             'O que é um «fogo» para efeitos do n.º 2 do artigo 3.º do Decreto-Lei n.º 314/2003, não o '
             'definindo nenhum dos dois diplomas?',
             'Respondida — capítulo 5'],
            ['5',
             'No n.º 1 do artigo 3.º do Decreto-Lei n.º 314/2003, «alojamento» designa o facto de alojar '
             'ou o estabelecimento, sentido em que a mesma palavra é usada no Decreto-Lei n.º 276/2001?',
             'Respondida — capítulo 9'],
            ['6',
             'Que alcance tem a al. c) do n.º 3 do artigo 14.º do Decreto-Lei n.º 314/2003 ao qualificar '
             'o objeto da infração como «habitações e terrenos anexos»?',
             'Respondida — capítulo 9'],
            ['7',
             'Havendo excesso de animais num alojamento registado, há concurso de contraordenações entre '
             'o artigo 14.º do Decreto-Lei n.º 314/2003 e o regime sancionatório do Decreto-Lei n.º '
             '276/2001, ou consunção?',
             'Em aberto'],
            ['8',
             'Pode a câmara municipal, ao abrigo do n.º 5 do artigo 3.º do Decreto-Lei n.º 314/2003, '
             'notificar o titular de um alojamento registado na DGAV para retirar animais para o canil '
             'ou gatil municipal?',
             'Em aberto'],
            ['9',
             'Havendo conflito entre os dois diplomas, prevalece a especialidade do Decreto-Lei n.º '
             '276/2001 quanto aos alojamentos ou a posterioridade do Decreto-Lei n.º 314/2003, à luz do '
             'n.º 3 do artigo 7.º do Código Civil?',
             'Em aberto']],
           [Cm(1.2), Cm(12.2), Cm(3.0)])

    h2(doc, '17.1', 'Limites materiais da análise')
    numlist(doc, [
        'Não há decisão judicial, parecer publicado nem orientação administrativa que resolva '
        'expressamente a questão central. A conclusão é interpretativa.',
        'O elemento textual mais incómodo é a al. c) do n.º 3 do artigo 14.º — «habitações **e terrenos '
        'anexos**». A resposta proposta é que essa alínea delimita o âmbito do artigo 3.º no seu '
        'conjunto, e que o n.º 1 alcança efetivamente o quintal; o que não faz é converter o «fogo» do '
        'n.º 2 em «prédio». É matéria da questão 6.',
        'As **tabelas do anexo III** foram obtidas do Diário da República n.º 241, de 17 de outubro de '
        '2001, que publica os anexos I a VII. Falta incorporá-las e demonstrar numericamente a lotação '
        'por superfície.',
        'O **texto original do Diário da República n.º 290, de 17 de dezembro de 2003**, foi obtido e '
        'está usado no capítulo 14. Falta o processo legislativo do Decreto-Lei n.º 315/2003, cujo '
        'preâmbulo nada diz sobre a ressalva da al. p).',
        'A pesquisa jurisprudencial cobre apenas os tribunais superiores. **Não cobre a primeira '
        'instância**, onde se decide a maior parte das impugnações de atos municipais, nem os processos '
        'de contraordenação decididos administrativamente. Ausência de casuística publicada não equivale '
        'a ausência de casos.',
        'Os textos do n.º 2 do artigo 112.º da Constituição e do artigo 7.º do Código Civil, usados no '
        'capítulo 13, foram **conferidos em fonte oficial** e coincidem integralmente com os que aqui '
        'se citam. O método usado fica descrito no ponto 18.2, por ser útil a quem repita o trabalho.',
    ])

    # ------------------------------------------------------------------ 18
    h1(doc, '18.', 'Nota metodológica')

    h2(doc, '18.1', 'Fontes e pesquisa de jurisprudência')
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

    h2(doc, '18.2', 'Como consultar o Diário da República de forma verificável')
    para(doc,
         'As páginas de legislação consolidada do Diário da República eletrónico são construídas no '
         'navegador e não servem o texto a quem as consulte por meios automáticos. Isso não impede a '
         'verificação: o jornal oficial está integralmente disponível em PDF, e é essa a fonte a usar. '
         'Três regimes, consoante a data.')
    numlist(doc, [
        '**Atos posteriores a 1976** — o PDF do Diário da República tem camada de texto e pode ser lido e '
        'pesquisado diretamente. Foi assim que se obtiveram, para este estudo, o Diário da República n.º '
        '241, de 17 de outubro de 2001, o n.º 290, de 17 de dezembro de 2003, e o n.º 104, de 29 de maio '
        'de 2026.',
        '**Atos anteriores a 1976** — o PDF é uma digitalização sem camada de texto. A pesquisa por '
        'palavra falha, mas a página lê-se convertendo-a em imagem. Foi assim que se conferiu o artigo '
        '7.º do Código Civil no Diário do Governo n.º 274, I série, de 25 de novembro de 1966, a '
        'páginas 1886.',
        '**Textos republicados** — quando o que se procura é um texto consolidado por republicação, como '
        'a Constituição na redação da Lei Constitucional n.º 1/2005, recorre-se à edição institucional '
        'em PDF de entidade pública — foi usada a do Tribunal Constitucional e a da Comissão Nacional de '
        'Eleições.',
    ])
    destaque(doc, [
        'A regra prática que daqui resulta: **um compilador privado serve para localizar a norma, nunca '
        'para a citar**. A citação faz-se sempre contra o PDF do jornal oficial, pelo caminho que a data '
        'do ato determinar.'])

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
