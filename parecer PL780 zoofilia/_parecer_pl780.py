# -*- coding: utf-8 -*-
"""Parecer DGAV sobre o Projeto de Lei n.º 780/XVII/2.ª (PAN) — ofensas sexuais contra animais.

Registo técnico, incidência sobre animais de companhia. Gerado por gerar_parecer.py.
"""
from _memo_engine import *
from docx.shared import Cm


def construir(doc):
    capa(doc,
         'Direção-Geral de Alimentação e Veterinária',
         'Projeto de Lei n.º 780/XVII/2.ª (PAN)',
         'Criminaliza a prática da zoofilia reforçando a proteção animal e a tutela penal e '
         'contraordenacional — parecer técnico',
         'Divisão com competência em animais de companhia · Processo n.º ____ · Data ____')

    enquadramento(doc, [
        '**Objeto.** Pronúncia sobre o Projeto de Lei n.º 780/XVII/2.ª, apresentado em 22 de setembro de '
        '2026, que altera o artigo 387.º do Código Penal e adita a alínea h) ao n.º 3 do artigo 1.º da Lei '
        'n.º 92/95, de 12 de setembro.',
        '**Âmbito da pronúncia.** O presente parecer incide sobre os animais de companhia, matéria da '
        'competência desta divisão. As observações relativas às normas gerais e às demais espécies são '
        'formuladas a título de indicação, sem prejuízo da pronúncia das unidades competentes.',
        '**Sentido.** Favorável, condicionado à correção das insuficiências identificadas no ponto 5.1.'])

    # ------------------------------------------------------------------ 1
    h1(doc, '1.', 'O que o projeto dispõe')
    numlist(doc, [
        '**Código Penal.** O n.º 3 do artigo 387.º passa a comportar duas alíneas, sob o elemento comum '
        '«sem motivo legítimo»: a al. a) reproduz o crime de maus tratos vigente; a al. b) acrescenta '
        '«Ofender sexualmente um animal de companhia através de cópula, coito anal, coito oral ou a '
        'introdução vaginal, anal ou oral de partes do corpo ou de objetos». Moldura inalterada — prisão de '
        '6 meses a 1 ano ou multa de 60 a 120 dias.',
        '**Lei n.º 92/95.** Adita-se a al. h) ao n.º 3 do artigo 1.º, com fórmula equivalente mas referida '
        'a «animais», sem qualificação de espécie ou afetação.',
    ])
    destaque(doc, [
        'Note-se, para o que segue: a conduta sexual passa a ser punível **sem dependência da prova de dor, '
        'sofrimento ou lesão**. É este o efeito útil da iniciativa, e é o que a legislação vigente não '
        'assegura.'])

    # ------------------------------------------------------------------ 2
    h1(doc, '2.', 'Enquadramento vigente: o que cada norma exige')
    para(doc,
         'A lacuna não se demonstra por argumento, demonstra-se por confronto. O quadro seguinte reúne as '
         'normas hoje mobilizáveis e o pressuposto que cada uma exige.')
    tabela(doc,
           ['Norma', 'Conduta abrangida', 'Pressuposto exigido'],
           [['N.º 1 do art.º 387.º do Código Penal', 'Morte de animal de companhia',
             'Morte consumada'],
            ['N.º 3 do art.º 387.º do Código Penal',
             '«infligir dor, sofrimento ou quaisquer outros maus tratos físicos»',
             '**Resultado provado** — dor, sofrimento ou maus tratos físicos'],
            ['N.ºs 4 e 5 do art.º 387.º do Código Penal',
             'Agravação, incluindo quando o crime seja determinado «para excitação»',
             'Pressupõe o crime-base do n.º 3 provado'],
            ['N.º 1 do art.º 1.º da Lei n.º 92/95', '«violências injustificadas»',
             'Morte, **ou** sofrimento cruel **e** prolongado, **ou** graves lesões'],
            ['Al. a) do n.º 3 do art.º 1.º da Lei n.º 92/95',
             '«actuações que […] ele seja obviamente incapaz de realizar ou que estejam obviamente para '
             'além das suas possibilidades»',
             'Juízo de incapacidade manifesta; fora de emergência'],
            ['Al. e) do n.º 3 do art.º 1.º da Lei n.º 92/95',
             'Utilização em «filmagens» e atividades semelhantes',
             '«dor ou sofrimentos consideráveis»'],
            ['Art.º 6.º do Decreto-Lei n.º 276/2001', 'Dever especial de cuidado do detentor',
             '**Sem sanção quando o perigo recaia sobre o próprio animal** (ver ponto 3)'],
            ['N.º 3 do art.º 1305.º-A do Código Civil', 'Limite ao direito de propriedade',
             'Maus tratos «que resultem em sofrimento injustificado, abandono ou morte»; norma civil, não '
             'sancionatória'],
            ['Art.º 212.º do Código Penal (dano)', 'Via utilizada na prática',
             'Tutela o património do proprietário; inaplicável se o agente for o detentor'],
           ],
           [Cm(4.6), Cm(6.0), Cm(5.6)])

    # ------------------------------------------------------------------ 3
    h1(doc, '3.', 'A lacuna que a iniciativa supre')
    numlist(doc, [
        '**Toda a tutela vigente é de resultado.** Nenhuma das normas do quadro pune o acto em si. Exigem '
        'morte, lesão grave, sofrimento cruel e prolongado, dor ou sofrimento consideráveis, perigo para '
        'terceiro, ou dano patrimonial. A ofensa sexual que não deixe marca física demonstrável — que a '
        'literatura pericial indica ser frequente — não encontra tipo.',
        '**O dever de cuidado não está sancionado quando o perigo recai sobre o próprio animal.** O artigo '
        '6.º do Decreto-Lei n.º 276/2001 impõe ao detentor o dever de cuidar «de forma a não pôr em causa '
        'os parâmetros de bem-estar». Mas as contraordenações que o sancionam são apenas duas: a al. j) do '
        'n.º 1 do artigo 68.º, quando a violação «crie perigo para a vida ou integridade física de outro '
        'animal», e a al. b) do n.º 2, quando crie perigo «de outrem». **Violar o dever de cuidado pondo em '
        'perigo o próprio animal não é contraordenação.** É precisamente aí que a ofensa sexual se situa: '
        'não põe em perigo terceiro nem outro animal.',
        '**A via do dano é estruturalmente inadequada.** O crime de dano tutela o património do '
        'proprietário, não o animal, e é inaplicável quando o agente seja o próprio detentor — que é a '
        'hipótese mais frequente.',
        '**O ordenamento já qualificou o motivo sexual como especialmente censurável.** A al. c) do n.º 5 '
        'do artigo 387.º inclui, entre as circunstâncias reveladoras de especial censurabilidade ou '
        'perversidade, a de o crime «ser determinado pela avidez, pelo prazer de matar ou de causar '
        'sofrimento, **para excitação** ou por qualquer motivo torpe ou fútil». A agravante existe; falta o '
        'tipo que ela pressupõe.',
    ])
    destaque(doc, [
        'Em termos técnicos: a iniciativa não cria proteção nova onde já existia. **Desloca o momento da '
        'tutela** — do resultado para o acto. É essa deslocação que responde à insuficiência descrita, e é '
        'ela que confere à iniciativa utilidade normativa autónoma.'])
    nota(doc, [
        '**Observação.** Não se toma posição sobre a opção de política criminal, que é do legislador. '
        'Constata-se apenas que a insuficiência apontada na exposição de motivos é verificável no '
        'articulado vigente, pelo confronto do ponto 2.'])

    # ------------------------------------------------------------------ 4
    h1(doc, '4.', 'Dimensão higiossanitária e zoonótica')
    para(doc,
         'O parecer desta Direção-Geral não se esgota no bem-estar animal. A conduta em causa envolve '
         'contacto directo de mucosas genitais, oral e anal entre espécies, sem qualquer barreira '
         'sanitária, e é, nessa medida, matéria de saúde pública veterinária.')
    numlist(doc, [
        '**Via de transmissão bidirecional.** O contacto de mucosas com secreções genitais e fluidos '
        'orgânicos constitui via de transmissão para agentes zoonóticos excretados por essas vias, '
        'designadamente *Brucella* spp. e *Leptospira* spp. Está documentado o isolamento de *Brucella* em '
        'urina, sémen e outros fluidos orgânicos, e descrita a transmissão sexual da brucelose entre '
        'humanos (Li *et al.*, 2020).',
        '**Associação epidemiológica documentada.** Um estudo caso-controlo multicêntrico com 118 doentes '
        'com carcinoma do pénis e 374 controlos apurou prevalência de contacto sexual com animais de '
        '**44,9% nos casos contra 31,6% nos controlos** (p<0,008), com excesso significativo de doenças '
        'venéreas no grupo exposto (p<0,001), identificando a exposição como factor de risco independente '
        'em análise multivariada (Zequi *et al.*, 2012).',
        '**Consequência para a fiscalização.** A conduta não é apenas questão de bem-estar: é factor de '
        'risco higiossanitário que justifica intervenção da autoridade sanitária veterinária independente '
        'da prova de sofrimento do animal. Esta dimensão é a que melhor sustenta, no plano técnico, a '
        'punibilidade do acto em si — e não está invocada na exposição de motivos do projeto.',
    ])
    nota(doc, [
        '**Observação.** Sugere-se que esta dimensão seja levada à fundamentação da iniciativa. Confere-lhe '
        'apoio técnico que a fundamentação actual, centrada no bem-estar e no direito comparado, não '
        'mobiliza, e reforça a competência das autoridades sanitárias na deteção e comunicação destas '
        'situações.'])

    # ------------------------------------------------------------------ 5
    pagebreak(doc)
    h1(doc, '5.', 'Insuficiências da redação proposta')

    h2(doc, '5.1', 'Sobreinclusão sobre actos médico-veterinários e zootécnicos')
    destaque(doc, [
        'É a única insuficiência que esta Direção-Geral considera **premente**, e respeita exclusivamente à '
        'norma proposta para a Lei n.º 92/95.'])
    para(doc,
         'A al. h) proposta descreve, entre as condutas proibidas, «a introdução vaginal, anal ou oral de '
         'partes do corpo ou de objetos». Diferentemente da norma penal — que subordina ambas as alíneas ao '
         'elemento «sem motivo legítimo» —, a norma contraordenacional **não comporta qualquer elemento '
         'limitador**.')
    citacao(doc, [
        '3 — São também proibidos os actos consistentes em:',
    ], 'Corpo do n.º 3 do artigo 1.º da Lei n.º 92/95, de 12 de setembro')
    para(doc,
         'O n.º 1 do mesmo artigo não supre a falta. Aquele número é autodefinido — «considerando-se como '
         'tais os actos consistentes em, sem necessidade, se infligir a morte, o sofrimento cruel e '
         'prolongado ou graves lesões» —, e o n.º 3 abre com «São **também** proibidos», acrescentando e não '
         'especificando. A demonstração é interna ao artigo: as alíneas a), b), c), e) e f) do n.º 3 '
         'carregam limitadores próprios — «em casos que não sejam de emergência», «com excepção dos usados '
         'na arte equestre e nas touradas autorizadas por lei», «salvo experiência científica de comprovada '
         'necessidade», «salvo na prática da caça». Se o n.º 1 se transmitisse ao n.º 3, todos seriam '
         'redundantes. As alíneas sem limitador — d) e g) — são precisamente as que descrevem condutas que '
         'não admitem motivo legítimo.')
    para(doc,
         'Na letra da norma proposta ficam, pois, abrangidos actos correntes da prática clínica e '
         'zootécnica:')
    bullets(doc, [
        'termometria rectal;',
        'palpação transrectal para diagnóstico de gestação;',
        'ecografia transrectal; vaginoscopia; citologia vaginal;',
        'inseminação artificial e transferência de embriões;',
        'colheita de sémen por vagina artificial ou eletroejaculação;',
        'sondagem nasogástrica ou oral e entubação endotraqueal;',
        'enemas, administração de supositórios, desimpactação rectal, cateterização uretral;',
        'exploração obstétrica e assistência ao parto distócico.',
    ])
    para(doc,
         'Cumpre, porém, delimitar o alcance real da objeção. O artigo 32.º do Regime Geral das '
         'Contra-Ordenações manda aplicar subsidiariamente ao regime substantivo as normas do Código Penal, '
         'pelo que operam as causas de exclusão da ilicitude do seu artigo 31.º. O acto praticado no '
         'exercício da atividade médico-veterinária, regulada pelo Estatuto da Ordem dos Médicos '
         'Veterinários, estaria justificado. **Não se sustenta, portanto, que um médico veterinário viesse '
         'a ser sancionado.**')
    destaque(doc, [
        'A objeção é de estrutura da norma, não de resultado final:',
        '**Primeira.** A norma fica sobreinclusiva na sua face, e a legitimidade do acto passa a discutir-se '
        'por causa de justificação não escrita. Inverte-se a estrutura devida: a conduta é típica e a '
        'licitude alega-se depois.',
        '**Segunda.** O artigo 11.º da Lei n.º 92/95 atribui a fiscalização ao ICNF, a esta Direção-Geral, '
        'aos médicos veterinários municipais, às câmaras municipais, à ASAE, à GNR, à PSP, às polícias '
        'municipais e às restantes autoridades policiais. Uma norma cuja aplicação correcta depende de '
        'apreciação de causa de justificação não escrita é inadequada a este universo de entidades.',
        '**Terceira.** Cria-se assimetria injustificada dentro do mesmo acto legislativo: a norma penal '
        'escreve «sem motivo legítimo»; a contraordenacional nada escreve. E o efeito é mais gravoso onde a '
        'prática legítima é mais frequente, porquanto a contraordenação alcança todas as espécies, '
        'incluindo os animais de produção, em que a palpação transrectal e a inseminação artificial são '
        'prática diária.'])

    h2(doc, '5.2', 'Taxatividade da enumeração')
    para(doc,
         'A enumeração é fechada — «através de cópula, coito anal, coito oral ou a introdução vaginal, anal '
         'ou oral de partes do corpo ou de objetos». Ficam fora, entre outras, a masturbação do animal, o '
         'contacto oral-genital sem coito e a imposição de monta a animal sobre pessoa ou sobre outro '
         'animal, incluindo quando a desproporção de porte seja susceptível de causar lesões. A exposição '
         'de motivos refere expressamente «masturbação, contacto oral-genital», que o articulado depois não '
         'abrange.')

    h2(doc, '5.3', 'Conteúdos audiovisuais anunciados e não articulados')
    para(doc,
         'A exposição de motivos declara pretender criminalizar «a produção e difusão de conteúdos que '
         'representem a prática de crimes contra animais». O articulado não contém disposição sobre a '
         'matéria. Assinala-se que a al. e) do n.º 3 do artigo 1.º da Lei n.º 92/95 já proíbe a utilização '
         'de animais em «filmagens» de que resultem «dor ou sofrimentos consideráveis» — o que cobre parte '
         'da produção e nada da difusão.')

    h2(doc, '5.4', 'Dever de comunicação médico-veterinária — questão a ponderar')
    para(doc,
         'A fundamentação da iniciativa assenta, em parte relevante, no papel da medicina veterinária '
         'forense na deteção, documentação e comunicação destas situações. O articulado não prevê, '
         'contudo, dever de comunicação, protocolo pericial ou via de articulação com esta Direção-Geral.')
    nota(doc, [
        '**Questão que se suscita, sem juízo prévio.** Deverá a iniciativa prever dever de comunicação a '
        'cargo do médico veterinário que, no exercício da sua atividade, detete indícios compatíveis com '
        'ofensa sexual? E, em caso afirmativo, como se articula esse dever com o sigilo profissional '
        'consagrado no Código Deontológico Médico-Veterinário, e a quem deve a comunicação ser dirigida?',
        'A questão excede o objeto do projeto e envolve matéria estatutária da Ordem dos Médicos '
        'Veterinários, pelo que se deixa à consideração, sugerindo-se, se for entendido pertinente, a '
        'audição daquela entidade.'])

    # ------------------------------------------------------------------ 6
    h1(doc, '6.', 'Alterações prementes, à consideração')
    para(doc,
         'Uma só correção é considerada premente. As restantes são de aperfeiçoamento e ficam à '
         'consideração superior.')
    tabela(doc,
           ['Ponto', 'Correção', 'Grau'],
           [['5.1', 'Introdução, na al. h) proposta para a Lei n.º 92/95, de elemento que restrinja a '
                    'conduta à finalidade sexual — ou, em alternativa, de ressalva expressa dos actos '
                    'médico-veterinários e zootécnicos legalmente praticados. A primeira solução é '
                    'preferível: com elemento finalístico, o acto clínico não chega a preencher a norma, '
                    'dispensando ressalva e a sua actualização',
             '**Premente**'],
            ['5.2', 'Conversão da enumeração em exemplificativa e previsão da conduta de imposição de '
                    'monta', 'Aperfeiçoamento'],
            ['5.3', 'Articulação da disposição sobre conteúdos, ou supressão do anúncio na exposição de '
                    'motivos', 'Aperfeiçoamento'],
            ['5.4', 'Ponderação de dever de comunicação médico-veterinária, com audição da Ordem dos '
                    'Médicos Veterinários', 'A ponderar'],
            ['4.', 'Aditamento da fundamentação higiossanitária e zoonótica à exposição de motivos',
             'A ponderar'],
           ],
           [Cm(1.8), Cm(11.6), Cm(2.8)])
    nota(doc, [
        '**Nota de âmbito.** Assinala-se, a título de indicação e sem prejuízo da pronúncia das unidades '
        'competentes, que a norma penal proposta se insere no Título VI do Código Penal, cujo artigo 389.º, '
        'n.º 2, exclui do conceito de animal de companhia os factos relacionados com a utilização para fins '
        'de exploração agrícola, pecuária ou agroindustrial. Em consequência, a tutela penal não abrangerá '
        'as espécies pecuárias, subsistindo para estas apenas a tutela contraordenacional da Lei n.º 92/95.'])

    # ------------------------------------------------------------------ 7
    h1(doc, '7.', 'Conclusão')
    numlist(doc, [
        'A insuficiência invocada na exposição de motivos **verifica-se**: a tutela vigente é toda de '
        'resultado, e a violação do dever de cuidado que ponha em perigo o próprio animal não é '
        'contraordenável.',
        'A iniciativa **tem utilidade normativa autónoma**, por deslocar a tutela do resultado para o acto.',
        'A conduta em causa apresenta **relevância higiossanitária e zoonótica** documentada, que sustenta a '
        'intervenção da autoridade sanitária veterinária e que a fundamentação do projeto não mobiliza.',
        'A redação proposta para a Lei n.º 92/95 é **sobreinclusiva**, abrangendo na sua letra actos '
        'correntes da prática clínica e zootécnica. A correção deste ponto é **premente**.',
        'Nada mais se opõe, em termos técnicos, à aprovação da iniciativa.',
    ])

    # ------------------------------------------------------------------ 8
    h1(doc, '8.', 'Referências')
    h2(doc, '8.1', 'Legislação')
    bullets(doc, [
        'Código Penal, aprovado pelo Decreto-Lei n.º 48/95, de 15 de março — artigos 31.º, 212.º, 387.º, '
        '388.º-A e 389.º, este último na redação da Lei n.º 39/2020, de 18 de agosto.',
        'Lei n.º 92/95, de 12 de setembro — artigos 1.º, 11.º, 12.º e 13.º, os três últimos aditados pela '
        'Lei n.º 6/2022, de 7 de janeiro.',
        'Decreto-Lei n.º 276/2001, de 17 de outubro — artigos 6.º e 68.º.',
        'Código Civil — artigos 201.º-B e 1305.º-A, aditados pela Lei n.º 8/2017, de 3 de março.',
        'Regime Geral das Contra-Ordenações, aprovado pelo Decreto-Lei n.º 433/82, de 27 de outubro — '
        'artigo 32.º.',
        'Estatuto da Ordem dos Médicos Veterinários, aprovado pelo Decreto-Lei n.º 368/91, de 4 de outubro, '
        'alterado pelas Leis n.ºs 117/97, de 4 de novembro, e 125/2015, de 3 de setembro.',
    ])
    h2(doc, '8.2', 'Literatura científica')
    bullets(doc, [
        'ZEQUI, S. C., GUIMARÃES, G. C., FONSECA, F. P., *et al.* — «Sex with Animals (SWA): Behavioral '
        'Characteristics and Possible Association with Penile Cancer. A Multicenter Study». *The Journal of '
        'Sexual Medicine*, 2012, 9 (7), pp. 1860-1867. DOI: 10.1111/j.1743-6109.2011.02512.x',
        'LI, N., YU, F., PENG, F., ZHANG, X., JIA, B. — «Probable sexual transmission of brucellosis». '
        '*IDCases*, 2020, 21, e00871. DOI: 10.1016/j.idcr.2020.e00871 · PMID: 32642429',
    ])
    nota(doc, [
        'Os textos legais foram conferidos nos respetivos números do Diário da República, e não em versões '
        'consolidadas de compiladores.'])
