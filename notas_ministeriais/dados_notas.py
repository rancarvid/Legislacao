# -*- coding: utf-8 -*-
"""Conteúdo das notas de apoio à atividade ministerial.

Cada ficha é permanente e vive aqui. O Word é gerado por `gerar_nota.py` e
nunca se edita à mão.

Campos de cada ficha, pela ordem em que aparecem na tabela:

    enquadramento      Enquadramento do tema
    pontos_sensiveis   Pontos sensíveis / Linha defensiva
    mensagens_chave    Mensagens-chave
    contexto           Contexto e caracterização do setor
    acoes_medidas      Ações em curso / Medidas adotadas
    prioridades        Prioridades futuras
    impacto            Matérias com impacto político, parlamentar e mediático
    riscos             Riscos / Constrangimentos

As quatro primeiras correspondem ao modelo fixado pelo Gabinete do Senhor
Ministro; as quatro últimas são o desdobramento pedido pela Senhora
Diretora-Geral. O gerador sombreia-as de forma diferente, como no modelo.

Cada campo é uma lista de parágrafos. Uma entrada que comece por «- » sai
como marca.

A ficha tem ainda quatro campos de controlo, que o gerador verifica:

    tema                    Designação do tema, como sai no cabeçalho
    unidade                 Unidade orgânica que acompanha o tema
    atualizado              AAAA-MM-DD da última alteração à ficha
    registo                 Pares (data, o que mudou). É daqui que sai o bloco
                            «Evoluções relevantes» da atualização mensal, pelo
                            que uma alteração sem linha de registo desaparece
    legislacao_verificada   (data, âmbito varrido, resultado) do último
                            varrimento de legislação nova
"""

# Designações fixas. O gerador recusa gerar se encontrar as formas erradas.
DESIGNACOES_PROIBIDAS = [
    ("Regulamento Geral do Animal de Companhia", "Regime Geral do Animal de Companhia"),
    ("Regulamento Geral dos Animais de Companhia", "Regime Geral do Animal de Companhia"),
    ("Regime Geral dos Animais de Companhia", "Regime Geral do Animal de Companhia"),
    ("Regulamento 2026/1818", "Regulamento (UE) 2026/1818"),
    ("Regulamento 2026_1818", "Regulamento (UE) 2026/1818"),
    ("Bem Estar", "bem-estar"),
    ("Bem-Estar", "bem-estar"),
    ("Regulamento (EU)", "Regulamento (UE)"),
    ("Direcção-Geral de Alimentação", "Direção-Geral de Alimentação"),
]

# Expressões que não são erro mas que não passam sem se confirmar o que se quis
# dizer. O gerador avisa e gera.
DESIGNACOES_A_CONFIRMAR = [
    ("2023/0447", "é o número do procedimento legislativo, não do ato. Numa nota ao Gabinete "
                  "citar o Regulamento (UE) 2026/1818."),
    ("legislação vigente", "confirmar que não se está a tratar o RGAC, o Código do Animal de "
                           "Companhia ou o Regime Geral do Bem-Estar dos Animais de Companhia "
                           "como direito em vigor: são propostas."),
]

# Expressões onde a forma «proibida» está correta por ser nome próprio de um
# diploma ou de uma proposta. O gerador ignora a ocorrência quando ela cai
# dentro de uma destas.
EXCECOES_DESIGNACAO = [
    "Regime Geral do Bem-Estar dos Animais de Companhia",
]

ROTULOS = [
    ("enquadramento", "Enquadramento do tema", "modelo"),
    ("pontos_sensiveis", "Pontos sensíveis /\nLinha defensiva", "modelo"),
    ("mensagens_chave", "Mensagens-chave", "modelo"),
    ("contexto", "Contexto e caracterização do setor", "modelo"),
    ("acoes_medidas", "Ações em curso /\nMedidas adotadas", "dgav"),
    ("prioridades", "Prioridades futuras", "dgav"),
    ("impacto", "Matérias com impacto:\nPolítico /\nParlamentar /\nMediático", "dgav"),
    ("riscos", "Riscos /\nConstrangimentos", "dgav"),
]

FICHAS = {}

FICHAS["rgac"] = {
    "tema": "Regime Geral do Animal de Companhia (RGAC)",
    "unidade": "",
    "atualizado": "2026-10-02",

    "enquadramento": [
        "O Regime Geral do Animal de Companhia, doravante designado RGAC, constitui uma proposta de "
        "agregação do ordenamento jurídico português dedicado aos animais de companhia.",
        "Visa-se ainda a instituição de novos mecanismos que permitam densificar a proteção do bem-estar "
        "animal e a vinculação ao dever de detenção responsável, em resposta às fragilidades identificadas "
        "no regime de detenção e no controlo de animais errantes.",
        "Todo o tratamento jurídico das matérias respeitantes aos animais de companhia será revisto e "
        "reformulado, excluindo apenas as de natureza específica que justifiquem tratamento autónomo.",
        "O processo iniciou-se após a transição de competências concretizada a 1 de julho de 2025, por "
        "força do Decreto-Lei n.º 63/2025, de 7 de abril. Desde então, o seu desenvolvimento tem sido "
        "assegurado em conciliação com as obrigações decorrentes da operacionalização dos avisos de apoio "
        "ao bem-estar dos animais de companhia, designadamente a sua preparação, publicação, análise e "
        "efetivação.",
        "A 10 de agosto de 2026 foi publicado no Jornal Oficial da União Europeia o Regulamento (UE) "
        "2026/1818 do Parlamento Europeu e do Conselho, de 17 de junho de 2026, relativo ao bem-estar dos "
        "cães e dos gatos e à respetiva rastreabilidade, que passa a ser o referencial europeu de "
        "aplicação direta com o qual o RGAC tem de ser compatibilizado.",
    ],

    "pontos_sensiveis": [
        "O prazo. O trabalho decorre desde julho de 2025 e a primeira versão consolidada foi remetida a 30 "
        "de junho de 2026. Linha defensiva: não se trata de compilação, mas de substituição de mais de duas "
        "dezenas de diplomas de épocas diferentes, com remissões cruzadas, feita em simultâneo com a "
        "execução dos avisos de apoio. A primeira versão existe, está entregue e tem revisão jurídica "
        "formal feita.",
        "A espera pelo Regulamento europeu. Pode ser invocado que se aguardou pelo texto europeu em vez de "
        "legislar. Linha defensiva: o Regulamento é de aplicação direta e altera matérias estruturantes — "
        "criação e reprodução, detenção responsável, funcionamento dos alojamentos e formação. Legislar "
        "antes do texto final obrigaria a rever o diploma logo a seguir. O trabalho de correspondência "
        "entre o projeto nacional e o texto europeu foi feito em paralelo e não parado.",
        "A sobrelotação dos centros de recolha oficial e dos alojamentos. Linha defensiva: é o problema "
        "que o RGAC visa atacar na raiz, pela detenção responsável e pela esterilização, e não apenas pela "
        "capacidade instalada. A resposta de capacidade corre pelos avisos de apoio, que estão em execução.",
        "O regime sancionatório. Haverá pressão em dois sentidos opostos — agravar as molduras e, do lado "
        "dos operadores, atenuar a carga. Linha defensiva: o critério é a exequibilidade. Uma sanção "
        "inaplicável ou que prescreva não protege nenhum animal.",
        "A lista positiva de animais de companhia. Matéria sensível junto dos operadores e dos detentores "
        "de espécies não tradicionais. Linha defensiva: o RGAC não fixa a lista; cria a habilitação "
        "normativa para a instituir, com base em evidência científica a levantar, acompanhando a tendência "
        "europeia.",
        "A articulação com os municípios. Linha defensiva: a repartição de competências é matéria a "
        "clarificar no diploma, e é precisamente uma das fragilidades que motivam a revisão.",
    ],

    "mensagens_chave": [
        "Toda a legislação respeitante a animais de companhia será revista e reformulada, com o objetivo de "
        "tornar mais eficazes a proteção do bem-estar animal, a detenção responsável e o controlo dos "
        "animais errantes.",
        "O RGAC reúne num único diploma o regime do bem-estar, da saúde e da identificação dos animais de "
        "companhia, hoje disperso por mais de duas dezenas de diplomas.",
        "A proposta está entregue. A primeira versão consolidada foi remetida à Secretaria de Estado a 30 "
        "de junho de 2026.",
        "O diploma é a base legal nacional de execução do Regulamento (UE) 2026/1818, cujas obrigações se "
        "tornam aplicáveis de forma faseada a partir de 31 de agosto de 2028.",
    ],

    "contexto": [
        "A legislação atual respeitante a animais de companhia encontra-se muito dispersa e, em alguns "
        "pontos, desatualizada.",
        "A realidade atual enfrenta diversos desafios: o número de animais errantes, a sobrelotação dos "
        "alojamentos, designadamente dos centros de recolha oficial e das instalações de alojamento "
        "zoófilo, a sensibilização para a detenção responsável, com foco na promoção da esterilização e na "
        "prevenção do abandono, e a necessidade de reforço da fiscalização.",
        "A consolidação normativa abrangerá toda a legislação em vigor, em correspondência com o "
        "Regulamento (UE) 2026/1818.",
        "O Regulamento (UE) 2026/1818 tem 7 capítulos, 33 artigos e 3 anexos. Entrou em vigor no vigésimo "
        "dia seguinte ao da publicação e é aplicável a partir de 31 de agosto de 2028, com datas diferidas "
        "fixadas no seu artigo 33.º, que vão de 31 de agosto de 2029 a 1 de julho de 2036 consoante a "
        "obrigação. Esta calendarização condiciona o faseamento que o RGAC tem de prever.",
    ],

    "acoes_medidas": [
        "Elaboração da proposta de revisão da legislação de bem-estar, identificação e saúde dos animais de "
        "companhia, assente na análise sistemática de mais de duas dezenas de diplomas conexos.",
        "Correspondência entre o Regulamento (UE) 2026/1818 e os diplomas nacionais vigentes, incluindo os "
        "projetos preexistentes, designadamente o Código do Animal de Companhia e a proposta de Regime "
        "Geral do Bem-Estar dos Animais de Companhia, apresentada em 2024 e 2025.",
        "A 30 de junho de 2026 foi remetida à Secretaria de Estado a primeira versão do RGAC, elaborada "
        "pela DGAV. O documento resultou de trabalho técnico desenvolvido por uma equipa multidisciplinar e "
        "assentou na análise e consolidação da legislação nacional em vigor, de propostas legislativas "
        "anteriores e do texto europeu então em preparação.",
        "Foram considerados os contributos recebidos de entidades externas, designadamente da ANVETEM, da "
        "Ordem dos Médicos Veterinários e do Sindicato Nacional dos Médicos Veterinários. Não foram "
        "recebidos contributos da FEDRA nem do CPC.",
        "A versão remetida foi objeto de primeira revisão jurídica formal, incidente sobre a estrutura do "
        "diploma, a revisão parcial do articulado, a elaboração do regime contraordenacional e a proposta "
        "de preâmbulo.",
        "O documento carece ainda de revisão jurídica global, designadamente quanto às remissões internas "
        "do articulado e aos anexos de natureza técnica, bem como da validação de aspetos identificados "
        "durante a revisão efetuada.",
        "Sem prejuízo destes aspetos, o documento constitui base sólida para apreciação superior, "
        "refletindo uma proposta integrada que visa reunir, num único diploma, o regime aplicável ao "
        "bem-estar, à saúde e à identificação dos animais de companhia.",
    ],

    "prioridades": [
        "Consolidação da proposta com as conclusões da análise comparativa.",
        "Análise de impacto normativo, com avaliação dos efeitos esperados na população animal, nos "
        "operadores económicos e nas autoridades competentes.",
        "Alinhamento com o texto final do Regulamento (UE) 2026/1818, publicado a 10 de agosto de 2026, "
        "incluindo o faseamento das obrigações previsto no seu artigo 33.º.",
        "Articulação com as entidades intervenientes: municípios, médicos veterinários e operadores.",
        "Revisão jurídica global do articulado, das remissões internas e dos anexos técnicos.",
    ],

    "impacto": [
        "Consolidação normativa: criação da base legal nacional para a execução do regulamento comunitário "
        "sobre o bem-estar e a rastreabilidade de cães e gatos.",
        "Regulação técnica e científica: estabelecimento de normas de saúde, bem-estar e identificação "
        "animal, fundamentadas no conhecimento científico e técnico multidisciplinar.",
        "Gestão de populações: resposta aos desafios de bem-estar e implementação de uma estratégia "
        "integrada para a gestão de animais errantes.",
        "Abordagem One Health: interligação entre saúde animal, bem-estar e identificação eletrónica como "
        "pilares do conceito de Saúde Única.",
        "Políticas públicas integradas: definição e execução de estratégias transversais no âmbito dos "
        "animais de companhia.",
    ],

    "riscos": [
        "Dispersão normativa. O processo é complexo e multidisciplinar, envolvendo a compatibilização de "
        "diplomas de épocas diferentes, com remissões cruzadas e regimes específicos, a par do alinhamento "
        "com normas europeias de aplicação direta. A morosidade reflete a necessidade de um trabalho "
        "estruturado, que garanta coerência jurídica e técnica e evite sobreposições ou contradições.",
        "Atualização permanente da análise, por forma a integrar as alterações ao texto europeu e garantir "
        "o alinhamento com a redação final.",
        "O Regulamento (UE) 2026/1818 introduz normas que modificam significativamente a legislação "
        "portuguesa, designadamente quanto às regras de criação e reprodução animal, à detenção "
        "responsável, ao funcionamento dos alojamentos e à formação. O novo regime terá de ir além da "
        "compilação legislativa, devendo prever e concretizar as normas europeias.",
        "A aplicação de um paradigma atualizado de proteção animal é compatível com o objetivo do RGAC, mas "
        "a sua implementação exige ponderação e planeamento, acautelando o equilíbrio entre um quadro "
        "regulamentar mais exigente e a salvaguarda dos seus destinatários finais. A formulação do RGAC "
        "deverá prever a sua exequibilidade, de modo a prevenir o agravamento das situações que "
        "comprometem o bem-estar dos animais ou a sobrecarga de serviços que operam já no limite da sua "
        "capacidade instalada.",
        "Torna-se imperativo prever um regime sancionatório adequado, de natureza inequivocamente "
        "dissuasora mas exequível, obstando ao risco de prescrição procedimental e garantindo a "
        "efetividade da proteção animal.",
        "A reforma transcende a esfera dos canídeos e felídeos, abrangendo a diversidade de espécies "
        "detidas como animais de companhia. A evidência atual alerta para a inaptidão de certas espécies "
        "para a detenção enquanto animais de companhia. A revisão deverá prever a disponibilidade de meios "
        "para o levantamento da evidência científica e a habilitação normativa necessária para acompanhar "
        "a tendência europeia de instituição de uma lista positiva de animais de companhia.",
    ],

    "legislacao_verificada": (
        "2026-10-02",
        "Diário da República, 1.ª série, n.os 125 a 192, de 1 de julho a 2 de outubro de 2026, "
        "varrimento integral; Jornal Oficial da União Europeia no mesmo período.",
        "Nenhuma alteração ao Decreto-Lei n.º 276/2001, ao Decreto-Lei n.º 314/2003, ao "
        "Decreto-Lei n.º 315/2009, à Lei n.º 27/2016 ou ao Decreto-Lei n.º 82/2019, e nenhum "
        "diploma nacional de execução do Regulamento (UE) 2026/1818. Saiu o Decreto-Lei n.º "
        "173/2026, de 1 de setembro, que fixa condições de transporte de animais de companhia e "
        "de cães de assistência nos transportes públicos, e o Decreto n.º 18/2026, de 7 de "
        "setembro, que exclui do regime florestal terrenos em Montalegre para a construção de um "
        "centro de recolha oficial. Na União Europeia, nada de novo sobre bem-estar ou "
        "rastreabilidade de cães e gatos depois do Regulamento (UE) 2026/1818.",
    ),

    "registo": [
        ("2026-08-28", "Primeira nota remetida ao Gabinete."),
        ("2026-10-02", "Ficha permanente criada. Preenchidos os pontos sensíveis e a linha defensiva, que "
                       "estavam em branco. Corrigida a designação do diploma e a citação do Regulamento "
                       "(UE) 2026/1818. Acrescentado o faseamento do artigo 33.º."),
        ("2026-10-02", "Varrimento da legislação publicada entre 1 de julho e 2 de outubro de "
                       "2026, nacional e europeia. Sem alterações ao regime dos animais de "
                       "companhia. Registado no campo «legislacao_verificada»."),
    ],
}
