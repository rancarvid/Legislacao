# -*- coding: utf-8 -*-
from _memo_engine import *
from docx.shared import Cm

CONCORD = []   # (codigo, diploma, ref_leve, ref_completa)


def cit(doc, modo, lines, diploma, leve, completa):
    """modo A: referencia completa sob a caixa. modo B: referencia leve + codigo."""
    if modo == 'A':
        citacao(doc, lines, f'{completa}')
    else:
        cod = f'C{len(CONCORD) + 1}'
        CONCORD.append((cod, diploma, leve, completa))
        citacao(doc, lines, f'{cod}   ·   {diploma}, {leve}')


W = Cm(16.6)


def construir(doc, modo):
    del CONCORD[:]

    capa(doc,
         'Memorando técnico',
         'Criação de cães e gatos em pequena escala',
         'Regime nacional vigente, Regulamento (UE) 2026/1818 e projeto de Regime Geral do Animal de Companhia',
         'Direção-Geral de Alimentação e Veterinária   ·   Divisão de Bem-Estar dos Animais para Fins '
         'Experimentais, Companhia e Zoológicos   ·   setembro de 2026')

    enquadramento(doc, [
        'O projeto de Regime Geral do Animal de Companhia referido neste memorando é uma versão de trabalho, '
        'em harmonização interna. As soluções nele constantes não correspondem a direito vigente nem vinculam '
        'a posição final da Direção-Geral. As citações do Regulamento (UE) 2026/1818 reproduzem a versão '
        'portuguesa publicada no Jornal Oficial de 10 de agosto de 2026, que é texto autêntico.'])

    # ------------------------------------------------------------------ 1
    h1(doc, '1.', 'Objeto')
    para(doc,
         'Este memorando fixa o enquadramento jurídico da criação de cães e gatos em pequena escala e reúne os '
         'elementos necessários para responder às questões suscitadas publicamente sobre a matéria. Articula, '
         'para o efeito, o Decreto-Lei n.º 276/2001, de 17 de outubro, que rege o acesso e o exercício da '
         'atividade; o Decreto-Lei n.º 314/2003, de 17 de dezembro, cuja delimitação se trata no ponto 4.3; o '
         'Regulamento (UE) 2026/1818, do Parlamento Europeu e do Conselho, de 17 de junho de 2026; e o projeto '
         'de Regime Geral do Animal de Companhia.')
    para(doc,
         'A ordem de exposição é deliberada. Começa-se pelo que já vincula, passa-se ao que passará a vincular '
         'e só depois se trata do que está em elaboração. A distinção entre estes três planos é a principal '
         'fonte de equívoco no debate público sobre esta matéria.')

    # ------------------------------------------------------------------ 2
    h1(doc, '2.', 'Conclusões')
    destaque(doc, [
        'Não existe, no direito vigente, no Regulamento ou no projeto de regime, qualquer figura de criador '
        'dispensado de registo junto da autoridade competente. O Regulamento admite um regime reduzido de '
        'obrigações de bem-estar para quem produza até duas ninhadas por ano civil; **o projeto de regime não '
        'acolhe essa redução**, aplicando a todos os estabelecimentos de criação o conjunto integral das '
        'obrigações.'])
    numlist(doc, [
        'O acesso à atividade depende hoje de mera comunicação prévia ou de permissão administrativa. Uma e '
        'outra dão lugar a número de identificação pessoal e intransmissível, e os criadores são publicitados '
        'no sítio da Direção-Geral. Nenhum criador registado é anónimo perante a autoridade competente nem '
        'perante o público.',

        'O Regulamento dispensa os estabelecimentos de criação até duas ninhadas por ano civil de um conjunto '
        'delimitado de obrigações do seu Capítulo II, que inclui o espaço disponível mínimo, a temperatura das '
        'áreas de parto, a iluminação, a inspeção diária dos animais e as especificações de socialização e '
        'enriquecimento. Não os dispensa da notificação e do registo do estabelecimento, que o artigo 9.º '
        'mantém sem exceção.',

        'A identificação e o registo individual dos animais e os requisitos da publicidade em linha constam do '
        'Capítulo III do Regulamento. O artigo 5.º dispõe exclusivamente sobre o Capítulo II e não lhes é '
        'aplicável. A rastreabilidade não comporta redução em função da escala.',

        'A opção do projeto de regime de não acolher a redução do artigo 5.º constitui regra nacional mais '
        'restritiva na aceção do artigo 30.º do Regulamento e deve ser comunicada à Comissão Europeia até 31 '
        'de agosto de 2028.',

        'A ponderação técnica realizada em sede interna incidiu sobre a exigência de instalações '
        'individualizadas constante do artigo 25.º do Decreto-Lei n.º 276/2001, e não sobre o registo, a '
        'identificação, a rastreabilidade ou o controlo reprodutivo. Mesmo na sua formulação mais permissiva, '
        'situa-se acima do que o direito da União admite dispensar.',

        'Os limites de alojamento do Decreto-Lei n.º 314/2003 respeitam à detenção doméstica de animais e não '
        'fixam a capacidade dos estabelecimentos de criação, que é matéria própria do Decreto-Lei n.º 276/2001 '
        '(ponto 4.3 e anexo autónomo).',
    ])

    # ------------------------------------------------------------------ 3
    h1(doc, '3.', 'Delimitação do que está em causa')
    para(doc,
         'A discussão pública associou à revisão legislativa em curso um conjunto de propósitos que não '
         'correspondem ao seu conteúdo. Importa separá-los do que efetivamente foi ponderado.')
    tabela(doc,
           ['Matéria suscitada', 'Situação'],
           [
            ['Criação de uma figura de criador dispensado de registo',
             'Não existe no direito vigente, no Regulamento nem no projeto de regime. Nenhum dos três prevê '
             'exercício da atividade sem título de acesso.'],
            ['Criação de um terceiro título de acesso, a par da mera comunicação prévia e da permissão '
             'administrativa',
             'Não está prevista. O projeto mantém os dois títulos existentes e distribui-os por escala, no '
             'sentido da maior exigência.'],
            ['Redução das obrigações de identificação e de rastreabilidade',
             'Não. Constam do Capítulo III do Regulamento, cujo âmbito o artigo 5.º não alcança, e aplicam-se '
             'a todos os cães e gatos, incluindo os detidos por particulares.'],
            ['Adequação dos requisitos de instalações à dimensão do estabelecimento',
             'Matéria efetivamente ponderada em sede técnica, incidente sobre os n.os 1 e 2 do artigo 25.º do '
             'Decreto-Lei n.º 276/2001. Não consta da versão do projeto remetida à tutela.'],
            ['Incompatibilidade com o direito da União',
             'O Regulamento admite expressamente a modulação por escala (artigo 5.º) e a manutenção de regras '
             'nacionais mais restritivas (artigo 30.º). A opção do projeto situa-se acima da linha de base '
             'europeia, não abaixo.'],
           ],
           [Cm(5.6), Cm(11.0)])

    # ------------------------------------------------------------------ 4
    h1(doc, '4.', 'Regime nacional vigente')

    h2(doc, '4.1', 'Acesso e exercício da atividade')
    para(doc,
         'O Decreto-Lei n.º 276/2001 regula, nos termos do seu artigo 1.º, o exercício da atividade de '
         'exploração de alojamentos, independentemente do seu fim, e de venda de animais de companhia. O '
         'critério de sujeição é a atividade, não a dimensão: basta uma fêmea reprodutora cujas crias se '
         'destinem ao comércio.')
    cit(doc, modo,
        ["«Criação comercial de animais de companhia», a atividade que consiste em possuir uma ou mais fêmeas "
         "reprodutoras cujas crias sejam destinadas ao comércio."],
        'Decreto-Lei n.º 276/2001', 'artigo 2.º', 'Al. aa) do artigo 2.º do Decreto-Lei n.º 276/2001')
    cit(doc, modo,
        ['1 — Sem prejuízo do disposto no Decreto-Lei n.º 10/2015, de 16 de janeiro, quanto aos '
         'estabelecimentos de comércio a retalho de animais de companhia, o exercício da atividade de '
         'exploração de alojamentos, bem como a atividade de criação comercial de animais de companhia depende '
         'de:',
         'a) Mera comunicação prévia, no caso dos centros de recolha, alojamentos para hospedagem, com ou sem '
         'fins lucrativos, criação comercial de animais de companhia, em qualquer caso com exceção dos '
         'destinados exclusivamente à venda, sem prejuízo do disposto na alínea seguinte;',
         'b) Permissão administrativa, no caso dos alojamentos para hospedagem com fins lucrativos destinados '
         'à reprodução e criação de animais potencialmente perigosos, nomeadamente de cães das raças '
         'consideradas como potencialmente perigosas.'],
        'Decreto-Lei n.º 276/2001', 'artigo 3.º', 'N.º 1 do artigo 3.º do Decreto-Lei n.º 276/2001')
    para(doc,
         'Dois efeitos deste regime são frequentemente ignorados no debate, e são decisivos: o título de acesso '
         'gera número identificador e a identidade do criador é pública.')
    cit(doc, modo,
        ['11 — A comunicação prévia ou a permissão administrativa dão lugar a um número de identificação, o '
         'qual é pessoal e intransmissível.',
         '12 — A DGAV publicita, no seu sítio de Internet, os nomes dos criadores comerciais de animais de '
         'companhia e respetivo município de atividade e número de identificação.'],
        'Decreto-Lei n.º 276/2001', 'artigo 3.º', 'N.os 11 e 12 do artigo 3.º do Decreto-Lei n.º 276/2001')
    para(doc,
         'A mera comunicação prévia é dirigida à Direção-Geral e integra, entre outros elementos, a localização '
         'do alojamento, a caracterização das atividades, a indicação do médico veterinário responsável, a '
         'capacidade máxima de animais e respetivas espécies a alojar, o número de animais detidos, espécies e '
         'raças, e declaração de responsabilidade quanto ao cumprimento da legislação aplicável em matéria de '
         'instalações, equipamentos, higiene, saúde e bem-estar dos animais.')
    para(doc,
         'Assinala-se uma limitação do regime vigente que a revisão deve corrigir. As obrigações dos artigos '
         '4.º e 5.º dirigem-se aos titulares de alojamentos para hospedagem, e a hospedagem com fins '
         'lucrativos é definida por referência a interesses comerciais ou lucrativos. Quem cria sem intuito '
         'declarado de lucro fica, por essa via, fora do âmbito. É esta a lacuna que a proposta de abandonar o '
         'critério do fim lucrativo se destina a fechar.')
    cit(doc, modo,
        ['«Hospedagem com fins lucrativos» o alojamento para reprodução, criação, manutenção e venda de animais '
         'de companhia que vise interesses comerciais ou lucrativos, incluindo-se no alojamento para '
         'manutenção os hotéis e os centros de treino de cães com alojamento.'],
        'Decreto-Lei n.º 276/2001', 'artigo 2.º', 'Al. q) do artigo 2.º do Decreto-Lei n.º 276/2001')

    h2(doc, '4.2', 'Responsabilidade médico-veterinária, registos e instalações')
    para(doc,
         'O alojamento deve dispor de médico veterinário responsável, cujas competências a lei fixa de forma '
         'taxativa.')
    cit(doc, modo,
        ['2 — Ao médico veterinário responsável pelo alojamento compete:',
         'a) A elaboração e a execução de programas e ações que visem a saúde e o bem-estar dos animais e o seu '
         'acompanhamento, bem como a emissão de pareceres relativos à saúde e ao bem-estar dos animais;',
         'b) A orientação técnica do pessoal que cuida dos animais;',
         'c) A colaboração com as autoridades competentes em todas as ações que estas determinarem.'],
        'Decreto-Lei n.º 276/2001', 'artigo 4.º', 'N.º 2 do artigo 4.º do Decreto-Lei n.º 276/2001')
    para(doc,
         'Os registos a conservar durante um ano são igualmente definidos por enumeração.')
    cit(doc, modo,
        ['1 — Os titulares da exploração dos alojamentos para hospedagem de animais de companhia, com ou sem '
         'fins lucrativos, com fins médico-veterinários e os centros de recolha devem manter, pelo prazo de um '
         'ano, os seguintes registos:',
         'a) A identificação do detentor do animal, designadamente nome e morada;',
         'b) A identificação dos animais, nomeadamente o número de identificação, se aplicável, nome, espécie, '
         'raça, idade e quaisquer sinais particulares, sempre que aplicável;',
         'c) O número de animais por espécie;',
         'd) O movimento mensal, nomeadamente registos relativos à origem e às datas das entradas, nascimentos, '
         'mortes e, ainda, datas de saída e destino dos animais.'],
        'Decreto-Lei n.º 276/2001', 'artigo 5.º', 'N.º 1 do artigo 5.º do Decreto-Lei n.º 276/2001')
    para(doc,
         'Quanto às instalações, o diploma exige compartimentação individualizada. É esta a norma sobre a qual '
         'incidiu a ponderação técnica referida no ponto 3, e convém que seja lida no seu teor exato, por ser '
         'frequentemente parafraseada de modo inexato.')
    cit(doc, modo,
        ['1 — Os alojamentos no âmbito deste capítulo devem possuir instalações individualizadas destinadas à '
         'armazenagem de alimentos e equipamento limpo e à lavagem e recolha de material.',
         '2 — Os alojamentos para a reprodução/criação, para além do disposto no número anterior, devem possuir '
         'instalações individualizadas destinadas à maternidade e à criação até à idade adulta, a quarentena, a '
         'enfermaria, o manuseamento de alimentos e à higienização dos animais.'],
        'Decreto-Lei n.º 276/2001', 'artigo 25.º', 'N.os 1 e 2 do artigo 25.º do Decreto-Lei n.º 276/2001')
    para(doc,
         'O mesmo artigo impõe ainda enriquecimento ambiental e área de recreio para cães e gatos, e remete os '
         'parâmetros dimensionais para o anexo I do diploma. É daqui, e não de qualquer outro diploma, que '
         'resulta a capacidade admissível de um alojamento.')
    cit(doc, modo,
        ['5 — Os alojamentos referidos ao abrigo deste capítulo devem possuir estruturas e objetos que permitam '
         'enriquecer o meio ambiente, nomeadamente prateleiras, poleiros, ninhos, esconderijos e material para '
         'entretenimento dos animais conforme as espécies e o seu grau de desenvolvimento, consoante se trate '
         'de adultos, jovens ou fêmeas com ninhadas. Para além disso, os alojamentos destinados a cães e gatos '
         'devem também possuir área de recreio, coberta ou descoberta.',
         '6 — Os alojamentos referidos neste capítulo devem obedecer aos parâmetros mínimos adequados à '
         'espécie, nomeadamente os constantes do anexo i do presente diploma, do qual faz parte integrante.'],
        'Decreto-Lei n.º 276/2001', 'artigo 25.º', 'N.os 5 e 6 do artigo 25.º do Decreto-Lei n.º 276/2001')

    h2(doc, '4.3', 'Decreto-Lei n.º 314/2003: enquadramento e delimitação')
    para(doc,
         'O Decreto-Lei n.º 314/2003 aprova o Programa Nacional de Luta e Vigilância Epidemiológica da Raiva '
         'Animal e Outras Zoonoses e estabelece as regras relativas à posse e detenção, comércio, exposições e '
         'entrada em território nacional de animais suscetíveis à raiva. Releva para esta matéria por dois '
         'motivos: fixa limites ao número de animais alojados por fogo e impõe documentação sanitária nos '
         'estabelecimentos de comércio.')
    cit(doc, modo,
        ['1 — O alojamento de cães e gatos em prédios urbanos, rústicos ou mistos, fica sempre condicionado à '
         'existência de boas condições do mesmo e ausência de riscos hígio-sanitários relativamente à '
         'conspurcação ambiental e doenças transmissíveis ao homem.',
         '2 — Nos prédios urbanos podem ser alojados até três cães ou quatro gatos adultos por cada fogo, não '
         'podendo no total ser excedido o número de quatro animais, excepto se, a pedido do detentor, e '
         'mediante parecer vinculativo do médico veterinário municipal e do delegado de saúde, for autorizado '
         'alojamento até ao máximo de seis animais adultos, desde que se verifiquem todos os requisitos '
         'hígio-sanitários e de bem-estar animal legalmente exigidos.',
         '4 — Nos prédios rústicos ou mistos podem ser alojados até seis animais adultos, podendo tal número '
         'ser excedido se a dimensão do terreno o permitir e desde que as condições de alojamento obedeçam aos '
         'requisitos estabelecidos no n.º 1.'],
        'Decreto-Lei n.º 314/2003', 'artigo 3.º',
        'N.os 1, 2 e 4 do artigo 3.º do Decreto-Lei n.º 314/2003')
    para(doc,
         'Estes limites regulam a detenção doméstica. Não constituem limiar de capacidade dos estabelecimentos '
         'de criação nem condicionam o acesso à atividade. Os fundamentos desta leitura desenvolvem-se em anexo '
         'autónomo; sintetizam-se aqui os essenciais.')
    bullets(doc, [
        '**Objeto e destinatário.** O diploma é legislação sanitária de luta contra a raiva. A epígrafe do '
        'artigo 3.º é «Detenção de cães e gatos» e o seu destinatário é o detentor, referido ao fogo. O '
        'Decreto-Lei n.º 276/2001 tem por objeto o exercício de uma atividade.',

        '**Articulação expressa feita pelo legislador.** O Decreto-Lei n.º 315/2003, publicado no mesmo dia do '
        'Decreto-Lei n.º 314/2003, alterou o Decreto-Lei n.º 276/2001 para excecionar da definição de '
        '«hospedagem sem fins lucrativos» as fracções autónomas em regime de propriedade horizontal a que se '
        'refere o n.º 3 do artigo 3.º do diploma da raiva. Confrontado com a coexistência dos dois regimes, o '
        'legislador subtraiu a detenção doméstica ao conceito de alojamento sujeito a título de acesso, em vez '
        'de a converter em limite de capacidade.',

        '**Leitura confirmada pela doutrina.** A propósito do mesmo artigo 3.º, sustentou-se que «a limitação '
        'prevista nesta norma vale para efeito de prevenção de zoonoses» e que seria abusivo dela extrair uma '
        'limitação geral aos poderes do proprietário. Se os limites não conformam sequer o direito de '
        'propriedade e as relações de vizinhança, menos podem condicionar o acesso a uma atividade económica '
        'regulada por diploma próprio.',

        '**Critérios logicamente independentes.** O Decreto-Lei n.º 276/2001 desencadeia-se com uma fêmea '
        'reprodutora; o Decreto-Lei n.º 314/2003 com o quarto animal adulto no fogo. Pode haver atividade sem '
        'excesso de lotação e lotação sem atividade.',

        '**A capacidade tem regime próprio.** É declarada na mera comunicação prévia e aferida pelos parâmetros '
        'do anexo I do Decreto-Lei n.º 276/2001, por força do n.º 6 do artigo 25.º. A lei especial dos '
        'alojamentos é essa.',

        '**Consequência da tese contrária.** Se os limites por fogo valessem como capacidade dos '
        'estabelecimentos, nenhum criador em prédio urbano poderia deter mais de quatro animais adultos, e o '
        'limiar europeu de cinco fêmeas reprodutoras seria inaplicável em meio urbano. O resultado contraria a '
        'arquitetura do Regulamento e a do próprio projeto de regime.',

        '**Classificação predial é critério tributário.** Prédio urbano, rústico e misto são categorias do '
        'Código do Imposto Municipal sobre Imóveis. Fazer depender a licitude de uma atividade económica da '
        'matriz predial não encontra apoio na lei nem resiste a um juízo de proporcionalidade.',

        '**O direito da União afasta a relevância do tipo de prédio.** O Regulamento define estabelecimento de '
        'criação como qualquer instalação ou estrutura, incluindo casas particulares, onde são mantidos cães ou '
        'gatos para fins de reprodução com vista à colocação da sua descendência no mercado.',
    ])
    para(doc,
         'O que o Decreto-Lei n.º 314/2003 efetivamente impõe a quem comercializa consta do seu artigo 5.º e '
         'esgota-se em documentação sanitária, identificação eletrónica e profilaxias. Não regula a criação nem '
         'a reprodução.')
    cit(doc, modo,
        ['1 — Os cães e gatos que se encontrem em estabelecimentos destinados ao seu comércio devem estar '
         'acompanhados do respectivo boletim sanitário de cães e gatos, onde deve estar aposta a etiqueta '
         'autocolante comprovativa da identificação electrónica, quando aplicável, e ter asseguradas as acções '
         'de profilaxia médica e sanitária obrigatórias ou consideradas adequadas à saúde e idade dos animais '
         'pelo médico veterinário.'],
        'Decreto-Lei n.º 314/2003', 'artigo 5.º', 'N.º 1 do artigo 5.º do Decreto-Lei n.º 314/2003')

    # ------------------------------------------------------------------ 5
    h1(doc, '5.', 'Regulamento (UE) 2026/1818')
    para(doc,
         'O Regulamento é diretamente aplicável, sem transposição. Foi publicado no Jornal Oficial de 10 de '
         'agosto de 2026 e entra em vigor no vigésimo dia seguinte, mas só é aplicável a partir de 31 de agosto '
         'de 2028, com diferimentos até 2036 que o ponto 5.6 detalha.')

    h2(doc, '5.1', 'Conceitos operativos')
    para(doc,
         'O Regulamento não define criador. Regula estabelecimentos e operadores, e determina a sujeição pela '
         'colocação no mercado.')
    cit(doc, modo,
        ['«Estabelecimento de criação», qualquer instalação ou estrutura, incluindo casas particulares, onde '
         'são mantidos cães ou gatos para fins de reprodução com vista à colocação da sua descendência no '
         'mercado.',
         '«Operador», qualquer pessoa singular ou coletiva que coloca cães ou gatos no mercado e é responsável '
         'por um estabelecimento de criação, por um estabelecimento de venda ou por um abrigo e pelos cães ou '
         'gatos aí detidos, ou que coloca cães ou gatos num lar de acolhimento e é responsável pelos cães ou '
         'gatos aí detidos.',
         '«Colocação no mercado», a venda, oferta para fins de venda, distribuição ou qualquer outra forma de '
         'transferência de propriedade ou responsabilidade relativa a cães e gatos, quer a título oneroso quer '
         'a título gratuito, assim como a publicidade de cães e gatos para esses fins, com exceção das doações '
         'ocasionais a intervalos irregulares por pessoas singulares que não sejam operadores sem publicidade '
         'em linha.'],
        'Regulamento (UE) 2026/1818', 'artigo 4.º', 'Artigo 4.º do Regulamento (UE) 2026/1818')
    para(doc,
         'A exceção final merece registo, por ser a única margem de informalidade que o direito da União '
         'contém em matéria de acesso: quem faça doações ocasionais, a intervalos irregulares e sem '
         'publicidade em linha, não coloca no mercado, não é operador e não está sujeito ao Capítulo II. Essa '
         'margem resulta do texto europeu e não de opção nacional. Permanece em apreciação interna se a '
         'legislação nacional deve fechá-la, ao abrigo do artigo 30.º.')

    h2(doc, '5.2', 'O regime reduzido do artigo 5.º')
    para(doc,
         'O artigo 5.º não exclui do Regulamento os estabelecimentos de criação de menor dimensão. Sujeita-os a '
         'uma lista positiva e taxativa de obrigações. Tudo o que dela não conste deixa de lhes ser exigível '
         'pelo direito da União.')
    cit(doc, modo,
        ['1 — Um estabelecimento de criação em que não sejam produzidas mais de duas ninhadas por ano civil '
         'para colocação no mercado apenas está sujeito às obrigações previstas no artigo 6.º, no artigo 7.º, '
         'n.os 1, 3, 4 e 5, nos artigos 8.º, 9.º e 11.º, no artigo 14.º, n.os 2, 3 e 4, no artigo 15.º, n.os 3, '
         '4 e 8, no artigo 16.º, n.º 1, alíneas b), c) e d), no artigo 17.º, n.º 2, 3, 5 e 7, no artigo 18.º, '
         'no artigo 19.º, n.º 1 e nos pontos 3 e 4.3 do anexo I.'],
        'Regulamento (UE) 2026/1818', 'artigo 5.º', 'N.º 1 do artigo 5.º do Regulamento (UE) 2026/1818')
    para(doc,
         'O quadro seguinte traduz essa lista. A leitura conjugada com o artigo 33.º impõe uma advertência: o '
         'regime reduzido dispensa obrigações de bem-estar substantivas, e não apenas formalidades.')
    ok = {2: OK_BG}
    no = {2: NO_BG}
    tabela(doc,
           ['Disposição', 'Matéria', 'Até 2 ninhadas'],
           [
            ['Artigo 6.º', 'Princípios gerais de bem-estar', 'Aplicável'],
            ['Artigo 7.º, n.os 1, 3, 4 e 5',
             'Responsabilidade do operador; proibição de crueldade e de abandono; realojamento na cessação de '
             'atividade', 'Aplicável'],
            ['Artigo 7.º, n.os 6 e 7',
             'Número suficiente de tratadores; monitorização por indicadores baseados nos animais',
             'Não aplicável'],
            ['Artigo 8.º',
             'Estratégia de criação; conformações extremas; consanguinidade; híbridos', 'Aplicável'],
            ['Artigo 9.º', 'Notificação e registo do estabelecimento', 'Aplicável'],
            ['Artigo 10.º', 'Aprovação do estabelecimento', 'Não aplicável'],
            ['Artigo 11.º', 'Informação ao adquirente e historial clínico e sanitário', 'Aplicável'],
            ['Artigo 12.º', 'Competências dos tratadores de animais', 'Não aplicável'],
            ['Artigo 13.º', 'Visitas de aconselhamento para assegurar o bem-estar', 'Não aplicável'],
            ['Artigo 14.º, n.os 2, 3 e 4',
             'Água e alimento adequados; limpeza e conceção das instalações de alimentação', 'Aplicável'],
            ['Artigo 14.º, n.º 1, e anexo I, ponto 1', 'Frequência mínima de alimentação', 'Não aplicável'],
            ['Artigo 15.º, n.os 3, 4 e 8',
             'Proibição de contentores; acesso diário ao exterior de pelo menos uma hora; ritmo circadiano',
             'Aplicável'],
            ['Artigo 15.º, n.os 1, 2, 5, 6 e 7, e anexo I, ponto 2',
             'Espaço disponível mínimo; temperatura das áreas de parto; iluminação; adequação e limpeza do '
             'edifício e do equipamento; zonas de descanso; proteção climática; gatis; zona termicamente '
             'neutra; aquecimento e arrefecimento', 'Não aplicável'],
            ['Artigo 16.º, n.º 1, als. b), c) e d)',
             'Cuidados de saúde, isolamento de animais doentes e assistência médico-veterinária', 'Aplicável'],
            ['Artigo 16.º, n.º 1, al. a), e n.º 2',
             'Inspeção dos animais pelos tratadores pelo menos uma vez por dia; medidas de proteção da saúde '
             'nos estabelecimentos de criação', 'Não aplicável'],
            ['Artigo 17.º, n.os 2, 3, 5 e 7',
             'Não restrição dos movimentos naturais; proibição de amarrar por mais de uma hora; condições para '
             'comportamentos sociais; disponibilização de enriquecimentos', 'Aplicável'],
            ['Artigo 17.º, n.os 1 e 6, e anexo I, pontos 4.1 e 4.2',
             'Especificações de socialização e de enriquecimento', 'Não aplicável'],
            ['Artigo 18.º', 'Práticas dolorosas e mutilações', 'Aplicável'],
            ['Artigo 19.º, n.º 1', 'Espetáculos, exposições e concursos de beleza', 'Aplicável'],
            ['Anexo I, ponto 3',
             'Limites reprodutivos: idade mínima, três ninhadas em dois anos, período de recuperação, duas '
             'cesarianas, exame veterinário em idade avançada', 'Aplicável'],
            ['Anexo I, ponto 4.3', 'Idade mínima de separação das crias', 'Aplicável'],
           ],
           [Cm(4.4), Cm(9.6), Cm(2.6)],
           shades=[ok, ok, no, ok, ok, no, ok, no, no, ok, no, ok, no, ok, no, ok, no, ok, ok, ok, ok])

    h2(doc, '5.3', 'O que não admite redução por escala')
    para(doc,
         'A epígrafe do artigo 5.º é «Isenções das obrigações definidas no presente capítulo». O seu âmbito '
         'esgota-se no Capítulo II. As obrigações de identificação e registo dos animais e de publicidade em '
         'linha integram o Capítulo III e aplicam-se sem qualquer modulação por dimensão do estabelecimento. É '
         'esta a resposta técnica à objeção de que um regime proporcional favoreceria o comércio ilegal.')
    cit(doc, modo,
        ['1 — Todos os cães e gatos detidos em estabelecimentos, colocados no mercado ou detidos por um '
         'proprietário de animais de companhia ou por qualquer outra pessoa singular ou coletiva devem ser '
         'identificados individualmente através de um único transponder injetável que contenha um circuito '
         'integrado legível que cumpra os requisitos estabelecidos no anexo II.',
         '2 — Os operadores asseguram que os cães e gatos nascidos nos seus estabelecimentos sejam '
         'identificados individualmente no prazo de três meses após o seu nascimento e sempre antes da data da '
         'sua colocação no mercado.'],
        'Regulamento (UE) 2026/1818', 'artigo 20.º',
        'N.os 1 e 2 do artigo 20.º do Regulamento (UE) 2026/1818')
    para(doc,
         'A universalidade do n.º 1 tem consequência prática relevante: mesmo quem beneficie da exceção das '
         'doações ocasionais está obrigado a identificar e a registar os animais. A margem de informalidade '
         'existente no direito da União respeita ao acesso à atividade, nunca à rastreabilidade do animal.')

    h2(doc, '5.4', 'Notificação, registo e aprovação')
    para(doc,
         'A notificação do estabelecimento é obrigação sem exceções, aplicável desde a primeira ninhada '
         'colocada no mercado. O seu conteúdo coincide, em larga medida, com o da mera comunicação prévia '
         'nacional, o que permite absorvê-la sem criar procedimento novo.')
    cit(doc, modo,
        ['1 — Os operadores notificam as autoridades competentes da sua atividade, facultando pelo menos as '
         'seguintes informações para cada um dos seus estabelecimentos:',
         'a) O nome, o endereço e dados de contacto do operador;',
         'b) A localização do estabelecimento;',
         'c) O tipo de estabelecimento: estabelecimento de criação, estabelecimento de venda, abrigo ou lar de '
         'acolhimento;',
         'd) A espécie e, para os estabelecimentos de criação, as raças dos cães ou gatos detidos no '
         'estabelecimento;',
         'e) A capacidade do estabelecimento, expressa em termos de número máximo de cães e gatos que podem ser '
         'detidos no estabelecimento;',
         'f) No caso dos estabelecimentos de criação, o número estimado de ninhadas a colocar no mercado por '
         'ano.'],
        'Regulamento (UE) 2026/1818', 'artigo 9.º', 'N.º 1 do artigo 9.º do Regulamento (UE) 2026/1818')
    para(doc,
         'Acima dos limiares, o Regulamento exige aprovação prévia, e essa aprovação assenta em inspeção. Trata-'
         'se de controlo prévio ao local, e não de mera verificação documental.')
    cit(doc, modo,
        ['1 — Os operadores de estabelecimentos de criação que produzam ou tencionem produzir mais de cinco '
         'ninhadas por ano civil, ou que, a qualquer momento, detenham um total combinado de mais de cinco '
         'cadelas reprodutoras ou gatas reprodutoras, só podem colocar cães ou gatos no mercado após aprovação '
         'do seu estabelecimento de criação pela autoridade competente.',
         '2 — A autoridade competente efetua inspeções no local para verificar se o estabelecimento de criação '
         'cumpre os requisitos do presente regulamento. Os Estados-Membros podem autorizar que estas inspeções '
         'sejam realizadas à distância, desde que o meio de comunicação à distância utilizado permita recolher '
         'provas suficientes para que a autoridade competente realize inspeções fiáveis. A autoridade '
         'competente só deve conceder certificados de aprovação a estabelecimentos de criação que cumpram os '
         'requisitos do presente regulamento.'],
        'Regulamento (UE) 2026/1818', 'artigo 10.º',
        'N.os 1 e 2 do artigo 10.º do Regulamento (UE) 2026/1818')

    h2(doc, '5.5', 'Reprodução e crias')
    para(doc,
         'Os limites reprodutivos constam do ponto 3 do anexo I e aplicam-se integralmente aos estabelecimentos '
         'até duas ninhadas, tal como o artigo 8.º. É um dos domínios em que o regime reduzido não cede, e é '
         'também aquele em que o direito da União inova face ao regime nacional.')
    tabela(doc,
           ['Matéria', 'Regra'],
           [
            ['Início da reprodução',
             'Gatas a partir dos 10 meses. Cadelas não antes do segundo cio.'],
            ['Frequência',
             'Máximo de três ninhadas, incluindo nados-mortos, num período de dois anos.'],
            ['Recuperação',
             'Período mínimo de um ano após três ninhadas em dois anos.'],
            ['Cesarianas',
             'A fêmea submetida a duas cesarianas deixa de ser utilizada para a reprodução.'],
            ['Idade avançada',
             'Exame físico e confirmação escrita de médico veterinário para cadelas com oito ou mais anos e '
             'gatas com seis ou mais anos.'],
            ['Separação das crias',
             'Cachorros: oito semanas. Gatinhos em estabelecimento de criação: doze semanas. Antecipação apenas '
             'por parecer escrito de médico veterinário.'],
            ['Conformações extremas',
             'Proibida a utilização para reprodução de animais com características de conformação extremas de '
             'elevado risco, com consulta prévia de médico veterinário ou pessoa qualificada independente.'],
            ['Consanguinidade e híbridos',
             'Proibida a reprodução entre progenitores e descendência, entre irmãos, entre meios-irmãos ou '
             'entre avós e netos, salvo aprovação para preservação de raças locais com património genético '
             'limitado. Proibida a reprodução para produção de híbridos.'],
           ],
           [Cm(4.3), Cm(12.3)])

    h2(doc, '5.6', 'Calendário de aplicação')
    para(doc,
         'O Regulamento é hoje direito vigente, mas quase nenhuma das suas obrigações é ainda exigível. A '
         'distinção entre entrada em vigor e início de aplicação é essencial para situar corretamente o debate '
         'e para calendarizar a adaptação nacional.')
    tabela(doc,
           ['Data', 'Disposições'],
           [
            ['31.08.2028',
             'Regra geral, incluindo o artigo 5.º, o artigo 9.º (notificação e registo de estabelecimentos), o '
             'artigo 20.º (identificação e registo dos animais) e o anexo I, ponto 3 (limites reprodutivos). '
             'Termo do prazo do n.º 2 do artigo 30.º para comunicação das regras nacionais mais restritivas.'],
            ['31.08.2029', 'Artigo 16.º (saúde).'],
            ['01.07.2030',
             'Artigo 8.º, n.º 2 (conformações extremas). Artigo 21.º, n.º 3, e artigo 23.º, n.º 1, a partir de '
             '31.08.2030.'],
            ['31.08.2031',
             'Artigo 15.º (alojamento) e, com ele, o anexo I, ponto 2 (espaço, temperatura e iluminação). '
             'Artigo 22.º, n.º 1, als. a), b) e c); artigo 23.º, n.os 3 e 4; artigo 26.º, n.os 1, 2 e 3.'],
            ['31.08.2033', 'Artigo 12.º, n.os 2 e 3 (competências dos tratadores).'],
            ['31.08.2034', 'Artigo 10.º (aprovação dos estabelecimentos acima dos limiares).'],
            ['01.07.2036', 'Artigo 8.º, n.º 1 (genótipos). Artigo 26.º, n.º 4, a partir de 31.08.2036.'],
           ],
           [Cm(2.8), Cm(13.8)])
    nota(doc, [
        'O regime de aprovação previsto no artigo 10.º, que constitui o escalão superior do modelo proposto no '
        'ponto 7, só é aplicável a partir de **31 de agosto de 2034**. Até lá, o controlo dos estabelecimentos '
        'de maior dimensão assenta no direito nacional, designadamente na permissão administrativa e nos '
        'controlos oficiais realizados nos termos do Regulamento (UE) 2017/625.'])

    # ------------------------------------------------------------------ 6
    h1(doc, '6.', 'Projeto de Regime Geral do Animal de Companhia')
    para(doc,
         'O projeto consolida o regime nacional e adapta os procedimentos ao Regulamento. Na versão de trabalho '
         'em apreciação, mantém os dois títulos de acesso existentes e redistribui-os em função da escala, no '
         'sentido do agravamento.')

    h2(doc, '6.1', 'Títulos de acesso')
    cit(doc, modo,
        ['1 — Sem prejuízo do disposto no Decreto-Lei n.º 48/2011, de 1 de abril, alterado pelo Decreto-Lei n.º '
         '10/2015, de 16 de janeiro, quanto aos estabelecimentos de comércio a retalho de animais de companhia, '
         'o exercício da atividade de exploração de estabelecimentos depende de:',
         'a) Mera comunicação prévia, no caso dos centros de recolha oficial, abrigos, estabelecimentos de '
         'reprodução e criação, e de manutenção, com exceção dos destinados exclusivamente à venda, sem '
         'prejuízo do disposto na alínea seguinte;',
         'b) Permissão administrativa, no caso dos estabelecimentos destinados à reprodução e criação de '
         'animais potencialmente perigosos, nomeadamente de cães das raças consideradas como potencialmente '
         'perigosas, bem como, os estabelecimentos de criação que produzam ou tencionem produzir mais de cinco '
         'ninhadas por ano civil, ou que, a qualquer momento, detenham um total combinado de mais de cinco '
         'cadelas ou gatas reprodutoras.'],
        'Projeto de RGAC', 'artigo 45.º',
        'N.º 1 do artigo 45.º do projeto de RGAC, 1.ª revisão formal da DAJA, versão de trabalho de junho de 2026')
    para(doc,
         'O projeto absorve o artigo 9.º do Regulamento na mera comunicação prévia e o artigo 10.º na permissão '
         'administrativa. Não cria figura nova. O efeito líquido, face ao direito vigente, é de agravamento: '
         'estabelecimentos hoje sujeitos a mera comunicação prévia passam a carecer de permissão administrativa '
         'quando ultrapassem os limiares europeus.')

    h2(doc, '6.2', 'A opção mais restritiva e o artigo 30.º')
    para(doc,
         'A versão de trabalho do projeto não contém a redução do artigo 5.º. A expressão «duas ninhadas» não '
         'ocorre no seu articulado. A consequência é que todas as obrigações de bem-estar e de rastreabilidade '
         'se aplicam a qualquer estabelecimento de criação, independentemente do número de ninhadas ou de '
         'fêmeas reprodutoras. Trata-se de uma opção deliberada, que o Regulamento expressamente comporta.')
    cit(doc, modo,
        ['1 — O presente regulamento não obsta a que os Estados-Membros mantenham ou adotem regras nacionais '
         'mais restritivas que visem uma proteção mais ampla do bem-estar dos cães e gatos detidos em '
         'estabelecimentos e uma maior rastreabilidade dos cães e gatos, desde que essas regras não sejam '
         'incompatíveis com o presente regulamento e não interfiram com o correto funcionamento do mercado '
         'interno.',
         '2 — Os Estados-Membros informam, até 31 de agosto de 2028, a Comissão acerca de quaisquer regras '
         'nacionais mais restritivas que tencionem manter em conformidade com o n.º 1 do presente artigo.'],
        'Regulamento (UE) 2026/1818', 'artigo 30.º',
        'N.os 1 e 2 do artigo 30.º do Regulamento (UE) 2026/1818')
    destaque(doc, [
        'Duas consequências devem ser retidas. Primeira: a não concessão da redução do artigo 5.º é uma regra '
        'nacional mais restritiva e **carece de comunicação à Comissão até 31 de agosto de 2028**. Segunda: '
        'qualquer aligeiramento que venha a ser ponderado quanto a instalações parte de um patamar nacional '
        'já superior ao europeu, e não de uma derrogação ao direito da União.'])

    h2(doc, '6.3', 'Matérias por consolidar')
    bullets(doc, [
        'Atualização das remissões internas e das referências ao Regulamento, hoje provisórias no articulado.',
        'Harmonização entre os limites reprodutivos do anexo I do Regulamento e as opções do anexo técnico '
        'nacional.',
        'Coerência entre a proibição de contentores do n.º 3 do artigo 15.º do Regulamento e as tabelas '
        'nacionais que ainda empregam a expressão «gaiola».',
        'Articulação da definição de criador com o regime de registo. A definição em projeto conserva a '
        'referência a atividade comercial, que é incompatível com o propósito assumido de abandonar o critério '
        'do fim lucrativo.',
        'Decisão quanto à exceção das doações ocasionais na definição de colocação no mercado, que o projeto '
        'transcreve do Regulamento e que constitui a única margem de informalidade em matéria de acesso.',
        'Delimitação dos requisitos estruturais suscetíveis de equivalência funcional, nos termos do ponto 7.3.',
    ])
    nota(doc, [
        'A hipótese de caducidade quinquenal do registo, por vezes referida a propósito deste projeto, não '
        'constitui matéria do articulado. Consta de uma nota de trabalho dirigida ao serviço jurídico, que '
        'propõe ponderar um regime de renovação da comunicação ou da permissão ao fim de cinco anos, com a '
        'finalidade de manter a lista de estabelecimentos atualizada para efeitos de afetação de meios em '
        'situações de catástrofe ou emergência. Deve ser tratada como questão de desenho registral, não como '
        'requisito de acesso à atividade.'])

    # ------------------------------------------------------------------ 7
    h1(doc, '7.', 'Modelo nacional')

    h2(doc, '7.1', 'Escalões')
    para(doc,
         'O Regulamento estabelece dois patamares: o regime reduzido do artigo 5.º e a aprovação do artigo '
         '10.º. O escalão intermédio do quadro seguinte é construção nacional, destinada a tornar visível a '
         'faixa que, não beneficiando da redução europeia, também não atinge os limiares de aprovação. Em todos '
         'os escalões o título de acesso gera número de identificação e publicitação, e em todos se aplica o '
         'direito nacional.')
    tabela(doc,
           ['Escalão', 'Critério', 'Título de acesso', 'Regime material'],
           [
            ['Pequena escala',
             'Até 2 ninhadas por ano civil colocadas no mercado',
             'Mera comunicação prévia, com registo no SIAC',
             'Regime nacional integral. O projeto não acolhe a redução do artigo 5.º do Regulamento.'],
            ['Regime geral',
             'De 3 a 5 ninhadas por ano civil, sem exceder 5 fêmeas reprodutoras',
             'Mera comunicação prévia, com registo no SIAC',
             'Regime nacional integral e regime geral do Regulamento.'],
            ['Sujeito a aprovação',
             'Mais de 5 ninhadas por ano civil ou mais de 5 cadelas ou gatas reprodutoras',
             'Permissão administrativa, absorvendo a aprovação do artigo 10.º',
             'Regime integral, com inspeção prévia ao local e lista pública de estabelecimentos aprovados, a '
             'partir de 31.08.2034.'],
            ['Animais potencialmente perigosos',
             'Reprodução e criação de animais potencialmente perigosos, independentemente da escala',
             'Permissão administrativa',
             'Requisitos específicos de segurança, reprodução, registo e comércio.'],
           ],
           [Cm(3.0), Cm(4.3), Cm(4.0), Cm(5.3)])
    nota(doc, [
        'O número de identificação e a publicitação do criador não são privativos do escalão superior. '
        'Resultam hoje dos n.os 11 e 12 do artigo 3.º do Decreto-Lei n.º 276/2001 e abrangem todos os '
        'criadores registados. A lista pública prevista no n.º 3 do artigo 10.º do Regulamento é adicional e '
        'específica dos estabelecimentos aprovados, e não substitui aquela.'])

    h2(doc, '7.2', 'Núcleo não dispensável')
    para(doc,
         'Qualquer modulação por escala deve deixar intacto o conjunto seguinte, que é o que assegura a '
         'identificação do responsável, a rastreabilidade do animal e a possibilidade de controlo.')
    bullets(doc, [
        'Título de acesso, número de identificação e publicitação do criador.',
        'Declaração da capacidade máxima, das espécies e raças, do número de fêmeas reprodutoras e do número '
        'estimado de ninhadas a colocar no mercado por ano.',
        'Indicação do médico veterinário responsável e exercício efetivo das competências do n.º 2 do artigo '
        '4.º do Decreto-Lei n.º 276/2001.',
        'Identificação individual das crias até aos três meses e sempre antes da colocação no mercado, com '
        'registo em nome do operador e atualização na transmissão.',
        'Registo de nascimentos, mortes, entradas, saídas, origem e destino dos animais.',
        'Observância dos limites reprodutivos do ponto 3 do anexo I do Regulamento e das proibições do artigo '
        '8.º.',
        'Alimentação, água, higiene, saúde, exercício e socialização adequados.',
        'Informação escrita ao adquirente, incluindo historial clínico e sanitário.',
        'Elementos de verificação nos anúncios em linha.',
        'Acesso das autoridades para controlo e sujeição a medidas corretivas.',
    ])

    h2(doc, '7.3', 'Margem de simplificação')
    para(doc,
         'A simplificação admissível incide sobre o modo de cumprimento dos requisitos estruturais, não sobre '
         'as obrigações materiais. Concretiza-se em equivalência funcional documentada, aferida em função do '
         'número, espécie, idade e condição dos animais. O critério de fronteira é verificável: uma solução é '
         'admissível se preservar a função sanitária ou comportamental que a exigência original visa, e não o '
         'é se a suprimir.')
    tabela(doc,
           ['Exigência', 'Equivalência admissível', 'Limite'],
           [
            ['Instalação individualizada para armazenagem de alimentos e equipamento limpo (n.º 1 do artigo '
             '25.º)',
             'Armazenamento protegido e separado em compartimento partilhado, com separação física e '
             'identificação',
             'Contacto entre alimento, material sujo e produtos de limpeza'],
            ['Instalação individualizada para lavagem e recolha de material (n.º 1 do artigo 25.º)',
             'Zona delimitada com ponto de água e protocolo de limpeza documentado',
             'Ausência de ponto de água ou de separação face às áreas de alojamento'],
            ['Instalação individualizada para manuseamento de alimentos (n.º 2 do artigo 25.º)',
             'Superfície de uso multifuncional em momentos distintos, com protocolo de higienização registado',
             'Uso simultâneo ou sem protocolo verificável'],
            ['Enfermaria e quarentena (n.º 2 do artigo 25.º)',
             'Compartimento único com capacidade de isolamento efetivo, quando o número de animais o permita',
             'Impossibilidade de isolar um animal doente ou recém-chegado'],
            ['Maternidade e criação até à idade adulta (n.º 2 do artigo 25.º)',
             'Área dedicada dentro do espaço doméstico, com possibilidade de a mãe se afastar das crias',
             'Ausência de área reservada ou de refúgio para a fêmea'],
           ],
           [Cm(5.0), Cm(6.4), Cm(5.2)])
    destaque(doc, [
        'Não é admissível equivalência que reduza o espaço disponível, comprometa o isolamento sanitário, '
        'impeça o exercício e a socialização, dificulte a inspeção dos animais ou fragilize a rastreabilidade. '
        'A proporcionalidade aplica-se à forma, nunca ao conteúdo da obrigação.'])

    # ------------------------------------------------------------------ 8
    pagebreak(doc)
    h1(doc, '8.', 'Elementos de suporte à audição')
    para(doc,
         'Reúnem-se as questões previsivelmente suscitadas, a resposta correspondente e a norma que a sustenta. '
         'As respostas remetem para os pontos anteriores, onde as citações constam na íntegra.')

    qa = [
        ('Está prevista a criação de uma figura de criador informal?',
         'Não. Nem o direito vigente, nem o Regulamento, nem o projeto de regime preveem o exercício da '
         'atividade de criação sem título de acesso junto da autoridade competente. O projeto mantém os dois '
         'títulos existentes, a mera comunicação prévia e a permissão administrativa, e alarga o segundo aos '
         'estabelecimentos que ultrapassem os limiares europeus.',
         'Artigo 3.º do Decreto-Lei n.º 276/2001; artigo 45.º do projeto; artigos 9.º e 10.º do Regulamento'),

        ('Que matéria foi então efetivamente ponderada?',
         'A adequação à escala dos requisitos de instalações individualizadas exigidos pelos n.os 1 e 2 do '
         'artigo 25.º do Decreto-Lei n.º 276/2001, concebidos para alojamentos de dimensão significativa. A '
         'ponderação decorreu em sede de grupo de trabalho técnico e não consta da versão do projeto remetida '
         'à tutela. Não incidiu sobre registo, identificação, rastreabilidade ou controlo reprodutivo.',
         'N.os 1 e 2 do artigo 25.º do Decreto-Lei n.º 276/2001'),

        ('Uma solução proporcional é compatível com o direito da União?',
         'É. O artigo 5.º do Regulamento institui ele próprio um regime reduzido para os estabelecimentos até '
         'duas ninhadas por ano civil, dispensando-os, entre outras obrigações, do espaço disponível mínimo, '
         'da temperatura das áreas de parto, da iluminação e das especificações de socialização. A modulação '
         'por escala é opção do legislador europeu, não invenção nacional.',
         'N.º 1 do artigo 5.º do Regulamento'),

        ('O regime nacional em preparação é mais permissivo do que o europeu?',
         'É mais exigente. O projeto não acolhe a redução do artigo 5.º e aplica a totalidade das obrigações a '
         'todos os estabelecimentos de criação. Mesmo a ponderação técnica mais permissiva que chegou a ser '
         'equacionada quanto a instalações permanece acima da linha de base europeia. A opção deve ser '
         'comunicada à Comissão até 31 de agosto de 2028.',
         'Artigo 30.º do Regulamento'),

        ('A medida reduz a fiscalização?',
         'Não altera os poderes nem os deveres de controlo. Os controlos oficiais regem-se pelo Regulamento '
         '(UE) 2017/625 e assentam em análise de risco, independentemente da dimensão do estabelecimento. '
         'Acima dos limiares, o Regulamento acrescenta inspeção prévia ao local como condição de aprovação, '
         'exigência que o direito nacional vigente não contém.',
         'N.º 2 do artigo 10.º do Regulamento'),

        ('A medida facilita o comércio ilegal?',
         'As obrigações de identificação e registo dos animais e os requisitos da publicidade em linha '
         'integram o Capítulo III do Regulamento. O artigo 5.º dispõe apenas sobre o Capítulo II e não lhes é '
         'aplicável. A identificação individual abrange todos os cães e gatos, incluindo os detidos por '
         'particulares. Nenhuma redução por escala atinge a rastreabilidade.',
         'Epígrafe do artigo 5.º; n.º 1 do artigo 20.º; artigo 21.º do Regulamento'),

        ('Um caso recente envolvendo um estabelecimento registado com várias centenas de animais não demonstra '
         'a insuficiência do registo?',
         'Demonstra insuficiência de controlo, não excesso de proporcionalidade. Um estabelecimento dessa '
         'dimensão situa-se muito acima dos limiares do artigo 10.º e integra o escalão sujeito a aprovação '
         'com inspeção prévia ao local. Nada tem em comum com a criação em pequena escala, que é o objeto da '
         'ponderação em causa. O caso reforça a necessidade de capacidade inspetiva e de cruzamento de dados, '
         'e é precisamente isso que o registo universal das ninhadas e a ficha de verificação dos anúncios '
         'visam servir.',
         'N.os 1 e 2 do artigo 10.º do Regulamento'),

        ('Quem cria sem fins lucrativos fica de fora?',
         'Fica, no regime vigente, por efeito da definição de hospedagem com fins lucrativos. É lacuna '
         'identificada e o projeto destina-se a fechá-la, abandonando o critério do fim lucrativo. O '
         'Regulamento segue o mesmo sentido: sujeita quem coloca no mercado, a título oneroso ou gratuito.',
         'Al. q) do artigo 2.º do Decreto-Lei n.º 276/2001; artigo 4.º do Regulamento'),

        ('Subsiste alguma margem de informalidade?',
         'Uma, e resulta do texto europeu: a exceção das doações ocasionais a intervalos irregulares por '
         'pessoas singulares que não sejam operadores, sem publicidade em linha, que ficam fora do conceito de '
         'colocação no mercado e, por essa via, do Capítulo II. Mesmo nesse caso subsiste a obrigação de '
         'identificar e registar o animal. Está em apreciação se a legislação nacional deve fechar essa '
         'margem, ao abrigo do artigo 30.º.',
         'Artigo 4.º e n.º 1 do artigo 20.º do Regulamento'),

        ('A partir de quando se aplica o novo regime?',
         'O Regulamento é aplicável, em regra, a partir de 31 de agosto de 2028. A identificação dos animais e '
         'a notificação dos estabelecimentos aplicam-se nessa data. As exigências de alojamento, incluindo o '
         'espaço disponível mínimo, apenas a partir de 31 de agosto de 2031. A aprovação dos estabelecimentos '
         'acima dos limiares apenas a partir de 31 de agosto de 2034.',
         'Artigo 33.º do Regulamento'),

        ('Os limites de animais por fogo não resolvem a questão da dimensão?',
         'São norma de detenção doméstica, inserida na legislação de luta contra a raiva, e não fixam a '
         'capacidade dos estabelecimentos de criação. A capacidade é declarada na mera comunicação prévia e '
         'aferida pelos parâmetros do anexo I do Decreto-Lei n.º 276/2001. Os fundamentos constam do ponto '
         '4.3 e do anexo autónomo.',
         'Artigo 3.º do Decreto-Lei n.º 314/2003; n.º 6 do artigo 25.º do Decreto-Lei n.º 276/2001'),
    ]
    for q, a, b in qa:
        p = doc.add_paragraph(); spacing(p, 9, 3); keep_together(p)
        font(p.add_run(q), 9.8, HEAD, bold=True)
        pa = doc.add_paragraph(); spacing(pa, 0, 3)
        pa.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        font(pa.add_run(a), 9.8, INK)
        pb = doc.add_paragraph(); spacing(pb, 0, 4)
        font(pb.add_run('Base normativa:  '), 7.8, MUTE, bold=True)
        font(pb.add_run(b), 7.8, MUTE)

    # ------------------------------------------------------------------ 9
    h1(doc, '9.', 'Referências')
    bullets(doc, [
        'Decreto-Lei n.º 276/2001, de 17 de outubro, na redação atual.',
        'Decreto-Lei n.º 314/2003, de 17 de dezembro, na redação atual.',
        'Decreto-Lei n.º 315/2003, de 17 de dezembro.',
        'Regulamento (UE) 2026/1818 do Parlamento Europeu e do Conselho, de 17 de junho de 2026, relativo ao '
        'bem-estar dos cães e dos gatos e à respetiva rastreabilidade (JO L, 2026/1818, de 10.8.2026).',
        'Regulamento (UE) 2016/429 do Parlamento Europeu e do Conselho, de 9 de março de 2016.',
        'Regulamento (UE) 2017/625 do Parlamento Europeu e do Conselho, de 15 de março de 2017.',
        'Projeto de Regime Geral do Animal de Companhia, 1.ª revisão formal da DAJA, versão de trabalho de '
        'junho de 2026.',
    ], marker='·')

    if modo == 'B':
        pagebreak(doc)
        h1(doc, 'Anexo', 'Quadro de concordâncias')
        para(doc,
             'Referência completa de cada citação transcrita no corpo do memorando, pela ordem em que ocorre.')
        linhas = []
        for cod, dip, lev, full in CONCORD:
            curto = full.replace(' do ' + dip, '', 1)
            linhas.append([cod, dip, curto])
        tabela(doc, ['', 'Diploma', 'Referência'], linhas,
               [Cm(1.1), Cm(5.5), Cm(10.0)])
