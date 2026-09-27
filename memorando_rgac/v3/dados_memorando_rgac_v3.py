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
        ],
        "proposta": "Art. 76.º, n.º 2: «O titular e o detentor, ou os seus representantes, devem comunicar a morte ou o desaparecimento do animal de companhia ao SIAC […]».",
        "levantado": [
            "Análise interna",
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
        ],
        "proposta": "Acrescentar ao art. [[Contraordenações]] a contraordenação de abandono, nos termos da definição do art. [[Definições]], imputável ao titular e ao detentor.",
        "levantado": [
            "Análise interna",
            "Teresa Quintela de Brito, RJLB 2019 (o crime de abandono só abrange quem já tem dever de guarda)",
            "Raúl Farias, e-book do CEJ «Direito dos animais» (2022): o abandono situa-se ao nível da detenção",
            "Cátia Simões, RJLB 2019 (o abandono é difícil de provar)",
            "Tribunal Constitucional, Acórdão 478/2024 (o art. 388.º do Código Penal não é inconstitucional)",
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
        ],
        "proposta": "Decidir se a família de acolhimento informal fica proibida ou se passa a ter um registo simples no SIAC, como detentor, com limite de animais e dever de comunicação.",
        "levantado": [
            "Estratégia Nacional para os Animais Errantes (ENAE), pp. 30-31",
            "Contributos dos médicos veterinários municipais (6.3.2026)",
            "PAN (estatuto da família de acolhimento, 2024)",
            "SNMV (contra registos provisórios no SIAC)",
            "Raúl Farias, e-book do CEJ (2022): as associações, como pessoas coletivas, não respondem pelo crime de abandono",
        ],
        "estado": "Parcialmente resolvido",
        "rel": ["TIT-13", "CED-02"],
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
        ],
        "proposta": "Articular o art. [[Obrigações das câmaras municipais]], n.º 9 com o art. 1323.º do Código Civil: permitir a guarda provisória pelo achador, com dever de comunicação e leitura do transponder num prazo curto.",
        "levantado": [
            "Análise interna",
        ],
        "estado": "Aberto",
        "rel": ["CED-02", "CED-16"],
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
        ],
        "proposta": "Manter pelo menos o nível da Lei 27/2016: «as câmaras municipais asseguram, diretamente ou por protocolo, programas CED para gatos, sempre que se justifique».",
        "levantado": [
            "ENAE, p. 35 («Os programas CED não estão instituídos em todo o território»)",
            "Livre e PAN (respostas de 2024)",
            "ARPA (o CED é dever legal dos municípios, dez. 2022)",
            "Gunther e outros, PNAS 2022, e Boone e outros, 2019 (o CED só resulta com esterilização intensa e contínua)",
            "Comissão Europeia, SWD(2024) 88 (errantes fora do âmbito do Regulamento (UE) 2026/1818)",
        ],
        "estado": "Aberto",
        "rel": ["CED-02"],
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
        ],
        "proposta": "Definir as duas entidades no art. [[Definições]] ou no próprio art. [[Programas de captura, esterilização e devolução ao local de origem]], e dizer que o município, como titular, responde nos termos gerais, com direito de regresso sobre a entidade responsável.",
        "levantado": [
            "CDU (resposta de 2024)",
            "Análise interna",
            "PCP (proposta ao OE2026)",
            "ARPA (dez. 2022)",
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
]

# ------------------------------------------------------------------ epígrafes renomeadas
# Quando uma versão nova do RGAC mudar a epígrafe de um artigo, basta uma linha aqui
# («epígrafe antiga»: «epígrafe nova») para todas as fichas, lapsos e revisões passarem a apontar
# para o artigo certo. O gerador diz quais as epígrafes a reconciliar e sugere as candidatas.
RENOMEACOES = {
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
]

REGISTO_ALTERACOES = _V1.REGISTO_ALTERACOES + [
    ("3.0 (ensaio)", "27.9.2026", "Ensaio da opção B, a partir do ensaio 2.0: o código permanente passa a ser a sigla do tema principal e um número dentro do tema (TIT-01 a TIT-18, CED-01 a CED-17). Localização pela epígrafe, ordem do RGAC e etiquetas mantêm-se como no ensaio 2.0."),
    ("2.0 (ensaio)", "27.9.2026", "Ensaio da opção A: códigos permanentes TIT-01 a CED-17 (correspondência no Anexo F); fichas presas aos artigos pela epígrafe, com numeração calculada a partir da versão atual do RGAC; memorando ordenado por capítulo e artigo; temas como etiquetas (Anexo E). Conteúdo das fichas igual ao da versão 1.7."),
]
