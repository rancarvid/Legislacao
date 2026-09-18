# -*- coding: utf-8 -*-
from _memo_engine import *
from docx.shared import Cm


def construir(doc):
    capa(doc,
         'Anexo ao memorando técnico',
         'Delimitação entre o Decreto-Lei n.º 314/2003 e o Decreto-Lei n.º 276/2001',
         'Os limites de alojamento por prédio não constituem limiar de capacidade dos estabelecimentos de '
         'criação',
         'Direção-Geral de Alimentação e Veterinária   ·   setembro de 2026')

    h1(doc, '1.', 'Questão')
    para(doc,
         'Discute-se se os limites de animais por fogo fixados no artigo 3.º do Decreto-Lei n.º 314/2003 '
         'condicionam a capacidade dos estabelecimentos de criação de cães e gatos e, por essa via, o acesso à '
         'atividade regulada pelo Decreto-Lei n.º 276/2001. A leitura afirmativa tem sido sustentada sem '
         'demonstração e conduz a resultados que a própria arquitetura dos dois diplomas não comporta.')
    destaque(doc, [
        'Conclusão: os limites do artigo 3.º do Decreto-Lei n.º 314/2003 são normas de polícia sanitária sobre '
        'a detenção doméstica de animais. Não fixam a lotação dos alojamentos sujeitos ao Decreto-Lei n.º '
        '276/2001, cuja capacidade tem regime próprio, e não constituem condição de acesso à atividade de '
        'criação.'])

    h1(doc, '2.', 'Argumento literal e teleológico')
    para(doc,
         'O Decreto-Lei n.º 314/2003 aprova o Programa Nacional de Luta e Vigilância Epidemiológica da Raiva '
         'Animal e Outras Zoonoses e estabelece as regras relativas à posse e detenção, comércio, exposições e '
         'entrada em território nacional de animais suscetíveis à raiva. O seu objeto é sanitário e '
         'epidemiológico. A epígrafe do artigo 3.º é «Detenção de cães e gatos»; o sujeito das suas normas é o '
         'detentor; a unidade de referência é o fogo.')
    para(doc,
         'O Decreto-Lei n.º 276/2001 tem objeto distinto. Nos termos do seu artigo 1.º, regula o exercício da '
         'atividade de exploração de alojamentos, independentemente do seu fim, e de venda de animais de '
         'companhia. Uma norma dirige-se a quem detém; a outra a quem exerce uma atividade.')
    para(doc,
         'A finalidade confirma a leitura. O n.º 1 do artigo 3.º do Decreto-Lei n.º 314/2003 condiciona o '
         'alojamento à ausência de riscos hígio-sanitários relativamente à conspurcação ambiental e a doenças '
         'transmissíveis ao homem. O bem jurídico é a saúde pública na sua dimensão de vizinhança, não a '
         'proteção do animal na atividade económica, que é o objeto do Decreto-Lei n.º 276/2001 enquanto '
         'diploma de execução da Convenção Europeia para a Proteção dos Animais de Companhia.')
    para(doc,
         'A doutrina que se debruçou sobre o artigo 3.º recusou, pelas mesmas razões, que os seus limites '
         'valham fora do domínio sanitário. A propósito da tentativa de deles extrair uma limitação geral aos '
         'poderes do proprietário de fracção autónoma, escreveu-se o seguinte.')
    citacao(doc,
            ['Seria no mínimo abusivo pretender retirar daqui uma limitação geral em termos de detenção de '
             'animais numa fracção autónoma, numa limitação matreira aos poderes conferidos pelo código civil '
             'aos proprietários.',
             'A limitação prevista nesta norma vale para efeito de prevenção de zoonoses. Mal se compreenderia, '
             'num diploma desta natureza, uma limitação geral, feita em abstracto (sem qualquer atenção, por '
             'exemplo, à dimensão da fracção autónoma) aos poderes conferidos ao proprietário pelo Direito '
             'Civil.',
             'O limite máximo aqui estabelecido releva para efeitos de luta e vigilância epidemiológica, '
             'indiciando riscos higío-sanitários, não pretende regular relações de vizinhança, nem tutelar '
             'direitos de personalidade dos outros conviventes no prédio.'],
            'Sandra Passinhas, «Os animais e o regime português da propriedade horizontal», Revista da Ordem '
            'dos Advogados, Ano 66, Vol. II, setembro de 2006')
    para(doc,
         'O raciocínio vale por maioria de razão no caso presente. Se os limites do artigo 3.º não podem ser '
         'invocados para conformar o conteúdo do direito de propriedade e as relações de vizinhança, que são '
         'matéria civil próxima do seu campo de incidência material, menos ainda podem sê-lo para condicionar '
         'o acesso a uma atividade económica regulada por diploma próprio, com autoridade competente, '
         'procedimento e regime sancionatório distintos.')

    h1(doc, '3.', 'Argumento sistemático: a articulação feita pelo legislador')
    para(doc,
         'Este é o elemento decisivo e resulta da sequência legislativa. O Decreto-Lei n.º 314/2003 e o '
         'Decreto-Lei n.º 315/2003 têm a mesma data, 17 de dezembro de 2003. O segundo alterou o Decreto-Lei '
         'n.º 276/2001. No mesmo momento em que introduziu no ordenamento os limites de detenção por fogo, o '
         'legislador interveio no diploma dos alojamentos para articular os dois regimes.')
    para(doc,
         'A redação original de 2001 da definição de hospedagem sem fins lucrativos não continha qualquer '
         'remissão para legislação sanitária.')
    citacao(doc,
            ["p) 'Hospedagem sem fins lucrativos' alojamento, permanente ou temporário, de animais de companhia "
             "que não vise a obtenção de rendimentos;"],
            'Al. p) do artigo 2.º do Decreto-Lei n.º 276/2001, redação originária de 17 de outubro de 2001')
    para(doc,
         'O Decreto-Lei n.º 315/2003 acrescentou-lhe uma exceção expressa, por remissão para o artigo 3.º do '
         'diploma da raiva.')
    citacao(doc,
            ["p) 'Hospedagem sem fins lucrativos', alojamento, permanente ou temporário, de animais de "
             "companhia que não vise a obtenção de rendimentos, com excepção das referidas no n.º 3 do artigo "
             "3.º do diploma que aprova o Plano Nacional de Luta e Vigilância da Raiva Animal e outras "
             "Zoonoses;"],
            'Al. p) do artigo 2.º do Decreto-Lei n.º 276/2001, na redação do Decreto-Lei n.º 315/2003')
    para(doc,
         'O sentido da intervenção é inequívoco. Confrontado com a coexistência dos dois regimes, o legislador '
         'não converteu os limites de detenção em limiar de capacidade dos alojamentos. Fez o inverso: '
         'subtraiu ao conceito de alojamento sujeito a título de acesso as situações de detenção que o diploma '
         'sanitário regula. Delimitou os planos em vez de os sobrepor.')
    para(doc,
         'O n.º 3 do artigo 3.º para que se remete permanece hoje na redação originária de 2003, tal como todo '
         'o artigo 3.º, que nunca foi alterado. Tem o seguinte teor.')
    citacao(doc,
            ['3 — No caso de fracções autónomas em regime de propriedade horizontal, o regulamento do '
             'condomínio pode estabelecer um limite de animais inferior ao previsto no número anterior.'],
            'N.º 3 do artigo 3.º do Decreto-Lei n.º 314/2003, redação originária')
    para(doc,
         'A concordância gramatical fixa o sentido da exceção: «das referidas» reporta-se às fracções '
         'autónomas. O alojamento de animais numa fracção autónoma em regime de propriedade horizontal não é, '
         'para efeitos do Decreto-Lei n.º 276/2001, hospedagem sem fins lucrativos, e não fica por isso sujeito '
         'a mera comunicação prévia nos termos da al. a) do n.º 1 do seu artigo 3.º.')
    para(doc,
         'A opção é significativa. O legislador podia ter transformado os limites de detenção em teto de '
         'lotação dos alojamentos, e não o fez. Retirou do universo dos alojamentos sujeitos a título de acesso '
         'a situação doméstica que o diploma sanitário passava a regular. A exceção é estreita, porque '
         'circunscrita à fracção autónoma, mas a direção da intervenção é inequívoca e vale como elemento '
         'interpretativo quanto à relação entre os dois regimes.')

    h3(doc, 'Alcance exato da exceção')
    para(doc,
         'Conjugada com a al. a) do n.º 1 do artigo 3.º, que sujeita a mera comunicação prévia os alojamentos '
         'para hospedagem com ou sem fins lucrativos, a exceção produz o seguinte resultado.')
    tabela(doc,
           ['Situação', 'Qualificação', 'Título de acesso'],
           [
            ['Animais detidos sem intuito de rendimento em fracção autónoma',
             'Excluída da hospedagem sem fins lucrativos pela al. p)',
             'Nenhum. Rege o regulamento de condomínio e, em caso de excesso, a remoção municipal do n.º 5 do '
             'artigo 3.º do Decreto-Lei n.º 314/2003'],
            ['Alojamento sem intuito de rendimento explorado fora de fracção autónoma, designadamente abrigo '
             'de associação',
             'Hospedagem sem fins lucrativos',
             'Mera comunicação prévia'],
            ['Alojamento para reprodução, criação, manutenção ou venda com interesse comercial ou lucrativo, '
             'em qualquer tipo de prédio, incluindo fracção autónoma',
             'Hospedagem com fins lucrativos, al. q), **sem qualquer exceção**',
             'Mera comunicação prévia ou permissão administrativa'],
           ],
           [Cm(5.0), Cm(5.4), Cm(6.2)])

    h3(doc, 'Argumento a contrario: a alínea q) nunca foi excecionada')
    para(doc,
         'A alínea q) define a hospedagem com fins lucrativos como o alojamento para reprodução, criação, '
         'manutenção e venda de animais de companhia. É a norma que qualifica o estabelecimento de criação. '
         'Nunca conteve, em nenhuma das dez versões do diploma entre 2001 e a redação atual, qualquer remissão '
         'para o regime da raiva ou para os limites de detenção.')
    para(doc,
         'O contraste é decisivo. No mesmo ato em que criou os limites por fogo, o legislador introduziu a '
         'exceção na alínea p) e não a introduziu na alínea q). Soube excecionar quando quis excecionar. Se '
         'tivesse pretendido que os limites de detenção do Decreto-Lei n.º 314/2003 condicionassem os '
         'alojamentos de reprodução e criação, teria feito na alínea q) o que fez na alínea p). A ausência é '
         'deliberada e opõe-se à tese de que aqueles limites valem como teto de lotação dos estabelecimentos.')

    h3(doc, 'Defeitos de redação da remissão')
    para(doc,
         'A remissão é imperfeita, em três planos que importa distinguir, porque nenhum deles afeta a '
         'conclusão anterior.')
    numlist(doc, [
        '**Designação incorreta do diploma remetido.** A alínea p) refere o «Plano Nacional de Luta e '
        'Vigilância da Raiva Animal e outras Zoonoses». A designação legal, fixada no artigo 1.º tanto do '
        'Decreto-Lei n.º 91/2001 como do Decreto-Lei n.º 314/2003, é «Programa Nacional de Luta e Vigilância '
        'Epidemiológica da Raiva Animal e Outras Zoonoses». Erram o substantivo e omite-se o qualificativo. '
        'É lapso objetivo, e subsiste desde 2003.',

        '**Remissão indireta.** O n.º 3 do artigo 3.º não define uma categoria de alojamento: é norma '
        'habilitante do regulamento de condomínio. As fracções autónomas aparecem nele como cenário de '
        'aplicação, não como objeto regulado. A remissão capta o referente pretendido por acidente da redação '
        'e não por técnica legislativa. A formulação correta seria excecionar diretamente «as fracções '
        'autónomas em regime de propriedade horizontal».',

        '**Incompletude.** A exceção cobre apenas a fracção autónoma. A detenção doméstica em moradia, em '
        'prédio rústico ou em prédio misto fica formalmente fora dela. Se o propósito era subtrair a detenção '
        'doméstica ao conceito de alojamento, a exceção é mais estreita do que o seu fim.',
    ])
    para(doc,
         'Não há, em contrapartida, erro no número remetido. O n.º 3 é o único do artigo 3.º onde figura um '
         'substantivo feminino plural, «fracções autónomas», com o qual concorda a expressão «das referidas» '
         'usada na alínea p). A concordância gramatical confirma que o legislador visou aquele número e não '
         'outro. Os lapsos de designação e de técnica não permitem, por si, concluir por lapso de numeração.')

    h1(doc, '4.', 'Argumento do critério de aplicação')
    para(doc,
         'Os dois regimes acionam-se por factos distintos e logicamente independentes. O Decreto-Lei n.º '
         '276/2001 desencadeia-se pela atividade: basta possuir uma fêmea reprodutora cujas crias se destinem '
         'ao comércio. O Decreto-Lei n.º 314/2003 desencadeia-se pelo número de animais adultos no fogo.')
    tabela(doc,
           ['Situação', 'Decreto-Lei n.º 276/2001', 'Decreto-Lei n.º 314/2003'],
           [
            ['Uma fêmea reprodutora, uma ninhada por ano, em apartamento',
             'Atividade sujeita a mera comunicação prévia',
             'Dentro do limite de detenção'],
            ['Quatro cães adultos sem qualquer reprodução',
             'Sem atividade; não sujeito',
             'No limite; carece de parecer para exceder'],
            ['Seis cães adultos em prédio rústico, sem reprodução',
             'Sem atividade; não sujeito',
             'Dentro do limite'],
            ['Doze cães adultos em estabelecimento de criação licenciado',
             'Capacidade declarada e aferida pelo anexo I',
             'Norma de detenção doméstica não aplicável'],
           ],
           [Cm(5.4), Cm(5.7), Cm(5.5)])
    para(doc,
         'A independência dos critérios demonstra que nenhum deles é condição do outro. Se os limites de '
         'detenção funcionassem como limiar de capacidade, o segundo e o terceiro casos configurariam '
         'atividade regulada, o que manifestamente não sucede.')

    h1(doc, '5.', 'A capacidade dos alojamentos tem regime próprio')
    para(doc,
         'O Decreto-Lei n.º 276/2001 dispõe de mecanismo autónomo e completo de fixação da capacidade. Esta é '
         'declarada pelo interessado no procedimento de acesso e aferida por parâmetros dimensionais '
         'constantes do próprio diploma.')
    citacao(doc,
            ['h) A capacidade máxima de animais e respetivas espécies a alojar;'],
            'Al. h) do n.º 1 do artigo 3.º-A do Decreto-Lei n.º 276/2001')
    citacao(doc,
            ['6 — Os alojamentos referidos neste capítulo devem obedecer aos parâmetros mínimos adequados à '
             'espécie, nomeadamente os constantes do anexo i do presente diploma, do qual faz parte '
             'integrante.'],
            'N.º 6 do artigo 25.º do Decreto-Lei n.º 276/2001')
    para(doc,
         'Havendo regime especial completo para a capacidade dos alojamentos, não há lacuna que justifique '
         'recorrer a norma de outro diploma, com objeto diverso, para a integrar. A regra da especialidade '
         'impõe a prevalência do Decreto-Lei n.º 276/2001 nesta matéria.')

    h1(doc, '6.', 'Argumento da arquitetura sancionatória')
    para(doc,
         'Os dois diplomas reagem ao incumprimento por vias que não se comunicam. O Decreto-Lei n.º 314/2003 '
         'confere à câmara municipal, após vistoria conjunta do delegado de saúde e do médico veterinário '
         'municipal, o poder de notificar o detentor para retirar os animais para o canil ou gatil municipal. '
         'É medida de polícia sanitária sobre um agregado doméstico.')
    citacao(doc,
            ['5 — Em caso de não cumprimento do disposto nos números anteriores, as câmaras municipais, após '
             'vistoria conjunta do delegado de saúde e do médico veterinário municipal, notificam o detentor '
             'para retirar os animais para o canil ou gatil municipal no prazo estabelecido por aquelas '
             'entidades, caso o detentor não opte por outro destino que reúna as condições estabelecidas pelo '
             'presente diploma.'],
            'N.º 5 do artigo 3.º do Decreto-Lei n.º 314/2003')
    para(doc,
         'O Decreto-Lei n.º 276/2001 dispõe de regime sancionatório próprio aplicável ao titular da exploração, '
         'com medidas de suspensão e encerramento e responsabilidade contraordenacional. A diferença de '
         'destinatário, de autoridade competente e de consequência jurídica confirma que os planos são '
         'distintos.')

    h1(doc, '7.', 'A classificação predial é critério tributário')
    para(doc,
         'Prédio urbano, prédio rústico e prédio misto são categorias definidas nos artigos 2.º a 6.º do Código '
         'do Imposto Municipal sobre Imóveis, para efeitos de incidência e avaliação. Não exprimem aptidão '
         'sanitária, dimensão útil nem adequação ao alojamento de animais. Um apartamento de trezentos metros '
         'quadrados com logradouro e uma habitação exígua integram a mesma categoria.')
    para(doc,
         'Fazer depender a licitude de uma atividade económica, e o respetivo limiar de exercício, da '
         'classificação matricial do imóvel conduziria a diferenciação sem fundamento material bastante. A '
         'mesma atividade, com o mesmo número de animais e as mesmas condições efetivas, seria lícita ou '
         'ilícita consoante a inscrição na matriz predial. Uma interpretação com este resultado não satisfaz '
         'as exigências de necessidade e de proporcionalidade que vinculam a restrição de direitos económicos.')
    para(doc,
         'Acresce que o Decreto-Lei n.º 314/2003 usa a classificação predial para um fim que lhe é adequado: '
         'aproximar, de forma expedita, o risco de conspurcação e de transmissão de zoonoses em contexto de '
         'vizinhança. Transpor esse critério para a regulação de uma atividade desvirtua-o.')

    h1(doc, '8.', 'O direito da União afasta a relevância do tipo de prédio')
    para(doc,
         'O Regulamento (UE) 2026/1818 define o estabelecimento de criação em termos que abrangem '
         'expressamente a habitação particular, sem qualquer distinção quanto à natureza do imóvel.')
    citacao(doc,
            ['«Estabelecimento de criação», qualquer instalação ou estrutura, incluindo casas particulares, '
             'onde são mantidos cães ou gatos para fins de reprodução com vista à colocação da sua '
             'descendência no mercado.'],
            'Al. o) do artigo 4.º do Regulamento (UE) 2026/1818')
    para(doc,
         'O critério europeu é funcional: releva a afetação do espaço à reprodução com vista à colocação no '
         'mercado, não a sua qualificação jurídica ou tributária. A partir de 31 de agosto de 2028, uma leitura '
         'nacional que fizesse depender o conceito de estabelecimento da classificação predial colidiria com '
         'esta definição.')

    h1(doc, '9.', 'Consequências da tese contrária')
    para(doc,
         'A leitura que converte os limites de detenção em limiar de capacidade produz resultados que o sistema '
         'não comporta e que, por isso, a infirmam.')
    bullets(doc, [
        'Nenhum estabelecimento de criação instalado em prédio urbano poderia deter mais de quatro animais '
        'adultos, ou seis mediante parecer vinculativo. O limiar europeu de mais de cinco cadelas ou gatas '
        'reprodutoras, que aciona a aprovação do artigo 10.º do Regulamento, seria inaplicável em meio urbano.',

        'A permissão administrativa prevista na al. b) do n.º 1 do artigo 45.º do projeto de regime ficaria '
        'esvaziada de conteúdo quanto a uma parte substancial do território.',

        'A capacidade máxima declarada na mera comunicação prévia e os parâmetros do anexo I do Decreto-Lei '
        'n.º 276/2001 tornar-se-iam inúteis, por serem sempre precedidos de um teto fixado alhures.',

        'Um alojamento licenciado com capacidade para doze cães, aprovado pela autoridade competente ao abrigo '
        'do Decreto-Lei n.º 276/2001, estaria simultaneamente em infração ao Decreto-Lei n.º 314/2003. A '
        'antinomia seria permanente e insanável.',
    ])
    para(doc,
         'Presumindo o intérprete que o legislador consagrou as soluções mais acertadas e soube exprimir o seu '
         'pensamento em termos adequados, nos termos do artigo 9.º do Código Civil, deve ser afastada a '
         'interpretação que gera antinomia permanente entre dois diplomas que o próprio legislador articulou '
         'no mesmo dia.')

    h1(doc, '10.', 'O que o Decreto-Lei n.º 314/2003 efetivamente impõe a quem comercializa')
    para(doc,
         'A única disposição do diploma que intersecta estabelecimentos é o artigo 5.º, e refere-se a '
         'estabelecimentos destinados ao comércio. Não menciona criação nem reprodução, e o seu conteúdo '
         'esgota-se em documentação sanitária.')
    citacao(doc,
            ['1 — Os cães e gatos que se encontrem em estabelecimentos destinados ao seu comércio devem estar '
             'acompanhados do respectivo boletim sanitário de cães e gatos, onde deve estar aposta a etiqueta '
             'autocolante comprovativa da identificação electrónica, quando aplicável, e ter asseguradas as '
             'acções de profilaxia médica e sanitária obrigatórias ou consideradas adequadas à saúde e idade '
             'dos animais pelo médico veterinário.',
             '2 — Os cães com idade superior a 3 meses de idade devem possuir certificado das acções de '
             'profilaxia consideradas obrigatórias para a espécie.'],
            'Artigo 5.º do Decreto-Lei n.º 314/2003')
    para(doc,
         'Estas obrigações são cumulativas com as do Decreto-Lei n.º 276/2001 e serão absorvidas pelo regime de '
         'rastreabilidade do Capítulo III do Regulamento. Não têm qualquer incidência sobre a capacidade do '
         'estabelecimento nem sobre o título de acesso.')

    h1(doc, '11.', 'Síntese')
    tabela(doc,
           ['', 'Decreto-Lei n.º 314/2003', 'Decreto-Lei n.º 276/2001'],
           [
            ['Objeto', 'Luta e vigilância epidemiológica da raiva e outras zoonoses; posse e detenção',
             'Exercício da atividade de exploração de alojamentos e de venda'],
            ['Destinatário', 'Detentor', 'Titular da exploração'],
            ['Unidade de referência', 'Fogo; prédio urbano, rústico ou misto', 'Alojamento'],
            ['Facto gerador', 'Número de animais adultos no fogo',
             'Exercício da atividade; uma fêmea reprodutora basta'],
            ['Bem jurídico', 'Saúde pública e salubridade de vizinhança',
             'Saúde e bem-estar animal na atividade económica'],
            ['Reação ao incumprimento',
             'Notificação municipal para remoção dos animais, após vistoria conjunta',
             'Suspensão, encerramento e contraordenação'],
            ['Fixação da capacidade', 'Não regula',
             'Declarada na mera comunicação prévia e aferida pelo anexo I'],
           ],
           [Cm(3.3), Cm(6.6), Cm(6.7)])
    destaque(doc, [
        'Os dois diplomas são cumulativamente aplicáveis a quem cria cães ou gatos na sua habitação: enquanto '
        'detentor, observa os limites e as condições higiossanitárias do Decreto-Lei n.º 314/2003; enquanto '
        'operador, cumpre o Decreto-Lei n.º 276/2001 e, a partir de 2028, o Regulamento. **Cumulação não é '
        'sobreposição.** Nenhum dos regimes fixa o limiar do outro.'])

    h1(doc, '12.', 'Recomendação')
    numlist(doc, [
        'Explicitar no futuro regime que os limites de detenção previstos na legislação sanitária não '
        'constituem limiar de capacidade dos estabelecimentos, cuja lotação é declarada no título de acesso e '
        'aferida pelos parâmetros técnicos aplicáveis.',
        'Reformular a exceção da al. p) do artigo 2.º do Decreto-Lei n.º 276/2001. Deve excecionar '
        'diretamente a detenção doméstica, sem remissão, corrigindo simultaneamente a designação do diploma '
        'remetido, hoje incorreta, e a assimetria entre quem detém animais em fracção autónoma e quem os '
        'detém em moradia ou em prédio rústico.',

        'Manter a alínea q), relativa ao alojamento para reprodução, criação, manutenção e venda, sem qualquer '
        'exceção fundada em limites de detenção, em linha com a opção seguida desde 2001.',
        'Assegurar que a definição nacional de estabelecimento de criação acompanha o Regulamento quanto à '
        'inclusão das casas particulares, afastando qualquer relevância da classificação predial.',
    ])
