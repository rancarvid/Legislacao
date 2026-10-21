"""
Memorando de acompanhamento do RGAC, versão 3.0 (ENSAIO da opção B, a partir do ensaio 2.0).

Diferenças face à versão 1.x (ver ../PROPOSTAS_ORGANIZACAO.md):
  - Cada ficha tem um código permanente SIGLA-NN: a sigla do tema principal (a primeira etiqueta) e o
    próximo número livre desse tema (TIT-19, CED-18, REG-01, ...). Nunca muda nem se reutiliza,
    mesmo que o RGAC seja renumerado ou que a ficha ganhe outras etiquetas.
  - A ficha fica presa ao artigo principal pela EPÍGRAFE ("artigo"), não pelo número.
  - Nas referências a artigos do RGAC escreve-se a epígrafe entre [[ ]]: "art. [[Registo]], n.º 1".
    O gerador troca pela numeração da versão atual do RGAC (estrutura_rgac.json).
    Se a epígrafe se repetir no RGAC, indica-se a ocorrência: [[Sistema de Informação de Animais de Companhia#2]].
  - Referências a outros diplomas escrevem-se à mão, com o nome do diploma (DL 82/2019, art. 16.º).
  - Os temas passam a etiquetas (ETIQUETAS). Uma ficha pode ter várias.
  - O memorando arruma-se pelos capítulos e artigos da versão atual do RGAC.

A bibliografia, as posições externas (Anexo B) e as constantes vêm da versão 1.x, sem duplicação.
"""

import importlib.util as _ilu
import os as _os

_spec = _ilu.spec_from_file_location(
    "_v1", _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "dados_memorando_rgac.py"))
_V1 = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_V1)

# Partilhado com a versão 1.x
FICHEIRO_RGAC = _V1.FICHEIRO_RGAC
VERSAO_RGAC = _V1.VERSAO_RGAC
ORIGENS = _V1.ORIGENS
ESTADOS = _V1.ESTADOS
ESTADOS_REVISAO = _V1.ESTADOS_REVISAO
ESTADOS_REGULAMENTO = _V1.ESTADOS_REGULAMENTO
STAKEHOLDERS = _V1.STAKEHOLDERS
BIBLIOGRAFIA = _V1.BIBLIOGRAFIA
DOMINIOS_IMPRENSA = _V1.DOMINIOS_IMPRENSA
DATA_LIGACOES = _V1.DATA_LIGACOES

VERSAO_MEMORANDO = "3.0 (ensaio), com o conteúdo da versão " + _V1.VERSAO_MEMORANDO
DATA_MEMORANDO = _V1.DATA_MEMORANDO

INTRODUCAO = [
    "Este memorando serve para acompanhar o trabalho sobre o RGAC. Regista os problemas que vamos "
    "encontrando no texto, os que já existem na legislação em vigor e continuam por resolver, e as "
    "críticas feitas por entidades externas. É um documento vivo: cada nova versão acrescenta fichas "
    "ou muda o estado das que já existem.",
    "O memorando segue a ordem do RGAC. Cada ficha aparece no capítulo e junto ao artigo onde está o "
    "problema principal. A numeração dos artigos e capítulos é sempre a da versão do RGAC indicada acima; "
    "quando o RGAC mudar, o memorando é gerado de novo e os números acompanham a mudança.",
    "Cada ficha tem um código permanente formado pela sigla do seu tema principal e por um número "
    "sequencial dentro desse tema: TIT-01 é a primeira ficha de titularidade, CED-07 a sétima de CED. O "
    "código não depende da numeração do RGAC e nunca muda. Quando um problema fica resolvido, a ficha "
    "mantém-se com o estado Resolvido.",
    "Uma ficha pode tocar mais de um tema. O tema principal dá o código; os outros aparecem como etiquetas. "
    "O Anexo E junta as fichas de cada tema, incluindo as que o têm como tema secundário.",
    "Os lapsos formais (remissões erradas, números repetidos, gralhas, marcas de trabalho no texto) não têm "
    "ficha: ficam no Anexo C, com código L. O Anexo D mostra, artigo a artigo, o que já foi revisto.",
    "A legislação vigente citada foi confirmada online (DRE e PGDL), na pasta Legislação vigente e nos "
    "ficheiros do repositório. As posições de entidades externas assentam só em documentos; notícias de "
    "imprensa não são usadas como fonte.",
]

CAMPOS_FICHA = [
    ("Onde", "Artigos do RGAC em causa, com o capítulo."),
    ("Etiquetas", "Temas a que a ficha pertence."),
    ("Origem", "Se o problema foi criado pelo RGAC, se já existia, ou se o RGAC o resolve em parte."),
    ("Problema", "Descrição curta."),
    ("Proposta", "Solução ou redação sugerida, quando já existe."),
    ("Quem levantou", "Entidades ou documentos que apontaram o problema."),
    ("Estado", "Aberto, Parcialmente resolvido ou Resolvido."),
]

# Temas. A sigla é o prefixo do código das fichas cujo tema principal é esse (primeira etiqueta).
# Tema novo: acrescentar aqui uma sigla de três letras e o nome.
ETIQUETAS = {
    "TIT": "Titularidade e detenção",
    "CED": "CED, colónias e animais errantes",
    "REG": "Identificação e registo",
    "EST": "Estabelecimentos e operadores",
    "SAN": "Fiscalização e contraordenações",
    "FIN": "Disposições finais e revogações",
    "BEM": "Bem-estar e deveres de detenção",
    "REP": "Reprodução e comércio",
    "ZOO": "Zoonoses e saúde pública",
    "PER": "Animais perigosos",
}

# Enquadramento dos temas transversais (texto de contexto, aparece antes das fichas)
TRANSVERSAIS = [
    {"etiqueta": "TIT", "titulo": "Titular, detentor, proprietário e operador", "intro": [
        "Na legislação em vigor, detentor tem dois sentidos. No DL 276/2001, no DL 314/2003 e na Portaria 146/2017 é a pessoa responsável pelo animal. No DL 82/2019 é só o possuidor precário do art. 1253.º do Código Civil. O titular é a figura do registo SIAC. O proprietário é a figura do Código Civil.",
        "O RGAC revoga aqueles decretos-leis (art. [[Norma revogatória]], n.º 1) e passa a ter um só conjunto de definições (art. [[Definições]]). Isso resolve a dispersão, mas cria problemas novos na forma como define o titular e na forma como distribui os deveres entre titular e detentor.",
    ]},
    {"etiqueta": "CED", "titulo": "Programas CED, colónias e animais errantes", "intro": [
        "Hoje o regime CED está na Lei 27/2016 (art. 4.º) e na Portaria 146/2017 (art. 9.º). A Lei diz que o Estado assegura a concretização de programas CED para gatos. A Portaria diz que as câmaras podem autorizar colónias.",
        "O RGBEAC (jun. 2025, art. 44.º) tinha transformado o CED num dever das câmaras, com cuidadores identificados. O RGAC voltou ao modelo da Portaria (arts. [[Programas de captura, esterilização e devolução ao local de origem]] e [[Programa CED em prédios privados]]) e revoga a Lei 27/2016. Acrescenta o registo das colónias no SIAC e o regime do CED em prédios privados.",
    ]},
]

# ------------------------------------------------------------------ fichas
# Campos: cod (permanente), cod_ensaio_2 e cod_antigo (rastreio), artigo (epígrafe do artigo principal),
# titulo, etiquetas (a primeira é o tema principal e dá a sigla do código), onde, origem, problema,
# proposta, levantado, estado, rel.
# Ficha nova: sigla do tema principal + próximo número livre desse tema (o gerador mostra-o no fim);
# "artigo" é a epígrafe exata do artigo principal no RGAC.
FICHAS = [
    {
        "cod": "TIT-01",
        "cod_ensaio_2": "P-01",
        "cod_antigo": "T-01",
        "artigo": "Definições",
        "titulo": "A definição de titular depende só do registo",
        "etiquetas": ["TIT"],
        "onde": [
            "art. [[Definições]], definição de «Titular»",
            "art. [[Registo no Sistema de Informação de Animais de Companhia (SIAC)]], n.º 1",
        ],
        "origem": "RGAC",
        "problema": [
            "O titular é definido como quem «figura, na base de dados oficial, como proprietário». Ao mesmo tempo, o registo faz-se «em nome do respetivo titular» (art. [[Registo no Sistema de Informação de Animais de Companhia (SIAC)]], n.º 1). A definição é circular: é titular quem está registado e regista-se em nome do titular.",
            "No DL 82/2019 o titular era o proprietário ou o possuidor cuja posse faz presumir a propriedade (art. 3.º, al. f), ligado ao art. 1268.º do Código Civil). Esse critério permitia decidir em nome de quem registar. Com a revogação do DL 82/2019, deixa de existir.",
        ],
        "proposta": "Definir titular como «o proprietário ou o possuidor cuja posse faça presumir a propriedade, em cujo nome é efetuado o registo no SIAC», mantendo a referência ao operador.",
        "levantado": [
            "Análise interna (balanço de 25.9.2026)",
            "ARPA, parecer sobre o DL 82/2019 (dez. 2022)",
        ],
        "estado": "Aberto",
        "rel": ["TIT-02", "TIT-03"],
    },
    {
        "cod": "TIT-02",
        "cod_ensaio_2": "P-02",
        "cod_antigo": "T-02",
        "artigo": "Registo no Sistema de Informação de Animais de Companhia (SIAC)",
        "titulo": "Registo em nome de quem detém o animal e não de quem é dono",
        "etiquetas": ["TIT", "REG"],
        "onde": [
            "art. [[Registo no Sistema de Informação de Animais de Companhia (SIAC)]], n.º 5",
        ],
        "origem": "RGAC",
        "problema": [
            "O art. [[Registo no Sistema de Informação de Animais de Companhia (SIAC)]], n.º 5 manda registar os animais «detidos por pessoas singulares ou coletivas que não operadores» em nome dessas pessoas. Segue a versão portuguesa do art. 20.º, n.º 3 do Regulamento (UE) 2026/1818. A versão inglesa usa o critério da propriedade («owned by»).",
            "Lida com a definição de titular (TIT-01), a norma permite registar como titular quem só detém o animal, por exemplo uma família de acolhimento ou um cuidador.",
        ],
        "proposta": "Substituir «detidos por» por «que sejam proprietárias de».",
        "levantado": [
            "Análise interna (confronto com o Regulamento (UE) 2026/1818)",
            "ARPA, parecer sobre o DL 82/2019 (dez. 2022)",
        ],
        "estado": "Aberto",
        "rel": ["TIT-01", "TIT-14"],
    },
    {
        "cod": "TIT-03",
        "cod_ensaio_2": "P-03",
        "cod_antigo": "T-03",
        "artigo": "Definições",
        "titulo": "Sem regra sobre o valor do registo SIAC face à propriedade",
        "etiquetas": ["TIT"],
        "onde": [
            "art. [[Definições]]",
            "art. [[Sistema de Informação de Animais de Companhia#1]]",
            "art. [[Registo no Sistema de Informação de Animais de Companhia (SIAC)]]",
        ],
        "origem": "VIGENTE",
        "problema": [
            "Nem a lei atual nem o RGAC dizem se o registo SIAC faz presumir a propriedade, se essa presunção pode ser afastada e como se corrige um registo errado.",
            "A versão DAJA de 29.6.2026 tinha uma regra de prevalência do registo (art. 5.º, n.º 4). Essa regra caiu na revisão formal e nada a substituiu. Os tribunais decidem caso a caso: o Tribunal da Relação de Lisboa (30.4.2025, proc. 1642/24.4T8AMD.L1-8) tratou o registo como elemento relevante, mas não decisivo.",
        ],
        "proposta": "Prever uma presunção de titularidade pelo registo, que possa ser afastada por prova em contrário, «sem prejuízo do direito de propriedade nos termos do Código Civil», e um procedimento de retificação do registo.",
        "levantado": [
            "Acórdão do TRL de 30.4.2025",
            "Análise interna",
            "PCP, proposta ao OE2026 (registo informativo sem responsabilidade, 5.11.2025)",
            "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): a falta de registo no SIAC serviu de prova contra a alegada propriedade de terceiro",
        ],
        "estado": "Aberto",
        "rel": ["TIT-01"],
    },
    {
        "cod": "TIT-04",
        "cod_ensaio_2": "P-04",
        "cod_antigo": "T-04",
        "artigo": "Deveres do titular",
        "titulo": "O detentor deixa de ter de comunicar a morte do animal",
        "etiquetas": ["TIT", "REG"],
        "onde": [
            "art. [[Deveres do titular]], n.º 2",
            "art. [[Alterações ao registo]], n.º 3",
        ],
        "origem": "RGAC",
        "problema": [
            "No regime atual, o detentor deve comunicar ao SIAC a morte ou o desaparecimento, sob pena de presunção de abandono (DL 82/2019, art. 16.º, n.º 2). No RGAC esse dever passa só para o titular (art. [[Deveres do titular]], n.º 2). O detentor fica só com o dever de comunicar o desaparecimento e a recuperação (art. [[Alterações ao registo]], n.º 3).",
            "Quem tem o animal consigo, como uma família de acolhimento, um lar de acolhimento ou um cuidador, deixa de ter dever próprio quando o animal morre.",
            "A jurisprudência faz recair os deveres de cuidado sobre quem tem o controlo de facto do animal, e não sobre o proprietário que se afastou. No acórdão do Tribunal da Relação do Porto de 8.5.2024, o dono original deixara o cão em 2018 e foi condenada a pessoa que o tinha a seu cuidado.",
        ],
        "proposta": "Art. 76.º, n.º 2: «O titular e o detentor, ou os seus representantes, devem comunicar a morte ou o desaparecimento do animal de companhia ao SIAC […]».",
        "levantado": [
            "Análise interna",
            "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): deveres do detentor nos termos do art. 1253.º do Código Civil",
        ],
        "estado": "Aberto",
        "rel": ["TIT-05"],
    },
    {
        "cod": "TIT-05",
        "cod_ensaio_2": "P-05",
        "cod_antigo": "T-05",
        "artigo": "Alterações ao registo",
        "titulo": "A presunção de abandono remete para normas erradas e não diz a quem se aplica",
        "etiquetas": ["TIT", "REG"],
        "onde": [
            "art. [[Alterações ao registo]], n.º 7",
        ],
        "origem": "RGAC",
        "problema": [
            "O art. [[Alterações ao registo]], n.º 7 remete para os prazos «previstos no n.º 2 e 3». O n.º 2 trata da transmissão de titularidade, não da morte.",
            "Remete também, para a sanção, para a «alínea e) do artigo 139.º». O art. [[Medidas preventivas]] trata de medidas preventivas e não tem alíneas.",
            "A norma não diz se o abandono se presume do titular ou do detentor. Sendo uma norma sancionatória, estas falhas podem impedir a sua aplicação.",
        ],
        "proposta": "Corrigir as remissões (n.º 3 do art. [[Alterações ao registo]] e a alínea certa do art. [[Contraordenações]]) e indicar a quem se presume o abandono.",
        "levantado": [
            "Análise interna",
        ],
        "estado": "Aberto",
        "rel": ["TIT-04", "TIT-06"],
    },
    {
        "cod": "TIT-06",
        "cod_ensaio_2": "P-06",
        "cod_antigo": "T-06",
        "artigo": "Contraordenações",
        "titulo": "O abandono não aparece como contraordenação",
        "etiquetas": ["TIT", "SAN"],
        "onde": [
            "art. [[Contraordenações]]",
            "art. [[Definições]], definição de «Abandono»",
        ],
        "origem": "RGAC",
        "problema": [
            "O RGAC define abandono no art. [[Definições]] e revoga o DL 276/2001, cujo art. 68.º, n.º 2, al. c) punia o abandono como contraordenação. A lista de contraordenações do art. [[Contraordenações]] não inclui o abandono.",
            "Fica só a via penal (art. 388.º do Código Penal), que exige dever de guarda e perigo para a alimentação e cuidados do animal. A presunção de abandono do art. [[Alterações ao registo]], n.º 7 fica sem sanção a que se ligar.",
            "O Regulamento (UE) 2026/1818 manda prever sanções «inclusive as aplicáveis ao abandono de cães e gatos pelos operadores» (art. 32.º), aplicável a partir de 31.8.2028.",
        ],
        "proposta": "Acrescentar ao art. [[Contraordenações]] a contraordenação de abandono, nos termos da definição do art. [[Definições]], imputável ao titular e ao detentor. O art. 32.º do Regulamento (UE) 2026/1818 torna-o obrigatório pelo menos para os operadores, a partir de 31.8.2028.",
        "levantado": [
            "Análise interna",
            "Teresa Quintela de Brito, RJLB 2019 (o crime de abandono só abrange quem já tem dever de guarda)",
            "Raúl Farias, e-book do CEJ «Direito dos animais» (2022): o abandono situa-se ao nível da detenção",
            "Cátia Simões, RJLB 2019 (o abandono é difícil de provar)",
            "Tribunal Constitucional, Acórdão 478/2024 (o art. 388.º do Código Penal não é inconstitucional)",
            "Regulamento (UE) 2026/1818, art. 32.º (sanções para o abandono pelos operadores)",
        ],
        "estado": "Aberto",
        "rel": ["TIT-05"],
    },
    {
        "cod": "TIT-07",
        "cod_ensaio_2": "P-07",
        "cod_antigo": "T-07",
        "artigo": "Norma revogatória",
        "titulo": "As portarias mantidas usam detentor no sentido antigo",
        "etiquetas": ["TIT", "FIN"],
        "onde": [
            "art. [[Norma revogatória]], n.º 2",
        ],
        "origem": "RGAC",
        "problema": [
            "O art. [[Norma revogatória]], n.º 2 mantém em vigor as portarias aprovadas ao abrigo dos diplomas revogados «com as necessárias adaptações».",
            "A Portaria 146/2017 usa detentor no sentido de responsável pelo animal: animais «não reclamados pelos seus detentores» (art. 8.º, n.º 4), «novos detentores» para quem adota (art. 8.º, n.º 6), esterilização «a expensas dos respetivos detentores» (art. 10.º, n.º 1). Com a definição do RGAC, estas normas passariam a visar só o possuidor precário. A Portaria regulamenta ainda a Lei 27/2016, que o RGAC revoga.",
        ],
        "proposta": "Acrescentar ao art. [[Norma revogatória]], n.º 2: «as referências a detentor constantes dos diplomas regulamentares mantidos em vigor entendem-se feitas ao titular ou ao detentor, consoante o caso».",
        "levantado": [
            "Análise interna (validação tripla da Portaria 146/2017)",
            "APMVEAC, revisão crítica (9.4.2021)",
        ],
        "estado": "Aberto",
        "rel": [],
    },
    {
        "cod": "TIT-08",
        "cod_ensaio_2": "P-08",
        "cod_antigo": "T-08",
        "artigo": "Registo no Sistema de Informação de Animais de Companhia (SIAC)",
        "titulo": "Animais perigosos: o operador pode ser uma sociedade, o titular não",
        "etiquetas": ["TIT", "REG"],
        "onde": [
            "art. [[Registo no Sistema de Informação de Animais de Companhia (SIAC)]], n.ºs 3, 6 e 7",
        ],
        "origem": "RGAC",
        "problema": [
            "Os animais nascidos e detidos em estabelecimentos são registados em nome do operador (art. [[Registo no Sistema de Informação de Animais de Companhia (SIAC)]], n.º 3), que pode ser pessoa coletiva. Mas num animal perigoso ou potencialmente perigoso «só pode figurar como titular uma pessoa singular, maior de 16 anos» (n.º 6), com exceção apenas para município e associação zoófila (n.º 7).",
            "Um criador ou uma loja constituídos como sociedade não cabem em nenhuma das regras.",
        ],
        "proposta": "Ressalvar no n.º 6 os operadores de estabelecimentos licenciados.",
        "levantado": [
            "Análise interna",
        ],
        "estado": "Aberto",
        "rel": [],
    },
    {
        "cod": "TIT-09",
        "cod_ensaio_2": "P-09",
        "cod_antigo": "T-09",
        "artigo": "Definições",
        "titulo": "«Titular ou operador» quando o operador já é titular",
        "etiquetas": ["TIT"],
        "onde": [
            "art. [[Definições]], definição de «Titular»",
            "art. [[Sistema de Informação de Animais de Companhia#2]], n.º 5",
            "art. [[Alterações ao registo]], n.º 3",
        ],
        "origem": "RGAC",
        "problema": [
            "A definição de titular já abrange o operador. Mesmo assim, vários artigos falam em «titular ou operador» ou em «residência do titular ou da morada do operador». Não fica claro se os deveres do titular se aplicam ao operador ou se são deveres diferentes.",
        ],
        "proposta": "Escolher uma solução: ou o operador é uma espécie de titular (e basta dizer titular), ou são figuras distintas (e a definição de titular deixa de incluir o operador).",
        "levantado": [
            "Análise interna",
        ],
        "estado": "Aberto",
        "rel": ["TIT-01"],
    },
    {
        "cod": "TIT-10",
        "cod_ensaio_2": "P-10",
        "cod_antigo": "T-10",
        "artigo": "Situações especiais de registo",
        "titulo": "Terminologia do CRO ainda não uniforme",
        "etiquetas": ["TIT", "REG"],
        "onde": [
            "art. [[Situações especiais de registo]], n.ºs 8 e 9",
            "art. [[Controlo da reprodução pelas câmaras municipais]], n.º 3",
            "art. [[Exame clínico dos animais e período mínimo de permanência]], n.º 2",
            "art. [[Destino dos animais]], n.º 13",
            "art. [[Condições da cedência]], n.º 1",
        ],
        "origem": "PARCIAL",
        "problema": [
            "Na versão das 18h00 os arts. [[Exame clínico dos animais e período mínimo de permanência]], [[Destino dos animais]] e [[Condições da cedência]] passaram a falar de titulares. Ficam por alinhar o art. [[Situações especiais de registo]], n.º 8 («não sejam reclamados pelos seus proprietários») e o art. [[Controlo da reprodução pelas câmaras municipais]], n.º 3 («titulares ou detentores»), todos para o mesmo prazo de 15 dias.",
        ],
        "proposta": "Usar titular para quem tem direito a reclamar o animal e detentor só para quem o tem à guarda.",
        "levantado": [
            "Análise interna",
        ],
        "estado": "Parcialmente resolvido",
        "rel": [],
    },
    {
        "cod": "TIT-11",
        "cod_ensaio_2": "P-11",
        "cod_antigo": "T-11",
        "artigo": "Contraordenações",
        "titulo": "Contraordenação dirigida só aos detentores",
        "etiquetas": ["TIT", "SAN"],
        "onde": [
            "art. [[Contraordenações]], n.º 2",
        ],
        "origem": "RGAC",
        "problema": [
            "O art. [[Contraordenações]], n.º 2 pune «O incumprimento, pelos detentores, dos deveres previstos no artigo XX.º». Com a nova definição, detentor é só o possuidor precário. Se os deveres em causa forem do titular, a contraordenação não o abrange.",
        ],
        "proposta": "Fixar a remissão e escrever «pelos titulares ou detentores», consoante o dever.",
        "levantado": [
            "Análise interna",
        ],
        "estado": "Aberto",
        "rel": ["TIT-06"],
    },
    {
        "cod": "TIT-12",
        "cod_ensaio_2": "P-12",
        "cod_antigo": "T-12",
        "artigo": "Obrigações gerais em matéria de bem-estar",
        "titulo": "Redação por decidir no art. [[Obrigações gerais em matéria de bem-estar]]",
        "etiquetas": ["TIT", "EST"],
        "onde": [
            "art. [[Obrigações gerais em matéria de bem-estar]], n.º 1",
        ],
        "origem": "RGAC",
        "problema": [
            "O texto diz «Os detentores Operadores ??de animais de companhia que se dediquem à sua reprodução, criação, manutenção ou venda». A troca de palavra ficou por decidir.",
        ],
        "proposta": "«Os operadores que se dediquem à reprodução, criação, manutenção ou venda de animais de companhia».",
        "levantado": [
            "Análise interna (revisão de 30.6.2026, 18h00)",
        ],
        "estado": "Aberto",
        "rel": [],
    },
    {
        "cod": "TIT-13",
        "cod_ensaio_2": "P-13",
        "cod_antigo": "T-13",
        "artigo": "Detenção responsável",
        "titulo": "Quem responde pelos danos causados pelo animal",
        "etiquetas": ["TIT"],
        "onde": [
            "artigo mais próximo: art. [[Detenção responsável]] (sem norma própria no RGAC)",
            "sem norma própria, salvo animais perigosos (seguro a cargo do titular)",
        ],
        "origem": "VIGENTE",
        "problema": [
            "O RGAC não diz se responde pelos danos o titular ou o detentor. Continuam a aplicar-se o art. 493.º do Código Civil (quem tem o encargo de vigilância) e o art. 502.º (quem usa o animal no seu interesse).",
            "Os médicos veterinários municipais perguntam, a propósito das famílias de acolhimento: «Quais são aqui as responsabilidades dos titulares (Associações) e quais as responsabilidades dos detentores dos animais (FAT)?».",
        ],
        "proposta": "Norma que diga que o titular e o detentor respondem nos termos gerais do Código Civil e que, entre operador e lar de acolhimento, a responsabilidade se reparte por contrato.",
        "levantado": [
            "Contributos dos médicos veterinários municipais (6.3.2026)",
            "Tribunal da Relação de Coimbra, proc. 281/10.1TBCV.C1 (11.7.2012)",
            "STJ, proc. 478/05.6TBMGL.C1.S1 (14.11.2013): os arts. 493.º e 502.º do Código Civil podem coexistir",
            "Tribunal da Relação de Lisboa, proc. 3121/03.4TBCSC.L1-6 (24.11.2009)",
            "Tribunal da Relação de Coimbra, proc. 6/22.9GCPBL.C1 (7.2.2024): dever de vigilância do detentor",
            "CDU (resposta de 2024)",
            "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): dever de atuar do detentor, nos termos do DL 82/2019, art. 3.º, al. a), e do art. 1253.º do Código Civil",
        ],
        "estado": "Aberto",
        "rel": ["TIT-14", "CED-08"],
    },
    {
        "cod": "TIT-14",
        "cod_ensaio_2": "P-14",
        "cod_antigo": "T-14",
        "artigo": "Definições",
        "titulo": "Família de acolhimento sem operador fica sem enquadramento",
        "etiquetas": ["TIT"],
        "onde": [
            "art. [[Definições]], definição de «Lar de acolhimento»",
            "art. [[Lares de acolhimento]]",
        ],
        "origem": "PARCIAL",
        "problema": [
            "O RGAC só enquadra o lar de acolhimento associado a um operador e «para efeitos de colocação no mercado». O animal fica registado em nome do operador. Isto resolve o acolhimento feito para uma associação com estabelecimento autorizado.",
            "Quem acolhe por iniciativa própria, sem operador, continua sem figura. O RGBEAC (jun. 2025) tinha a família de acolhimento temporário definida e regulada (arts. 4.º e 101.º). Uma revisora pediu «ELIMINAR ESTE CAPÍTULO» e a figura foi substituída pelo lar de acolhimento do Regulamento europeu.",
            "O estatuto de detentor já abrange quem acolhe por iniciativa própria. O RGAC define detentor como o possuidor precário nos termos do art. 1253.º do Código Civil, responsável «enquanto se mantiver como tal» (art. [[Definições]]). A al. a) do art. 1253.º abrange «Os que exercem o poder de facto sem intenção de agir como beneficiários do direito». O Tribunal da Relação do Porto aplicou o mesmo conceito, a partir do DL 82/2019, a quem tinha um cão na sua esfera de disponibilidade. O que falta não é o estatuto. Falta o regime: registo, limite de animais e forma de pôr termo ao acolhimento (ver TIT-20).",
        ],
        "proposta": "Decidir se a família de acolhimento informal fica proibida ou se passa a ter um registo simples no SIAC, como detentor, com limite de animais e dever de comunicação.",
        "levantado": [
            "Estratégia Nacional para os Animais Errantes (ENAE), pp. 30-31",
            "Contributos dos médicos veterinários municipais (6.3.2026)",
            "PAN (estatuto da família de acolhimento, 2024)",
            "SNMV (contra registos provisórios no SIAC)",
            "Raúl Farias, e-book do CEJ (2022): as associações, como pessoas coletivas, não respondem pelo crime de abandono",
            "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): conceito de detentor do DL 82/2019 e do art. 1253.º do Código Civil",
        ],
        "estado": "Parcialmente resolvido",
        "rel": ["TIT-13", "CED-02",
            "TIT-20",
        ],
    },
    {
        "cod": "TIT-15",
        "cod_ensaio_2": "P-15",
        "cod_antigo": "T-15",
        "artigo": "Obrigações das câmaras municipais",
        "titulo": "Quem encontra um animal passa a poder ser punido",
        "etiquetas": ["TIT"],
        "onde": [
            "art. [[Obrigações das câmaras municipais]], n.º 9",
            "art. [[Contraordenações]], n.º 2",
        ],
        "origem": "RGAC",
        "problema": [
            "O art. [[Obrigações das câmaras municipais]], n.º 9 manda comunicar a presença de um animal errante aos serviços veterinários municipais ou às autoridades policiais. O art. [[Contraordenações]], n.º 2 pune «A recolha de animais sem apresentação dos mesmos ao serviço veterinário municipal».",
            "Isto choca com o regime do achado do Código Civil (art. 1323.º), que permite ao achador anunciar o achado, ficar com o animal ao fim de um ano e retê-lo se houver receio de maus-tratos. Quem recolhe crias ou um animal ferido fica exposto a coima.",
            "Hoje a recolha por particular está prevista. O n.º 2 do art. 7.º da Portaria 146/2017 manda comunicar o animal errante aos serviços municipais ou às entidades policiais, «ou o animal é entregue a uma dessas entidades, se quem o observou também o capturou». O art. [[Obrigações das câmaras municipais]], n.º 9 reproduz a primeira parte e omite esta.",
            "O art. [[Obrigações das câmaras municipais]], n.º 3 diz que a captura e a recolha «competem, exclusivamente, às câmaras municipais». Na lei vigente a competência é atribuída às câmaras sem exclusivo: DL 276/2001, art. 19.º, n.º 1; DL 314/2003, art. 8.º, n.º 1; Lei 75/2013, anexo I, art. 33.º, n.º 1, al. ii). O Provedor de Justiça entendeu que as competências camarárias nesta matéria não são exclusivas, por referência a outras entidades públicas.",
            "O art. [[Contraordenações]], n.º 2 tem duas alíneas que se contradizem. Uma pune a recolha «sem apresentação dos mesmos ao serviço veterinário municipal», o que supõe que a recolha seguida de apresentação é lícita. A outra pune a recolha «por entidade diversa das câmaras municipais», o que a proíbe sempre.",
            "O art. 1323.º do Código Civil trata do animal perdido. Uma cria nascida na rua nunca teve dono e pode ser adquirida por ocupação (art. 1318.º do Código Civil). A coima do art. [[Contraordenações]], n.º 2 atinge também este caso.",
            "Os regulamentos municipais lidos admitem a entrega por quem encontra o animal: Setúbal (RSBEAMS 2020, art. 44.º, n.º 1, al. b)), Braga (Aviso 5616/2023, art. 57.º, n.º 1, al. b)), Évora (regulamento do CRO, art. 19.º, n.º 7) e Coimbra (Aviso 6348/2023, art. 12.º). O art. 11.º, n.º 3 do regulamento de Coimbra omite, como o RGAC, a parte final do n.º 2 do art. 7.º da Portaria.",
        ],
        "proposta": "Repor no art. [[Obrigações das câmaras municipais]], n.º 9 a parte final do n.º 2 do art. 7.º da Portaria 146/2017. Ressalvar no n.º 3 a recolha pontual por particular seguida de entrega ou comunicação num prazo curto, e as capturas em programa CED autorizado (ver CED-04). No art. [[Contraordenações]], n.º 2 manter só a recolha sem apresentação, com prazo fixado, e retirar a recolha por entidade diversa das câmaras. Articular com os arts. 1318.º e 1323.º do Código Civil.",
        "levantado": [
            "Análise interna",
            "Provedor de Justiça, processo R-4579/08 (Lajes do Pico): as competências camarárias não são exclusivas",
            "Regulamentos municipais de Setúbal, Braga, Évora e Coimbra (leitura de 8.10.2026)",
            "Análise interna (pedido de esclarecimento sobre gatos de colónia acolhidos, Setúbal, 8.10.2026)",
        ],
        "estado": "Aberto",
        "rel": ["CED-02", "CED-16",
            "CED-04",
            "TIT-20",
        ],
    },
    {
        "cod": "TIT-16",
        "cod_ensaio_2": "P-16",
        "cod_antigo": "T-16",
        "artigo": "Detenção responsável",
        "titulo": "Detentores de facto que dizem tratar de animais errantes",
        "etiquetas": ["TIT"],
        "onde": [
            "artigo mais próximo: art. [[Detenção responsável]] (sem norma própria no RGAC)",
            "sem norma própria",
        ],
        "origem": "VIGENTE",
        "problema": [
            "Os médicos veterinários municipais relatam casos de particulares que mantêm grupos de animais em propriedades privadas e dizem que são errantes, para que o Estado suporte os custos. Pedem um mecanismo de responsabilização dos detentores de facto.",
        ],
        "proposta": "Presunção de detenção para quem, de forma regular, aloja, alimenta ou controla o acesso aos animais num prédio de que dispõe.",
        "levantado": [
            "Contributos dos médicos veterinários municipais (6.3.2026)",
            "Tribunal da Relação de Lisboa, proc. 3121/03.4TBCSC.L1-6 (24.11.2009): detentor é aquele em cuja casa o animal é albergado",
            "ENAE (família de acolhimento temporário e cuidador não regulados)",
            "Lei 8/2017, art. 493.º-A do Código Civil (despesas de quem socorreu o animal)",
        ],
        "estado": "Aberto",
        "rel": ["CED-10"],
    },
    {
        "cod": "TIT-17",
        "cod_ensaio_2": "P-17",
        "cod_antigo": "T-17",
        "artigo": "Alterações ao registo",
        "titulo": "Prazos de comunicação ao SIAC mais pesados do que o Regulamento europeu",
        "etiquetas": ["TIT", "REG"],
        "onde": [
            "art. [[Alterações ao registo]], n.º 3",
            "art. [[Situações especiais de registo]], n.º 2",
        ],
        "origem": "RGAC",
        "problema": [
            "Morte: 2 dias úteis, com atestado médico-veterinário ou prova de incineração. Desaparecimento e recuperação: 24 horas. Entrada no território por operador: 5 dias úteis.",
            "O Regulamento (UE) 2026/1818 pede o registo da morte «em conformidade com as condições estabelecidas pelo Estado-Membro», sem prazo, e só se aplica aos proprietários particulares a partir de 2036 (cães) e 2041 (gatos) (art. 20.º, n.º 7). O falhanço destes prazos arrasta a presunção de abandono (TIT-05).",
        ],
        "proposta": "Rever os prazos. Dispensar a prova da morte quando a morte é registada por médico veterinário. Ponderar as 72 horas para o desaparecimento.",
        "levantado": [
            "OMV (propõe 72 horas)",
            "SNMV (propõe 48 horas)",
            "Comentário DAJA ao art. [[Alterações ao registo]] («Pode se de difícil aplicabilidade»)",
        ],
        "estado": "Aberto",
        "rel": ["TIT-05"],
    },
    {
        "cod": "TIT-18",
        "cod_ensaio_2": "P-18",
        "cod_antigo": "T-18",
        "artigo": "Definições",
        "titulo": "Animais deixados em centros veterinários",
        "etiquetas": ["TIT"],
        "onde": [
            "art. [[Definições]], definição de «Abandono»",
        ],
        "origem": "VIGENTE",
        "problema": [
            "A definição de abandono fala da remoção do animal sem comprovativo da transmissão da sua guarda. Não trata o caso do animal deixado num centro de atendimento médico-veterinário e que o titular não volta a buscar. O centro fica com o animal sem saber se o pode entregar, a quem e quando.",
        ],
        "proposta": "Prever um termo de responsabilidade na entrada do animal e um prazo a partir do qual se presume o abandono, com entrega a CRO ou associação e comunicação ao SIAC.",
        "levantado": [
            "OMV, parecer sobre abandono de animais em centros veterinários (nov. 2015)",
            "Cátia Simões, RJLB 2019 (o animal não recolhido de hotel ou CAMV escapa à definição de abandono)",
        ],
        "estado": "Aberto",
        "rel": ["TIT-05", "TIT-06"],
    },
    {
        "cod": "TIT-19",
        "cod_ensaio_2": "P-36",
        "cod_antigo": "T-19",
        "artigo": "Definições",
        "titulo": "Nada diz quem é titular quando o animal não tem proprietário",
        "etiquetas": ["TIT"],
        "onde": [
            "art. [[Definições]], definição de «Titular»",
            "art. [[Registo no Sistema de Informação de Animais de Companhia (SIAC)]], n.º 1",
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 6",
        ],
        "origem": "PARCIAL",
        "problema": [
            "A al. f) do art. 3.º do DL 82/2019 define o titular como o proprietário ou o possuidor «cuja posse faça presumir a propriedade». As duas hipóteses pressupõem um dono, ou um possuidor que atua como tal. O animal que ninguém tem como seu não cabe em nenhuma delas.",
            "O problema não é a falta de detenção. A titularidade nunca exigiu que o titular detenha o animal: o DL 82/2019 prevê o titular que não detém, no art. 13.º, n.º 2, al. d), que o obriga a comunicar o desaparecimento, no art. 14.º, n.º 1, que fala do «titular ou o simples detentor», e no art. 22.º, al. a), que alinha «titular, possuidor ou detentor». O que falta é a regra para o animal sem dono.",
            "O RGAC fecha a lacuna só no CED, ao mandar registar os gatos de colónia em nome do município (art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 6). Fica de fora o animal perdido antes de ser reclamado, o cão errante recolhido e o animal apreendido, e a definição geral continua assente no proprietário.",
            "O critério civil tem ainda um defeito próprio. A posse faz presumir a propriedade, mas o n.º 1 do art. 1268.º do Código Civil faz essa presunção ceder quando exista registo anterior a favor de outrem. O registo serve para provar a propriedade e a propriedade determina quem se registra.",
        ],
        "proposta": "Assentar a definição de titular no registo, com a presunção ilidível proposta na ficha TIT-03, e acrescentar uma norma supletiva: não havendo proprietário conhecido, é titular a entidade a quem a lei comete a responsabilidade pelo animal, designadamente a câmara municipal, através do CRO, nos casos de recolha e nos programas CED. Esta proposta qualifica a da ficha TIT-01: repor o critério do DL 82/2019 não fecha a lacuna, porque esse critério também pressupõe proprietário ou possuidor.",
        "levantado": [
            "Análise interna (titularidade dos animais em programas CED, 2.10.2026)",
        ],
        "estado": "Aberto",
        "rel": ["TIT-01", "TIT-02", "TIT-03", "CED-08"],
    },
    {
        "cod": "CED-01",
        "cod_ensaio_2": "P-19",
        "cod_antigo": "C-01",
        "artigo": "Programas de captura, esterilização e devolução ao local de origem",
        "titulo": "O CED passa a ser só uma faculdade das câmaras",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 1",
            "art. [[Norma revogatória]], n.º 1 (revogação da Lei 27/2016)",
        ],
        "origem": "RGAC",
        "problema": [
            "O art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 1 diz que as câmaras «podem […] autorizar» colónias. Hoje, acima da Portaria, está a Lei 27/2016, cujo art. 4.º diz que o Estado «assegura» a concretização de programas CED para gatos. O RGAC revoga essa lei. O dever legal desaparece e o CED fica dependente da vontade de cada câmara.",
            "O RGBEAC dizia «devem as câmaras municipais […] executar programas». Uma revisora comentou «A Lei 27 diz podem», o que não corresponde ao texto da lei.",
            "A proposta de resposta da DGAV à MIAR (24.10.2025) conclui que não há contradição insanável entre a Lei 27/2016 e a Portaria 146/2017, porque a matéria dos animais errantes é competência dos municípios. Não analisa o «assegura» do art. 4.º da Lei, que é o argumento central da MIAR. Apoia-se no Código Administrativo de 1940 e na Lei 75/2013, anexo I, art. 33.º, n.º 1, als. ii) e jj), que falam em abate e em animais nocivos (ver CED-19).",
            "A resposta da Direção de Serviços à MIAR (20.10.2025) funda o carácter facultativo do CED no n.º 2 do art. 9.º da Portaria 146/2017. A faculdade está no n.º 1 («podem […] autorizar»). O n.º 2 trata de quem toma a iniciativa.",
        ],
        "proposta": "Posição desta análise: a leitura que trata o CED como mera faculdade municipal, adotada na resposta da Direção de Serviços à MIAR (20.10.2025) e na proposta de resposta da DGAV (24.10.2025), é um erro de interpretação. O art. 4.º da Lei 27/2016 impõe ao Estado um dever («assegura») e indica o meio de o cumprir: os centros de recolha oficial, que são municipais. A competência municipal identifica quem executa o dever. Não o elimina. O «podem […] autorizar» do art. 9.º, n.º 1 da Portaria 146/2017 refere-se à autorização de cada colónia em local designado e tem de ser lido em conformidade com a Lei, porque são inválidos os regulamentos «desconformes com a Constituição, a lei e os princípios gerais de direito administrativo» (CPA, art. 143.º, n.º 1). O n.º 2 do art. 9.º só trata de quem toma a iniciativa e não pode fundar o carácter facultativo. Para o RGAC: manter pelo menos o nível da Lei 27/2016: «as câmaras municipais asseguram, diretamente ou por protocolo, programas CED para gatos, sempre que se justifique».",
        "levantado": [
            "ENAE, p. 35 («Os programas CED não estão instituídos em todo o território»)",
            "Livre e PAN (respostas de 2024)",
            "ARPA (o CED é dever legal dos municípios, dez. 2022)",
            "Gunther e outros, PNAS 2022, e Boone e outros, 2019 (o CED só resulta com esterilização intensa e contínua)",
            "Comissão Europeia, SWD(2024) 88 (errantes fora do âmbito do Regulamento (UE) 2026/1818)",
            "MIAR (dez. 2024 a out. 2025): o CED é dever do Estado e as associações não precisam de validação autárquica",
            "DGAV, proposta de resposta à MIAR (24.10.2025): o CED depende de autorização municipal",
        ],
        "estado": "Aberto",
        "rel": ["CED-02",
            "CED-19",
        ],
    },
    {
        "cod": "CED-02",
        "cod_ensaio_2": "P-20",
        "cod_antigo": "C-02",
        "artigo": "Programas de captura, esterilização e devolução ao local de origem",
        "titulo": "O cuidador de colónia não existe no texto",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programas de captura, esterilização e devolução ao local de origem]] (todo)",
            "art. [[Definições]] (sem definição)",
        ],
        "origem": "RGAC",
        "problema": [
            "A palavra cuidador não aparece no RGAC. O RGBEAC incluía os cuidadores no plano de formação e no plano de gestão da colónia. O plano de gestão do RGAC só identifica o médico veterinário e as pessoas da entidade responsável (art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 6, al. a)).",
            "Quem alimenta e vigia a colónia continua sem posição, sem deveres e sem proteção. Pode ser qualificado como detentor em nome do município e ficar exposto a responsabilidade civil (TIT-13) e à proibição de alimentar (CED-03).",
        ],
        "proposta": "Criar a figura do cuidador de colónia registado no SIAC, associado à colónia, como detentor em nome do município, com deveres e limites de responsabilidade definidos.",
        "levantado": [
            "ENAE, p. 35 («não está definido o conceito de \"cuidador da colónia\"»)",
            "Contributos dos médicos veterinários municipais (6.3.2026)",
            "PAN (figura do animal comunitário, PJL 662/XV)",
            "OMV, parecer ao PJL 662/XV (5.1.2024): contra o animal comunitário por diluir a responsabilidade",
            "PAN, PJL 662/XV (definição de animal comunitário)",
            "Município do Fundão, Edital 145/2023, art. 4.º, n.º 1 (cuidador registado responsável pela colónia)",
            "Município da Moita, Regulamento 143/2025, art. 3.º, n.º 2",
        ],
        "estado": "Aberto",
        "rel": ["CED-03", "TIT-13", "TIT-14"],
    },
    {
        "cod": "CED-03",
        "cod_ensaio_2": "P-21",
        "cod_antigo": "C-03",
        "artigo": "Controlo ambiental",
        "titulo": "Proibição nacional de alimentar animais na via pública",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Controlo ambiental]], n.º 3",
            "art. [[Contraordenações]], n.º 2 («A alimentação na via pública em violação do disposto no artigo XX.º»)",
        ],
        "origem": "RGAC",
        "problema": [
            "O art. [[Controlo ambiental]], n.º 3 proíbe alimentar animais na via pública, salvo em plano aprovado pela câmara, e o art. [[Contraordenações]] pune a infração. Hoje estas proibições existem só em alguns regulamentos municipais.",
            "A ENAE aponta esses regulamentos como obstáculo ao CED. Sem a figura do cuidador (CED-02) e com o CED dependente de autorização (CED-01), quem alimenta uma colónia não autorizada passa a cometer uma contraordenação. Nenhum revisor comentou a norma.",
        ],
        "proposta": "Excecionar expressamente os cuidadores de colónias registadas e os pontos de alimentação previstos em plano municipal de gestão de colónias.",
        "levantado": [
            "ENAE, p. 35 («Existem regulamentos ou posturas camarárias que proíbem alimentar animais errantes»)",
            "Contributo de um médico veterinário municipal (pede coimas aos alimentadores, posição contrária)",
            "Município do Fundão, Edital 145/2023 (o regime das colónias é exceção à proibição geral de alimentar na via pública)",
            "Provedor de Justiça, Relatório 2020 (campanhas da DGAV contra a alimentação de errantes)",
        ],
        "estado": "Aberto",
        "rel": ["CED-02"],
    },
    {
        "cod": "CED-04",
        "cod_ensaio_2": "P-22",
        "cod_antigo": "C-04",
        "artigo": "Obrigações das câmaras municipais",
        "titulo": "Só as câmaras podem capturar, mas o CED pode ser gerido por outras entidades",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Obrigações das câmaras municipais]], n.º 3",
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 4",
            "art. [[Contraordenações]], n.º 2",
        ],
        "origem": "RGAC",
        "problema": [
            "O art. [[Obrigações das câmaras municipais]], n.º 3 diz que a captura e a recolha de animais «competem, exclusivamente, às câmaras municipais», e o art. [[Contraordenações]] pune a «recolha e captura de animais por entidade diversa das câmaras municipais».",
            "O art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 4 admite que a câmara atribua a gestão do CED a outra entidade por protocolo. Na prática, as capturas para CED são feitas por associações e voluntários. Sem ressalva, ficam a cometer uma contraordenação.",
        ],
        "proposta": "Ressalvar no art. [[Obrigações das câmaras municipais]], n.º 3 as capturas feitas no âmbito de programa CED autorizado, pela entidade responsável ou por pessoas identificadas no plano de gestão.",
        "levantado": [
            "Análise interna",
        ],
        "estado": "Aberto",
        "rel": ["CED-02", "CED-08"],
    },
    {
        "cod": "CED-05",
        "cod_ensaio_2": "P-23",
        "cod_antigo": "C-05",
        "artigo": "Programas de captura, esterilização e devolução ao local de origem",
        "titulo": "Passagem obrigatória pelo CRO antes de o gato entrar na colónia",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 6, al. d)",
        ],
        "origem": "VIGENTE",
        "problema": [
            "Os gatos capturados têm de ser entregues no CRO para verificação da aptidão antes de integrarem a colónia. A regra vem da Portaria 146/2017 e sobrecarrega os CRO, cuja falta de espaço é a principal dificuldade apontada pelo relatório de avaliação da Lei 27/2016.",
            "O projeto de revisão da Portaria de 2021 revogava esta alínea. O RGBEAC também não a tinha.",
        ],
        "proposta": "Substituir a entrega no CRO por avaliação feita pelo médico veterinário do programa, com registo no SIAC.",
        "levantado": [
            "Relatório final do GTBEA (DGAV, 2021)",
            "Projeto de revisão da Portaria 146/2017 (ANMP, 2021)",
            "Provedor de Justiça, Relatório 2023 (queixas sobre sobrelotação dos CRO)",
        ],
        "estado": "Aberto",
        "rel": [],
    },
    {
        "cod": "CED-06",
        "cod_ensaio_2": "P-24",
        "cod_antigo": "C-06",
        "artigo": "Programas de captura, esterilização e devolução ao local de origem",
        "titulo": "Exclusão dos cães do CED",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 3",
        ],
        "origem": "VIGENTE",
        "problema": [
            "O RGAC mantém que o CED «não é aplicável a cães». É o ponto mais disputado entre as entidades. A OMV e a APMVEAC são contra o CED para cães. PAN e BE são a favor. Os médicos veterinários municipais propõem um regime excecional de cães comunitários, reconhecidos caso a caso pelo médico veterinário municipal. A FEDRA propõe parques de matilhas.",
            "O RGAC não prevê nenhuma alternativa para matilhas e cães assilvestrados quando o CRO não tem capacidade.",
        ],
        "proposta": "Manter a exclusão da devolução de cães à via pública, mas prever uma alternativa: parques de realojamento de matilhas ou um regime excecional de cão comunitário com critérios de segurança.",
        "levantado": [
            "OMV, parecer ao PJL 662/XV (5.1.2024): contra o CED em cães",
            "WOAH, Código Sanitário dos Animais Terrestres, cap. 7.7 (CED em cães só como medida complementar)",
            "APMVEAC (parecer set. 2023)",
            "PAN e BE (2024)",
            "Contributos dos médicos veterinários municipais (6.3.2026)",
            "FEDRA",
            "PCP (proposta ao OE2026)",
            "Livre (programa 2024)",
            "Movimento de Intervenção pelas Matilhas (Coimbra)",
            "Projeto de alteração da Portaria 146/2017 (esterilização excecional de cães)",
        ],
        "estado": "Aberto",
        "rel": [],
    },
    {
        "cod": "CED-07",
        "cod_ensaio_2": "P-25",
        "cod_antigo": "C-07",
        "artigo": "Programas de captura, esterilização e devolução ao local de origem",
        "titulo": "Remissões e numeração erradas no artigo do CED",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.ºs 1, 2, 5, 6 e 9",
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 6, al. e)",
            "art. [[Situações especiais de registo]], n.º 12",
        ],
        "origem": "RGAC",
        "problema": [
            "O n.º 1 remete para os «artigos 65.º e 66.º (controlo ambiental e controlo das populações errantes e assilvestradas)», que são agora os arts. [[Controlo ambiental]] e [[Controlo das populações errantes e assilvestradas]].",
            "Há dois n.º 5 e dois n.º 6. O n.º 9 remete para os requisitos «referidos no n.º 4», que são os do n.º 6. Os n.ºs 2 e 9 dizem o mesmo (medidas corretivas e suspensão).",
            "A al. e) do n.º 6 manda registar os gatos «em nome da câmara municipal promotora». O art. [[Situações especiais de registo]], n.º 12 diz «em nome do município responsável pelo programa CED».",
        ],
        "proposta": "Renumerar, corrigir as remissões, fundir os n.ºs 2 e 9 e usar «município» nos dois artigos.",
        "levantado": [
            "Revisão editorial de 10.6.2026 (ponto B9)",
            "Análise interna",
        ],
        "estado": "Aberto",
        "rel": [],
    },
    {
        "cod": "CED-08",
        "cod_ensaio_2": "P-26",
        "cod_antigo": "C-08",
        "artigo": "Programas de captura, esterilização e devolução ao local de origem",
        "titulo": "Entidade promotora, entidade responsável e titular: quem responde pela colónia",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.ºs 4, 5 (segundo), 6 e 10",
            "art. [[Situações especiais de registo]], n.º 12",
        ],
        "origem": "VIGENTE",
        "problema": [
            "O artigo usa entidade promotora (a câmara) e entidade responsável (quem gere por protocolo) sem as definir e sem dizer quem responde por quê. Os gatos são registados em nome do município, que fica titular. As despesas são da entidade promotora ou do protocolo (n.º 10).",
            "Não se diz quem responde pelos danos causados por gatos de colónia. A CDU referiu as «questões práticas e de responsabilidade civil» para ter prudência no alargamento do CED.",
            "Há duas leituras na DGAV sobre o titular dos gatos CED. A proposta de resposta à MIAR (24.10.2025) admite que o CRO ou a associação zoófila sejam titulares, «podendo essa questão ficar definida nos referidos programas CED», com base no DL 82/2019, art. 3.º, al. f), e art. 17.º. A nota jurídica sobre a titularidade (out. 2026) conclui que o titular é o município, pelo DL 82/2019, art. 11.º, n.º 5, e pela entrega obrigatória no CRO (Portaria 146/2017, art. 9.º, n.º 4, al. d)). O art. 17.º é uma isenção de taxa e não um critério de titularidade, e a titularidade não pode ser fixada por um programa. O RGAC segue a segunda leitura (art. [[Situações especiais de registo]], n.º 12).",
        ],
        "proposta": "Definir as duas entidades no art. [[Definições]] ou no próprio art. [[Programas de captura, esterilização e devolução ao local de origem]], e dizer que o município, como titular, responde nos termos gerais, com direito de regresso sobre a entidade responsável. Alinhar a posição interna da DGAV antes de responder a outros pedidos sobre a titularidade dos gatos CED.",
        "levantado": [
            "CDU (resposta de 2024)",
            "Análise interna",
            "PCP (proposta ao OE2026)",
            "ARPA (dez. 2022)",
            "DGAV, proposta de resposta à MIAR (24.10.2025): CRO ou associação podem ser titulares",
            "MIAR (2024 e 2025): recusa ser titular de animais de rua",
        ],
        "estado": "Aberto",
        "rel": ["TIT-13", "CED-04"],
    },
    {
        "cod": "CED-09",
        "cod_ensaio_2": "P-27",
        "cod_antigo": "C-09",
        "artigo": "Programas de captura, esterilização e devolução ao local de origem",
        "titulo": "Registo da colónia no SIAC sem conteúdo definido",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 6, al. f)",
            "art. [[Sistema de Informação de Animais de Companhia#1]]",
        ],
        "origem": "PARCIAL",
        "problema": [
            "O RGAC prevê o registo da colónia no SIAC, com georreferenciação, número de animais e entidade responsável. É um avanço: hoje não é possível saber quantas colónias existem nem onde.",
            "Falta dizer se a colónia tem número próprio, quem atualiza o registo, se os cuidadores ficam registados e se o registo é público.",
        ],
        "proposta": "Número nacional de colónia, atualização pela entidade responsável, cuidadores associados e registo anual de entradas, saídas e mortes.",
        "levantado": [
            "ENAE, p. 35 («não é possível aferir o número de animais nem o número e localização das colónias»)",
            "ENAE, §33 (número de registo nacional da colónia)",
            "Provedor de Justiça, Relatório 2023 (planos CED autorizados sem divulgação pública)",
        ],
        "estado": "Parcialmente resolvido",
        "rel": ["CED-02"],
    },
    {
        "cod": "CED-10",
        "cod_ensaio_2": "P-28",
        "cod_antigo": "C-10",
        "artigo": "Programa CED em prédios privados",
        "titulo": "Colónias em prédios privados",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programa CED em prédios privados]]",
        ],
        "origem": "PARCIAL",
        "problema": [
            "O RGAC admite o CED em prédios privados, com anuência escrita do proprietário, dever de colaborar e contraordenação em caso de obstrução. Os médicos veterinários municipais dizem que a maioria das colónias está em quintais.",
            "Ficam por resolver: o que fazer quando o proprietário não autoriza; o dever de colaborar inclui a alimentação (n.º 3), o que obriga o proprietário a tarefas que não escolheu; e os prédios devolutos, para os quais um comentário DAJA sugere a posse administrativa pelos municípios.",
        ],
        "proposta": "Prever a situação de recusa (intervenção por razões de saúde pública ou bem-estar animal) e retirar a alimentação do dever de colaboração do proprietário.",
        "levantado": [
            "Contributos dos médicos veterinários municipais (6.3.2026)",
            "Comentário DAJA ao art. [[Programas de captura, esterilização e devolução ao local de origem]] (prédios devolutos, posse administrativa, RJUE)",
        ],
        "estado": "Parcialmente resolvido",
        "rel": ["TIT-16"],
    },
    {
        "cod": "CED-11",
        "cod_ensaio_2": "P-29",
        "cod_antigo": "C-11",
        "artigo": "Programas de captura, esterilização e devolução ao local de origem",
        "titulo": "CED e conservação da natureza",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 5",
        ],
        "origem": "VIGENTE",
        "problema": [
            "O RGAC diz só que o CED «deve ser evitado» em parques públicos, refúgios de vida selvagem e habitats. Não diz quem decide nem como. O RGBEAC exigia consulta prévia ao ICNF em áreas classificadas. O projeto de revisão da Portaria de 2021 exigia articulação com o ICNF.",
            "A SPEA aponta a predação por gatos como ameaça às aves marinhas.",
        ],
        "proposta": "Exigir parecer do ICNF para colónias em áreas classificadas ou na sua proximidade.",
        "levantado": [
            "SPEA",
            "RGBEAC (jun. 2025), art. 44.º, n.º 3",
            "SPEA, parecer Açores 2020 (84% da predação de cagarros por gatos)",
            "Trouwborst e Somsen, Journal of Environmental Law, 2020 (Diretivas Aves e Habitats)",
            "Galão e outros, Biological Conservation, 2025 (predação na Madeira)",
            "Loss, Will e Marra, Nature Communications, 2013",
            "Projeto de alteração da Portaria 146/2017 (articulação com o ICNF)",
        ],
        "estado": "Aberto",
        "rel": [],
    },
    {
        "cod": "CED-12",
        "cod_ensaio_2": "P-30",
        "cod_antigo": "C-12",
        "artigo": "Obrigatoriedade do uso de coleira ou peitoral e trela ou açaimo",
        "titulo": "Gatos de colónia em infração permanente",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Obrigatoriedade do uso de coleira ou peitoral e trela ou açaimo]], n.º 1",
            "art. [[Definições]], definição de «Animal errante»",
            "art. [[Obrigações das câmaras municipais]], n.º 1, al. a)",
        ],
        "origem": "RGAC",
        "problema": [
            "O art. [[Obrigatoriedade do uso de coleira ou peitoral e trela ou açaimo]], n.º 1 obriga todos os cães e gatos na via pública a usar coleira com o contacto do detentor. Os gatos de colónia não a usam.",
            "Pela definição do art. [[Definições]], um gato fora do controlo e da guarda do detentor é errante, e a câmara deve capturar os errantes (art. [[Obrigações das câmaras municipais]], n.º 1, al. a)). Um gato de colónia CED encaixa nas duas normas.",
        ],
        "proposta": "Excecionar os gatos integrados em programa CED, identificados pelo corte na orelha e pelo transponder, no art. [[Obrigatoriedade do uso de coleira ou peitoral e trela ou açaimo]] e na definição de animal errante.",
        "levantado": [
            "Revisão editorial de 10.6.2026 (pontos A4 e A5)",
        ],
        "estado": "Aberto",
        "rel": [],
    },
    {
        "cod": "CED-13",
        "cod_ensaio_2": "P-31",
        "cod_antigo": "C-13",
        "artigo": "Programas de captura, esterilização e devolução ao local de origem",
        "titulo": "Crias e gatos sociáveis: retirar ou devolver",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 7",
        ],
        "origem": "VIGENTE",
        "problema": [
            "O RGAC manda libertar os gatos na colónia de origem, salvo deslocalização «nos termos a definir e divulgar pela DGAV». Não diz o que fazer com as crias em idade de socialização nem com os gatos dóceis.",
            "A ENAE diz que esses animais são retirados das colónias e encaminhados para adoção. Não há critério nem procedimento para distinguir o gato feral do sociável.",
        ],
        "proposta": "Norma que mande encaminhar para adoção as crias em idade de socialização e os adultos sociáveis, com critério definido pela DGAV.",
        "levantado": [
            "ENAE, p. 34 («Sempre que possível, os animais adultos dóceis e as crias que ainda estejam em idade de socialização são retirados das colónias e encaminhados para adoção»)",
            "APMVEAC (adoção de animais com menos de 6 meses, 2021)",
        ],
        "estado": "Aberto",
        "rel": ["TIT-15"],
    },
    {
        "cod": "CED-14",
        "cod_ensaio_2": "P-32",
        "cod_antigo": "C-14",
        "artigo": "Programas de captura, esterilização e devolução ao local de origem",
        "titulo": "Suspensão do programa e recolha dos gatos sem garantias",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.ºs 2 e 9",
        ],
        "origem": "VIGENTE",
        "problema": [
            "A câmara pode suspender o programa e recolher os gatos para o CRO. Não há audiência da entidade responsável, prazo para corrigir, nem destino previsto para os gatos se o CRO não tiver espaço.",
        ],
        "proposta": "Prever notificação prévia com prazo para corrigir e um plano de destino dos animais antes da recolha.",
        "levantado": [
            "Análise interna (inventário de zonas cinzentas do CED)",
        ],
        "estado": "Aberto",
        "rel": ["CED-07"],
    },
    {
        "cod": "CED-15",
        "cod_ensaio_2": "P-33",
        "cod_antigo": "C-15",
        "artigo": "Programas de captura, esterilização e devolução ao local de origem",
        "titulo": "Meios: médicos veterinários municipais e financiamento",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.ºs 1, 5 (segundo) e 10",
        ],
        "origem": "VIGENTE",
        "problema": [
            "O CED depende de parecer vinculativo e da supervisão do médico veterinário municipal ou ao serviço do município. Há concelhos sem médico veterinário municipal. As despesas ficam para a entidade promotora ou para o protocolo, sem fonte de financiamento prevista.",
        ],
        "proposta": "Admitir médico veterinário contratado ou partilhado entre municípios e ligar o CED às linhas de apoio da DGAV.",
        "levantado": [
            "Relatório final do GTBEA (DGAV, 2021): financiamento como principal constrangimento",
            "Inventário interno de zonas cinzentas do CED (zona 20)",
            "PCP (2021)",
        ],
        "estado": "Aberto",
        "rel": [],
    },
    {
        "cod": "CED-16",
        "cod_ensaio_2": "P-34",
        "cod_antigo": "C-16",
        "artigo": "Programas de captura, esterilização e devolução ao local de origem",
        "titulo": "Conflito com vizinhos e dimensão da colónia",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Programas de captura, esterilização e devolução ao local de origem]], n.º 6 (segundo)",
        ],
        "origem": "VIGENTE",
        "problema": [
            "O RGAC diz que a dimensão da colónia não pode pôr em causa a salubridade, a saúde pública e a segurança, mas não dá critério. Os médicos veterinários municipais relatam casos em que os cuidadores pedem o CED e os vizinhos exigem a recolha dos animais, e dizem que recolher milhares de gatos assilvestrados para os CRO não é viável.",
        ],
        "proposta": "Critérios de dimensão por tipo de local no manual da DGAV e um procedimento de mediação antes de decidir a recolha.",
        "levantado": [
            "Contributos dos médicos veterinários municipais (6.3.2026)",
        ],
        "estado": "Aberto",
        "rel": ["CED-14"],
    },
    {
        "cod": "CED-17",
        "cod_ensaio_2": "P-35",
        "cod_antigo": "C-17",
        "artigo": "Controlo das populações errantes e assilvestradas",
        "titulo": "Plano municipal de controlo de errantes sem conteúdo mínimo nem consequências",
        "etiquetas": ["CED"],
        "onde": [
            "art. [[Controlo das populações errantes e assilvestradas]], n.ºs 1 a 3",
        ],
        "origem": "VIGENTE",
        "problema": [
            "As câmaras devem apresentar à DGAV, todos os anos, um plano de controlo das populações errantes. O artigo não diz que dados são obrigatórios, não liga o plano ao registo das colónias no SIAC e não prevê consequências para quem não o apresenta. Um comentário do grupo de trabalho pede isso mesmo.",
        ],
        "proposta": "Fixar os dados mínimos (colónias, número de gatos esterilizados, capturas, entradas e saídas do CRO), retirá-los do SIAC sempre que possível e ligar o acesso a apoios públicos à entrega do plano.",
        "levantado": [
            "Comentário do grupo de trabalho ao art. [[Controlo das populações errantes e assilvestradas]] («prever sanções para os Municípios que não informam a DGAV»)",
        ],
        "estado": "Aberto",
        "rel": ["CED-09"],
    },
    {
        "cod": "TIT-20",
        "cod_ensaio_2": "P-37",
        "cod_antigo": "T-20",
        "artigo": "Centros de recolha",
        "titulo": "Quem acolhe um animal errante pode ficar sem saída lícita",
        "etiquetas": [
            "TIT",
            "CED"
        ],
        "onde": [
            "art. [[Definições]], definição de «Abandono»",
            "art. [[Centros de recolha]], n.ºs 7 e 8",
            "art. [[Obrigações das câmaras municipais]], n.º 9"
        ],
        "origem": "VIGENTE",
        "problema": [
            "Quem acolhe um animal errante passa a ser detentor (art. [[Definições]]). Se depois o devolver à rua, a conduta cabe na definição de abandono: remoção «pelo detentor ou titular» sem comprovativo da transmissão da guarda para outra pessoa, para o município ou para associação zoófila (art. [[Definições]]). Pode ainda caber no art. 388.º do Código Penal, que pune quem, «tendo o dever de guardar, vigiar ou assistir animal de companhia», o abandona.",
            "A saída lícita é entregar o animal. O art. [[Centros de recolha]], n.º 7 só deixa pedir a recolha ao CRO aos titulares, e só por circunstâncias supervenientes. O n.º 8 manda os restantes titulares recorrer a associação zoófila. O detentor que não é titular não aparece em nenhum dos dois números. O art. [[Obrigações das câmaras municipais]], n.º 9 deixou de prever a entrega por quem capturou o animal (ver TIT-15).",
            "No regime vigente o problema já existe na prática. Os regulamentos municipais permitem recusar a receção por sobrelotação (Setúbal, RSBEAMS 2020, art. 57.º, n.º 6) ou depois de ponderar fatores de risco (Coimbra, Aviso 6348/2023, art. 12.º, n.º 2). Quem acolheu fica entre a recusa do CRO e a proibição de abandono."
        ],
        "proposta": "Prever no art. [[Centros de recolha]] que o detentor de animal errante que o tenha recolhido possa entregá-lo ao CRO. A recusa do CRO deve ser fundamentada e indicar alternativa: associação zoófila, lar de acolhimento ou integração no programa CED. A entrega recusada afasta a presunção de abandono.",
        "levantado": [
            "Análise interna (pedido de esclarecimento sobre gatos de colónia acolhidos, Setúbal, 8.10.2026)",
            "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): o detentor que não cuida do animal deve diligenciar a sua entrega a canil ou organização que o possa receber",
            "Regulamentos municipais de Setúbal (2020) e Coimbra (2023)"
        ],
        "estado": "Aberto",
        "rel": [
            "TIT-14",
            "TIT-15"
        ]
    },
    {
        "cod": "CED-18",
        "cod_ensaio_2": "P-38",
        "cod_antigo": "C-18",
        "artigo": "Definições",
        "titulo": "A definição de animal errante passa a abranger qualquer animal não identificado",
        "etiquetas": [
            "CED"
        ],
        "onde": [
            "art. [[Definições]], definição de «Animal errante»",
            "art. [[Obrigações das câmaras municipais]], n.º 1, al. a)"
        ],
        "origem": "PARCIAL",
        "problema": [
            "Hoje há duas definições. O DL 276/2001 (art. 2.º, n.º 1, al. c)) considera errante o animal encontrado em lugar público fora do controlo e guarda do detentor, «ou relativamente ao qual existam fortes indícios de que foi abandonado ou não tem detentor e não esteja identificado». O DL 314/2003 (art. 2.º, al. n)) só considera errante o cão ou gato encontrado em local público, fora do controlo ou vigilância do detentor, «e não identificado». Uma cria sem dono nascida num quintal é errante para o primeiro e não para o segundo.",
            "O RGAC unifica, mas troca o «e» por «ou»: é errante também o animal «que não tem detentor ou não se encontra identificado» (art. [[Definições]]). Lida à letra, qualquer animal não identificado é errante, mesmo em casa e com detentor, incluindo as crias antes do prazo de identificação. O art. [[Obrigações das câmaras municipais]], n.º 1, al. a) limita a captura aos errantes encontrados em lugares públicos, o que atenua o efeito, mas as outras normas que usam o conceito ficam com um âmbito que não se pretende."
        ],
        "proposta": "Repor a conjunção cumulativa: «que não tem detentor e não se encontra identificado». Ponderar excluir da definição os gatos integrados em programa CED (ver CED-12).",
        "levantado": [
            "Análise interna (8.10.2026)"
        ],
        "estado": "Aberto",
        "rel": [
            "CED-12",
            "TIT-15"
        ]
    },
    {
        "cod": "CED-19",
        "cod_ensaio_2": "P-39",
        "cod_antigo": "C-19",
        "artigo": "Obrigações das câmaras municipais",
        "titulo": "A Lei 75/2013 ainda atribui às câmaras o abate de canídeos e gatídeos",
        "etiquetas": [
            "CED"
        ],
        "onde": [
            "artigo mais próximo: art. [[Obrigações das câmaras municipais]] (sem norma própria no RGAC)",
            "sem norma própria"
        ],
        "origem": "VIGENTE",
        "problema": [
            "O anexo I da Lei 75/2013, art. 33.º, n.º 1, al. ii), dá à câmara municipal a competência para «Proceder à captura, alojamento e abate de canídeos e gatídeos». A redação é anterior à Lei 27/2016, que proibiu o abate como forma de controlo da população, e não foi alterada.",
            "O RGAC revoga a Lei 27/2016 (art. [[Norma revogatória]], n.º 1) e não altera a Lei 75/2013. A norma geral de competência das câmaras continua a falar em abate."
        ],
        "proposta": "Alterar a al. ii) para «Proceder à captura, recolha, alojamento e esterilização de animais de companhia errantes». Verificar se, por ser matéria de competências das autarquias, a alteração exige lei da Assembleia da República ou autorização legislativa.",
        "levantado": [
            "Análise interna (8.10.2026)"
        ],
        "estado": "Aberto",
        "rel": [
            "CED-17"
        ]
    },
    {
        "cod": "BEM-01",
        "cod_ensaio_2": "P-40",
        "cod_antigo": "P-01",
        "artigo": "Necessidades comportamentais",
        "titulo": "A amarração no domicílio fica sem duração máxima nem requisitos verificáveis",
        "etiquetas": [
            "BEM"
        ],
        "onde": [
            "art. [[Necessidades comportamentais]], n.ºs 4 e 5",
            "art. [[Práticas de maneio e contenção proibidas]], n.º 1, al. i)",
            "art. [[Contraordenações]], n.º 2"
        ],
        "origem": "RGAC",
        "problema": [
            "O art. [[Necessidades comportamentais]], n.º 4 proíbe amarrar cães e gatos por mais de uma hora. Estende a todos os titulares e detentores a regra que o Regulamento (UE) 2026/1818 fixa só para os operadores (art. 17.º, n.º 3).",
            "O n.º 5 exceciona a amarração «temporariamente no domicílio de titular ou detentor», com quatro condições cumulativas. Nenhuma fixa duração máxima, características do meio de amarração ou casos em que a amarração é sempre proibida. A condição «necessidade pontual e temporária» não é verificável no local. A condição de o endereço registado no SIAC coincidir com o do detentor não tem relação com o bem-estar do animal.",
            "Condenação por amarração diária. O Tribunal da Relação do Porto confirmou, em 8.5.2024, a condenação por maus-tratos a animal de companhia, por omissão (art. 387.º, n.ºs 1 e 2, do Código Penal), de quem mantinha um cão de cerca de 10 anos «diariamente acorrentado» e, no dia da intervenção, «fechado numa casota de madeira tipo gaiola, não conseguindo este sequer manter-se em pé». Pena de 200 dias de multa e pena acessória de proibição de detenção de animais de companhia por dois anos e seis meses (art. 388.º-A do Código Penal). O cão foi eutanasiado. A exceção do n.º 5, tal como está redigida, não permite distinguir com segurança uma situação destas de uma amarração lícita até ela chegar ao crime.",
            "O art. [[Contraordenações]], n.º 2 remete sempre para «artigo XX.º». Não é possível confirmar que a violação dos n.ºs 4 e 5 do art. [[Necessidades comportamentais]] tem coima.",
            "O Projeto de Lei n.º 612/XVII/1.ª (BE, 5.5.2026) propõe critérios objetivos: até três horas por dia, meio com pelo menos três metros ou o triplo do comprimento do animal, destorcedor, ligação por peitoral ou coleira larga, um animal por ponto de fixação, e proibição absoluta para animais com menos de seis meses, fêmeas gestantes ou lactantes, animais doentes e em aviso meteorológico laranja ou vermelho (arts. 6.º e 7.º)."
        ],
        "proposta": "Fixar no n.º 5 uma duração máxima diária, requisitos técnicos do meio de amarração (comprimento mínimo, destorcedor, peitoral ou coleira larga, um animal por ponto) e casos de proibição absoluta (crias, fêmeas gestantes ou lactantes, animais doentes, aviso meteorológico laranja ou vermelho). Retirar a condição do endereço no SIAC. Prever coima expressa para a violação dos n.ºs 4 e 5 no art. [[Contraordenações]].",
        "levantado": [
            "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): condenação por maus-tratos de cão mantido diariamente acorrentado",
            "Projeto de Lei n.º 612/XVII/1.ª (BE, 5.5.2026), arts. 6.º e 7.º",
            "Regulamento (UE) 2026/1818, art. 17.º, n.º 3",
            "Análise interna (8.10.2026)"
        ],
        "estado": "Aberto",
        "rel": []
    },
    {
        "cod": "REG-01",
        "cod_ensaio_2": "P-41",
        "cod_antigo": "A-01",
        "artigo": "Âmbito Objetivo",
        "titulo": "Duas normas diferentes sobre que espécies são animais de companhia",
        "etiquetas": [
            "REG"
        ],
        "onde": [
            "art. [[Âmbito Objetivo]], n.º 2",
            "art. [[Animais de companhia]], n.ºs 1 a 3",
            "art. [[Definições]], definição de «Animal de companhia»"
        ],
        "origem": "RGAC",
        "problema": [
            "O art. [[Âmbito Objetivo]], n.º 2 diz que são animais de companhia as espécies da Parte A do Anexo I do Regulamento (UE) 2016/429 e, «quando detidos para fins de companhia», as da Parte B. O art. [[Animais de companhia]], n.º 2 diz que as espécies da Parte B são «também considerados animais de companhia», sem essa condição. O n.º 3 acrescenta as espécies de uma lista positiva a aprovar por portaria. A definição do art. [[Definições]] remete só para o art. [[Âmbito Objetivo]], n.º 2.",
            "O conceito tem efeitos fora do RGAC. O Tribunal da Relação do Porto usou a remissão do DL 82/2019, art. 4.º, n.º 1, para o Regulamento (UE) 2016/429 para delimitar o animal de companhia do art. 389.º do Código Penal. Revogado o DL 82/2019, essa leitura passa a apoiar-se no RGAC, que tem duas regras diferentes."
        ],
        "proposta": "Manter uma só norma: a do art. [[Âmbito Objetivo]], n.º 2, com a condição para a Parte B. No art. [[Animais de companhia]] ficam só a lista positiva e as exceções.",
        "levantado": [
            "Análise interna (8.10.2026)",
            "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): conceito penal de animal de companhia"
        ],
        "estado": "Aberto",
        "rel": []
    },
    {
        "cod": "SAN-01",
        "cod_ensaio_2": "P-42",
        "cod_antigo": "S-01",
        "artigo": "Contraordenações",
        "titulo": "Os deveres dos CRO e o relatório anual ficam sem coima",
        "etiquetas": [
            "SAN",
            "EST"
        ],
        "onde": [
            "art. [[Contraordenações]], n.º 2, als. e) a g), s), t), u) e v)",
            "art. [[Regime de Gestão e Registo de Animais de Companhia (CRO e Abrigo)]], n.ºs 4 e 5",
            "art. [[Sistema de Informação de Animais de Companhia#1]], n.º 1",
            "art. [[Plataforma Nacional de Adoção de Animais de Companhia]], n.º 6",
            "art. [[Controlo da reprodução pelas câmaras municipais]], n.ºs 3, 4 e 8",
            "art. [[Obrigações das câmaras municipais]], n.ºs 1 e 2",
            "art. [[Centros de recolha oficial]], n.º 1",
            "art. [[Destino dos animais]], n.ºs 8, 13 e 14",
            "art. [[Eutanásia]], n.ºs 1 e 6",
            "art. [[Direito subsidiário]]"
        ],
        "origem": "PARCIAL",
        "problema": [
            "Hoje os deveres dos CRO estão na Lei 27/2016 (art. 3.º) e na Portaria 146/2017 (arts. 7.º a 11.º): captura e recolha, esterilização antes da adoção, encaminhamento para adoção, proibição do abate por sobrelotação e relatório anual de gestão. Nenhum destes dois diplomas tem contraordenações.",
            "A coima só chega por via indireta. O DL 276/2001, art. 68.º, n.º 1, pune a falta de mera comunicação prévia do centro de recolha (al. a)) e «O alojamento de animais de companhia em desrespeito das condições fixadas no presente diploma» (al. f)). Para os centros de recolha, essas condições são as dos arts. 41.º e 8.º a 16.º (art. 42.º, n.º 1): instalações, espaço, ambiente, alimentação, maneio, higiene, segurança e cuidados de saúde. A al. f) não abrange a adoção, a esterilização nem o envio de dados. O art. 7.º, n.º 3, proíbe infligir a morte a um animal «sem necessidade», e a sua violação é contraordenação muito grave (art. 68.º, n.º 2, al. d)), com instrução pela DGAV (art. 70.º). O tipo visa a violência contra o animal: a morte gratuita, o sofrimento e as lesões, com a gravidade do abandono e das lutas (art. 68.º, n.º 2). Não abrange a occisão feita por médico veterinário, por método sem dor e por decisão do CRO, mesmo quando o motivo é proibido, como a sobrelotação. O abate nos CRO tem regime próprio, sem coima (DL 276/2001, art. 19.º; Lei 27/2016, art. 3.º, n.ºs 4 a 8), e o princípio da legalidade não deixa usar o tipo da violência para cobrir essa falta. A al. i) pune «O abate em desrespeito das disposições do artigo 19.º», mas o art. 19.º não tem a proibição da Lei 27/2016 e o seu n.º 10 dispõe: «A recolha, captura e abate compulsivo de cães e gatos é regulada por legislação própria». O DL 82/2019, art. 21.º, n.º 1, pune o CRO que deixa sair um animal sem identificação (al. a), com o art. 5.º, n.º 3) e o CRO titular que não regista no SIAC a transmissão ou a morte do animal (al. c), com os arts. 11.º, n.º 5, e 13.º).",
            "A Lei 92/95 tem uma norma geral, além da do DL 276/2001. O art. 1.º, n.º 1, proíbe «todas as violências injustificadas contra animais», incluindo os atos que, «sem necessidade», lhes infligem a morte. O art. 12.º, n.º 1, acrescentado pela Lei 6/2022, diz que «As infrações ao disposto na presente lei constituem contraordenação», com coima de 500 a 44 800 euros para pessoa coletiva. Pela mesma razão, também não abrange a occisão por sobrelotação num CRO. A instrução e a decisão cabem à câmara municipal (art. 14.º), que é também quem gere o CRO. O RGAC revoga a Lei 92/95 (art. [[Norma revogatória]], n.º 1, al. a)) e o art. [[Contraordenações]] não tem norma geral.",
            "Hoje os CRO não têm dever de enviar dados à DGAV. A Lei 27/2016, art. 3.º, n.º 9, obriga-os a publicitar o relatório de gestão no primeiro mês de cada ano, e a DGAV faz o relatório nacional «com base» nesses relatórios (n.º 10). O Decreto Regulamentar 4/2025 e o Despacho 2836/2026 repetem esta lógica. Nenhuma destas normas tem sanção. O DL 276/2001, art. 68.º, n.º 1, al. d), só abrange dados pedidos para funções desse decreto-lei. O único reporte com consequência é o financeiro, dos beneficiários de incentivos (Lei 73-A/2025, art. 125.º, n.º 3; Despacho 9102/2026, arts. 14.º e 15.º): revogação do apoio e restituição das verbas.",
            "O relatório nacional de 2025 da DGAV mostra os limites deste modelo. Os dados vêm do CVAR/IE e de uma tabela pedida por correio eletrónico. Responderam 133 dos 220 municípios com CRO (60,5 %) e 37 não registaram no CVAR/IE a atividade de 2025. Do CVAR/IE só se usam as recolhas e as eutanásias, porque não distingue a adoção da entrega a associações, nem as esterilizações e vacinações feitas no CRO das restantes. Os dados são apresentados por município e não por CRO. Um CRO intermunicipal, como o de Proença-a-Nova, gerido por uma associação de 12 municípios (Regulamento n.º 164/2022), não tem linha própria. O registo mensal no CVAR/IE é um dever do médico veterinário que executa a campanha antirrábica (Portaria 264/2013, anexo, art. 6.º, n.º 1, al. d)), também sem sanção.",
            "O município pode ser arguido. O regime das contraordenações económicas equipara os municípios a pequenas empresas (DL 9/2021, anexo, art. 19.º, n.º 4, al. b)). O RGAC remete para o regime geral das contraordenações (art. [[Direito subsidiário]]), que não tem esta regra.",
            "O RGAC resolve uma parte. O art. [[Contraordenações]], n.º 2, al. u), pune a falta de CRO (art. [[Centros de recolha oficial]], n.º 1). Como o CRO passa a ser estabelecimento (art. [[Definições]]), as als. e) a g) abrangem os seus requisitos técnicos e a mera comunicação prévia. Todas as remissões estão em «artigo XX.º».",
            "Ficam sem coima a omissão de captura e recolha (art. [[Obrigações das câmaras municipais]], n.ºs 1 e 2), a esterilização pelo próprio CRO antes da adoção (art. [[Controlo da reprodução pelas câmaras municipais]], n.º 3; art. [[Destino dos animais]], n.º 13), o encaminhamento para adoção e a sua divulgação (art. [[Destino dos animais]], n.ºs 13 e 14) e o relatório anual (art. [[Regime de Gestão e Registo de Animais de Companhia (CRO e Abrigo)]], n.ºs 4 e 5). A al. s) remete para o n.º 8 do art. [[Controlo da reprodução pelas câmaras municipais]], que só pune o adotante (n.º 4). A al. t) pune quem capture sem ser a câmara, e não a câmara que deixa de capturar.",
            "O art. [[Regime de Gestão e Registo de Animais de Companhia (CRO e Abrigo)]] descreve o conteúdo do relatório anual, mas não diz quem o recebe nem até quando. O art. [[Sistema de Informação de Animais de Companhia#1]], n.º 1, diz que o SIAC guarda «os registos submetidos pelos CRO no âmbito do relatório anual», sem norma que mande submetê-los. Há um comentário da DAJA a esse artigo: «Remeter para Portaria».",
            "A al. v) pune «A eutanásia de animais em violação do disposto no n.º 6 do artigo XX.º». Vem do Código do Animal (art. 89.º, n.º 2, al. u)), onde remetia para o art. 75.º, n.º 6, segundo o qual a eutanásia compete aos médicos veterinários. No RGAC essa regra está no art. [[Destino dos animais]], n.º 8, e o art. [[Eutanásia]], n.º 6, trata do registo do motivo no SIAC. Em nenhuma das leituras fica abrangida a proibição do art. [[Eutanásia]], n.º 1 (eutanásia por sobrepopulação, sobrelotação ou incapacidade económica), que é a regra central da Lei 27/2016 (art. 3.º, n.º 4).",
            "O art. [[Plataforma Nacional de Adoção de Animais de Companhia]] (Plataforma Nacional de Adoção) previa no n.º 6 «contraordenação grave» para quem não registasse os animais na plataforma, incluindo os CRO. O artigo está rasurado nesta versão. O art. [[Contraordenações]] não tem graus de gravidade.",
            "O Regulamento (UE) 2026/1818 manda fixar sanções para as violações do regulamento, «inclusive as aplicáveis ao abandono de cães e gatos pelos operadores», e diz que devem ser «efetivas, proporcionadas e dissuasivas» (art. 32.º, aplicável a partir de 31.8.2028). O abrigo é «qualquer instalação ou estrutura, incluindo as casas particulares, onde são detidos cães ou gatos não desejados, abandonados, perdidos, confiscados ou anteriormente errantes, para efeitos de colocação no mercado» (art. 4.º, al. r)). A colocação no mercado inclui a transferência a título gratuito (art. 4.º, al. g))."
        ],
        "proposta": "No art. [[Regime de Gestão e Registo de Animais de Companhia (CRO e Abrigo)]]: fixar no decreto-lei o dever de o CRO submeter o relatório anual no SIAC até 31 de janeiro, com os dados dos n.ºs 4 e 5, e o dever de a DGAV publicar o relatório nacional até 31 de março. O pormenor pode ir para portaria, como propõe a DAJA, mas o dever e o prazo ficam no decreto-lei. O relatório deve ser feito por CRO, com as entradas e saídas discriminadas pelo município de origem, para que os CRO intermunicipais fiquem visíveis. No art. [[Contraordenações]]: punir a falta ou o atraso do relatório anual e do plano do art. [[Controlo das populações errantes e assilvestradas]] (ver CED-17); ligar a al. v) ao art. [[Eutanásia]], n.º 1 e primeiro n.º 2, e ao art. [[Destino dos animais]], n.º 8; alargar a al. s) ao art. [[Controlo da reprodução pelas câmaras municipais]], n.º 3, e ao art. [[Destino dos animais]], n.º 13; acrescentar os deveres de destino e cedência dos arts. [[Destino dos animais]] e [[Condições da cedência]]. Ligar o acesso a apoios públicos à entrega do relatório, como o art. [[Registo Nacional das Associações Zoófilas]], n.º 4, já faz para o registo das associações zoófilas. Confirmar que o CRO é tratado como abrigo para efeitos do Regulamento (UE) 2026/1818 e que a lista de contraordenações cobre os deveres europeus dos abrigos até 31.8.2028, incluindo o abandono pelos operadores (ver TIT-06). Ponderar uma norma geral como a da Lei 92/95, art. 12.º, n.º 1, ou pelo menos coima expressa, com a gravidade que hoje tem no DL 276/2001 (art. 68.º, n.º 2, al. d)), para o art. [[Proibição de violência e maus-tratos]], n.º 1 (morte sem motivo legítimo). Ver FIN-01.",
        "levantado": [
            "Análise interna (13.10.2026)",
            "Comentário da DAJA ao art. [[Regime de Gestão e Registo de Animais de Companhia (CRO e Abrigo)]] («Remeter para Portaria»)"
        ],
        "estado": "Aberto",
        "rel": [
            "CED-17",
            "TIT-06",
            "TIT-11",
            "CED-19",
            "FIN-01"
        ]
    },
    {
        "cod": "FIN-01",
        "cod_ensaio_2": "P-43",
        "cod_antigo": "F-01",
        "artigo": "Norma revogatória",
        "titulo": "A revogação total da Lei 92/95 apaga normas que não tratam de animais de companhia",
        "etiquetas": [
            "FIN",
            "SAN",
            "BEM"
        ],
        "onde": [
            "art. [[Norma revogatória]], n.º 1, al. a)",
            "art. [[Âmbito Objetivo]], n.ºs 1, 2 e 9",
            "art. [[Contraordenações]]"
        ],
        "origem": "RGAC",
        "problema": [
            "O RGAC aplica-se só aos animais de companhia (arts. [[Objeto]] e [[Âmbito Objetivo]]) e exclui a fauna selvagem e os touros de lide (art. [[Âmbito Objetivo]], n.º 9). Mas revoga por inteiro a Lei 92/95 (art. [[Norma revogatória]], n.º 1, al. a)), que protege todos os animais.",
            "Para os animais que não são de companhia perdem-se as proibições gerais do art. 1.º da Lei 92/95, incluindo o tiro ao voo de pombos (n.º 3, al. g)), a autorização municipal para o comércio, a guarda remunerada e a exibição de animais (art. 2.º), a autorização de espetáculos com animais e o regime das touradas, com a proibição dos touros de morte e a sua exceção (art. 3.º), e a regra sobre animais feridos (art. 4.º).",
            "Para todos os animais perdem-se a legitimidade das associações zoófilas para pedir medidas preventivas e urgentes e para se constituírem assistentes, com dispensa de custas (arts. 9.º e 10.º), e o regime contraordenacional acrescentado pela Lei 6/2022 (arts. 11.º a 16.º), incluindo a norma geral do art. 12.º, n.º 1. O RGAC não tem normas equivalentes. As medidas cautelares em caso de crime de maus-tratos a animais de companhia (art. 1.º-A) só têm equivalente parcial no art. [[Obrigações das câmaras municipais]], n.ºs 5 a 7.",
            "O RGAC substitui os arts. 5.º a 8.º da Lei 92/95. O transporte público de animais de companhia (art. 7.º) passa para o art. [[Transporte de animais em transportes públicos]]."
        ],
        "proposta": "Na al. a) do n.º 1 do art. [[Norma revogatória]], revogar só os arts. 5.º a 8.º da Lei 92/95 e manter os restantes. Passar para o RGAC, para os animais de companhia, a legitimidade das associações zoófilas e uma norma geral de contraordenação (ver SAN-01). Verificar se a revogação das normas processuais e das que tocam crimes (arts. 1.º-A, 9.º e 10.º da Lei 92/95) cabe na competência do Governo ou exige lei da Assembleia da República.",
        "levantado": [
            "Análise interna (13.10.2026)"
        ],
        "estado": "Aberto",
        "rel": [
            "SAN-01",
            "TIT-06"
        ]
    },
    {
        "cod": "FIN-02",
        "cod_ensaio_2": "P-44",
        "cod_antigo": "F-02",
        "artigo": "Norma revogatória",
        "titulo": "O DL 74/2007 é ressalvado e revogado ao mesmo tempo",
        "etiquetas": [
            "FIN"
        ],
        "onde": [
            "art. [[Âmbito Objetivo]], n.º 8",
            "art. [[Norma revogatória]], n.º 1, al. f)"
        ],
        "origem": "RGAC",
        "problema": [
            "O art. [[Âmbito Objetivo]], n.º 8, diz que o decreto-lei «não prejudica a aplicação do Decreto-Lei n.º 74/2007, de 27 de março», relativo ao acesso das pessoas com deficiência acompanhadas de cães de assistência. O art. [[Norma revogatória]], n.º 1, al. f), revoga esse decreto-lei.",
            "O RGAC trata da licença do cão de assistência, mas não do direito de acesso a locais, transportes e estabelecimentos. Revogado o DL 74/2007, esse direito fica sem norma."
        ],
        "proposta": "Retirar a al. f) do n.º 1 do art. [[Norma revogatória]] e manter o DL 74/2007, como diz o art. [[Âmbito Objetivo]], n.º 8. Se se quiser integrá-lo no RGAC, transpor o regime de acesso e só então revogar.",
        "levantado": [
            "Análise interna (13.10.2026)"
        ],
        "estado": "Aberto",
        "rel": [
            "FIN-01"
        ]
    },
    {
        "cod": "SAN-02",
        "cod_ensaio_2": "P-45",
        "cod_antigo": "G-01",
        "artigo": "Obrigações das câmaras municipais",
        "titulo": "A recolha por razões de bem-estar passa da DGAV para as câmaras e o destino para o médico veterinário municipal",
        "etiquetas": [
            "SAN",
            "BEM"
        ],
        "onde": [
            "art. [[Obrigações das câmaras municipais]], n.ºs 5 a 8",
            "art. [[Destino dos animais]], n.º 1"
        ],
        "origem": "RGAC",
        "problema": [
            "Hoje, quando está em causa a saúde e o bem-estar dos animais, a recolha cabe à DGAV, «com a intervenção das câmaras municipais, se necessário», e às autoridades policiais (DL 276/2001, art. 19.º, n.º 8). Os animais vão para CRO e é a DGAV que «decide o destino dos mesmos» (n.º 9).",
            "O art. [[Obrigações das câmaras municipais]], n.º 5 passa a recolha para as câmaras municipais, «quando possível com a colaboração das autoridades policiais». O n.º 8 entrega o destino ao «MVM ou médico-veterinário do município». A DGAV deixa de aparecer nas duas normas.",
            "A Lei 92/95, art. 1.º-A, n.º 1, aditado pela Lei 39/2020, obriga as forças de segurança, os órgãos de polícia criminal, a DGAV e os municípios a desencadear a recolha quando há evidência de crime de maus-tratos a animais de companhia. O RGAC revoga a Lei 92/95 (ver FIN-01) e o art. [[Obrigações das câmaras municipais]] só cobre parte deste dever.",
            "O n.º 8 não distingue os animais apreendidos. Quando há processo penal, os animais são confiados a depositários idóneos e o destino é decidido pela autoridade judiciária (CPP, arts. 178.º, n.º 2, e 186.º, n.º 1, na redação da Lei 39/2020). Quando há processo de contraordenação, decide a autoridade administrativa (DL 9/2021, anexo, arts. 49.º e 50.º). Em nenhum dos casos decide o MVM.",
            "O n.º 7 só prevê mandado judicial para lutas e só a pedido das entidades policiais.",
            "A proposta de procedimento-tipo da OMV e da ANVETEM (v3.0, 26.8.2026) assenta no modelo vigente, com a DGAV a coordenar e a decidir o destino. Se o art. [[Obrigações das câmaras municipais]] ficar como está, esse procedimento terá de ser refeito."
        ],
        "proposta": "Decidir quem lidera a recolha por razões de bem-estar. Se passar para as câmaras, manter a possibilidade de a DGAV a determinar e acompanhar. Ressalvar no n.º 8 os animais apreendidos, cujo destino é o fixado pela autoridade que ordenou a apreensão. Integrar no RGAC, para todas as autoridades, o dever do art. 1.º-A da Lei 92/95. Prever o pedido de mandado também pela DGAV.",
        "levantado": [
            "Análise interna (14.10.2026), a propósito da proposta de procedimento-tipo de intervenção da OMV e da ANVETEM à DGAV (v3.0, 26.8.2026)"
        ],
        "estado": "Aberto",
        "rel": [
            "FIN-01",
            "SAN-03",
            "TIT-21"
        ]
    },
    {
        "cod": "TIT-21",
        "cod_ensaio_2": "P-46",
        "cod_antigo": "G-02",
        "artigo": "Destino dos animais",
        "titulo": "A presunção de abandono aos 15 dias não ressalva animais apreendidos nem animais socorridos em emergência",
        "etiquetas": [
            "TIT",
            "REG"
        ],
        "onde": [
            "art. [[Destino dos animais]], n.º 13",
            "art. [[Situações especiais de registo]], n.ºs 8 e 9"
        ],
        "origem": "VIGENTE",
        "problema": [
            "O art. [[Destino dos animais]], n.º 13 presume abandonados os animais acolhidos pelos CRO e não reclamados em quinze dias, e manda esterilizá-los e encaminhá-los para adoção. O art. [[Situações especiais de registo]], n.ºs 8 e 9 manda registá-los no SIAC em nome do operador do CRO após 15 dias. Reproduz a Lei 27/2016, art. 3.º, n.º 1, e o DL 82/2019, art. 11.º, n.º 5.",
            "Os animais retirados por decisão de autoridade também entram em CRO (art. [[Obrigações das câmaras municipais]], n.º 8; hoje, DL 276/2001, art. 19.º, n.º 9). Não estão por reclamar: estão à ordem de uma decisão. Lida à letra, a norma deixa dar para adoção um animal apreendido num processo penal antes de o juiz decidir.",
            "O mesmo vale para os animais socorridos em acidente grave ou catástrofe. Uma família desalojada pode não reclamar o animal em quinze dias. Desde a Lei 38/2026, os municípios têm de planear o alojamento de animais em emergência (Lei 65/2007, art. 2.º, n.º 2, al. e)).",
            "O n.º 13 remete ainda para o «prazo previsto no artigo XX»."
        ],
        "proposta": "Ressalvar no art. [[Destino dos animais]], n.º 13 e no art. [[Situações especiais de registo]], n.ºs 8 e 9: (i) os animais apreendidos ou recolhidos por decisão de autoridade, cujo destino é o fixado nessa decisão; (ii) os animais recolhidos em acidente grave ou catástrofe, com prazo mais longo, contado da notificação do titular identificado no SIAC. Prever no SIAC um estado próprio para cada caso.",
        "levantado": [
            "Análise interna (14.10.2026), a propósito da proposta de procedimento-tipo de intervenção da OMV e da ANVETEM à DGAV (v3.0, 26.8.2026)"
        ],
        "estado": "Aberto",
        "rel": [
            "SAN-02",
            "BEM-02",
            "TIT-05"
        ]
    },
    {
        "cod": "SAN-03",
        "cod_ensaio_2": "P-47",
        "cod_antigo": "S-02",
        "artigo": "Medidas preventivas",
        "titulo": "A apreensão provisória serve só as contraordenações e admite devolver os animais ao local de origem",
        "etiquetas": [
            "SAN",
            "REG"
        ],
        "onde": [
            "art. [[Medidas preventivas]], n.ºs 1, 3 e 8",
            "art. [[Direito subsidiário]]",
            "art. [[Fiscalização]], n.º 3"
        ],
        "origem": "PARCIAL",
        "problema": [
            "O art. [[Medidas preventivas]] regula a apreensão provisória dos animais usados numa contraordenação, com fiel depositário, termo de depósito e relatório da DSAVR. Segue o modelo do DL 315/2009 (art. 39.º) e do DL 265/2007. Mas no DL 315/2009 os n.ºs 2 a 6 desse artigo (auto, depositário, termo de depósito) estão revogados, e o n.º 1, na redação do DL 9/2021, manda fazer a apreensão «nos termos do RJCE». O art. [[Medidas preventivas]] volta a regular essas matérias e deixa cair a remissão para o RJCE.",
            "O n.º 8 permite, quando o detentor recusa ser fiel depositário ou é desconhecido, encaminhar os animais para locais onde esteja garantido o seu bem-estar, «nomeadamente o retorno ao local de origem». Em maus-tratos ou em alojamento sem condições, o local de origem é a causa do problema. A fórmula vem do DL 315/2009, art. 39.º, n.º 8, escrito para animais perigosos, cujas infrações são sobretudo de licenciamento e segurança, e não de condições do local.",
            "Hoje as contraordenações do DL 276/2001 seguem o regime das contraordenações económicas (DL 276/2001, art. 68.º). Esse regime permite medidas cautelares sem audição prévia, a apreensão de «seres vivos», o detentor como fiel depositário salvo manifesto inconveniente, e o destino antecipado em caso de «perigo para a saúde ou para o bem-estar de animais» (DL 9/2021, anexo, arts. 48.º a 50.º). O recurso não tem efeito suspensivo (art. 52.º, n.º 3). O RGAC remete para o regime geral das contraordenações (art. [[Direito subsidiário]]) e o art. [[Medidas preventivas]] não reproduz estas regras.",
            "O artigo não ressalva o processo penal. Aí os animais apreendidos são confiados a depositários idóneos e, quando deixam de ser necessários à prova, entregues a quem foi nomeado seu fiel depositário (CPP, arts. 178.º, n.º 2, e 186.º, n.ºs 1 e 7, na redação da Lei 39/2020).",
            "Não há ligação ao SIAC. Um animal apreendido não fica marcado como tal e a titularidade pode ser transmitida durante o processo. Também não está prevista a cedência voluntária dos animais pelo detentor no ato da apreensão."
        ],
        "proposta": "Reescrever o art. [[Medidas preventivas]]: (i) excluir o retorno ao local de origem quando a apreensão se funde em maus-tratos ou falta de condições; (ii) prever o destino antecipado por razões de bem-estar, como no RJCE, ou manter as contraordenações do RGAC no regime das contraordenações económicas; (iii) ressalvar o regime do CPP quando haja processo penal; (iv) prever no SIAC o estado «sob apreensão», com bloqueio de transmissões; (v) prever a cedência voluntária pelo detentor, registada no SIAC, sem prejuízo da responsabilidade contraordenacional ou criminal.",
        "levantado": [
            "Análise interna (14.10.2026), a propósito da proposta de procedimento-tipo de intervenção da OMV e da ANVETEM à DGAV (v3.0, 26.8.2026)"
        ],
        "estado": "Aberto",
        "rel": [
            "SAN-02",
            "TIT-21",
            "SAN-01"
        ]
    },
    {
        "cod": "BEM-02",
        "cod_ensaio_2": "P-48",
        "cod_antigo": "E-01",
        "artigo": "Sistemas de proteção",
        "titulo": "Nada sobre animais de companhia em acidente grave ou catástrofe",
        "etiquetas": [
            "BEM",
            "EST",
            "REG"
        ],
        "onde": [
            "art. [[Sistemas de proteção]]",
            "art. [[Destino dos animais]], n.º 13",
            "Lei 38/2026, de 3 de agosto"
        ],
        "origem": "VIGENTE",
        "problema": [
            "A Lei 38/2026, em vigor desde 8.8.2026, integrou o socorro animal na proteção civil. Os municípios têm de planear a busca, o salvamento, a evacuação, o alojamento e o abastecimento dos animais, com simulacros (Lei 65/2007, art. 2.º, n.º 2, al. e)). A DGAV passa a ter representante na Comissão Nacional e nas comissões distritais de proteção civil (Lei 27/2006, art. 37.º, n.º 1, al. f), e art. 39.º, n.º 1, al. i)) e nos centros de coordenação operacional nacional e regionais. O teatro de operações passa a ter uma «zona de concentração de acolhimento de animais» (DL 90-A/2022, anexo, art. 13.º, al. d)).",
            "O RGAC não refere a Lei 38/2026 nem a proteção civil, salvo a remissão do art. [[Sistemas de proteção]] para as medidas da ANEPC contra incêndios nas instalações. Não há dever de plano de evacuação para CRO, abrigos ou estabelecimentos, muitos em zona rural ou florestal. A lei vigente também não o tem: o DL 276/2001, art. 11.º, só exige proteção contra incêndios em edifícios fechados.",
            "Não está regulada a guarda temporária de animais socorridos nem a reunificação com o titular através do SIAC. A eutanásia fora de CRO e de CAMV não tem enquadramento: a Lei 27/2016, art. 3.º, n.º 6, só a admite nesses locais.",
            "A presunção de abandono de quinze dias aplica-se aos animais socorridos que entrem em CRO (ver TIT-21).",
            "Não há base legal clara para a DGAV partilhar com os serviços municipais de proteção civil a lista de estabelecimentos registados e os dados do SIAC necessários ao planeamento.",
            "A proposta de procedimento-tipo da OMV e da ANVETEM (26.8.2026) trata o socorro, mas como orientação administrativa. A análise interna das propostas ENAE, FEDRA e APMVEAC já tinha registado esta omissão (ponto 2.5)."
        ],
        "proposta": "Aditar um artigo sobre animais de companhia em acidente grave ou catástrofe, articulado com a Lei 38/2026: (i) plano de evacuação para CRO, abrigos e estabelecimentos acima de certa dimensão, integrado no plano municipal de emergência; (ii) partilha com os serviços de proteção civil da lista de estabelecimentos registados e dos dados do SIAC necessários; (iii) guarda temporária e reunificação, com leitura do transponder e consulta ao SIAC; (iv) suspensão da presunção de abandono enquanto vigorar a situação de alerta, contingência ou calamidade; (v) eutanásia no local por médico veterinário quando o transporte não seja possível.",
        "levantado": [
            "Análise interna (14.10.2026), a propósito da proposta de procedimento-tipo de intervenção da OMV e da ANVETEM à DGAV (v3.0, 26.8.2026)"
        ],
        "estado": "Aberto",
        "rel": [
            "TIT-21"
        ]
    },
    {
        "cod": "PER-01",
        "cod_ensaio_2": "P-49",
        "cod_antigo": "D-01",
        "artigo": "Classificação como animal perigoso",
        "titulo": "Duas vias para retirar a classificação de perigoso, sem ligação entre elas",
        "etiquetas": [
            "PER",
            "REG"
        ],
        "onde": [
            "art. [[Classificação como animal perigoso]], n.ºs 1, 3 e 5",
            "art. [[Atualização de registo SIAC]], n.ºs 1 a 3",
            "art. [[Procedimento em caso de agressão]], n.ºs 2, 4 e 5",
            "art. [[Licença de cães e articulação com o Sistema de Informação de Animais de Companhia]], n.º 7",
            "art. [[Detenção de cães perigosos ou potencialmente perigosos]], n.º 2",
            "art. [[Proibição de reprodução]], n.º 2",
            "DL 315/2009, art. 3.º, al. b), art. 9.º, art. 14.º e art. 19.º, n.º 2",
            "DL 82/2019, art. 13.º, n.º 1"
        ],
        "origem": "PARCIAL",
        "problema": [
            "No DL 315/2009, o animal é perigoso quando se verifica um dos factos do art. 3.º, al. b): ter mordido, atacado ou ofendido uma pessoa; ter ferido gravemente ou morto outro animal fora da propriedade do detentor; ter sido declarado agressivo pelo detentor; ou ter sido considerado um risco pela autoridade competente. As juntas de freguesia registam no SIAC os episódios que determinam a classificação (art. 9.º, n.º 1, e art. 14.º, n.º 3). A única via expressa para a retirar é o registo das «decisões definitivas proferidas em processo criminal ou contraordenacional» que fundamentem a eliminação da classificação (art. 9.º, n.º 2).",
            "A lei vigente não dá ao MVM poder para retirar a classificação. Quando se apura que o auto policial que relatou a agressão não tem fundamento, não há via própria fora do processo criminal ou contraordenacional. Entretanto o cão fica sujeito a licença, seguro, açaimo e esterilização (DL 315/2009, art. 5.º, art. 10.º, art. 13.º e art. 19.º, n.º 2).",
            "O RGAC muda o modelo. O registo dos episódios passa para o MVM ou para o médico veterinário ao serviço do município (art. [[Atualização de registo SIAC]], n.º 1; art. [[Classificação como animal perigoso]], n.º 3; art. [[Procedimento em caso de agressão]], n.º 4). A junta de freguesia deixa de poder alterar a classificação (art. [[Licença de cães e articulação com o Sistema de Informação de Animais de Companhia]], n.º 7). O art. [[Classificação como animal perigoso]], n.º 5 permite ao MVM reverter a classificação, «oficiosamente ou a requerimento do interessado», «sempre que seja feita prova em contrário».",
            "O art. [[Atualização de registo SIAC]], n.º 2 mantém a via do DL 315/2009: a DGAV regista no SIAC as decisões definitivas que fundamentem a eliminação da classificação, e o n.º 3 manda o tribunal e as autoridades administrativas comunicar-lhe a decisão. Ficam duas vias para o mesmo efeito, com dois decisores, sem regra que as ligue.",
            "O art. [[Classificação como animal perigoso]], n.º 5 não diz quem regista a reversão no SIAC, nem que ela é notificada ao titular e à junta de freguesia que emitiu a licença (art. [[Detenção de cães perigosos ou potencialmente perigosos]], n.º 2). Não diz que prova basta para a «prova em contrário». Não trata o caso de haver processo criminal ou contraordenacional pendente sobre os mesmos factos: o MVM pode reverter e o tribunal dar depois os factos como provados, ou o contrário.",
            "O cão classificado como perigoso deve ser esterilizado (art. [[Proibição de reprodução]], n.º 2). Se a classificação cair depois, a esterilização não se desfaz. O RGAC não suspende este efeito enquanto a classificação é contestada.",
            "No SIAC, só altera o registo quem tiver perfil para isso, atribuído pela DGAV (DL 82/2019, art. 13.º, n.º 1). A competência que o RGAC dá ao MVM só funciona se o perfil a acompanhar."
        ],
        "proposta": "Ligar as duas vias no art. [[Classificação como animal perigoso]]. (i) O MVM reverte por decisão fundamentada, regista a reversão no SIAC e notifica o titular e a junta de freguesia. (ii) Dar exemplos de prova em contrário: decisão definitiva de arquivamento ou de absolvição, retificação do auto pela entidade autuante, erro na identificação do animal. (iii) No art. [[Atualização de registo SIAC]], n.º 2, a DGAV regista a decisão definitiva e o MVM retira dela as consequências, para não haver duas decisões sobre o mesmo facto. (iv) Com processo pendente, o MVM pode suspender a esterilização do art. [[Proibição de reprodução]], n.º 2 até à decisão, mantendo as medidas de circulação do art. [[Medidas de segurança reforçadas na circulação]]. (v) Ajustar os perfis de acesso ao SIAC à nova competência.",
        "levantado": [
            "Análise interna (20.10.2026), a propósito de uma consulta: pode o MVM retirar no SIAC a classificação de perigoso quando o auto da GNR que relatou a agressão não tem fundamento"
        ],
        "estado": "Aberto",
        "rel": []
    },
    {
        "cod": "EST-01",
        "cod_ensaio_2": "P-50",
        "cod_antigo": "E-02",
        "artigo": "Suspensão de atividade e encerramento dos estabelecimentos",
        "titulo": "O encerramento de estabelecimentos fica sem medida cautelar, sem regra para os animais e sem efeito no registo",
        "etiquetas": [
            "EST",
            "BEM",
            "SAN"
        ],
        "onde": [
            "art. [[Suspensão de atividade e encerramento dos estabelecimentos]], n.ºs 1, 4 e 7",
            "art. [[Alteração de funcionamento dos estabelecimentos]], n.º 2",
            "art. [[Permissão de reabertura após suspensão da atividade]]",
            "art. [[Medidas preventivas]], n.º 1",
            "art. [[Sanções acessórias]], n.º 1"
        ],
        "origem": "VIGENTE",
        "problema": [
            "O art. [[Suspensão de atividade e encerramento dos estabelecimentos]] repete o art. 3.º-G do DL 276/2001. O diretor-geral suspende ou encerra depois de processo instruído pela DSAVR, com relatório e proposta. Não há medida cautelar própria para o período entre a fiscalização e a decisão final. Hoje a DGAV tem de recorrer à medida provisória do art. 89.º do CPA ou às medidas cautelares do art. 48.º do RJCE, que só servem dentro de um processo de contraordenação e que o art. 27.º do RJCE afasta quando o mesmo facto é crime.",
            "O caso do alojamento PT1225FL, em Amarante, mostra a falha. A fiscalização foi em 22.6.2026. Os animais saíram no próprio dia pela via penal. A proposta de encerramento chegou ao diretor-geral em setembro, sem medida provisória, com o prazo de caducidade de 120 dias do art. 128.º, n.º 6 do CPA a correr e sem que a lei diga se se conta em dias úteis.",
            "O n.º 7 manda as câmaras executar a decisão e recolher os animais «nos termos do artigo XX.º (recolha e encaminhamento de animais)». Esse artigo não existe. Não se diz para onde vão os animais, quem decide o destino, quem suporta a guarda, nem como se articula com a apreensão penal (CPP, arts. 178.º e 186.º) e com a apreensão do art. [[Medidas preventivas]]. O n.º 7 remete ainda para «os n.ºs 3 e 4», que são a instrução e a regra da suspensão (ver L-18).",
            "O encerramento não tem efeito no registo. O número de identificação é pessoal e intransmissível (DL 276/2001, art. 3.º, n.º 11), mas nada impede o titular de apresentar nova mera comunicação prévia no dia seguinte, para o mesmo local ou para outro. O art. [[Alteração de funcionamento dos estabelecimentos]], n.º 2 trata só da cessação voluntária. O art. [[Permissão de reabertura após suspensão da atividade]] só prevê a reabertura após suspensão. O único travão seria a sanção acessória de interdição, que o RGAC deixa cair (ver SAN-04).",
            "O artigo deixa ao CPA a audiência prévia, a dispensa por urgência e o prazo de decisão. Num procedimento de polícia sanitária com animais vivos, estas regras gerais chegam tarde: a urgência que justificaria a dispensa de audiência esgota-se com a retirada dos animais, e a decisão final chega a um local já vazio."
        ],
        "proposta": "Rever o art. [[Suspensão de atividade e encerramento dos estabelecimentos]]: (i) poder de suspensão cautelar imediata da atividade, pelo diretor-geral ou pela DSAVR, sem audiência prévia, com prazo e com audiência posterior, nos termos do art. 89.º do CPA; (ii) norma sobre os animais em caso de suspensão ou encerramento: quem os recolhe, onde ficam, quem decide o destino, encargos a cargo do titular, e ressalva dos animais apreendidos em processo penal ou contraordenacional; (iii) efeito do encerramento no registo: cancelamento do número de identificação e prazo durante o qual o titular não pode apresentar nova comunicação prévia, articulado com a sanção acessória de interdição; (iv) prazo próprio para a decisão, com ressalva expressa do art. 128.º, n.º 6 do CPA; (v) corrigir as remissões do n.º 7 (L-18).",
        "levantado": [
            "Análise interna (21.10.2026), a propósito da proposta de encerramento do alojamento PT1225FL, Amarante (Informação n.º 125893/26 da DSAVRN, processo P.9441/26)"
        ],
        "estado": "Aberto",
        "rel": [
            "SAN-04",
            "SAN-03",
            "SAN-02",
            "BEM-02"
        ]
    },
    {
        "cod": "SAN-04",
        "cod_ensaio_2": "P-51",
        "cod_antigo": "S-03",
        "artigo": "Sanções acessórias",
        "titulo": "As sanções acessórias perdem a interdição do exercício da atividade",
        "etiquetas": [
            "SAN",
            "EST"
        ],
        "onde": [
            "art. [[Sanções acessórias]], n.ºs 1 e 2",
            "art. [[Suspensão de atividade e encerramento dos estabelecimentos]]"
        ],
        "origem": "RGAC",
        "problema": [
            "Hoje o DL 276/2001, art. 69.º, al. b) prevê a «Interdição do exercício de uma profissão ou atividade reguladas no presente diploma, cujo exercício dependa de título público ou de autorização ou homologação de autoridade pública». O DL 82/2019, art. 22.º, al. b) prevê o mesmo. O RJCE, art. 28.º, n.º 1, al. c) prevê a interdição do exercício de atividades cujo exercício dependa de permissão administrativa.",
            "O art. [[Sanções acessórias]], n.º 1 do RGAC prevê a perda de objetos e animais, a privação de participar em feiras, mercados, exposições ou concursos, o encerramento de estabelecimento sujeito a autorização ou licença, a suspensão de autorizações, licenças e alvarás, e a privação de titularidade e detenção só de animais perigosos ou potencialmente perigosos. Não prevê a interdição do exercício da atividade.",
            "Sem interdição, o titular de um estabelecimento encerrado ao abrigo do art. [[Suspensão de atividade e encerramento dos estabelecimentos]] por maus-tratos ou riscos sanitários pode apresentar nova mera comunicação prévia logo a seguir. O encerramento como sanção acessória (al. c)) pressupõe estabelecimento «sujeito a autorização ou licença», e a maioria dos estabelecimentos fica sujeita a mera comunicação prévia.",
            "A privação de titularidade e detenção (al. e)) é limitada aos animais perigosos ou potencialmente perigosos. O Código Penal, art. 388.º-A, n.º 1, al. a) permite privar da detenção de animais de companhia até seis anos, mas só com condenação penal, que pode demorar anos. No caso do alojamento PT1225FL, em Amarante, a interdição administrativa é o único instrumento que impede a titular, arguida por maus-tratos, de voltar a registar um alojamento enquanto o processo-crime corre.",
            "A fórmula «cujo exercício dependa de título público ou de autorização ou homologação de autoridade pública» vem do regime geral das contraordenações de 1982 (DL 433/82, art. 21.º, n.º 1, al. b)) e pressupõe um regime de autorização. O DL 260/2012 substituiu a autorização dos alojamentos pela mera comunicação prévia e não reescreveu o art. 69.º do DL 276/2001. A mera comunicação prévia não é autorização nem permissão administrativa: o próprio DL 276/2001, art. 3.º, n.º 1 distingue a al. a) (mera comunicação prévia) da al. b) (permissão administrativa, só para animais perigosos). A Administração não emite ato; atribui um número «pessoal e intransmissível» (art. 3.º, n.º 11) e publicita-o (n.º 12).",
            "Daí resulta que, na leitura literal, nem a interdição (al. b)), nem o encerramento de estabelecimento «sujeito a autorização ou licença» (al. e)), nem a suspensão de «autorizações, licenças e alvarás» (al. f)) do art. 69.º do DL 276/2001 se aplicam hoje aos alojamentos com mera comunicação prévia. Só uma leitura funcional, que trate o número atribuído e publicitado pela DGAV como título público em sentido material, permite aplicar a interdição, e essa leitura é interpretação extensiva de norma sancionatória. O RJCE, art. 28.º, n.º 1, al. c) («Interdição do exercício de profissões ou de atividades cujo exercício dependa de permissão administrativa») tem o mesmo limite, porque no DL 92/2010 a mera comunicação prévia é a alternativa à permissão.",
            "O RGAC mantém a mesma arquitetura (mera comunicação prévia para a generalidade dos estabelecimentos, permissão administrativa para os perigosos e para os criadores de maior dimensão) e herda o problema: as sanções das als. c) e d) do art. [[Sanções acessórias]], n.º 1 continuam a pressupor autorização, licença ou alvará."
        ],
        "proposta": "Aditar ao art. [[Sanções acessórias]], n.º 1 a interdição do exercício da atividade de exploração de estabelecimentos e de criação de animais de companhia, definida sem referência a título, autorização ou licença: proibição de exercer a atividade e de apresentar mera comunicação prévia ou pedido de permissão administrativa durante o prazo fixado, com cancelamento do número de identificação, registo no SIAC e nos ficheiros da DGAV, e ineficácia de qualquer comunicação apresentada nesse período. Reescrever as als. c) e d) para abranger os estabelecimentos sujeitos a mera comunicação prévia. Ponderar alargar a privação de titularidade e detenção (al. e)) aos animais de companhia em geral, nas contraordenações muito graves por maus-tratos ou por falta de condições de alojamento, com duração máxima e registo no SIAC.",
        "levantado": [
            "Análise interna (21.10.2026), a propósito da proposta de encerramento do alojamento PT1225FL, Amarante (Informação n.º 125893/26 da DSAVRN, processo P.9441/26)"
        ],
        "estado": "Aberto",
        "rel": [
            "EST-01",
            "SAN-03"
        ]
    },
]

RESOLVIDOS = [
    ("Dois sentidos de detentor em leis diferentes",
     "O RGAC revoga o DL 276/2001, o DL 314/2003, o DL 315/2009 e o DL 82/2019 e fica com um só conjunto de definições (art. [[Norma revogatória]], n.º 1; art. [[Definições]]). O problema passa para as portarias (TIT-07)."),
    ("Abandono só por conduta dos detentores",
     "A definição de abandono abrange a conduta do «detentor ou titular» (art. [[Definições]])."),
    ("Adotante chamado detentor",
     "A isenção de taxa de licença passa a ser para os «titulares que tenham adotado» (art. [[Licença de cães e articulação com o Sistema de Informação de Animais de Companhia]], n.º 18)."),
    ("Titular dos gatos CED e dos animais recolhidos",
     "Gatos CED e animais não identificados recolhidos em CRO registados em nome do município (art. [[Situações especiais de registo]], n.ºs 10 e 12). Animais recolhidos por municípios sem CRO registados em nome do município de origem (art. [[Registo no Sistema de Informação de Animais de Companhia (SIAC)]], n.º 4). O CRO passa a operador (art. [[Definições]])."),
    ("Animais perigosos",
     "Titular pessoa singular maior de 16 anos, com exceção para município e associação zoófila (art. [[Registo no Sistema de Informação de Animais de Companhia (SIAC)]], n.ºs 6 e 7). Seguro a cargo do titular."),
    ("Proprietário no passaporte e titular no SIAC",
     "O proprietário que consta do passaporte tem de coincidir com o titular do SIAC (art. [[Deslocação dos animais]], n.º 4)."),
    ("Transmissão de titularidade",
     "Titular que transfere, 14 dias (art. [[Alterações ao registo]], n.º 2), igual ao Regulamento (UE) 2026/1818 (art. 20.º, n.º 4)."),
    ("Prazo em branco nos CRO",
     "O «prazo XXX dias» do art. [[Situações especiais de registo]], n.º 9 passou a 15 dias."),
]

# ------------------------------------------------------------------ lapsos formais
# "onde": epígrafes dos artigos (com #n se a epígrafe se repetir). "ficha": código P, se houver.
LAPSOS = [
    {"cod": "L-01", "onde": ["Plataforma Nacional de Adoção de Animais de Companhia", "Programa de vigilância e controlo em animais de companhia"], "estado": "Aberto", "ficha": "",
     "lapso": "Há dois artigos 81.º: «Plataforma Nacional de Adoção de Animais de Companhia» (cap. VIII) e «Programa de vigilância e controlo em animais de companhia» (cap. IX).",
     "correcao": "Renumerar a partir do segundo art. 81.º e rever todas as remissões para os artigos seguintes."},
    {"cod": "L-02", "onde": ["Plataforma Nacional de Adoção de Animais de Companhia"], "estado": "Aberto", "ficha": "",
     "lapso": "O art. [[Plataforma Nacional de Adoção de Animais de Companhia]] (Plataforma Nacional de Adoção) está sob uma subsecção sem número, com a epígrafe «PLATAFORMA NACIONAL DE REGISTO DOS ALOJAMENTOS» (seguida de SIAC), que não corresponde ao conteúdo do artigo.",
     "correcao": "Numerar a subsecção e dar-lhe epígrafe que corresponda ao artigo, ou retirar a subsecção."},
    {"cod": "L-03", "onde": ["Instrução e decisão", "Exames médico-veterinários, laboratoriais ou outros"], "estado": "Aberto", "ficha": "",
     "lapso": "Há dois artigos 142.º. O segundo («Exames médico-veterinários, laboratoriais ou outros») está depois do Anexo II e da proposta de nota para a comunicação social, sob o título «SUBSECÇÃO III», com a nota «ALTERAR localização no documento!».",
     "correcao": "Decidir onde fica o artigo, colocá-lo no capítulo certo, renumerar e retirar a nota de trabalho."},
    {"cod": "L-04", "onde": ["Das estratégias de reprodução", "Outras disposições", "Alteração de funcionamento dos estabelecimentos"], "estado": "Aberto", "ficha": "",
     "lapso": "No cap. IV, a secção I tem subsecções II e III sem subsecção I, e a secção II tem subsecção II sem subsecção I.",
     "correcao": "Criar a subsecção I em cada secção ou retirar a divisão em subsecções."},
    {"cod": "L-05", "onde": ["Controlo da reprodução pelo titular", "Obrigações das câmaras municipais", "Destino dos animais", "Condições da cedência"], "estado": "Aberto", "ficha": "",
     "lapso": "No cap. X, as secções começam na II e saltam da III para a V (existem II, III, V e VI).",
     "correcao": "Renumerar as secções do cap. X."},
    {"cod": "L-06", "onde": ["Obrigações gerais em matéria de bem-estar"], "estado": "Aberto", "ficha": "TIT-12",
     "lapso": "O art. [[Obrigações gerais em matéria de bem-estar]], n.º 1 diz «Os detentores Operadores ??de animais de companhia».",
     "correcao": "Ver a ficha TIT-12."},
    {"cod": "L-07", "onde": ["Alterações ao registo"], "estado": "Aberto", "ficha": "TIT-05",
     "lapso": "O art. [[Alterações ao registo]], n.º 7 remete para os prazos «previstos no n.º 2 e 3» e para a «alínea e) do artigo 139.º», que não tem alíneas.",
     "correcao": "Ver a ficha TIT-05."},
    {"cod": "L-08", "onde": ["Programas de captura, esterilização e devolução ao local de origem"], "estado": "Aberto", "ficha": "CED-07",
     "lapso": "O art. [[Programas de captura, esterilização e devolução ao local de origem]] tem dois n.º 5 e dois n.º 6, remete no n.º 1 para os «artigos 65.º e 66.º» (agora arts. [[Controlo ambiental]] e [[Controlo das populações errantes e assilvestradas]]) e no n.º 9 para o «n.º 4».",
     "correcao": "Ver a ficha CED-07."},
    {"cod": "L-09", "onde": ["Contraordenações"], "estado": "Aberto", "ficha": "TIT-11",
     "lapso": "O art. [[Contraordenações]], n.º 2 pune o incumprimento «dos deveres previstos no artigo XX.º».",
     "correcao": "Ver a ficha TIT-11."},
    {
        "cod": "L-10",
        "onde": [
            "Necessidades comportamentais"
        ],
        "estado": "Aberto",
        "ficha": "BEM-01",
        "lapso": "O art. [[Necessidades comportamentais]], n.º 3 remete para «artigo YYº n.º 2 (Condições de manutenção de cães e gatos) segundo parágrafo». No n.º 5, as quatro condições não têm letra de alínea e a terceira tem a gralha «aas».",
        "correcao": "Fixar a remissão do n.º 3, numerar as condições do n.º 5 como alíneas a) a d) e corrigir «aas» para «as». Ver a ficha BEM-01."
    },
    {
        "cod": "L-11",
        "onde": [
            "Contraordenações"
        ],
        "estado": "Aberto",
        "ficha": "SAN-01",
        "lapso": "No art. [[Contraordenações]], n.º 2, depois da al. z) as alíneas recomeçam em a) e vão até j), repetindo letras. A segunda al. j) é uma nota de trabalho que começa por «[a aditar:». Quase todas as alíneas remetem para «artigo XX.º».",
        "correcao": "Continuar a numeração em aa), bb) e seguintes, ou dividir o n.º 2 em vários números. Fixar as remissões quando a numeração do RGAC estabilizar. Ver a ficha SAN-01."
    },
    {
        "cod": "L-12",
        "onde": [
            "Eutanásia"
        ],
        "estado": "Aberto",
        "ficha": "SAN-01",
        "lapso": "O art. [[Eutanásia]] tem dois n.º 2. Na al. b) do primeiro n.º 2 lê-se «encaminhamento para cessão», em vez de cedência.",
        "correcao": "Renumerar os números seguintes e corrigir as remissões para eles, incluindo a al. v) do art. [[Contraordenações]], n.º 2. Escrever «cedência». Ver a ficha SAN-01."
    },
    {
        "cod": "L-13",
        "onde": [
            "Condições particulares para a manutenção de peixes",
            "Instalações dos abrigos e centros de recolha oficial",
            "Outras disposições"
        ],
        "estado": "Aberto",
        "ficha": "",
        "lapso": "Na subsecção III do cap. IV, o artigo «Instalações dos abrigos e centros de recolha oficial» não tem número («Artigo º») e está entre o art. [[Condições particulares para a manutenção de peixes]] e o art. [[Outras disposições]]. No texto sem as alterações registadas é um segundo art. 39.º. No Anexo D aparece como 39-b. O art. [[Outras disposições]], n.º 1, aplica-se aos «estabelecimentos previstos no presente artigo», mas esse artigo não prevê estabelecimentos.",
        "correcao": "Numerar o artigo e renumerar os seguintes. No n.º 1 do artigo «Outras disposições», remeter para os estabelecimentos da subsecção III."
    },
    {
        "cod": "L-14",
        "onde": [
            "Controlo da reprodução pelas câmaras municipais"
        ],
        "estado": "Aberto",
        "ficha": "SAN-01",
        "lapso": "O art. [[Controlo da reprodução pelas câmaras municipais]], n.º 4, al. b), remete para «o registo previsto no n.º 2, artigo 59º + 4 (profilaxias médicas e outras intervenções)», que é uma marca de trabalho. O registo da esterilização está no art. [[Registo de profilaxias médicas e outras intervenções]], n.º 2. O n.º 8 escreve «n.º quatro».",
        "correcao": "Remeter para o art. [[Registo de profilaxias médicas e outras intervenções]], n.º 2, e escrever «n.º 4». Ver a ficha SAN-01."
    },
    {
        "cod": "L-15",
        "onde": [
            "Requisito das instalações adequadas à realização de esterilizações nos CRO"
        ],
        "estado": "Aberto",
        "ficha": "",
        "lapso": "No art. [[Requisito das instalações adequadas à realização de esterilizações nos CRO]], n.º 1, al. e), há a gralha «33proteção». A última alínea do n.º 1 não tem letra. A seguir ao n.º 1 vem o n.º 7.",
        "correcao": "Escrever «proteção», dar a letra f) à última alínea e numerar o n.º 7 como n.º 2."
    },
    {
        "cod": "L-16",
        "onde": [
            "Destino dos animais"
        ],
        "estado": "Aberto",
        "ficha": "",
        "lapso": "No art. [[Destino dos animais]], o n.º 2 remete para o «n.º 1 do artigo 70.º» e o n.º 3, al. c), para o «n.º 2 do artigo 72.º». São remissões do Código do Animal. No RGAC, o art. [[Situações especiais de registo]] trata de situações especiais de registo e o art. [[Registo de profilaxias médicas e outras intervenções]] do registo de profilaxias; a captura e a recolha estão no art. [[Obrigações das câmaras municipais]], n.º 1. Os n.ºs 4 e 15 remetem para «artigo XX» e o n.º 15 termina com a nota «Artigo Situações especiais de registo».",
        "correcao": "Remeter o n.º 2 para o art. [[Obrigações das câmaras municipais]], n.º 1. Fixar no n.º 3, al. c), e nos n.ºs 4 e 15 os prazos e artigos certos. Retirar a nota do fim do n.º 15."
    },
    {
        "cod": "L-17",
        "onde": [
            "Exame clínico dos animais e período mínimo de permanência"
        ],
        "estado": "Aberto",
        "ficha": "",
        "lapso": "No art. [[Exame clínico dos animais e período mínimo de permanência]], o n.º 4 remete para as despesas «previstas no n.º 2», que não trata de despesas. As despesas estão no art. [[Despesas]]. O n.º 5 remete para o «n.º X do artigo XXX». Depois do n.º 6 ficou a nota «Reescrever este nº, muito denso».",
        "correcao": "Remeter o n.º 4 para o art. [[Despesas]], n.º 1, fixar a remissão do n.º 5 e retirar a nota."
    },
    {
        "cod": "L-18",
        "onde": [
            "Suspensão de atividade e encerramento dos estabelecimentos",
            "Permissão de reabertura após suspensão da atividade",
            "Divulgação da suspensão de atividade, do encerramento e da reabertura de estabelecimento"
        ],
        "estado": "Aberto",
        "ficha": "",
        "lapso": "No art. [[Suspensão de atividade e encerramento dos estabelecimentos]], o primeiro dos motivos de suspensão aparece como «2 -» e os outros três como alíneas a) a c). Os números seguintes ficam deslocados. O n.º 5 diz «encerramento definitivo do alojamento», em vez de estabelecimento. O n.º 7 remete para a decisão «a que se referem os n.ºs 3 e 4», que agora são a instrução e a regra da suspensão, e para o «artigo XX.º». O art. [[Permissão de reabertura após suspensão da atividade]], n.ºs 1 e 2, remete para o prazo «fixado nos termos do n.º 4 do artigo anterior», que agora está no n.º 5. O art. [[Divulgação da suspensão de atividade, do encerramento e da reabertura de estabelecimento]] remete para os «artigos 39.º e 40.º», que tratam de peixes e de outras disposições; devia remeter para o art. [[Suspensão de atividade e encerramento dos estabelecimentos]] e o art. [[Permissão de reabertura após suspensão da atividade]].",
        "correcao": "Passar os quatro motivos a alíneas a) a d) do n.º 1 e renumerar o artigo. No n.º 5, trocar «alojamento» por «estabelecimento». No n.º 7, remeter para as decisões de suspensão e de encerramento e para o artigo da recolha e encaminhamento de animais. Corrigir as remissões do art. [[Permissão de reabertura após suspensão da atividade]] e do art. [[Divulgação da suspensão de atividade, do encerramento e da reabertura de estabelecimento]]."
    },
    {
        "cod": "L-19",
        "onde": [
            "Licença de cães e articulação com o Sistema de Informação de Animais de Companhia",
            "Classificação como animal perigoso",
            "Procedimento em caso de agressão"
        ],
        "estado": "Aberto",
        "ficha": "PER-01",
        "lapso": "Remissões por fixar nas normas dos cães perigosos. O art. [[Licença de cães e articulação com o Sistema de Informação de Animais de Companhia]], n.º 3 remete para o «artigo XXº (artigo perigosos)». O art. [[Classificação como animal perigoso]], n.º 2, al. a), remete para o «n.º X do artigo XX.º». O art. [[Procedimento em caso de agressão]], n.º 5 remete para a documentação «referida no n.º XX.º».",
        "correcao": "No art. [[Licença de cães e articulação com o Sistema de Informação de Animais de Companhia]], n.º 3 e no art. [[Procedimento em caso de agressão]], n.º 5, remeter para o art. [[Detenção de cães perigosos ou potencialmente perigosos]], n.º 3. No art. [[Classificação como animal perigoso]], n.º 2, al. a), remeter para o art. [[Medidas de segurança reforçadas na circulação]], n.º 2 (meios de contenção)."
    },
    {
        "cod": "L-20",
        "onde": [
            "Detenção de cães perigosos ou potencialmente perigosos",
            "Comprovativo de aprovação em formação",
            "Certificação de entidades formadoras",
            "Da obrigatoriedade de formação"
        ],
        "estado": "Aberto",
        "ficha": "",
        "lapso": "Remissões erradas ou incompletas nas normas da formação para cães perigosos. A última alínea do art. [[Detenção de cães perigosos ou potencialmente perigosos]], n.º 3 acaba em «como previsto no artigo.», sem número. O art. [[Comprovativo de aprovação em formação]] remete para a «alínea f) do n.º 2 do artigo anterior», mas o art. [[Validade da licença]] não tem alíneas e o comprovativo está no art. [[Detenção de cães perigosos ou potencialmente perigosos]], n.º 3. O art. [[Certificação de entidades formadoras]], n.º 1 fala da formação «prevista no número anterior», e é o primeiro número. O art. [[Da obrigatoriedade de formação]], n.º 1 diz «nos termos da para os titulares», com palavras em falta.",
        "correcao": "No art. [[Detenção de cães perigosos ou potencialmente perigosos]], n.º 3, remeter para o art. [[Comprovativo de aprovação em formação]]. No art. [[Comprovativo de aprovação em formação]], remeter para a última alínea do art. [[Detenção de cães perigosos ou potencialmente perigosos]], n.º 3. No art. [[Certificação de entidades formadoras]], n.º 1, escrever «no artigo anterior». No art. [[Da obrigatoriedade de formação]], n.º 1, completar a frase."
    },
]

# ------------------------------------------------------------------ epígrafes renomeadas
# Quando uma versão nova do RGAC mudar a epígrafe de um artigo, basta uma linha aqui
# («epígrafe antiga»: «epígrafe nova») para todas as fichas, lapsos e revisões passarem a apontar
# para o artigo certo. O gerador diz quais as epígrafes a reconciliar e sugere as candidatas.
RENOMEACOES = {
    "Centros de recolha": "Centros de recolha oficial",
}

# ------------------------------------------------------------------ cobertura da revisão
# Chave: epígrafe do artigo (com #n se repetida). Valor: estado, data, regulamento, nota.
REVISAO = {
}

# Correspondência dos códigos anteriores (Anexo F): versão 1.x, ensaio 2.0, ensaio 3.0
CORRESPONDENCIA = [
    ("T-01", "P-01", "TIT-01"),
    ("T-02", "P-02", "TIT-02"),
    ("T-03", "P-03", "TIT-03"),
    ("T-04", "P-04", "TIT-04"),
    ("T-05", "P-05", "TIT-05"),
    ("T-06", "P-06", "TIT-06"),
    ("T-07", "P-07", "TIT-07"),
    ("T-08", "P-08", "TIT-08"),
    ("T-09", "P-09", "TIT-09"),
    ("T-10", "P-10", "TIT-10"),
    ("T-11", "P-11", "TIT-11"),
    ("T-12", "P-12", "TIT-12"),
    ("T-13", "P-13", "TIT-13"),
    ("T-14", "P-14", "TIT-14"),
    ("T-15", "P-15", "TIT-15"),
    ("T-16", "P-16", "TIT-16"),
    ("T-17", "P-17", "TIT-17"),
    ("T-18", "P-18", "TIT-18"),
    ("T-19", "P-36", "TIT-19"),
    ("C-01", "P-19", "CED-01"),
    ("C-02", "P-20", "CED-02"),
    ("C-03", "P-21", "CED-03"),
    ("C-04", "P-22", "CED-04"),
    ("C-05", "P-23", "CED-05"),
    ("C-06", "P-24", "CED-06"),
    ("C-07", "P-25", "CED-07"),
    ("C-08", "P-26", "CED-08"),
    ("C-09", "P-27", "CED-09"),
    ("C-10", "P-28", "CED-10"),
    ("C-11", "P-29", "CED-11"),
    ("C-12", "P-30", "CED-12"),
    ("C-13", "P-31", "CED-13"),
    ("C-14", "P-32", "CED-14"),
    ("C-15", "P-33", "CED-15"),
    ("C-16", "P-34", "CED-16"),
    ("C-17", "P-35", "CED-17"),
    ("T-20", "P-37", "TIT-20"),
    ("C-18", "P-38", "CED-18"),
    ("C-19", "P-39", "CED-19"),
    ("P-01", "P-40", "BEM-01"),
    ("A-01", "P-41", "REG-01"),
    ("S-01", "P-42", "SAN-01"),
    ("F-01", "P-43", "FIN-01"),
    ("F-02", "P-44", "FIN-02"),
    ("G-01", "P-45", "SAN-02"),
    ("G-02", "P-46", "TIT-21"),
    ("S-02", "P-47", "SAN-03"),
    ("E-01", "P-48", "BEM-02"),
    ("D-01", "P-49", "PER-01"),
    ("E-02", "P-50", "EST-01"),
    ("S-03", "P-51", "SAN-04"),
]

REGISTO_ALTERACOES = _V1.REGISTO_ALTERACOES + [
    ("3.0 (ensaio)", "27.9.2026", "Ensaio da opção B, a partir do ensaio 2.0: o código permanente passa a ser a sigla do tema principal e um número dentro do tema (TIT-01 a TIT-18, CED-01 a CED-17). Localização pela epígrafe, ordem do RGAC e etiquetas mantêm-se como no ensaio 2.0."),
    ("2.0 (ensaio)", "27.9.2026", "Ensaio da opção A: códigos permanentes TIT-01 a CED-17 (correspondência no Anexo F); fichas presas aos artigos pela epígrafe, com numeração calculada a partir da versão atual do RGAC; memorando ordenado por capítulo e artigo; temas como etiquetas (Anexo E). Conteúdo das fichas igual ao da versão 1.7."),
]
