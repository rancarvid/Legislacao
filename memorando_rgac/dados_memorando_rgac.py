# -*- coding: utf-8 -*-
"""
Dados do Memorando de acompanhamento do RGAC.

Este ficheiro contem todo o conteudo do memorando. Para atualizar o memorando:
editar este ficheiro e correr  python3 memorando_rgac/gerar_memorando_rgac.py

Regras de escrita (ver .claude/skills/memorando-rgac/SKILL.md):
- frases curtas, linguagem simples, sem travessoes longos, sem italico, sem cores;
- referencias sempre no formato art. X.º, n.º Y, al. Z) do RGAC;
- nunca reutilizar um codigo de ficha; fichas resolvidas mudam de estado, nao se apagam.
"""

VERSAO_MEMORANDO = "1.13"
DATA_MEMORANDO = "9.10.2026"
DATA_LIGACOES = "27.9.2026"
FICHEIRO_RGAC = "RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO - Revisto 30-06-2026 18h00 Grupo.docx"
VERSAO_RGAC = ("RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO - Revisto 30-06-2026 18h00 Grupo.docx "
               "(revisão formal DAJA V1, revista pelo grupo em 30.6.2026, 18h00)")

# Valores admitidos
ORIGENS = {
    "RGAC": "Criado pelo RGAC",
    "VIGENTE": "Já existia no regime vigente e o RGAC não resolve",
    "PARCIAL": "Já existia; o RGAC resolve em parte",
}
ESTADOS = ("Aberto", "Parcialmente resolvido", "Resolvido")
ESTADOS_REVISAO = ("Por rever", "Em revisão", "Revisto")
ESTADOS_REGULAMENTO = ("A verificar", "Sem correspondência", "Conforme", "Divergente", "Integra o Regulamento")

INTRODUCAO = [
    "Este memorando serve para acompanhar o trabalho sobre o RGAC. Regista os problemas que vamos "
    "encontrando no texto, os que já existem na legislação em vigor e continuam por resolver, e as "
    "críticas feitas por entidades externas. É um documento vivo: cada nova versão acrescenta fichas "
    "ou muda o estado das que já existem.",
    "Cada problema de fundo tem uma ficha com um código fixo. Há dois temas transversais: T (titular, "
    "detentor, proprietário e operador) e C (programas CED, colónias e animais errantes). Os restantes "
    "problemas arrumam-se pelo capítulo do RGAC onde estão, cada um com a sua letra (ver a lista abaixo). "
    "Os códigos não se reutilizam. Quando um problema fica resolvido, a ficha mantém-se com o estado "
    "Resolvido.",
    "Os lapsos formais (remissões erradas, números repetidos, gralhas, marcas de trabalho no texto) não têm "
    "ficha: ficam numa tabela própria no Anexo C, com código L. O Anexo D mostra, artigo a artigo, o que já "
    "foi revisto, as fichas e os lapsos de cada artigo e a relação com o Regulamento (UE) 2026/1818.",
    "As referências a artigos são sempre à versão do RGAC indicada acima, salvo indicação em contrário. "
    "A legislação vigente citada foi confirmada online (DRE e PGDL), na pasta Legislação vigente e nos "
    "ficheiros do repositório.",
    "As posições de entidades externas assentam só em documentos: diplomas e projetos, pareceres, relatórios, "
    "estratégias, recomendações, acórdãos, doutrina e artigos científicos. Notícias de imprensa não são usadas "
    "como fonte.",
]

CAMPOS_FICHA = [
    ("Onde", "Artigos do RGAC em causa."),
    ("Origem", "Se o problema foi criado pelo RGAC, se já existia, ou se o RGAC o resolve em parte."),
    ("Problema", "Descrição curta."),
    ("Proposta", "Solução ou redação sugerida, quando já existe."),
    ("Quem levantou", "Entidades ou documentos que apontaram o problema."),
    ("Estado", "Aberto, Parcialmente resolvido ou Resolvido."),
]

# ---------------------------------------------------------------------------
# Tema T: titular, detentor, proprietario e operador
# ---------------------------------------------------------------------------
TEMA_T = {
    "letra": "T",
    "titulo": "Titular, detentor, proprietário e operador",
    "intro": [
        "Na legislação em vigor, detentor tem dois sentidos. No DL 276/2001, no DL 314/2003 e na Portaria "
        "146/2017 é a pessoa responsável pelo animal. No DL 82/2019 é só o possuidor precário do art. 1253.º "
        "do Código Civil. O titular é a figura do registo SIAC. O proprietário é a figura do Código Civil.",
        "O RGAC revoga aqueles decretos-leis (art. 149.º, n.º 1) e passa a ter um só conjunto de definições "
        "(art. 3.º). Isso resolve a dispersão, mas cria problemas novos na forma como define o titular e na "
        "forma como distribui os deveres entre titular e detentor.",
    ],
    "fichas": [
        {
            "cod": "T-01",
            "titulo": "A definição de titular depende só do registo",
            "onde": ["art. 3.º, definição de «Titular»", "art. 69.º, n.º 1"],
            "origem": "RGAC",
            "problema": [
                "O titular é definido como quem «figura, na base de dados oficial, como proprietário». Ao mesmo "
                "tempo, o registo faz-se «em nome do respetivo titular» (art. 69.º, n.º 1). A definição é "
                "circular: é titular quem está registado e regista-se em nome do titular.",
                "No DL 82/2019 o titular era o proprietário ou o possuidor cuja posse faz presumir a propriedade "
                "(art. 3.º, al. f), ligado ao art. 1268.º do Código Civil). Esse critério permitia decidir em nome "
                "de quem registar. Com a revogação do DL 82/2019, deixa de existir.",
            ],
            "proposta": "Definir titular como «o proprietário ou o possuidor cuja posse faça presumir a propriedade, "
                        "em cujo nome é efetuado o registo no SIAC», mantendo a referência ao operador.",
            "levantado": ["Análise interna (balanço de 25.9.2026)", "ARPA, parecer sobre o DL 82/2019 (dez. 2022)"],
            "estado": "Aberto",
            "rel": ["T-02", "T-03"],
        },
        {
            "cod": "T-02",
            "titulo": "Registo em nome de quem detém o animal e não de quem é dono",
            "onde": ["art. 69.º, n.º 5"],
            "origem": "RGAC",
            "problema": [
                "O art. 69.º, n.º 5 manda registar os animais «detidos por pessoas singulares ou coletivas que não "
                "operadores» em nome dessas pessoas. Segue a versão portuguesa do art. 20.º, n.º 3 do Regulamento "
                "(UE) 2026/1818. A versão inglesa usa o critério da propriedade («owned by»).",
                "Lida com a definição de titular (T-01), a norma permite registar como titular quem só detém o "
                "animal, por exemplo uma família de acolhimento ou um cuidador.",
            ],
            "proposta": "Substituir «detidos por» por «que sejam proprietárias de».",
            "levantado": ["Análise interna (confronto com o Regulamento (UE) 2026/1818)", "ARPA, parecer sobre o DL 82/2019 (dez. 2022)"],
            "estado": "Aberto",
            "rel": ["T-01", "T-14"],
        },
        {
            "cod": "T-03",
            "titulo": "Sem regra sobre o valor do registo SIAC face à propriedade",
            "onde": ["art. 3.º", "art. 5.º", "art. 69.º"],
            "origem": "VIGENTE",
            "problema": [
                "Nem a lei atual nem o RGAC dizem se o registo SIAC faz presumir a propriedade, se essa presunção "
                "pode ser afastada e como se corrige um registo errado.",
                "A versão DAJA de 29.6.2026 tinha uma regra de prevalência do registo (art. 5.º, n.º 4). Essa regra "
                "caiu na revisão formal e nada a substituiu. Os tribunais decidem caso a caso: o Tribunal da Relação "
                "de Lisboa (30.4.2025, proc. 1642/24.4T8AMD.L1-8) tratou o registo como elemento relevante, mas não "
                "decisivo.",
            ],
            "proposta": "Prever uma presunção de titularidade pelo registo, que possa ser afastada por prova em "
                        "contrário, «sem prejuízo do direito de propriedade nos termos do Código Civil», e um "
                        "procedimento de retificação do registo.",
            "levantado": ["Acórdão do TRL de 30.4.2025", "Análise interna", "PCP, proposta ao OE2026 (registo informativo sem responsabilidade, 5.11.2025)",
                "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): a falta de registo no SIAC serviu de prova contra a alegada propriedade de terceiro",
            ],
            "estado": "Aberto",
            "rel": ["T-01"],
        },
        {
            "cod": "T-04",
            "titulo": "O detentor deixa de ter de comunicar a morte do animal",
            "onde": ["art. 76.º, n.º 2", "art. 73.º, n.º 3"],
            "origem": "RGAC",
            "problema": [
                "No regime atual, o detentor deve comunicar ao SIAC a morte ou o desaparecimento, sob pena de "
                "presunção de abandono (DL 82/2019, art. 16.º, n.º 2). No RGAC esse dever passa só para o titular "
                "(art. 76.º, n.º 2). O detentor fica só com o dever de comunicar o desaparecimento e a recuperação "
                "(art. 73.º, n.º 3).",
                "Quem tem o animal consigo, como uma família de acolhimento, um lar de acolhimento ou um cuidador, "
                "deixa de ter dever próprio quando o animal morre.",
                "A jurisprudência faz recair os deveres de cuidado sobre quem tem o controlo de facto do animal, e não sobre o proprietário que se afastou. No acórdão do Tribunal da Relação do Porto de 8.5.2024, o dono original deixara o cão em 2018 e foi condenada a pessoa que o tinha a seu cuidado.",
            ],
            "proposta": "Art. 76.º, n.º 2: «O titular e o detentor, ou os seus representantes, devem comunicar a "
                        "morte ou o desaparecimento do animal de companhia ao SIAC […]».",
            "levantado": ["Análise interna",
                "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): deveres do detentor nos termos do art. 1253.º do Código Civil",
            ],
            "estado": "Aberto",
            "rel": ["T-05"],
        },
        {
            "cod": "T-05",
            "titulo": "A presunção de abandono remete para normas erradas e não diz a quem se aplica",
            "onde": ["art. 73.º, n.º 7"],
            "origem": "RGAC",
            "problema": [
                "O art. 73.º, n.º 7 remete para os prazos «previstos no n.º 2 e 3». O n.º 2 trata da transmissão de "
                "titularidade, não da morte.",
                "Remete também, para a sanção, para a «alínea e) do artigo 139.º». O art. 139.º trata de medidas "
                "preventivas e não tem alíneas.",
                "A norma não diz se o abandono se presume do titular ou do detentor. Sendo uma norma sancionatória, "
                "estas falhas podem impedir a sua aplicação.",
            ],
            "proposta": "Corrigir as remissões (n.º 3 do art. 73.º e a alínea certa do art. 140.º) e indicar a quem "
                        "se presume o abandono.",
            "levantado": ["Análise interna"],
            "estado": "Aberto",
            "rel": ["T-04", "T-06"],
        },
        {
            "cod": "T-06",
            "titulo": "O abandono não aparece como contraordenação",
            "onde": ["art. 140.º", "art. 3.º, definição de «Abandono»"],
            "origem": "RGAC",
            "problema": [
                "O RGAC define abandono no art. 3.º e revoga o DL 276/2001, cujo art. 68.º, n.º 2, al. c) punia o "
                "abandono como contraordenação. A lista de contraordenações do art. 140.º não inclui o abandono.",
                "Fica só a via penal (art. 388.º do Código Penal), que exige dever de guarda e perigo para a "
                "alimentação e cuidados do animal. A presunção de abandono do art. 73.º, n.º 7 fica sem sanção a "
                "que se ligar.",
            ],
            "proposta": "Acrescentar ao art. 140.º a contraordenação de abandono, nos termos da definição do art. 3.º, "
                        "imputável ao titular e ao detentor.",
            "levantado": ["Análise interna", "Teresa Quintela de Brito, RJLB 2019 (o crime de abandono só abrange quem já tem dever de guarda)",
                          "Raúl Farias, e-book do CEJ «Direito dos animais» (2022): o abandono situa-se ao nível da detenção",
                          "Cátia Simões, RJLB 2019 (o abandono é difícil de provar)",
                          "Tribunal Constitucional, Acórdão 478/2024 (o art. 388.º do Código Penal não é inconstitucional)"],
            "estado": "Aberto",
            "rel": ["T-05"],
        },
        {
            "cod": "T-07",
            "titulo": "As portarias mantidas usam detentor no sentido antigo",
            "onde": ["art. 149.º, n.º 2"],
            "origem": "RGAC",
            "problema": [
                "O art. 149.º, n.º 2 mantém em vigor as portarias aprovadas ao abrigo dos diplomas revogados «com "
                "as necessárias adaptações».",
                "A Portaria 146/2017 usa detentor no sentido de responsável pelo animal: animais «não reclamados "
                "pelos seus detentores» (art. 8.º, n.º 4), «novos detentores» para quem adota (art. 8.º, n.º 6), "
                "esterilização «a expensas dos respetivos detentores» (art. 10.º, n.º 1). Com a definição do RGAC, "
                "estas normas passariam a visar só o possuidor precário. A Portaria regulamenta ainda a Lei 27/2016, "
                "que o RGAC revoga.",
            ],
            "proposta": "Acrescentar ao art. 149.º, n.º 2: «as referências a detentor constantes dos diplomas "
                        "regulamentares mantidos em vigor entendem-se feitas ao titular ou ao detentor, consoante o caso».",
            "levantado": ["Análise interna (validação tripla da Portaria 146/2017)", "APMVEAC, revisão crítica (9.4.2021)"],
            "estado": "Aberto",
            "rel": [],
        },
        {
            "cod": "T-08",
            "titulo": "Animais perigosos: o operador pode ser uma sociedade, o titular não",
            "onde": ["art. 69.º, n.ºs 3, 6 e 7"],
            "origem": "RGAC",
            "problema": [
                "Os animais nascidos e detidos em estabelecimentos são registados em nome do operador (art. 69.º, "
                "n.º 3), que pode ser pessoa coletiva. Mas num animal perigoso ou potencialmente perigoso «só pode "
                "figurar como titular uma pessoa singular, maior de 16 anos» (n.º 6), com exceção apenas para "
                "município e associação zoófila (n.º 7).",
                "Um criador ou uma loja constituídos como sociedade não cabem em nenhuma das regras.",
            ],
            "proposta": "Ressalvar no n.º 6 os operadores de estabelecimentos licenciados.",
            "levantado": ["Análise interna"],
            "estado": "Aberto",
            "rel": [],
        },
        {
            "cod": "T-09",
            "titulo": "«Titular ou operador» quando o operador já é titular",
            "onde": ["art. 3.º, definição de «Titular»", "art. 63.º, n.º 5", "art. 73.º, n.º 3"],
            "origem": "RGAC",
            "problema": [
                "A definição de titular já abrange o operador. Mesmo assim, vários artigos falam em «titular ou "
                "operador» ou em «residência do titular ou da morada do operador». Não fica claro se os deveres do "
                "titular se aplicam ao operador ou se são deveres diferentes.",
            ],
            "proposta": "Escolher uma solução: ou o operador é uma espécie de titular (e basta dizer titular), ou "
                        "são figuras distintas (e a definição de titular deixa de incluir o operador).",
            "levantado": ["Análise interna"],
            "estado": "Aberto",
            "rel": ["T-01"],
        },
        {
            "cod": "T-10",
            "titulo": "Terminologia do CRO ainda não uniforme",
            "onde": ["art. 70.º, n.ºs 8 e 9", "art. 89.º, n.º 3", "art. 95.º, n.º 2", "art. 98.º, n.º 13",
                     "art. 99.º, n.º 1"],
            "origem": "PARCIAL",
            "problema": [
                "Na versão das 18h00 os arts. 95.º, 98.º e 99.º passaram a falar de titulares. Ficam por alinhar o "
                "art. 70.º, n.º 8 («não sejam reclamados pelos seus proprietários») e o art. 89.º, n.º 3 («titulares "
                "ou detentores»), todos para o mesmo prazo de 15 dias.",
            ],
            "proposta": "Usar titular para quem tem direito a reclamar o animal e detentor só para quem o tem à guarda.",
            "levantado": ["Análise interna"],
            "estado": "Parcialmente resolvido",
            "rel": [],
        },
        {
            "cod": "T-11",
            "titulo": "Contraordenação dirigida só aos detentores",
            "onde": ["art. 140.º, n.º 2"],
            "origem": "RGAC",
            "problema": [
                "O art. 140.º, n.º 2 pune «O incumprimento, pelos detentores, dos deveres previstos no artigo XX.º». "
                "Com a nova definição, detentor é só o possuidor precário. Se os deveres em causa forem do titular, "
                "a contraordenação não o abrange.",
            ],
            "proposta": "Fixar a remissão e escrever «pelos titulares ou detentores», consoante o dever.",
            "levantado": ["Análise interna"],
            "estado": "Aberto",
            "rel": ["T-06"],
        },
        {
            "cod": "T-12",
            "titulo": "Redação por decidir no art. 22.º",
            "onde": ["art. 22.º, n.º 1"],
            "origem": "RGAC",
            "problema": [
                "O texto diz «Os detentores Operadores ??de animais de companhia que se dediquem à sua reprodução, "
                "criação, manutenção ou venda». A troca de palavra ficou por decidir.",
            ],
            "proposta": "«Os operadores que se dediquem à reprodução, criação, manutenção ou venda de animais de companhia».",
            "levantado": ["Análise interna (revisão de 30.6.2026, 18h00)"],
            "estado": "Aberto",
            "rel": [],
        },
        {
            "cod": "T-13",
            "titulo": "Quem responde pelos danos causados pelo animal",
            "onde": ["sem norma no RGAC, salvo animais perigosos (seguro a cargo do titular)"],
            "origem": "VIGENTE",
            "problema": [
                "O RGAC não diz se responde pelos danos o titular ou o detentor. Continuam a aplicar-se o art. 493.º "
                "do Código Civil (quem tem o encargo de vigilância) e o art. 502.º (quem usa o animal no seu "
                "interesse).",
                "Os médicos veterinários municipais perguntam, a propósito das famílias de acolhimento: «Quais são "
                "aqui as responsabilidades dos titulares (Associações) e quais as responsabilidades dos detentores "
                "dos animais (FAT)?».",
            ],
            "proposta": "Norma que diga que o titular e o detentor respondem nos termos gerais do Código Civil e "
                        "que, entre operador e lar de acolhimento, a responsabilidade se reparte por contrato.",
            "levantado": ["Contributos dos médicos veterinários municipais (6.3.2026)", "Tribunal da Relação de Coimbra, proc. 281/10.1TBCV.C1 (11.7.2012)",
                          "STJ, proc. 478/05.6TBMGL.C1.S1 (14.11.2013): os arts. 493.º e 502.º do Código Civil podem coexistir",
                          "Tribunal da Relação de Lisboa, proc. 3121/03.4TBCSC.L1-6 (24.11.2009)",
                          "Tribunal da Relação de Coimbra, proc. 6/22.9GCPBL.C1 (7.2.2024): dever de vigilância do detentor", "CDU (resposta de 2024)",
                "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): dever de atuar do detentor, nos termos do DL 82/2019, art. 3.º, al. a), e do art. 1253.º do Código Civil",
            ],
            "estado": "Aberto",
            "rel": ["T-14", "C-08"],
        },
        {
            "cod": "T-14",
            "titulo": "Família de acolhimento sem operador fica sem enquadramento",
            "onde": ["art. 3.º, definição de «Lar de acolhimento»", "art. 41.º"],
            "origem": "PARCIAL",
            "problema": [
                "O RGAC só enquadra o lar de acolhimento associado a um operador e «para efeitos de colocação no "
                "mercado». O animal fica registado em nome do operador. Isto resolve o acolhimento feito para uma "
                "associação com estabelecimento autorizado.",
                "Quem acolhe por iniciativa própria, sem operador, continua sem figura. O RGBEAC (jun. 2025) tinha "
                "a família de acolhimento temporário definida e regulada (arts. 4.º e 101.º). Uma revisora pediu "
                "«ELIMINAR ESTE CAPÍTULO» e a figura foi substituída pelo lar de acolhimento do Regulamento europeu.",
                "O estatuto de detentor já abrange quem acolhe por iniciativa própria. O RGAC define detentor como o possuidor precário nos termos do art. 1253.º do Código Civil, responsável «enquanto se mantiver como tal» (art. 3.º). A al. a) do art. 1253.º abrange «Os que exercem o poder de facto sem intenção de agir como beneficiários do direito». O Tribunal da Relação do Porto aplicou o mesmo conceito, a partir do DL 82/2019, a quem tinha um cão na sua esfera de disponibilidade. O que falta não é o estatuto. Falta o regime: registo, limite de animais e forma de pôr termo ao acolhimento (ver T-20).",
            ],
            "proposta": "Decidir se a família de acolhimento informal fica proibida ou se passa a ter um registo "
                        "simples no SIAC, como detentor, com limite de animais e dever de comunicação.",
            "levantado": ["Estratégia Nacional para os Animais Errantes (ENAE), pp. 30-31",
                          "Contributos dos médicos veterinários municipais (6.3.2026)", "PAN (estatuto da família de acolhimento, 2024)", "SNMV (contra registos provisórios no SIAC)",
                          "Raúl Farias, e-book do CEJ (2022): as associações, como pessoas coletivas, não respondem pelo crime de abandono",
                "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): conceito de detentor do DL 82/2019 e do art. 1253.º do Código Civil",
            ],
            "estado": "Parcialmente resolvido",
            "rel": ["T-13", "C-02",
                "T-20",
            ],
        },
        {
            "cod": "T-15",
            "titulo": "Quem encontra um animal passa a poder ser punido",
            "onde": ["art. 91.º, n.º 9", "art. 140.º, n.º 2"],
            "origem": "RGAC",
            "problema": [
                "O art. 91.º, n.º 9 manda comunicar a presença de um animal errante aos serviços veterinários "
                "municipais ou às autoridades policiais. O art. 140.º, n.º 2 pune «A recolha de animais sem "
                "apresentação dos mesmos ao serviço veterinário municipal».",
                "Isto choca com o regime do achado do Código Civil (art. 1323.º), que permite ao achador anunciar "
                "o achado, ficar com o animal ao fim de um ano e retê-lo se houver receio de maus-tratos. Quem "
                "recolhe crias ou um animal ferido fica exposto a coima.",
                "Hoje a recolha por particular está prevista. O n.º 2 do art. 7.º da Portaria 146/2017 manda comunicar o animal errante aos serviços municipais ou às entidades policiais, «ou o animal é entregue a uma dessas entidades, se quem o observou também o capturou». O art. 91.º, n.º 9 reproduz a primeira parte e omite esta.",
                "O art. 91.º, n.º 3 diz que a captura e a recolha «competem, exclusivamente, às câmaras municipais». Na lei vigente a competência é atribuída às câmaras sem exclusivo: DL 276/2001, art. 19.º, n.º 1; DL 314/2003, art. 8.º, n.º 1; Lei 75/2013, anexo I, art. 33.º, n.º 1, al. ii). O Provedor de Justiça entendeu que as competências camarárias nesta matéria não são exclusivas, por referência a outras entidades públicas.",
                "O art. 140.º, n.º 2 tem duas alíneas que se contradizem. Uma pune a recolha «sem apresentação dos mesmos ao serviço veterinário municipal», o que supõe que a recolha seguida de apresentação é lícita. A outra pune a recolha «por entidade diversa das câmaras municipais», o que a proíbe sempre.",
                "O art. 1323.º do Código Civil trata do animal perdido. Uma cria nascida na rua nunca teve dono e pode ser adquirida por ocupação (art. 1318.º do Código Civil). A coima do art. 140.º, n.º 2 atinge também este caso.",
                "Os regulamentos municipais lidos admitem a entrega por quem encontra o animal: Setúbal (RSBEAMS 2020, art. 44.º, n.º 1, al. b)), Braga (Aviso 5616/2023, art. 57.º, n.º 1, al. b)), Évora (regulamento do CRO, art. 19.º, n.º 7) e Coimbra (Aviso 6348/2023, art. 12.º). O art. 11.º, n.º 3 do regulamento de Coimbra omite, como o RGAC, a parte final do n.º 2 do art. 7.º da Portaria.",
            ],
            "proposta": "Repor no art. 91.º, n.º 9 a parte final do n.º 2 do art. 7.º da Portaria 146/2017. Ressalvar no n.º 3 a recolha pontual por particular seguida de entrega ou comunicação num prazo curto, e as capturas em programa CED autorizado (ver C-04). No art. 140.º, n.º 2 manter só a recolha sem apresentação, com prazo fixado, e retirar a recolha por entidade diversa das câmaras. Articular com os arts. 1318.º e 1323.º do Código Civil.",
            "levantado": ["Análise interna",
                "Provedor de Justiça, processo R-4579/08 (Lajes do Pico): as competências camarárias não são exclusivas",
                "Regulamentos municipais de Setúbal, Braga, Évora e Coimbra (leitura de 8.10.2026)",
                "Análise interna (pedido de esclarecimento sobre gatos de colónia acolhidos, Setúbal, 8.10.2026)",
            ],
            "estado": "Aberto",
            "rel": ["C-02", "C-16",
                "C-04",
                "T-20",
            ],
        },
        {
            "cod": "T-16",
            "titulo": "Detentores de facto que dizem tratar de animais errantes",
            "onde": ["sem norma no RGAC"],
            "origem": "VIGENTE",
            "problema": [
                "Os médicos veterinários municipais relatam casos de particulares que mantêm grupos de animais em "
                "propriedades privadas e dizem que são errantes, para que o Estado suporte os custos. Pedem um "
                "mecanismo de responsabilização dos detentores de facto.",
            ],
            "proposta": "Presunção de detenção para quem, de forma regular, aloja, alimenta ou controla o acesso aos "
                        "animais num prédio de que dispõe.",
            "levantado": ["Contributos dos médicos veterinários municipais (6.3.2026)",
                          "Tribunal da Relação de Lisboa, proc. 3121/03.4TBCSC.L1-6 (24.11.2009): detentor é aquele em cuja casa o animal é albergado",
                          "ENAE (família de acolhimento temporário e cuidador não regulados)",
                          "Lei 8/2017, art. 493.º-A do Código Civil (despesas de quem socorreu o animal)"],
            "estado": "Aberto",
            "rel": ["C-10"],
        },
        {
            "cod": "T-17",
            "titulo": "Prazos de comunicação ao SIAC mais pesados do que o Regulamento europeu",
            "onde": ["art. 73.º, n.º 3", "art. 70.º, n.º 2"],
            "origem": "RGAC",
            "problema": [
                "Morte: 2 dias úteis, com atestado médico-veterinário ou prova de incineração. Desaparecimento e "
                "recuperação: 24 horas. Entrada no território por operador: 5 dias úteis.",
                "O Regulamento (UE) 2026/1818 pede o registo da morte «em conformidade com as condições "
                "estabelecidas pelo Estado-Membro», sem prazo, e só se aplica aos proprietários particulares a "
                "partir de 2036 (cães) e 2041 (gatos) (art. 20.º, n.º 7). O falhanço destes prazos arrasta a "
                "presunção de abandono (T-05).",
            ],
            "proposta": "Rever os prazos. Dispensar a prova da morte quando a morte é registada por médico "
                        "veterinário. Ponderar as 72 horas para o desaparecimento.",
            "levantado": ["OMV (propõe 72 horas)", "SNMV (propõe 48 horas)",
                          "Comentário DAJA ao art. 73.º («Pode se de difícil aplicabilidade»)"],
            "estado": "Aberto",
            "rel": ["T-05"],
        },
        {
            "cod": "T-18",
            "titulo": "Animais deixados em centros veterinários",
            "onde": ["art. 3.º, definição de «Abandono»"],
            "origem": "VIGENTE",
            "problema": [
                "A definição de abandono fala da remoção do animal sem comprovativo da transmissão da sua guarda. "
                "Não trata o caso do animal deixado num centro de atendimento médico-veterinário e que o titular "
                "não volta a buscar. O centro fica com o animal sem saber se o pode entregar, a quem e quando.",
            ],
            "proposta": "Prever um termo de responsabilidade na entrada do animal e um prazo a partir do qual se "
                        "presume o abandono, com entrega a CRO ou associação e comunicação ao SIAC.",
            "levantado": ["OMV, parecer sobre abandono de animais em centros veterinários (nov. 2015)",
                          "Cátia Simões, RJLB 2019 (o animal não recolhido de hotel ou CAMV escapa à definição de abandono)"],
            "estado": "Aberto",
            "rel": ["T-05", "T-06"],
        },
        {
            "cod": "T-19",
            "titulo": "Nada diz quem é titular quando o animal não tem proprietário",
            "onde": ["art. 3.º, definição de «Titular»", "art. 69.º, n.º 1", "art. 86.º, n.º 6"],
            "origem": "PARCIAL",
            "problema": [
                "A al. f) do art. 3.º do DL 82/2019 define o titular como o proprietário ou o possuidor «cuja "
                "posse faça presumir a propriedade». As duas hipóteses pressupõem um dono, ou um possuidor que "
                "atua como tal. O animal que ninguém tem como seu não cabe em nenhuma delas.",
                "O problema não é a falta de detenção. A titularidade nunca exigiu que o titular detenha o "
                "animal: o DL 82/2019 prevê o titular que não detém, no art. 13.º, n.º 2, al. d), que o obriga a "
                "comunicar o desaparecimento, no art. 14.º, n.º 1, que fala do «titular ou o simples detentor», e "
                "no art. 22.º, al. a), que alinha «titular, possuidor ou detentor». O que falta é a regra para o "
                "animal sem dono.",
                "O RGAC fecha a lacuna só no CED, ao mandar registar os gatos de colónia em nome do município "
                "(art. 86.º, n.º 6). Fica de fora o animal perdido antes de ser reclamado, o cão errante recolhido e o animal "
                "apreendido, e a definição geral continua assente no proprietário.",
                "O critério civil tem ainda um defeito próprio. A posse faz presumir a propriedade, mas o n.º 1 do "
                "art. 1268.º do Código Civil faz essa presunção ceder quando exista registo anterior a favor de "
                "outrem. O registo serve para provar a propriedade e a propriedade determina quem se registra.",
            ],
            "proposta": "Assentar a definição de titular no registo, com a presunção ilidível proposta na ficha "
                        "T-03, e acrescentar uma norma supletiva: não havendo proprietário conhecido, é titular a "
                        "entidade a quem a lei comete a responsabilidade pelo animal, designadamente a câmara "
                        "municipal, através do CRO, nos casos de recolha e nos programas CED. Esta proposta "
                        "qualifica a da ficha T-01: repor o critério do DL 82/2019 não fecha a lacuna, porque esse "
                        "critério também pressupõe proprietário ou possuidor.",
            "levantado": ["Análise interna (titularidade dos animais em programas CED, 2.10.2026)"],
            "estado": "Aberto",
            "rel": ["T-01", "T-02", "T-03", "C-08"],
        },
        {
            "cod": "T-20",
            "titulo": "Quem acolhe um animal errante pode ficar sem saída lícita",
            "onde": [
                "art. 3.º, definição de «Abandono»",
                "art. 94.º, n.ºs 7 e 8",
                "art. 91.º, n.º 9"
            ],
            "origem": "VIGENTE",
            "problema": [
                "Quem acolhe um animal errante passa a ser detentor (art. 3.º). Se depois o devolver à rua, a conduta cabe na definição de abandono: remoção «pelo detentor ou titular» sem comprovativo da transmissão da guarda para outra pessoa, para o município ou para associação zoófila (art. 3.º). Pode ainda caber no art. 388.º do Código Penal, que pune quem, «tendo o dever de guardar, vigiar ou assistir animal de companhia», o abandona.",
                "A saída lícita é entregar o animal. O art. 94.º, n.º 7 só deixa pedir a recolha ao CRO aos titulares, e só por circunstâncias supervenientes. O n.º 8 manda os restantes titulares recorrer a associação zoófila. O detentor que não é titular não aparece em nenhum dos dois números. O art. 91.º, n.º 9 deixou de prever a entrega por quem capturou o animal (ver T-15).",
                "No regime vigente o problema já existe na prática. Os regulamentos municipais permitem recusar a receção por sobrelotação (Setúbal, RSBEAMS 2020, art. 57.º, n.º 6) ou depois de ponderar fatores de risco (Coimbra, Aviso 6348/2023, art. 12.º, n.º 2). Quem acolheu fica entre a recusa do CRO e a proibição de abandono."
            ],
            "proposta": "Prever no art. 94.º que o detentor de animal errante que o tenha recolhido possa entregá-lo ao CRO. A recusa do CRO deve ser fundamentada e indicar alternativa: associação zoófila, lar de acolhimento ou integração no programa CED. A entrega recusada afasta a presunção de abandono.",
            "levantado": [
                "Análise interna (pedido de esclarecimento sobre gatos de colónia acolhidos, Setúbal, 8.10.2026)",
                "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): o detentor que não cuida do animal deve diligenciar a sua entrega a canil ou organização que o possa receber",
                "Regulamentos municipais de Setúbal (2020) e Coimbra (2023)"
            ],
            "estado": "Aberto",
            "rel": [
                "T-14",
                "T-15"
            ]
        },
    ],
}

# ---------------------------------------------------------------------------
# Tema C: programas CED, colonias e animais errantes
# ---------------------------------------------------------------------------
TEMA_C = {
    "letra": "C",
    "titulo": "Programas CED, colónias e animais errantes",
    "intro": [
        "Hoje o regime CED está na Lei 27/2016 (art. 4.º) e na Portaria 146/2017 (art. 9.º). A Lei diz que o "
        "Estado assegura a concretização de programas CED para gatos. A Portaria diz que as câmaras podem "
        "autorizar colónias.",
        "O RGBEAC (jun. 2025, art. 44.º) tinha transformado o CED num dever das câmaras, com cuidadores "
        "identificados. O RGAC voltou ao modelo da Portaria (arts. 86.º e 87.º) e revoga a Lei 27/2016. "
        "Acrescenta o registo das colónias no SIAC e o regime do CED em prédios privados.",
    ],
    "fichas": [
        {
            "cod": "C-01",
            "titulo": "O CED passa a ser só uma faculdade das câmaras",
            "onde": ["art. 86.º, n.º 1", "art. 149.º, n.º 1 (revogação da Lei 27/2016)"],
            "origem": "RGAC",
            "problema": [
                "O art. 86.º, n.º 1 diz que as câmaras «podem […] autorizar» colónias. Hoje, acima da Portaria, está "
                "a Lei 27/2016, cujo art. 4.º diz que o Estado «assegura» a concretização de programas CED para "
                "gatos. O RGAC revoga essa lei. O dever legal desaparece e o CED fica dependente da vontade de "
                "cada câmara.",
                "O RGBEAC dizia «devem as câmaras municipais […] executar programas». Uma revisora comentou «A Lei "
                "27 diz podem», o que não corresponde ao texto da lei.",
                "A proposta de resposta da DGAV à MIAR (24.10.2025) conclui que não há contradição insanável entre a Lei 27/2016 e a Portaria 146/2017, porque a matéria dos animais errantes é competência dos municípios. Não analisa o «assegura» do art. 4.º da Lei, que é o argumento central da MIAR. Apoia-se no Código Administrativo de 1940 e na Lei 75/2013, anexo I, art. 33.º, n.º 1, als. ii) e jj), que falam em abate e em animais nocivos (ver C-19).",
                "A resposta da Direção de Serviços à MIAR (20.10.2025) funda o carácter facultativo do CED no n.º 2 do art. 9.º da Portaria 146/2017. A faculdade está no n.º 1 («podem […] autorizar»). O n.º 2 trata de quem toma a iniciativa.",
            ],
            "proposta": "Posição desta análise: a leitura que trata o CED como mera faculdade municipal, adotada na resposta da Direção de Serviços à MIAR (20.10.2025) e na proposta de resposta da DGAV (24.10.2025), é um erro de interpretação. O art. 4.º da Lei 27/2016 impõe ao Estado um dever («assegura») e indica o meio de o cumprir: os centros de recolha oficial, que são municipais. A competência municipal identifica quem executa o dever. Não o elimina. O «podem […] autorizar» do art. 9.º, n.º 1 da Portaria 146/2017 refere-se à autorização de cada colónia em local designado e tem de ser lido em conformidade com a Lei, porque são inválidos os regulamentos «desconformes com a Constituição, a lei e os princípios gerais de direito administrativo» (CPA, art. 143.º, n.º 1). O n.º 2 do art. 9.º só trata de quem toma a iniciativa e não pode fundar o carácter facultativo. Para o RGAC: manter pelo menos o nível da Lei 27/2016: «as câmaras municipais asseguram, diretamente ou "
                        "por protocolo, programas CED para gatos, sempre que se justifique».",
            "levantado": ["ENAE, p. 35 («Os programas CED não estão instituídos em todo o território»)",
                          "Livre e PAN (respostas de 2024)", "ARPA (o CED é dever legal dos municípios, dez. 2022)",
                          "Gunther e outros, PNAS 2022, e Boone e outros, 2019 (o CED só resulta com esterilização intensa e contínua)",
                          "Comissão Europeia, SWD(2024) 88 (errantes fora do âmbito do Regulamento (UE) 2026/1818)",
                "MIAR (dez. 2024 a out. 2025): o CED é dever do Estado e as associações não precisam de validação autárquica",
                "DGAV, proposta de resposta à MIAR (24.10.2025): o CED depende de autorização municipal",
            ],
            "estado": "Aberto",
            "rel": ["C-02",
                "C-19",
            ],
        },
        {
            "cod": "C-02",
            "titulo": "O cuidador de colónia não existe no texto",
            "onde": ["art. 86.º (todo)", "art. 3.º (sem definição)"],
            "origem": "RGAC",
            "problema": [
                "A palavra cuidador não aparece no RGAC. O RGBEAC incluía os cuidadores no plano de formação e no "
                "plano de gestão da colónia. O plano de gestão do RGAC só identifica o médico veterinário e as "
                "pessoas da entidade responsável (art. 86.º, n.º 6, al. a)).",
                "Quem alimenta e vigia a colónia continua sem posição, sem deveres e sem proteção. Pode ser "
                "qualificado como detentor em nome do município e ficar exposto a responsabilidade civil (T-13) e "
                "à proibição de alimentar (C-03).",
            ],
            "proposta": "Criar a figura do cuidador de colónia registado no SIAC, associado à colónia, como detentor "
                        "em nome do município, com deveres e limites de responsabilidade definidos.",
            "levantado": ["ENAE, p. 35 («não está definido o conceito de "
                          "\"cuidador da colónia\"»)", "Contributos dos médicos veterinários municipais (6.3.2026)",
                          "PAN (figura do animal comunitário, PJL 662/XV)",
                          "OMV, parecer ao PJL 662/XV (5.1.2024): contra o animal comunitário por diluir a responsabilidade",
                          "PAN, PJL 662/XV (definição de animal comunitário)",
                          "Município do Fundão, Edital 145/2023, art. 4.º, n.º 1 (cuidador registado responsável pela colónia)",
                          "Município da Moita, Regulamento 143/2025, art. 3.º, n.º 2"],
            "estado": "Aberto",
            "rel": ["C-03", "T-13", "T-14"],
        },
        {
            "cod": "C-03",
            "titulo": "Proibição nacional de alimentar animais na via pública",
            "onde": ["art. 84.º, n.º 3", "art. 140.º, n.º 2 («A alimentação na via pública em violação do disposto no artigo XX.º»)"],
            "origem": "RGAC",
            "problema": [
                "O art. 84.º, n.º 3 proíbe alimentar animais na via pública, salvo em plano aprovado pela câmara, e "
                "o art. 140.º pune a infração. Hoje estas proibições existem só em alguns regulamentos municipais.",
                "A ENAE aponta esses regulamentos como obstáculo ao CED. Sem a figura do cuidador (C-02) e com o CED "
                "dependente de autorização (C-01), quem alimenta uma colónia não autorizada passa a cometer uma "
                "contraordenação. Nenhum revisor comentou a norma.",
            ],
            "proposta": "Excecionar expressamente os cuidadores de colónias registadas e os pontos de alimentação "
                        "previstos em plano municipal de gestão de colónias.",
            "levantado": ["ENAE, p. 35 («Existem regulamentos ou posturas camarárias que proíbem alimentar "
                          "animais errantes»)", "Contributo de um médico veterinário municipal (pede coimas aos "
                          "alimentadores, posição contrária)", "Município do Fundão, Edital 145/2023 (o regime das colónias é exceção à proibição geral de alimentar na via pública)",
                          "Provedor de Justiça, Relatório 2020 (campanhas da DGAV contra a alimentação de errantes)"],
            "estado": "Aberto",
            "rel": ["C-02"],
        },
        {
            "cod": "C-04",
            "titulo": "Só as câmaras podem capturar, mas o CED pode ser gerido por outras entidades",
            "onde": ["art. 91.º, n.º 3", "art. 86.º, n.º 4", "art. 140.º, n.º 2"],
            "origem": "RGAC",
            "problema": [
                "O art. 91.º, n.º 3 diz que a captura e a recolha de animais «competem, exclusivamente, às câmaras "
                "municipais», e o art. 140.º pune a «recolha e captura de animais por entidade diversa das câmaras "
                "municipais».",
                "O art. 86.º, n.º 4 admite que a câmara atribua a gestão do CED a outra entidade por protocolo. Na "
                "prática, as capturas para CED são feitas por associações e voluntários. Sem ressalva, ficam a "
                "cometer uma contraordenação.",
            ],
            "proposta": "Ressalvar no art. 91.º, n.º 3 as capturas feitas no âmbito de programa CED autorizado, pela "
                        "entidade responsável ou por pessoas identificadas no plano de gestão.",
            "levantado": ["Análise interna"],
            "estado": "Aberto",
            "rel": ["C-02", "C-08"],
        },
        {
            "cod": "C-05",
            "titulo": "Passagem obrigatória pelo CRO antes de o gato entrar na colónia",
            "onde": ["art. 86.º, n.º 6, al. d)"],
            "origem": "VIGENTE",
            "problema": [
                "Os gatos capturados têm de ser entregues no CRO para verificação da aptidão antes de integrarem a "
                "colónia. A regra vem da Portaria 146/2017 e sobrecarrega os CRO, cuja falta de espaço é a "
                "principal dificuldade apontada pelo relatório de avaliação da Lei 27/2016.",
                "O projeto de revisão da Portaria de 2021 revogava esta alínea. O RGBEAC também não a tinha.",
            ],
            "proposta": "Substituir a entrega no CRO por avaliação feita pelo médico veterinário do programa, com "
                        "registo no SIAC.",
            "levantado": ["Relatório final do GTBEA (DGAV, 2021)", "Projeto de revisão da Portaria 146/2017 (ANMP, 2021)",
                          "Provedor de Justiça, Relatório 2023 (queixas sobre sobrelotação dos CRO)"],
            "estado": "Aberto",
            "rel": [],
        },
        {
            "cod": "C-06",
            "titulo": "Exclusão dos cães do CED",
            "onde": ["art. 86.º, n.º 3"],
            "origem": "VIGENTE",
            "problema": [
                "O RGAC mantém que o CED «não é aplicável a cães». É o ponto mais disputado entre as entidades. A "
                "OMV e a APMVEAC são contra o CED para cães. PAN e BE são a favor. Os médicos veterinários "
                "municipais propõem um regime excecional de cães comunitários, reconhecidos caso a caso pelo "
                "médico veterinário municipal. A FEDRA propõe parques de matilhas.",
                "O RGAC não prevê nenhuma alternativa para matilhas e cães assilvestrados quando o CRO não tem "
                "capacidade.",
            ],
            "proposta": "Manter a exclusão da devolução de cães à via pública, mas prever uma alternativa: parques de "
                        "realojamento de matilhas ou um regime excecional de cão comunitário com critérios "
                        "de segurança.",
            "levantado": [
                          "OMV, parecer ao PJL 662/XV (5.1.2024): contra o CED em cães",
                          "WOAH, Código Sanitário dos Animais Terrestres, cap. 7.7 (CED em cães só como medida complementar)", "APMVEAC (parecer set. 2023)", "PAN e BE (2024)",
                          "Contributos dos médicos veterinários municipais (6.3.2026)", "FEDRA", "PCP (proposta ao OE2026)", "Livre (programa 2024)", "Movimento de Intervenção pelas Matilhas (Coimbra)", "Projeto de alteração da Portaria 146/2017 (esterilização excecional de cães)"],
            "estado": "Aberto",
            "rel": [],
        },
        {
            "cod": "C-07",
            "titulo": "Remissões e numeração erradas no artigo do CED",
            "onde": ["art. 86.º, n.ºs 1, 2, 5, 6 e 9", "art. 86.º, n.º 6, al. e)", "art. 70.º, n.º 12"],
            "origem": "RGAC",
            "problema": [
                "O n.º 1 remete para os «artigos 65.º e 66.º (controlo ambiental e controlo das populações errantes "
                "e assilvestradas)», que são agora os arts. 84.º e 85.º.",
                "Há dois n.º 5 e dois n.º 6. O n.º 9 remete para os requisitos «referidos no n.º 4», que são os do "
                "n.º 6. Os n.ºs 2 e 9 dizem o mesmo (medidas corretivas e suspensão).",
                "A al. e) do n.º 6 manda registar os gatos «em nome da câmara municipal promotora». O art. 70.º, "
                "n.º 12 diz «em nome do município responsável pelo programa CED».",
            ],
            "proposta": "Renumerar, corrigir as remissões, fundir os n.ºs 2 e 9 e usar «município» nos dois artigos.",
            "levantado": ["Revisão editorial de 10.6.2026 (ponto B9)", "Análise interna"],
            "estado": "Aberto",
            "rel": [],
        },
        {
            "cod": "C-08",
            "titulo": "Entidade promotora, entidade responsável e titular: quem responde pela colónia",
            "onde": ["art. 86.º, n.ºs 4, 5 (segundo), 6 e 10", "art. 70.º, n.º 12"],
            "origem": "VIGENTE",
            "problema": [
                "O artigo usa entidade promotora (a câmara) e entidade responsável (quem gere por protocolo) sem as "
                "definir e sem dizer quem responde por quê. Os gatos são registados em nome do município, que fica "
                "titular. As despesas são da entidade promotora ou do protocolo (n.º 10).",
                "Não se diz quem responde pelos danos causados por gatos de colónia. A CDU referiu as «questões "
                "práticas e de responsabilidade civil» para ter prudência no alargamento do CED.",
                "Há duas leituras na DGAV sobre o titular dos gatos CED. A proposta de resposta à MIAR (24.10.2025) admite que o CRO ou a associação zoófila sejam titulares, «podendo essa questão ficar definida nos referidos programas CED», com base no DL 82/2019, art. 3.º, al. f), e art. 17.º. A nota jurídica sobre a titularidade (out. 2026) conclui que o titular é o município, pelo DL 82/2019, art. 11.º, n.º 5, e pela entrega obrigatória no CRO (Portaria 146/2017, art. 9.º, n.º 4, al. d)). O art. 17.º é uma isenção de taxa e não um critério de titularidade, e a titularidade não pode ser fixada por um programa. O RGAC segue a segunda leitura (art. 70.º, n.º 12).",
            ],
            "proposta": "Definir as duas entidades no art. 3.º ou no próprio art. 86.º, e dizer que o município, "
                        "como titular, responde nos termos gerais, com direito de regresso sobre a entidade responsável. Alinhar a posição interna da DGAV antes de responder a outros pedidos sobre a titularidade dos gatos CED.",
            "levantado": ["CDU (resposta de 2024)", "Análise interna", "PCP (proposta ao OE2026)", "ARPA (dez. 2022)",
                "DGAV, proposta de resposta à MIAR (24.10.2025): CRO ou associação podem ser titulares",
                "MIAR (2024 e 2025): recusa ser titular de animais de rua",
            ],
            "estado": "Aberto",
            "rel": ["T-13", "C-04"],
        },
        {
            "cod": "C-09",
            "titulo": "Registo da colónia no SIAC sem conteúdo definido",
            "onde": ["art. 86.º, n.º 6, al. f)", "art. 5.º"],
            "origem": "PARCIAL",
            "problema": [
                "O RGAC prevê o registo da colónia no SIAC, com georreferenciação, número de animais e entidade "
                "responsável. É um avanço: hoje não é possível saber quantas colónias existem nem onde.",
                "Falta dizer se a colónia tem número próprio, quem atualiza o registo, se os cuidadores ficam "
                "registados e se o registo é público.",
            ],
            "proposta": "Número nacional de colónia, atualização pela entidade responsável, cuidadores associados "
                        "e registo anual de entradas, saídas e mortes.",
            "levantado": ["ENAE, p. 35 («não é possível aferir o número de animais nem o número e localização das "
                          "colónias»)", "ENAE, §33 (número de registo nacional da colónia)",
                          "Provedor de Justiça, Relatório 2023 (planos CED autorizados sem divulgação pública)"],
            "estado": "Parcialmente resolvido",
            "rel": ["C-02"],
        },
        {
            "cod": "C-10",
            "titulo": "Colónias em prédios privados",
            "onde": ["art. 87.º"],
            "origem": "PARCIAL",
            "problema": [
                "O RGAC admite o CED em prédios privados, com anuência escrita do proprietário, dever de colaborar "
                "e contraordenação em caso de obstrução. Os médicos veterinários municipais dizem que a maioria "
                "das colónias está em quintais.",
                "Ficam por resolver: o que fazer quando o proprietário não autoriza; o dever de colaborar inclui a "
                "alimentação (n.º 3), o que obriga o proprietário a tarefas que não escolheu; e os prédios "
                "devolutos, para os quais um comentário DAJA sugere a posse administrativa pelos municípios.",
            ],
            "proposta": "Prever a situação de recusa (intervenção por razões de saúde pública ou bem-estar animal) "
                        "e retirar a alimentação do dever de colaboração do proprietário.",
            "levantado": ["Contributos dos médicos veterinários municipais (6.3.2026)",
                          "Comentário DAJA ao art. 86.º (prédios devolutos, posse administrativa, RJUE)"],
            "estado": "Parcialmente resolvido",
            "rel": ["T-16"],
        },
        {
            "cod": "C-11",
            "titulo": "CED e conservação da natureza",
            "onde": ["art. 86.º, n.º 5"],
            "origem": "VIGENTE",
            "problema": [
                "O RGAC diz só que o CED «deve ser evitado» em parques públicos, refúgios de vida selvagem e habitats. "
                "Não diz quem decide nem como. O RGBEAC exigia consulta prévia ao ICNF em áreas classificadas. O "
                "projeto de revisão da Portaria de 2021 exigia articulação com o ICNF.",
                "A SPEA aponta a predação por gatos como ameaça às aves marinhas.",
            ],
            "proposta": "Exigir parecer do ICNF para colónias em áreas classificadas ou na sua proximidade.",
            "levantado": ["SPEA", "RGBEAC (jun. 2025), art. 44.º, n.º 3", "SPEA, parecer Açores 2020 (84% da predação de cagarros por gatos)",
                          "Trouwborst e Somsen, Journal of Environmental Law, 2020 (Diretivas Aves e Habitats)",
                          "Galão e outros, Biological Conservation, 2025 (predação na Madeira)",
                          "Loss, Will e Marra, Nature Communications, 2013", "Projeto de alteração da Portaria 146/2017 (articulação com o ICNF)"],
            "estado": "Aberto",
            "rel": [],
        },
        {
            "cod": "C-12",
            "titulo": "Gatos de colónia em infração permanente",
            "onde": ["art. 60.º, n.º 1", "art. 3.º, definição de «Animal errante»", "art. 91.º, n.º 1, al. a)"],
            "origem": "RGAC",
            "problema": [
                "O art. 60.º, n.º 1 obriga todos os cães e gatos na via pública a usar coleira com o contacto do "
                "detentor. Os gatos de colónia não a usam.",
                "Pela definição do art. 3.º, um gato fora do controlo e da guarda do detentor é errante, e a câmara "
                "deve capturar os errantes (art. 91.º, n.º 1, al. a)). Um gato de colónia CED encaixa nas duas "
                "normas.",
            ],
            "proposta": "Excecionar os gatos integrados em programa CED, identificados pelo corte na orelha e pelo "
                        "transponder, no art. 60.º e na definição de animal errante.",
            "levantado": ["Revisão editorial de 10.6.2026 (pontos A4 e A5)"],
            "estado": "Aberto",
            "rel": [],
        },
        {
            "cod": "C-13",
            "titulo": "Crias e gatos sociáveis: retirar ou devolver",
            "onde": ["art. 86.º, n.º 7"],
            "origem": "VIGENTE",
            "problema": [
                "O RGAC manda libertar os gatos na colónia de origem, salvo deslocalização «nos termos a definir e "
                "divulgar pela DGAV». Não diz o que fazer com as crias em idade de socialização nem com os gatos "
                "dóceis.",
                "A ENAE diz que esses animais são retirados das colónias e encaminhados para adoção. Não há critério "
                "nem procedimento para distinguir o gato feral do sociável.",
            ],
            "proposta": "Norma que mande encaminhar para adoção as crias em idade de socialização e os adultos "
                        "sociáveis, com critério definido pela DGAV.",
            "levantado": ["ENAE, p. 34 («Sempre que possível, os animais adultos dóceis e as crias que ainda "
                          "estejam em idade de socialização são retirados das colónias e encaminhados para adoção»)", "APMVEAC (adoção de animais com menos de 6 meses, 2021)"],
            "estado": "Aberto",
            "rel": ["T-15"],
        },
        {
            "cod": "C-14",
            "titulo": "Suspensão do programa e recolha dos gatos sem garantias",
            "onde": ["art. 86.º, n.ºs 2 e 9"],
            "origem": "VIGENTE",
            "problema": [
                "A câmara pode suspender o programa e recolher os gatos para o CRO. Não há audiência da entidade "
                "responsável, prazo para corrigir, nem destino previsto para os gatos se o CRO não tiver espaço.",
            ],
            "proposta": "Prever notificação prévia com prazo para corrigir e um plano de destino dos animais antes "
                        "da recolha.",
            "levantado": ["Análise interna (inventário de zonas cinzentas do CED)"],
            "estado": "Aberto",
            "rel": ["C-07"],
        },
        {
            "cod": "C-15",
            "titulo": "Meios: médicos veterinários municipais e financiamento",
            "onde": ["art. 86.º, n.ºs 1, 5 (segundo) e 10"],
            "origem": "VIGENTE",
            "problema": [
                "O CED depende de parecer vinculativo e da supervisão do médico veterinário municipal ou ao serviço "
                "do município. Há concelhos sem médico veterinário municipal. As despesas ficam para a entidade "
                "promotora ou para o protocolo, sem fonte de financiamento prevista.",
            ],
            "proposta": "Admitir médico veterinário contratado ou partilhado entre municípios e ligar o CED às linhas "
                        "de apoio da DGAV.",
            "levantado": ["Relatório final do GTBEA (DGAV, 2021): financiamento como principal constrangimento",
                          "Inventário interno de zonas cinzentas do CED (zona 20)", "PCP (2021)"],
            "estado": "Aberto",
            "rel": [],
        },
        {
            "cod": "C-16",
            "titulo": "Conflito com vizinhos e dimensão da colónia",
            "onde": ["art. 86.º, n.º 6 (segundo)"],
            "origem": "VIGENTE",
            "problema": [
                "O RGAC diz que a dimensão da colónia não pode pôr em causa a salubridade, a saúde pública e a "
                "segurança, mas não dá critério. Os médicos veterinários municipais relatam casos em que os "
                "cuidadores pedem o CED e os vizinhos exigem a recolha dos animais, e dizem que recolher milhares "
                "de gatos assilvestrados para os CRO não é viável.",
            ],
            "proposta": "Critérios de dimensão por tipo de local no manual da DGAV e um procedimento de mediação "
                        "antes de decidir a recolha.",
            "levantado": ["Contributos dos médicos veterinários municipais (6.3.2026)"],
            "estado": "Aberto",
            "rel": ["C-14"],
        },
        {
            "cod": "C-17",
            "titulo": "Plano municipal de controlo de errantes sem conteúdo mínimo nem consequências",
            "onde": ["art. 85.º, n.ºs 1 a 3"],
            "origem": "VIGENTE",
            "problema": [
                "As câmaras devem apresentar à DGAV, todos os anos, um plano de controlo das populações errantes. "
                "O artigo não diz que dados são obrigatórios, não liga o plano ao registo das colónias no SIAC e não "
                "prevê consequências para quem não o apresenta. Um comentário do grupo de trabalho pede isso mesmo.",
               
            ],
            "proposta": "Fixar os dados mínimos (colónias, número de gatos esterilizados, capturas, entradas e saídas "
                        "do CRO), retirá-los do SIAC sempre que possível e ligar o acesso a apoios públicos à entrega "
                        "do plano.",
            "levantado": ["Comentário do grupo de trabalho ao art. 85.º («prever sanções para os Municípios que não "
                          "informam a DGAV»)"],
            "estado": "Aberto",
            "rel": ["C-09"],
        },
        {
            "cod": "C-18",
            "titulo": "A definição de animal errante passa a abranger qualquer animal não identificado",
            "onde": [
                "art. 3.º, definição de «Animal errante»",
                "art. 91.º, n.º 1, al. a)"
            ],
            "origem": "PARCIAL",
            "problema": [
                "Hoje há duas definições. O DL 276/2001 (art. 2.º, n.º 1, al. c)) considera errante o animal encontrado em lugar público fora do controlo e guarda do detentor, «ou relativamente ao qual existam fortes indícios de que foi abandonado ou não tem detentor e não esteja identificado». O DL 314/2003 (art. 2.º, al. n)) só considera errante o cão ou gato encontrado em local público, fora do controlo ou vigilância do detentor, «e não identificado». Uma cria sem dono nascida num quintal é errante para o primeiro e não para o segundo.",
                "O RGAC unifica, mas troca o «e» por «ou»: é errante também o animal «que não tem detentor ou não se encontra identificado» (art. 3.º). Lida à letra, qualquer animal não identificado é errante, mesmo em casa e com detentor, incluindo as crias antes do prazo de identificação. O art. 91.º, n.º 1, al. a) limita a captura aos errantes encontrados em lugares públicos, o que atenua o efeito, mas as outras normas que usam o conceito ficam com um âmbito que não se pretende."
            ],
            "proposta": "Repor a conjunção cumulativa: «que não tem detentor e não se encontra identificado». Ponderar excluir da definição os gatos integrados em programa CED (ver C-12).",
            "levantado": [
                "Análise interna (8.10.2026)"
            ],
            "estado": "Aberto",
            "rel": [
                "C-12",
                "T-15"
            ]
        },
        {
            "cod": "C-19",
            "titulo": "A Lei 75/2013 ainda atribui às câmaras o abate de canídeos e gatídeos",
            "onde": [
                "sem norma no RGAC"
            ],
            "origem": "VIGENTE",
            "problema": [
                "O anexo I da Lei 75/2013, art. 33.º, n.º 1, al. ii), dá à câmara municipal a competência para «Proceder à captura, alojamento e abate de canídeos e gatídeos». A redação é anterior à Lei 27/2016, que proibiu o abate como forma de controlo da população, e não foi alterada.",
                "O RGAC revoga a Lei 27/2016 (art. 149.º, n.º 1) e não altera a Lei 75/2013. A norma geral de competência das câmaras continua a falar em abate."
            ],
            "proposta": "Alterar a al. ii) para «Proceder à captura, recolha, alojamento e esterilização de animais de companhia errantes». Verificar se, por ser matéria de competências das autarquias, a alteração exige lei da Assembleia da República ou autorização legislativa.",
            "levantado": [
                "Análise interna (8.10.2026)"
            ],
            "estado": "Aberto",
            "rel": [
                "C-17"
            ]
        },
    ],
}

# ---------------------------------------------------------------------------
# Pontos ja resolvidos pelo RGAC (para registo)
# ---------------------------------------------------------------------------

# ------------------------------------------------------------------ temas por capítulo
# Um tema por capítulo do RGAC. A letra é o prefixo dos códigos das fichas (por exemplo R-01).
# Para acrescentar uma ficha, basta pô-la na lista "fichas" do capítulo. Só aparecem no corpo do
# memorando os capítulos com fichas. Se a estrutura do RGAC mudar numa versão nova, rever
# "capitulos" (lista de capítulos do RGAC abrangidos, como aparecem em estrutura_rgac.json).
CAPITULOS = [
    {"letra": "A", "capitulos": ["Capítulo I"], "titulo": "Disposições gerais e definições (cap. I)", "intro": [], "fichas": [
        {
            "cod": "A-01",
            "titulo": "Duas normas diferentes sobre que espécies são animais de companhia",
            "onde": [
                "art. 2.º, n.º 2",
                "art. 4.º, n.ºs 1 a 3",
                "art. 3.º, definição de «Animal de companhia»"
            ],
            "origem": "RGAC",
            "problema": [
                "O art. 2.º, n.º 2 diz que são animais de companhia as espécies da Parte A do Anexo I do Regulamento (UE) 2016/429 e, «quando detidos para fins de companhia», as da Parte B. O art. 4.º, n.º 2 diz que as espécies da Parte B são «também considerados animais de companhia», sem essa condição. O n.º 3 acrescenta as espécies de uma lista positiva a aprovar por portaria. A definição do art. 3.º remete só para o art. 2.º, n.º 2.",
                "O conceito tem efeitos fora do RGAC. O Tribunal da Relação do Porto usou a remissão do DL 82/2019, art. 4.º, n.º 1, para o Regulamento (UE) 2016/429 para delimitar o animal de companhia do art. 389.º do Código Penal. Revogado o DL 82/2019, essa leitura passa a apoiar-se no RGAC, que tem duas regras diferentes."
            ],
            "proposta": "Manter uma só norma: a do art. 2.º, n.º 2, com a condição para a Parte B. No art. 4.º ficam só a lista positiva e as exceções.",
            "levantado": [
                "Análise interna (8.10.2026)",
                "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): conceito penal de animal de companhia"
            ],
            "estado": "Aberto",
            "rel": []
        },
    ]},
    {"letra": "P", "capitulos": ["Capítulo II"], "titulo": "Princípios gerais (cap. II)", "intro": [], "fichas": [
        {
            "cod": "P-01",
            "titulo": "A amarração no domicílio fica sem duração máxima nem requisitos verificáveis",
            "onde": [
                "art. 19.º, n.ºs 4 e 5",
                "art. 9.º, n.º 1, al. i)",
                "art. 140.º, n.º 2"
            ],
            "origem": "RGAC",
            "problema": [
                "O art. 19.º, n.º 4 proíbe amarrar cães e gatos por mais de uma hora. Estende a todos os titulares e detentores a regra que o Regulamento (UE) 2026/1818 fixa só para os operadores (art. 17.º, n.º 3).",
                "O n.º 5 exceciona a amarração «temporariamente no domicílio de titular ou detentor», com quatro condições cumulativas. Nenhuma fixa duração máxima, características do meio de amarração ou casos em que a amarração é sempre proibida. A condição «necessidade pontual e temporária» não é verificável no local. A condição de o endereço registado no SIAC coincidir com o do detentor não tem relação com o bem-estar do animal.",
                "Condenação por amarração diária. O Tribunal da Relação do Porto confirmou, em 8.5.2024, a condenação por maus-tratos a animal de companhia, por omissão (art. 387.º, n.ºs 1 e 2, do Código Penal), de quem mantinha um cão de cerca de 10 anos «diariamente acorrentado» e, no dia da intervenção, «fechado numa casota de madeira tipo gaiola, não conseguindo este sequer manter-se em pé». Pena de 200 dias de multa e pena acessória de proibição de detenção de animais de companhia por dois anos e seis meses (art. 388.º-A do Código Penal). O cão foi eutanasiado. A exceção do n.º 5, tal como está redigida, não permite distinguir com segurança uma situação destas de uma amarração lícita até ela chegar ao crime.",
                "O art. 140.º, n.º 2 remete sempre para «artigo XX.º». Não é possível confirmar que a violação dos n.ºs 4 e 5 do art. 19.º tem coima.",
                "O Projeto de Lei n.º 612/XVII/1.ª (BE, 5.5.2026) propõe critérios objetivos: até três horas por dia, meio com pelo menos três metros ou o triplo do comprimento do animal, destorcedor, ligação por peitoral ou coleira larga, um animal por ponto de fixação, e proibição absoluta para animais com menos de seis meses, fêmeas gestantes ou lactantes, animais doentes e em aviso meteorológico laranja ou vermelho (arts. 6.º e 7.º)."
            ],
            "proposta": "Fixar no n.º 5 uma duração máxima diária, requisitos técnicos do meio de amarração (comprimento mínimo, destorcedor, peitoral ou coleira larga, um animal por ponto) e casos de proibição absoluta (crias, fêmeas gestantes ou lactantes, animais doentes, aviso meteorológico laranja ou vermelho). Retirar a condição do endereço no SIAC. Prever coima expressa para a violação dos n.ºs 4 e 5 no art. 140.º.",
            "levantado": [
                "Tribunal da Relação do Porto, proc. 11/21.2GEVFR.P1 (8.5.2024): condenação por maus-tratos de cão mantido diariamente acorrentado",
                "Projeto de Lei n.º 612/XVII/1.ª (BE, 5.5.2026), arts. 6.º e 7.º",
                "Regulamento (UE) 2026/1818, art. 17.º, n.º 3",
                "Análise interna (8.10.2026)"
            ],
            "estado": "Aberto",
            "rel": []
        },
    ]},
    {"letra": "H", "capitulos": ["Capítulo III"], "titulo": "Detenção (cap. III)", "intro": [], "fichas": []},
    {"letra": "E", "capitulos": ["Capítulo IV"], "titulo": "Detenção em estabelecimentos (cap. IV)", "intro": [], "fichas": []},
    {"letra": "M", "capitulos": ["Capítulo V", "Capítulo VI", "Capítulo VII"],
     "titulo": "Alimentação, maneio, transporte, contenção e intervenções cirúrgicas (caps. V a VII)", "intro": [], "fichas": []},
    {"letra": "R", "capitulos": ["Capítulo VIII"], "titulo": "Registo, identificação e sistemas de informação (cap. VIII)", "intro": [], "fichas": []},
    {"letra": "Z", "capitulos": ["Capítulo IX"], "titulo": "Zoonoses (cap. IX)", "intro": [], "fichas": []},
    {"letra": "G", "capitulos": ["Capítulo X"], "titulo": "Gestão das populações animais (cap. X)", "intro": [], "fichas": []},
    {"letra": "K", "capitulos": ["Capítulo XI", "Capítulo XII", "Capítulo XIII"],
     "titulo": "Cadáveres, exposições, comércio e livros genealógicos (caps. XI a XIII)", "intro": [], "fichas": []},
    {"letra": "D", "capitulos": ["Capítulo XIV"], "titulo": "Animais perigosos e potencialmente perigosos (cap. XIV)", "intro": [], "fichas": []},
    {"letra": "S", "capitulos": ["Capítulo XV"], "titulo": "Medidas administrativas, fiscalização e contraordenações (cap. XV)", "intro": [], "fichas": []},
    {"letra": "F", "capitulos": ["Capítulo XVI", "Anexo I", "Anexo II"],
     "titulo": "Disposições finais e transitórias e anexos (cap. XVI e anexos)", "intro": [], "fichas": []},
]

# Ordem dos temas no memorando: primeiro os transversais, depois os capítulos.
TEMAS = [TEMA_T, TEMA_C] + CAPITULOS


# ------------------------------------------------------------------ lapsos formais
# Um lapso por entrada. "onde" usa a chave do artigo em estrutura_rgac.json (ex.: "86", "81-b").
# "ficha": código da ficha que já trata o mesmo ponto, se houver. Estados: os de ESTADOS.
LAPSOS = [
    {"cod": "L-01", "onde": ["81", "81-b"], "estado": "Aberto", "ficha": "",
     "lapso": "Há dois artigos 81.º: «Plataforma Nacional de Adoção de Animais de Companhia» (cap. VIII) e «Programa de vigilância e controlo em animais de companhia» (cap. IX).",
     "correcao": "Renumerar a partir do segundo art. 81.º e rever todas as remissões para os artigos seguintes."},
    {"cod": "L-02", "onde": ["81"], "estado": "Aberto", "ficha": "",
     "lapso": "O art. 81.º (Plataforma Nacional de Adoção) está sob uma subsecção sem número, com a epígrafe «PLATAFORMA NACIONAL DE REGISTO DOS ALOJAMENTOS» (seguida de SIAC), que não corresponde ao conteúdo do artigo.",
     "correcao": "Numerar a subsecção e dar-lhe epígrafe que corresponda ao artigo, ou retirar a subsecção."},
    {"cod": "L-03", "onde": ["142", "142-b"], "estado": "Aberto", "ficha": "",
     "lapso": "Há dois artigos 142.º. O segundo («Exames médico-veterinários, laboratoriais ou outros») está depois do Anexo II e da proposta de nota para a comunicação social, sob o título «SUBSECÇÃO III», com a nota «ALTERAR localização no documento!».",
     "correcao": "Decidir onde fica o artigo, colocá-lo no capítulo certo, renumerar e retirar a nota de trabalho."},
    {"cod": "L-04", "onde": ["32", "40", "49"], "estado": "Aberto", "ficha": "",
     "lapso": "No cap. IV, a secção I tem subsecções II e III sem subsecção I, e a secção II tem subsecção II sem subsecção I.",
     "correcao": "Criar a subsecção I em cada secção ou retirar a divisão em subsecções."},
    {"cod": "L-05", "onde": ["88", "91", "98", "99"], "estado": "Aberto", "ficha": "",
     "lapso": "No cap. X, as secções começam na II e saltam da III para a V (existem II, III, V e VI).",
     "correcao": "Renumerar as secções do cap. X."},
    {"cod": "L-06", "onde": ["22"], "estado": "Aberto", "ficha": "T-12",
     "lapso": "O art. 22.º, n.º 1 diz «Os detentores Operadores ??de animais de companhia».",
     "correcao": "Ver a ficha T-12."},
    {"cod": "L-07", "onde": ["73"], "estado": "Aberto", "ficha": "T-05",
     "lapso": "O art. 73.º, n.º 7 remete para os prazos «previstos no n.º 2 e 3» e para a «alínea e) do artigo 139.º», que não tem alíneas.",
     "correcao": "Ver a ficha T-05."},
    {"cod": "L-08", "onde": ["86"], "estado": "Aberto", "ficha": "C-07",
     "lapso": "O art. 86.º tem dois n.º 5 e dois n.º 6, remete no n.º 1 para os «artigos 65.º e 66.º» (agora arts. 84.º e 85.º) e no n.º 9 para o «n.º 4».",
     "correcao": "Ver a ficha C-07."},
    {"cod": "L-09", "onde": ["140"], "estado": "Aberto", "ficha": "T-11",
     "lapso": "O art. 140.º, n.º 2 pune o incumprimento «dos deveres previstos no artigo XX.º».",
     "correcao": "Ver a ficha T-11."},
    {
        "cod": "L-10",
        "onde": [
            "19"
        ],
        "estado": "Aberto",
        "ficha": "P-01",
        "lapso": "O art. 19.º, n.º 3 remete para «artigo YYº n.º 2 (Condições de manutenção de cães e gatos) segundo parágrafo». No n.º 5, as quatro condições não têm letra de alínea e a terceira tem a gralha «aas».",
        "correcao": "Fixar a remissão do n.º 3, numerar as condições do n.º 5 como alíneas a) a d) e corrigir «aas» para «as». Ver a ficha P-01."
    },
]


# ------------------------------------------------------------------ cobertura da revisão
# Uma entrada por artigo já trabalhado, com a chave de estrutura_rgac.json.
#   "estado": um de ESTADOS_REVISAO; "data": data da revisão; "regulamento": um de ESTADOS_REGULAMENTO;
#   "nota": texto curto (por exemplo, o artigo do Regulamento (UE) 2026/1818 em causa).
# Artigos sem entrada: aparecem «Por rever», ou «Parcial» se já tiverem fichas ou lapsos.
REVISAO = {
}

RESOLVIDOS = [
    ("Dois sentidos de detentor em leis diferentes",
     "O RGAC revoga o DL 276/2001, o DL 314/2003, o DL 315/2009 e o DL 82/2019 e fica com um só conjunto de "
     "definições (art. 149.º, n.º 1; art. 3.º). O problema passa para as portarias (T-07)."),
    ("Abandono só por conduta dos detentores",
     "A definição de abandono abrange a conduta do «detentor ou titular» (art. 3.º)."),
    ("Adotante chamado detentor",
     "A isenção de taxa de licença passa a ser para os «titulares que tenham adotado» (art. 79.º, n.º 18)."),
    ("Titular dos gatos CED e dos animais recolhidos",
     "Gatos CED e animais não identificados recolhidos em CRO registados em nome do município (art. 70.º, "
     "n.ºs 10 e 12). Animais recolhidos por municípios sem CRO registados em nome do município de origem "
     "(art. 69.º, n.º 4). O CRO passa a operador (art. 3.º)."),
    ("Animais perigosos",
     "Titular pessoa singular maior de 16 anos, com exceção para município e associação zoófila (art. 69.º, "
     "n.ºs 6 e 7). Seguro a cargo do titular."),
    ("Proprietário no passaporte e titular no SIAC",
     "O proprietário que consta do passaporte tem de coincidir com o titular do SIAC (art. 74.º, n.º 4)."),
    ("Transmissão de titularidade",
     "Titular que transfere, 14 dias (art. 73.º, n.º 2), igual ao Regulamento (UE) 2026/1818 (art. 20.º, n.º 4)."),
    ("Prazo em branco nos CRO",
     "O «prazo XXX dias» do art. 70.º, n.º 9 passou a 15 dias."),
]

# ---------------------------------------------------------------------------
# Posicoes de entidades externas (Anexo B). Preenchido com a pesquisa.
# Cada entrada: (tipo de entidade, entidade, data, tema T/C, posicao, fonte)
# ---------------------------------------------------------------------------
STAKEHOLDERS = [
    # (tipo de entidade, entidade, data, tema, posicao, fonte)
    # --- Documentos da Administracao
    ("Administração pública", "ICNF, Estratégia Nacional para os Animais Errantes (ENAE), consulta pública", "2023", "T e C",
     "Reconhece que não estão regulados a família de acolhimento temporário nem o estatuto de cuidador (pp. 30-31); que não está definido o cuidador de colónia, que não é possível saber o número e a localização das colónias, que há regulamentos municipais que proíbem alimentar errantes e que os CED não cobrem todo o território (p. 35). Diz que as crias em idade de socialização e os adultos dóceis são retirados das colónias para adoção (p. 34).",
     "https://www.icnf.pt/api/file/doc/41f8f44aee23be1a"),
    ("Administração pública", "DGAV, Relatório final do GTBEA (avaliação da Lei 27/2016)", "2021", "C",
     "Principal dificuldade na captura: falta de alojamento. Principal constrangimento dos alojamentos: financiamento. Recomenda rever as normas do programa CED e uniformizar conceitos.",
     "https://www.dgav.pt/wp-content/uploads/2021/08/Relatorio-FINAL-avaliacao-da-implementacao-da-Lei-27-2016.pdf"),
    ("Administração pública", "ICNF, projeto de alteração da Portaria 146/2017 enviado à ANMP", "2021", "C",
     "Tornava o CED um dever das câmaras, com a câmara como entidade responsável e registo SIAC em seu nome; incluía os cuidadores no plano de gestão; revogava a entrega prévia no CRO; exigia articulação com o ICNF em habitats de vida selvagem; admitia excecional e transitoriamente a esterilização de cães errantes sem capacidade no CRO. Citação: «Os programas CED nos refúgios de vida selvagem ou outros locais públicos que sirvam de habitat à vida selvagem devem ser articulados com o ICNF I.P.»",
     "https://anmp.pt/file-viewer/?pstid=41508"),
    ("Administração pública", "Provedor de Justiça, Recomendação 4/A/2013 (Síndrome de Diógenes)", "6.5.2013", "T",
     "Pede um guia para as autoridades de saúde nos casos de acumulação de animais, com articulação entre saúde, câmara, Ministério Público e tribunais.",
     "https://www.provedor-jus.pt/documentos/ambiente-salubridade-habitacao-acumulacao-de-residuos-saude-mental-sindrome-de-diogenes-004-a-2013/"),
    ("Administração pública", "Provedor de Justiça, Recomendação 82/A/96 (CM Oeiras)", "18.10.1996", "T",
     "Considera abusivo exigir a arrendatários de habitação social que prescindam dos animais. Citação: «Não se faça depender a celebração dos contratos de arrendamento de habitações a custos controladas do facto de os promitentes arrendatários prescindirem da posse dos seus animais domésticos».",
     "https://www.provedor-jus.pt/documentos/082A_96.pdf"),
    ("Administração pública", "Provedor de Justiça, anotação R4579/08 (CM Lajes do Pico)", "8.5.2009", "C",
     "A resposta a matilhas perigosas não é só municipal. Recomenda plano de ação coordenado entre câmara, forças de segurança e médico veterinário municipal.",
     "https://www.provedor-jus.pt/documentos/canideos-captura-alojamento-e-abate/"),
    # --- Medicos veterinarios municipais
    ("Médicos veterinários municipais", "Contributos dos MVM, reunião de Santarém", "6.3.2026", "T e C",
     "Pedem as figuras de cuidador, família de acolhimento temporário, fiel depositário e animal comunitário; um regime excecional de cães comunitários; responsabilização dos detentores de facto; enquadramento das colónias em quintais e do conflito entre cuidadores e vizinhos; clareza sobre responsabilidades entre associação titular e família de acolhimento. Um MVM pede coimas aos alimentadores; outro opõe-se ao CED.",
     "repositório: Contributos MVM.docx"),
    # --- Ordens e associacoes profissionais
    ("Ordens e associações profissionais", "OMV, parecer sobre abandono em centros veterinários", "nov. 2015", "T",
     "A lei é omissa sobre animais que os donos não vão buscar depois do tratamento. Propõe termo de responsabilidade com prazo a partir do qual se presume o abandono. Citação: «A legislação é omissa quanto à situação de animais abandonados, após tratamento, em CAMV's».",
     "https://www.omv.pt/dmdocuments/vi_formacao_omv/abandono_animais_camv_ultimoparecer_nov2015.pdf"),
    ("Ordens e associações profissionais", "OMV e SNMV, comentários nos documentos de trabalho do RGBEAC e do RGAC", "2025-2026", "T",
     "Prazo para comunicar desaparecimento: SNMV propõe 48 horas, OMV propõe 72 horas. SNMV opõe-se a registos provisórios no SIAC por gerarem dúvidas sobre a responsabilidade pelos atos do animal.",
     "repositório: Resumo_Comentarios_RGBEAC.docx"),
    ("Ordens e associações profissionais", "APMVEAC, revisão crítica da legislação", "9.4.2021", "T e C",
     "Critica que a lei ponha autarquias e sociedades zoófilas em pé de igualdade no abandono, sem definir estas últimas. Citação: «a lei pode estar a passar responsabilidades elevadas para um sector que os legisladores foram até agora incapazes de caracterizar e definir cabalmente.» Sobre a Portaria 146/2017, sugere rever a adoção de animais com menos de 6 meses sem esterilização.",
     "https://apmveac.pt/wp-content/uploads/2021/04/Legislacao.Animais.Companhia_09-04-2021-amarelo-final-.pdf"),
    ("Ordens e associações profissionais", "APMVEAC, parecer à ENAE", "set. 2023", "C",
     "Contra a dispersão de tutelas e contra o CED em cães. Diz que o enquadramento legal é parte do problema e que a eutanásia é ato clínico da responsabilidade exclusiva do médico veterinário.",
     "https://apmveac.pt/wp-content/uploads/2023/09/Parecer-APMVEAC-Consulta-Publica-ENAE.pdf"),
    # --- Juristas, academia e tribunais
    ("Juristas, academia e tribunais", "Teresa Quintela de Brito, «O abandono de animais de companhia», RJLB", "2019", "T",
     "O crime de abandono só pode ser cometido por quem já tem o dever de guardar, vigiar ou assistir o animal. Citação: «Não é possível a imputação de responsabilidade por estes crimes a associações ou sociedades zoófilas ou a quaisquer outras pessoas colectivas».",
     "https://www.cidp.pt/revistas/rjlb/2019/2/2019_02_0077_0095.pdf"),
    ("Juristas, academia e tribunais", "Tribunal da Relação de Coimbra, proc. 281/10.1TBCV.C1", "11.7.2012", "T",
     "O dever de vigilância do art. 493.º, n.º 1 do Código Civil decorre do poder de facto sobre o animal e não tem de recair sobre o dono.",
     "https://trc.pt/responsabilidade-civil-danos-causados-por-animais-dever-de-vigilancia/"),
    ("Juristas, academia e tribunais", "Tribunal da Relação de Lisboa, proc. 1642/24.4T8AMD.L1-8", "30.4.2025", "T",
     "O registo no SIAC pode relevar para presumir a propriedade, mas não afasta a prova da posse. O tribunal revogou uma decisão que se apoiava só no registo.",
     "https://www.dgsi.pt/jtrl.nsf/33182fc732316039802565fa00497eec/7462ba7a0546bac680258c8b0049a31e?OpenDocument"),
    ("Juristas, academia e tribunais", "Tribunal Constitucional, Acórdãos 70/2024 e 478/2024", "2024", "T",
     "Não julgam inconstitucionais os arts. 387.º e 388.º do Código Penal (maus-tratos e abandono), invertendo a jurisprudência anterior.",
     "https://www.tribunalconstitucional.pt/tc/acordaos/20240070.html"),
    # --- ONG
    ("ONG e associações de proteção animal", "ARPA, parecer sobre o DL 82/2019", "dez. 2022", "T e C",
     "Registar gatos de colónia em nome do cuidador torna-o responsável por animais que não controla, desincentiva a esterilização e cria falsas presunções de abandono. Defende o registo em nome do município nos CED municipais e que o CED é um dever legal dos municípios. Citação: «o que não podem é onerá-las com responsabilidades que além de não estarem legamente previstas, apenas as desencorajam a agir».",
     "https://www.arpa-associacao.pt/media/attachments/2022/12/14/parecer-arpa-versAo-4-final.pdf"),
    ("ONG e associações de proteção animal", "FEDRA, plano de políticas públicas", "2024", "C",
     "Diz que o microchip nos gatos de colónia não é viável na maioria dos casos e pede exceções. Propõe CED para cães e parques de matilhas.",
     "repositório: FEDRA - Plano de políticas públcias.pdf"),
    ("ONG e associações de proteção animal", "Movimento de Intervenção pelas Matilhas (Coimbra)", "s/d", "C",
     "Defende o CED em cães, com devolução ao território acompanhada por cuidadores, vacinação e microchip.",
     "https://matilhascoimbra.pt/pages/projecto-2"),
    # --- Partidos
    ("Partidos", "PAN", "2021 a 2025", "T e C",
     "Figura do animal comunitário (projeto aprovado na generalidade em 2021, caducado, retomado nos PJL 662/XV e 88/XVI). Estatuto da família de acolhimento temporário (2024). Critica o OE2026 por nenhum avanço para animais comunitários e matilhas.",
     "https://www.pan.com.pt/pan-destaca-vitorias-no-bem-estar-animal-mas-denuncia-retrocesso-grave-no-orcamento-do-estado-para-2026/"),
    ("Partidos", "PCP, proposta ao OE2026", "5.11.2025", "T e C",
     "Campanha nacional de esterilização com CED para cães não perigosos, registados no SIAC sem responsabilidade do município. Citação: «a título exclusivamente informativo, mediante a identificação genérica ‘Cães CED’ e com a exclusão das responsabilidades desses municípios inerentes à propriedade ou detenção desses animais».",
     "https://www.pcp.pt/campanha-nacional-de-esterilizacao-de-animais-errantes-0"),
    ("Partidos", "PCP", "12.11.2021", "C",
     "Contra criar novas figuras legais sem meios: a solução é a esterilização e uma rede pública de médicos veterinários.",
     "https://www.pcp.pt/solucao-prevencao-pela-esterilizacao-rede-publica-de-veterinarios-nao-abate-de-animais-abandonados"),
    ("Partidos", "Livre, programa eleitoral", "2024", "C",
     "Reforço dos CED e alargamento a cães errantes, valorização do animal comunitário, protocolos com associações com metas e financiamento.",
     "https://programa.partidolivre.pt/propostas/N.13/"),
    ("Partidos", "Respostas dos partidos (Maratona pelos Animais)", "mar. 2024", "C",
     "Sobre o CED em cães: PAN e BE a favor; Chega a favor em local circunscrito com cuidadores designados; CDU prudente por questões práticas e de responsabilidade civil; AD disponível para refletir; PS e IL não responderam.",
     "https://maratonapelosanimais.pt/wp-content/uploads/2024/03/respostas-completas.pdf"),
    # --- Municipios
    ("Municípios e ANMP", "Município do Fundão, Edital 145/2023: alimentação na via pública", "23.1.2023", "C",
     "O regulamento de colónias funciona como exceção a uma proibição geral de alimentar animais na via pública. Citação (art. 1.º, n.º 3): «O regime constante do presente regulamento constitui uma exceção à proibição geral de espalhar alimentos nas vias e noutros espaços públicos, suscetível de atrair animais errantes.» As despesas de manutenção e alimentação das colónias ficam a cargo do município (no regulamento da Moita ficam a cargo do cuidador).",
     "https://files.dre.pt/2s/2023/01/016000000/0033100335.pdf"),
    # --- Conservacao
    ("Conservação da natureza", "SPEA, parecer aos planos de gestão dos parques naturais dos Açores", "2020", "C",
     "Prioridade ao controlo de predadores introduzidos. Citação: «com prioridade para o controlo e esterilização de gatos (84% da predação é da responsabilidade dos gatos, Hervías et al., 2013)».",
     "https://www.spea.pt/wp-content/uploads/2020/09/ParecerSPEA_Planos-Gestao-Parques-Naturais-Ilha-2020.pdf"),
    ("Conservação da natureza", "SPEA", "27.12.2021", "C",
     "Recomenda gestão responsável dos gatos com dono, incluindo recolhimento noturno, para reduzir a predação de aves.",
     "https://spea.pt/um-gato-feliz-e-alimentado-mantem-o-passarinho-afastado/"),
    # --- Fontes documentais acrescentadas na versão 1.4
    ('Administração pública', 'Provedor de Justiça, Relatório à Assembleia da República 2023', '2024', 'C',
     'Queixas sobre sobrelotação dos CRO, falta de recolha de matilhas e colónias de gatos. Muitas colónias são afinal CED autorizados, sem divulgação pública. Citação: «Em muitos casos verifica-se estarem afinal em causa planos de gestão devidamente autorizados pelos serviços veterinários municipais, o que levanta a questão da falta da sua divulgação pública.»',
     'https://www.provedor-jus.pt/documentos/Relatorio%202023.pdf'),
    ('Administração pública', 'Provedor de Justiça, Relatório à Assembleia da República 2020', '2021', 'T e C',
     'Junta os errantes na via pública, o abandono e as campanhas da DGAV contra a alimentação de animais errantes. Citação: «a nossa preocupação tem a ver com a sobrepopulação, os animais errantes e o grave problema do abandono animal.»',
     'https://www.provedor-jus.pt/documentos/Relat2020%20_Relatorio.pdf'),
    ('Administração pública', 'Assembleia da República, nota técnica ao Projeto de Lei 88/XVI (animal comunitário)', '31.5.2024', 'C',
     'Enquadra a Lei 27/2016 e a Portaria 146/2017, lista as iniciativas anteriores e regista pareceres da ANAFRE e da ANMP. Citação: «Foram recebidos sobre o tema pareceres da Associação Nacional de Freguesias (ANAFRE) e da Associação Nacional de Municípios Portugueses (ANMP), disponíveis na página relativa a esta iniciativa.»',
     'https://app.parlamento.pt/webutils/docs/doc.pdf?path=6148523063484d364c793968636d356c6443397a6158526c63793959566b6c4d5a5763765130394e4c7a64445156426c6379394562324e31625756756447397a5357357059326c6864476c3259554e7662576c7a633246764c7a4d344d6d49795a5751334c574977597a59744e44457a596930354d574d794c544d354e446c684d445a6a4e474a6c597935775a47593d&fich=382b2ed7-b0c6-413b-91c2-3949a06c4bec.pdf&Inline=true'),
    ('Administração pública', 'ICNF, ENAE: famílias de acolhimento e cuidadores', '2023', 'T e C',
     'Reconhece que a família de acolhimento temporário e o estatuto de cuidador não estão regulados. Citação: «não se encontram regulados o conceito de “família de acolhimento temporário” de animais de companhia ou o estatuto de cuidador por forma a resultar clara a articulação entre estes e as entidades competentes.»',
     'https://www.icnf.pt/api/file/doc/41f8f44aee23be1a'),
    ('Organizações internacionais e União Europeia', 'Comissão Europeia, SWD(2024) 88 (síntese da evidência da proposta de regulamento sobre cães e gatos)', '27.3.2024', 'C',
     'Os animais errantes ficaram fora do âmbito da proposta que deu origem ao Regulamento (UE) 2026/1818, apesar de pedidos das ONG. A gestão de errantes e o CED continuam a ser matéria nacional. Citação: «Many NGOs also expressed their desire to include stray animals under the scope of any proposal regarding dogs and cats.» (Muitas ONG manifestaram também o desejo de incluir os animais errantes no âmbito de qualquer proposta relativa a cães e gatos.)',
     'https://food.ec.europa.eu/document/download/caf8cd1d-967a-4e60-a0e5-19401be1c6b3_en?filename=aw_awp_leg_dog-cat_swd-2024-88.pdf'),
    ('Organizações internacionais e União Europeia', 'WOAH, Código Sanitário dos Animais Terrestres, cap. 7.7 (gestão de populações de cães)', '10.6.2024', 'C e T',
     'Admite a captura, esterilização, vacinação e devolução de cães só como medida complementar, e nota que pode ser vista como abandono. Citação: «This method is not applicable in all situations and may be illegal in countries or regions where legislation prohibits the abandonment of dogs and authorities perceive the release of sterilised dogs as a form of abandonment.» (Este método não é aplicável em todas as situações e pode ser ilegal onde a lei proíba o abandono de cães e as autoridades considerem a libertação de cães esterilizados uma forma de abandono.)',
     'https://www.woah.org/fileadmin/Home/eng/Health_standards/tahc/2023/chapitre_aw_stray_dog.pdf'),
    ('Ordens e associações profissionais', 'OMV, parecer ao Projeto de Lei 662/XV (Of. 02/CD/2024)', '5.1.2024', 'T e C',
     'Parecer desfavorável ao animal comunitário, aos parques de matilhas e ao CED em cães. Citações: «O diluir da responsabilidade individual da detenção de um animal por vários indivíduos de uma comunidade conduz à desresponsabilização individual.» «A implementação dos programas CED em cães representa a normalização e legitimação da existência de cães na rua.»',
     'https://app.parlamento.pt/webutils/docs/doc.pdf?path=6148523063484d364c793968636d356c6443397a6158526c63793959566b786c5a793944543030764d5446445155564f5253394562324e31625756756447397a5357357059326c6864476c3259554e7662576c7a633246764c7a646c5a4746685a5749354c54466c4d4755744e4451305a4331684f544a6b4c57526c5a4464685a574e6a4f5467784d5335775a47593d&fich=7edaaeb9-1e0e-444d-a92d-ded7aecc9811.pdf&Inline=true'),
    ('Partidos', 'PAN, Projeto de Lei 662/XV (texto da iniciativa)', 'dez. 2023', 'C e T',
     'Propõe a figura do animal comunitário, com registo e guarda a cargo de uma pessoa ou de um grupo, sob supervisão da câmara municipal. Citação (nova al. ff)): «“Animal comunitário” qualquer animal, nomeadamente cães e gatos, autorizado a permanecer em espaço e via públicos limitados, a que o animal esteja habituado e onde esteja integrado, cujo registo, guarda, alimentação e cuidados médico-veterinários são assegurados por uma pessoa, singular ou coletiva, ou por um grupo de pessoas integradas numa comunidade local de moradores, residenciais ou profissionais, comunidades escolares ou entidades públicas, sob supervisão da Câmara Municipal.»',
     'https://app.parlamento.pt/webutils/docs/doc.pdf?path=6148523063484d364c793968636d356c6443397a6158526c63793959566b786c5a79394562324e31625756756447397a5357357059326c6864476c32595338774d44566d4d7a426c4e7931694d44557a4c54526c4e446b744f5455774d79316a4f5459794e544e6d4d47566a4e6a49755a47396a65413d3d&fich=005f30e7-b053-4e49-9503-c96253f0ec62.docx&Inline=true'),
    ('Juristas, academia e tribunais', 'Raúl Farias, em «Direito dos animais», e-book do CEJ', '2022', 'T',
     'O crime de abandono atinge quem detém o animal. As associações, como pessoas coletivas, não respondem criminalmente. Citações: «O agente do crime poderá ser todo aquele que tem o dever de guardar, vigiar ou assistir animal de companhia, o que coloca a esfera de punição normativa ao nível da detenção do animal.» «as pessoas coletivas não podem ser responsabilizadas criminalmente pela prática deste tipo de crime (art.º 11.º do Código Penal), o que afasta de imediato a imputação criminal de associações ou sociedades zoófilas […]»',
     'https://cej.justica.gov.pt/LinkClick.aspx?fileticket=VpuQj7jZ-us%3D&portalid=30'),
    ('Juristas, academia e tribunais', 'Cátia Simões (médica veterinária municipal), «O papel dos municípios na gestão do bem-estar animal», RJLB', '2019', 'T e C',
     'O abandono é difícil de provar e há situações que escapam à definição, como o animal não recolhido de um hotel ou de um CAMV e o depósito não consentido no CRO. Citação: «o abandono é uma ação difícil de comprovar, da qual até os infratores detetados em flagrante muitas vezes se conseguem escusar, esquivando-se assim ao pagamento da coima correspondente»',
     'https://www.cidp.pt/revistas/rjlb/2019/2/2019_02_0305_0348.pdf'),
    ('Juristas, academia e tribunais', 'Tribunal da Relação de Lisboa, proc. 3121/03.4TBCSC.L1-6', '24.11.2009', 'T',
     'O detentor tem um âmbito mais largo do que o proprietário. Citação do sumário: «a responsabilidade pelo risco recai sobre quem tiver a qualidade de “detentor do animal”, figura com um âmbito mais abrangente que a de “proprietário”; - “detentor” do animal é aquele em cuja casa o animal é albergado, não transitoriamente mas com um certo tempo de duração»',
     'https://jurisprudencia.pt/acordao/76412/'),
    ('Juristas, academia e tribunais', 'Supremo Tribunal de Justiça, proc. 478/05.6TBMGL.C1.S1', '14.11.2013', 'T',
     'Articula os arts. 493.º e 502.º do Código Civil: as duas responsabilidades podem coexistir. Citação do sumário: «O art. 493.º do CC tem em vista os animais que, por sua natureza, estão sujeitos à guarda e vigilância dos respectivos donos (ou de outrem sobre quem recaia tal obrigação).»',
     'https://jurisprudencia.pt/acordao/128487/'),
    ('Juristas, academia e tribunais', 'Tribunal da Relação de Coimbra, proc. 6/22.9GCPBL.C1', '7.2.2024', 'T',
     'O dever de vigilância cabe ao detentor. Citação do sumário: «Impende sobre o detentor de canídeo não classificado como perigoso o dever de o vigiar e assim evitar que ponha em risco a vida ou integridade física de outras pessoas ou animais.»',
     'https://jurisprudencia.pt/acordao/221373/'),
    ('Juristas, academia e tribunais', 'Tribunal Constitucional, Acórdão 867/2021', '10.11.2021', 'T',
     'Julgou inconstitucional o art. 387.º do Código Penal. É a decisão que os Acórdãos 70/2024 e 478/2024 vieram contrariar.',
     'https://www.tribunalconstitucional.pt/tc/acordaos/20210867.html'),
    ('Municípios e ANMP', 'Município do Fundão, Edital 145/2023 (Regulamento do Programa de Gestão das Colónias de Gatos)', '23.1.2023', 'C e T',
     'Modelo de cuidador registado, com termo de responsabilidade e supervisão do MVM. Citação (art. 4.º, n.º 1): «O cuidador registado é responsável pelo bem-estar dos gatos que integram a colónia ao seu cuidado, devendo assegurar a limpeza do local em que a sua manutenção é autorizada, bem como pela alimentação e a vigilância periódica dos mesmos.»',
     'https://files.dre.pt/2s/2023/01/016000000/0033100335.pdf'),
    ('Municípios e ANMP', 'Município da Moita, Regulamento 143/2025 (cuidador informal das colónias de gatos)', '23.1.2025', 'C e T',
     'A colónia e as despesas ficam a cargo do cuidador. Citação (art. 3.º, n.º 2): «As colónias autorizadas nos termos do presente regulamento são da responsabilidade dos respetivos cuidadores.»',
     'https://www.cm-moita.pt/cmmoita/uploads/writer_file/document/9889/regulamento_cuidador_informal.pdf'),
    ('Investigação científica', 'Gunther e outros, PNAS', '2022', 'C',
     'Estudo em Israel, à escala de uma cidade: o CED só reduz a população com esterilização intensa, contínua e em áreas contíguas. Citação: «We conclude that cat population management by TNR should be performed with high intensity, continuously, and in geographic contiguity to enable population reduction.» (Concluímos que a gestão da população de gatos por CED deve ser feita com alta intensidade, de forma contínua e em contiguidade geográfica, para permitir a redução da população.)',
     'https://pmc.ncbi.nlm.nih.gov/articles/PMC9169806/'),
    ('Investigação científica', 'Boone e outros, Frontiers in Veterinary Science 6:238', '2019', 'C',
     'Com baixa intensidade, as vantagens do CED desaparecem. Citação: «With sufficient intensity, management by TNR offers significant advantages in terms of combined lifesaving and population size reduction. At lower intensity levels, these advantages are greatly reduced or eliminated.» (Com intensidade suficiente, o CED traz vantagens claras em vidas salvas e redução da população. Com intensidade mais baixa, essas vantagens ficam muito reduzidas ou desaparecem.)',
     'https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2019.00238/full'),
    ('Investigação científica', 'Foley e outros, JAVMA 227(11)', '2005', 'C',
     'Em dois condados dos EUA, os programas CED não mostraram redução consistente do crescimento da população. Citação: «In both counties, results of analyses did not indicate a consistent reduction in per capita growth, the population multiplier, or the proportion of female cats that were pregnant.» (Em ambos os condados, as análises não mostraram redução consistente do crescimento per capita, do multiplicador populacional nem da proporção de gatas gestantes.)',
     'https://doi.org/10.2460/javma.2005.227.1775'),
    ('Investigação científica', 'Spehar e Wolf, Frontiers in Veterinary Science 6:77', '2019', 'C',
     'CED dirigido e devolução ao local reduziram as entradas de gatos e a eutanásia em seis abrigos municipais. Citação: «A median reduction of 32% in feline intake, as well as a median decline of 83% in feline euthanasia occurred across the six CCPs» (Redução mediana de 32% nas entradas de gatos e de 83% na eutanásia de gatos nos seis programas.)',
     'https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2019.00077/full'),
    ('Investigação científica', 'Azevedo e outros, Animals 15(6):771 (inquérito em Portugal)', '2025', 'C e T',
     'Inquérito com 1083 respostas em Portugal. Citação: «we found strong support for trap-neuter-release, sheltering, sanctions on abandonment, and educational campaigns.» (Encontrámos forte apoio ao CED, ao alojamento em abrigos, a sanções pelo abandono e a campanhas educativas.)',
     'https://pmc.ncbi.nlm.nih.gov/articles/PMC11939513/'),
    ('Conservação da natureza', 'Trouwborst e Somsen, Journal of Environmental Law 32(3)', '2020', 'C',
     'As Diretivas Aves e Habitats obrigam a controlar gatos sem dono que ameacem espécies ou sítios protegidos. Citação: «Regarding (unowned) stray and feral cats, these must be removed or controlled when they pose a threat to protected species and/or sites.» (Os gatos errantes e assilvestrados sem dono devem ser removidos ou controlados quando ameacem espécies ou sítios protegidos.)',
     'https://doi.org/10.1093/jel/eqz035'),
    ('Conservação da natureza', 'Galão e outros, Biological Conservation 305 (Madeira)', '2025', 'C',
     'Estudo na Madeira sobre a dieta de gatos em liberdade. Citação: «we found that cats consume over 20 distinct taxa from ten orders, including native and non-native prey, as well as taxa associated with anthropogenic food.» (Os gatos consomem mais de 20 taxa distintos de dez ordens, incluindo presas nativas e não nativas, e alimento de origem humana.)',
     'https://dspace.uevora.pt/rdpc/bitstream/10174/38522/1/Gal%C3%A3o%20et%20al_2025_When%20pets%20go%20wild.pdf'),
    ('Conservação da natureza', 'Loss, Will e Marra, Nature Communications 4:1396', '2013', 'C',
     'Nos EUA, os gatos sem dono causam a maior parte da mortalidade de fauna atribuída a gatos. Citação: «Un-owned cats, as opposed to owned pets, cause the majority of this mortality.» (São os gatos sem dono, e não os que têm dono, que causam a maior parte desta mortalidade.)',
     'https://www.nature.com/articles/ncomms2380'),
    ("Administração pública", "DGAV, proposta de resposta à MIAR", "24.10.2025", "C", "O CED depende de autorização da câmara municipal (Portaria 146/2017, art. 9.º, n.ºs 1 e 2) e não há contradição insanável com a Lei 27/2016, por a matéria dos errantes ser competência dos municípios (Código Administrativo, art. 49.º; Lei 75/2013, anexo I, art. 33.º, n.º 1, als. ii) e jj)). O CRO e as associações zoófilas podem ser titulares no SIAC, «podendo essa questão ficar definida nos referidos programas CED». Não analisa o art. 4.º da Lei 27/2016.", "repositório: CED/Proposta_resposta_DGAV_MIAR_2025-10-24.pdf"),
    ("ONG e associações de proteção animal", "MIAR, Movimento de Intervenção em Animais de Rua", "2024 e 2025", "C", "O CED é dever do Estado (Lei 27/2016, arts. 2.º, n.º 3, e 4.º) e a Portaria não o pode tornar facultativo. As associações não precisam de validação autárquica. Recusa ser titular de animais de rua e pede registo com indicação do município e da associação que esterilizou. Sem transponder, não pode candidatar as despesas aos avisos.", "repositório: CED/Proposta_resposta_DGAV_MIAR_2025-10-24.pdf"),
]

# Dominios de imprensa: o gerador recusa gerar se alguma fonte do Anexo B for destes dominios.
# As noticias ficam em pistas_imprensa_uso_interno.md, fora do memorando.
DOMINIOS_IMPRENSA = [
    "observador.pt", "publico.pt", "sapo.pt/artigo", "veterinaria-atual.pt", "lexpoint.pt",
    "greensavers.sapo.pt", "jornaleconomico", "tvi.iol.pt", "omirante.pt", "poligrafo.sapo.pt",
    "pit.nit.pt", "rtp.pt", "diariocoimbra.pt", "dn.pt", "jn.pt", "expresso.pt", "sabado.pt",
    "cmjornal.pt", "postal.pt", "interiordoavesso.pt", "gazetadascaldas.pt",
]

# Bibliografia. Cada entrada: (grupo, referência, ligação, palavra de controlo).
# A ligação é um URL ou «repositório: <ficheiro>». A palavra de controlo tem de aparecer no documento
# descarregado; serve a verificar_ligacoes.py. Vazia quando o sítio bloqueia pedidos automáticos.
BIBLIOGRAFIA = [
    # --- Legislação e regulamentos
    ("Legislação e regulamentos", "Código Civil, aprovado pelo Decreto-Lei n.º 47344/66, de 25 de novembro, versão em vigor.",
     "https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=775&tabela=leis", "47344"),
    ("Legislação e regulamentos", "Código Penal, aprovado pelo Decreto-Lei n.º 48/95, de 15 de março, versão em vigor.",
     "https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=109&tabela=leis", "48/95"),
    ("Legislação e regulamentos", "Decreto-Lei n.º 276/2001, de 17 de outubro (proteção dos animais de companhia), versão consolidada.",
     "https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=347&tabela=leis", "276/2001"),
    ("Legislação e regulamentos", "Decreto-Lei n.º 314/2003, de 17 de dezembro (Programa Nacional de Luta e Vigilância Epidemiológica da Raiva Animal e Outras Zoonoses), versão consolidada.",
     "https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=339&tabela=leis", "314/2003"),
    ("Legislação e regulamentos", "Decreto-Lei n.º 315/2009, de 29 de outubro (animais perigosos e potencialmente perigosos).",
     "https://diariodarepublica.pt/dr/detalhe/decreto-lei/315-2009-483402", ""),
    ("Legislação e regulamentos", "Lei n.º 27/2016, de 23 de agosto (rede de centros de recolha oficial e proibição do abate), Diário da República, 1.ª série, n.º 161.",
     "https://files.dre.pt/1s/2016/08/16100/0282702828.pdf", "centros de recolha"),
    ("Legislação e regulamentos", "Lei n.º 8/2017, de 3 de março (estatuto jurídico dos animais), Diário da República, 1.ª série, n.º 45.",
     "https://files.diariodarepublica.pt/1s/2017/03/04500/0114501149.pdf", "493"),
    ("Legislação e regulamentos", "Portaria n.º 146/2017, de 26 de abril (centros de recolha oficial e programas CED), Diário da República, 1.ª série, n.º 81.",
     "https://files.diariodarepublica.pt/1s/2017/04/08100/0205602059.pdf", "CED"),
    ("Legislação e regulamentos", "Decreto-Lei n.º 82/2019, de 27 de junho (Sistema de Informação de Animais de Companhia), versão consolidada.",
     "https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3093&tabela=leis", "82/2019"),
    ("Legislação e regulamentos", "Regulamento (UE) 2026/1818 do Parlamento Europeu e do Conselho, de 17 de junho de 2026, relativo ao bem-estar dos cães e dos gatos e à respetiva rastreabilidade, JO L, 10.8.2026.",
     "https://eur-lex.europa.eu/eli/reg/2026/1818/oj/por", "2026/1818"),
    ("Legislação e regulamentos", "Município do Fundão, Edital n.º 145/2023, Regulamento do Programa de Gestão das Colónias de Gatos, Diário da República, 2.ª série, n.º 16, 23.1.2023.",
     "https://files.dre.pt/2s/2023/01/016000000/0033100335.pdf", "cuidador registado"),
    ("Legislação e regulamentos", "Município da Moita, Regulamento n.º 143/2025, Regulamento do Cuidador Informal das Colónias de Gatos, Diário da República, 2.ª série, 23.1.2025.",
     "https://www.cm-moita.pt/cmmoita/uploads/writer_file/document/9889/regulamento_cuidador_informal.pdf", "cuidadores"),
    # --- Projetos e iniciativas legislativas
    ("Projetos e iniciativas legislativas", "Regime Geral do Animal de Companhia (RGAC), revisão formal DAJA V1, versão de trabalho revista pelo grupo em 30.6.2026, 18h00.",
     "repositório: RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO - Revisto 30-06-2026 18h00 Grupo.docx", ""),
    ("Projetos e iniciativas legislativas", "Regime Geral do Bem-Estar dos Animais de Companhia (RGBEAC), proposta de junho de 2025.",
     "repositório: RGBEAC_junh_2025 Original com Índice.docx", ""),
    ("Projetos e iniciativas legislativas", "RGBEAC, versão comentada de 19.2.2026.",
     "repositório: rgbeac 19.2.2026 (002).docx", ""),
    ("Projetos e iniciativas legislativas", "ICNF (2021). Projeto de alteração da Portaria n.º 146/2017, enviado à ANMP.",
     "https://anmp.pt/file-viewer/?pstid=41508", "146/2017"),
    ("Projetos e iniciativas legislativas", "PAN (2023). Projeto de Lei n.º 662/XV/1.ª, reconhece a figura do animal comunitário.",
     "https://app.parlamento.pt/webutils/docs/doc.pdf?path=6148523063484d364c793968636d356c6443397a6158526c63793959566b786c5a79394562324e31625756756447397a5357357059326c6864476c32595338774d44566d4d7a426c4e7931694d44557a4c54526c4e446b744f5455774d79316a4f5459794e544e6d4d47566a4e6a49755a47396a65413d3d&fich=005f30e7-b053-4e49-9503-c96253f0ec62.docx&Inline=true", "animal comunitário"),
    ("Projetos e iniciativas legislativas", "Assembleia da República (2024). Nota técnica ao Projeto de Lei n.º 88/XVI/1.ª (PAN), 31.5.2024.",
     "https://app.parlamento.pt/webutils/docs/doc.pdf?path=6148523063484d364c793968636d356c6443397a6158526c63793959566b6c4d5a5763765130394e4c7a64445156426c6379394562324e31625756756447397a5357357059326c6864476c3259554e7662576c7a633246764c7a4d344d6d49795a5751334c574977597a59744e44457a596930354d574d794c544d354e446c684d445a6a4e474a6c597935775a47593d&fich=382b2ed7-b0c6-413b-91c2-3949a06c4bec.pdf&Inline=true", "88/XVI"),
    # --- Documentos oficiais, estratégias e relatórios
    ("Documentos oficiais, estratégias e relatórios", "ICNF (2023). Estratégia Nacional para os Animais Errantes (ENAE), versão submetida a consulta pública.",
     "https://www.icnf.pt/api/file/doc/41f8f44aee23be1a", "Errantes"),
    ("Documentos oficiais, estratégias e relatórios", "DGAV (2021). Relatório final do Grupo de Trabalho para o Bem-Estar Animal: avaliação da implementação da Lei n.º 27/2016.",
     "https://www.dgav.pt/wp-content/uploads/2021/08/Relatorio-FINAL-avaliacao-da-implementacao-da-Lei-27-2016.pdf", "27/2016"),
    ("Documentos oficiais, estratégias e relatórios", "Provedor de Justiça (1996). Recomendação n.º 82/A/96, à Câmara Municipal de Oeiras, 18.10.1996.",
     "https://www.provedor-jus.pt/documentos/082A_96.pdf", "Oeiras"),
    ("Documentos oficiais, estratégias e relatórios", "Provedor de Justiça (2009). Canídeos: captura, alojamento e abate, anotação ao processo R4579/08 (Câmara Municipal das Lajes do Pico), 8.5.2009.",
     "https://www.provedor-jus.pt/documentos/canideos-captura-alojamento-e-abate/", "Lajes"),
    ("Documentos oficiais, estratégias e relatórios", "Provedor de Justiça (2013). Recomendação n.º 4/A/2013, acumulação de resíduos e animais (síndrome de Diógenes), 6.5.2013.",
     "https://www.provedor-jus.pt/documentos/ambiente-salubridade-habitacao-acumulacao-de-residuos-saude-mental-sindrome-de-diogenes-004-a-2013/", "Diógenes"),
    ("Documentos oficiais, estratégias e relatórios", "Provedor de Justiça (2021). Relatório à Assembleia da República 2020.",
     "https://www.provedor-jus.pt/documentos/Relat2020%20_Relatorio.pdf", "abandono animal"),
    ("Documentos oficiais, estratégias e relatórios", "Provedor de Justiça (2024). Relatório à Assembleia da República 2023.",
     "https://www.provedor-jus.pt/documentos/Relatorio%202023.pdf", "divulgação pública"),
    ("Documentos oficiais, estratégias e relatórios", "Comissão Europeia (2024). Commission Staff Working Document SWD(2024) 88 final, Summarising evidence supporting the legislative proposal on the welfare of dogs and cats and their traceability, 27.3.2024.",
     "https://food.ec.europa.eu/document/download/caf8cd1d-967a-4e60-a0e5-19401be1c6b3_en?filename=aw_awp_leg_dog-cat_swd-2024-88.pdf", "stray"),
    ("Documentos oficiais, estratégias e relatórios", "WOAH (2024). Terrestrial Animal Health Code, capítulo 7.7, Dog population management.",
     "https://www.woah.org/fileadmin/Home/eng/Health_standards/tahc/2023/chapitre_aw_stray_dog.pdf", "abandonment"),
    # --- Pareceres
    ("Pareceres de ordens, associações e ONG", "Ordem dos Médicos Veterinários (2015). Parecer sobre o abandono de animais em centros de atendimento médico-veterinário, novembro de 2015.",
     "https://www.omv.pt/dmdocuments/vi_formacao_omv/abandono_animais_camv_ultimoparecer_nov2015.pdf", "abandono"),
    ("Pareceres de ordens, associações e ONG", "Ordem dos Médicos Veterinários (2024). Parecer sobre o Projeto de Lei n.º 662/XV/1.ª (PAN), Of. n.º 02/CD/2024, 5.1.2024.",
     "https://app.parlamento.pt/webutils/docs/doc.pdf?path=6148523063484d364c793968636d356c6443397a6158526c63793959566b786c5a793944543030764d5446445155564f5253394562324e31625756756447397a5357357059326c6864476c3259554e7662576c7a633246764c7a646c5a4746685a5749354c54466c4d4755744e4451305a4331684f544a6b4c57526c5a4464685a574e6a4f5467784d5335775a47593d&fich=7edaaeb9-1e0e-444d-a92d-ded7aecc9811.pdf&Inline=true", "desresponsabilização"),
    ("Pareceres de ordens, associações e ONG", "APMVEAC (2021). Revisão crítica da legislação sobre animais de companhia, 9.4.2021.",
     "https://apmveac.pt/wp-content/uploads/2021/04/Legislacao.Animais.Companhia_09-04-2021-amarelo-final-.pdf", "companhia"),
    ("Pareceres de ordens, associações e ONG", "APMVEAC (2023). Parecer à consulta pública da Estratégia Nacional para os Animais Errantes, setembro de 2023.",
     "https://apmveac.pt/wp-content/uploads/2023/09/Parecer-APMVEAC-Consulta-Publica-ENAE.pdf", "ENAE"),
    ("Pareceres de ordens, associações e ONG", "ARPA (2022). Parecer sobre o Decreto-Lei n.º 82/2019, dezembro de 2022.",
     "https://www.arpa-associacao.pt/media/attachments/2022/12/14/parecer-arpa-versAo-4-final.pdf", "82/2019"),
    ("Pareceres de ordens, associações e ONG", "SPEA (2020). Parecer aos planos de gestão dos parques naturais de ilha dos Açores.",
     "https://www.spea.pt/wp-content/uploads/2020/09/ParecerSPEA_Planos-Gestao-Parques-Naturais-Ilha-2020.pdf", "gato"),
    ("Pareceres de ordens, associações e ONG", "SPEA (2021). Um gato feliz e alimentado mantém o passarinho afastado?, 27.12.2021.",
     "https://spea.pt/um-gato-feliz-e-alimentado-mantem-o-passarinho-afastado/", "gato"),
    ("Pareceres de ordens, associações e ONG", "FEDRA (2024). Plano de políticas públicas.",
     "repositório: FEDRA - Plano de políticas públcias.pdf", ""),
    ("Pareceres de ordens, associações e ONG", "Movimento de Intervenção pelas Matilhas (Coimbra). Projeto.",
     "https://matilhascoimbra.pt/pages/projecto-2", "atilha"),
    # --- Partidos
    ("Partidos", "PAN (2025). PAN destaca vitórias no bem-estar animal, mas denuncia retrocesso grave no Orçamento do Estado para 2026.",
     "https://www.pan.com.pt/pan-destaca-vitorias-no-bem-estar-animal-mas-denuncia-retrocesso-grave-no-orcamento-do-estado-para-2026/", "Orçamento"),
    ("Partidos", "PCP (2021). Solução: prevenção pela esterilização, rede pública de veterinários, não abate de animais abandonados, 12.11.2021.",
     "https://www.pcp.pt/solucao-prevencao-pela-esterilizacao-rede-publica-de-veterinarios-nao-abate-de-animais-abandonados", "esteriliza"),
    ("Partidos", "PCP (2025). Campanha nacional de esterilização de animais errantes, proposta ao Orçamento do Estado para 2026, 5.11.2025.",
     "https://www.pcp.pt/campanha-nacional-de-esterilizacao-de-animais-errantes-0", "esteriliza"),
    ("Partidos", "Livre (2024). Programa eleitoral, proposta N.13.",
     "https://programa.partidolivre.pt/propostas/N.13/", "nima"),
    ("Partidos", "Maratona pelos Animais (2024). Respostas completas dos partidos, março de 2024.",
     "https://maratonapelosanimais.pt/wp-content/uploads/2024/03/respostas-completas.pdf", "CED"),
    # --- Doutrina
    ("Doutrina", "Brito, Teresa Quintela de (2019). O abandono de animais de companhia. Revista Jurídica Luso-Brasileira, ano 5, n.º 2, pp. 77-95.",
     "https://www.cidp.pt/revistas/rjlb/2019/2/2019_02_0077_0095.pdf", "abandono"),
    ("Doutrina", "Simões, Cátia (2019). O papel dos municípios na gestão do bem-estar animal: desafios legais e gestão municipal. Revista Jurídica Luso-Brasileira, ano 5, n.º 2, pp. 305-348.",
     "https://www.cidp.pt/revistas/rjlb/2019/2/2019_02_0305_0348.pdf", "comprovar"),
    ("Doutrina", "Araújo, Fernando; Marinho, Carlos; Farias, Raúl; Sousa, Susana Aires de; Dias, Cristina (2022). Direito dos animais. Lisboa: Centro de Estudos Judiciários, coleção Formação Contínua.",
     "https://cej.justica.gov.pt/LinkClick.aspx?fileticket=VpuQj7jZ-us%3D&portalid=30", "detenção do animal"),
    # --- Jurisprudência
    ("Jurisprudência", "Tribunal da Relação de Lisboa, acórdão de 24.11.2009, proc. 3121/03.4TBCSC.L1-6.",
     "https://jurisprudencia.pt/acordao/76412/", "detentor"),
    ("Jurisprudência", "Tribunal da Relação de Coimbra, acórdão de 11.7.2012, proc. 281/10.1TBCV.C1.",
     "https://trc.pt/responsabilidade-civil-danos-causados-por-animais-dever-de-vigilancia/", "vigilância"),
    ("Jurisprudência", "Supremo Tribunal de Justiça, acórdão de 14.11.2013, proc. 478/05.6TBMGL.C1.S1.",
     "https://jurisprudencia.pt/acordao/128487/", "493"),
    ("Jurisprudência", "Tribunal Constitucional, Acórdão n.º 867/2021, de 10.11.2021.",
     "https://www.tribunalconstitucional.pt/tc/acordaos/20210867.html", "inconstitucional"),
    ("Jurisprudência", "Tribunal Constitucional, Acórdão n.º 70/2024, de 23.1.2024 (Plenário).",
     "https://www.tribunalconstitucional.pt/tc/acordaos/20240070.html", "387"),
    ("Jurisprudência", "Tribunal da Relação de Coimbra, acórdão de 7.2.2024, proc. 6/22.9GCPBL.C1.",
     "https://jurisprudencia.pt/acordao/221373/", "canídeo"),
    ("Jurisprudência", "Tribunal Constitucional, Acórdão n.º 478/2024, de 20.6.2024.",
     "https://www.tribunalconstitucional.pt/tc/acordaos/20240478.html", "388"),
    ("Jurisprudência", "Tribunal da Relação de Lisboa, acórdão de 30.4.2025, proc. 1642/24.4T8AMD.L1-8.",
     "https://www.dgsi.pt/jtrl.nsf/33182fc732316039802565fa00497eec/7462ba7a0546bac680258c8b0049a31e?OpenDocument", "1642/24"),
    # --- Artigos científicos
    ("Artigos científicos", "Loss, S. R.; Will, T.; Marra, P. P. (2013). The impact of free-ranging domestic cats on wildlife of the United States. Nature Communications, 4, 1396.",
     "https://www.nature.com/articles/ncomms2380", "Un-owned"),
    ("Artigos científicos", "Foley, P.; Foley, J. E.; Levy, J. K.; Paik, T. (2005). Analysis of the impact of trap-neuter-return programs on populations of feral cats. Journal of the American Veterinary Medical Association, 227(11), 1775-1781.",
     "https://doi.org/10.2460/javma.2005.227.1775", "feral cats"),
    ("Artigos científicos", "Boone, J. D. e outros (2019). A long-term lens: cumulative impacts of free-roaming cat management strategy and intensity on preventable cat mortalities. Frontiers in Veterinary Science, 6, 238.",
     "https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2019.00238/full", "intensity"),
    ("Artigos científicos", "Spehar, D. D.; Wolf, P. J. (2019). Integrated return-to-field and targeted trap-neuter-vaccinate-return programs result in reductions of feline intake and euthanasia at six municipal animal shelters. Frontiers in Veterinary Science, 6, 77.",
     "https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2019.00077/full", "intake"),
    ("Artigos científicos", "Trouwborst, A.; Somsen, H. (2020). Domestic cats (Felis catus) and European nature conservation law. Journal of Environmental Law, 32(3), 391-415.",
     "https://doi.org/10.1093/jel/eqz035", ""),
    ("Artigos científicos", "Gunther, I.; Hawlena, H.; Azriel, L.; Gibor, D.; Berke, O.; Klement, E. (2022). Reduction of free-roaming cat population requires high-intensity neutering in spatial contiguity to mitigate compensatory effects. Proceedings of the National Academy of Sciences, 119(15).",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC9169806/", "contiguity"),
    ("Artigos científicos", "Azevedo, A. e outros (2025). Social perceptions and attitudes towards free-roaming cats and dogs in Portugal: an exploratory study. Animals, 15(6), 771.",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC11939513/", "trap-neuter"),
    ("Artigos científicos", "Galão, M.; Soto, I.; Nunes, M.; Pedroso, N. M.; Rocha, R.; Rato, C. (2025). When pets go wild: integrating DNA metabarcoding and morphological analyses to investigate the impacts of free-ranging cats (Felis catus) on oceanic islands. Biological Conservation, 305, 111089.",
     "https://dspace.uevora.pt/rdpc/bitstream/10174/38522/1/Gal%C3%A3o%20et%20al_2025_When%20pets%20go%20wild.pdf", "distinct taxa"),
    ("Legislação e regulamentos", "Lei n.º 75/2013, de 12 de setembro (regime jurídico das autarquias locais), versão consolidada.", "https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1990&tabela=leis", "75/2013"),
    ("Legislação e regulamentos", "Município de Setúbal, Regulamento de Saúde e Bem-Estar Animal (RSBEAMS), aprovado pela Assembleia Municipal em 26.6.2020.", "https://www.mun-setubal.pt/wp-content/uploads/2020/07/RSBEAMS-2020.pdf", "CROAC"),
    ("Legislação e regulamentos", "Município de Coimbra, Aviso n.º 6348/2023, Diário da República, 2.ª série, n.º 61, de 27.3.2023.", "https://files.diariodarepublica.pt/gratuitos/2s/2023/03/2S061A0000S00.pdf", "Termo de Entrega"),
    ("Jurisprudência", "Tribunal da Relação do Porto, acórdão de 8.5.2024, proc. 11/21.2GEVFR.P1.", "https://www.dgsi.pt/jtrp.nsf/56a6e7121657f91e80257cda00381fdf/703e8b815ea39ece80258b34004b8157", "11/21.2GEVFR.P1"),
    ("Projetos e iniciativas legislativas", "Projeto de Lei n.º 612/XVII/1.ª (Bloco de Esquerda), de 5.5.2026: acorrentamento, alojamento, dispositivos coercivos e Plano Nacional pelo Bem-Estar dos Animais de Companhia.", "repositório: Projetos de lei/PJL 612-XVII BE - acorrentamento e dispositivos coercivos.pdf", ""),
    ("Documentos oficiais, estratégias e relatórios", "DGAV, proposta de resposta à MIAR sobre esterilizações CED em concelhos sem programa, 24.10.2025, com a correspondência da MIAR de 3.12.2024 a 21.10.2025 e a resposta da Direção de Serviços de 20.10.2025.", "repositório: CED/Proposta_resposta_DGAV_MIAR_2025-10-24.pdf", ""),
    # --- Documentos internos
    ("Documentos de trabalho do grupo", "Contributos dos médicos veterinários municipais, reunião de Santarém, 6.3.2026.",
     "repositório: Contributos MVM.docx", ""),
    ("Documentos de trabalho do grupo", "Resumo dos comentários ao RGBEAC (OMV, SNMV, DAJA e outros revisores).",
     "repositório: Resumo_Comentarios_RGBEAC.docx", ""),
]

REGISTO_ALTERACOES = [
    ("1", "25.9.2026", "Primeira versão. Tema T (18 fichas) e tema C (17 fichas). Anexo B com posições de entidades externas recolhidas no repositório e online."),
    ("1.1", "25.9.2026", "Correção de formatação: larguras fixas das colunas em todas as tabelas; anexos A e B em páginas na horizontal. Sem alterações de conteúdo."),
    ("1.2", "25.9.2026", "Correção das tabelas: as propriedades de largura estavam fora da ordem exigida pelo Word e eram ignoradas. Ficheiro validado contra o esquema. Sem alterações de conteúdo."),
    ("1.3", "25.9.2026", "Fontes: as posições conhecidas só pela imprensa passam para uma nota no fim do Anexo B e ficam marcadas nas fichas com «fonte: imprensa». A tabela principal do Anexo B fica reservada a documentos. Nenhuma posição foi retirada."),
    ("1.4", "25.9.2026", "Anexo B: 24 entradas novas com base em documentos lidos (relatórios do Provedor de Justiça 2020 e 2023, nota técnica da AR, SWD(2024) 88 da Comissão Europeia, WOAH, parecer da OMV ao PJL 662/XV, e-book do CEJ, RJLB, acórdãos do STJ, TRL, TRC e TC, regulamentos do Fundão e da Moita, artigos científicos sobre CED e predação). Novos grupos: Organizações internacionais e União Europeia; Investigação científica. Fichas T-06, T-13, T-14, T-16, T-18, C-01, C-02, C-03, C-05, C-06, C-09 e C-11 com fontes documentais acrescentadas."),
    ("1.5", "27.9.2026", "Retiradas do memorando todas as notícias de imprensa: 26 entradas do Anexo B, 20 referências nas fichas e uma frase da ficha C-17. O Anexo B passa a ter só fontes documentais."),
    ("1.6", "27.9.2026", "Bibliografia no fim do documento, por tipo de fonte, com ligações clicáveis, verificadas uma a uma. O Anexo C (Fontes) passa para a bibliografia. Corrigidas as ligações do parlamento, de artigos científicos e da Universidade de Évora. A entrada sobre regulamentos municipais de Oeiras e outros foi substituída pelo Edital 145/2023 do Fundão, por não ser possível verificar a fonte."),
    ("1.7", "27.9.2026", "Estrutura para a revisão do RGAC inteiro: um tema por capítulo, com letra própria; Anexo C com lapsos formais (L-01 a L-09, dos quais cinco novos: artigos 81.º e 142.º repetidos, segundo art. 142.º fora do lugar, subsecção com epígrafe que não corresponde, numeração de secções nos caps. IV e X); Anexo D com a cobertura da revisão artigo a artigo."),
    ("1.8", "27.9.2026", "O memorando passa a ser mantido em três versões com o mesmo conteúdo: a principal (esta) e os ensaios 2.0 e 3.0 de organização. Lapso L-08: a remissão do art. 86.º, n.º 1 passa a citar «artigos 65.º e 66.º» entre aspas, como está no RGAC."),
    ("1.9", "2.10.2026", "Ficha T-19: nada diz quem é titular quando o animal não tem proprietário. A definição da al. f) do art. 3.º do DL 82/2019 pressupõe dono ou possuidor com animus, e o RGAC só fecha a lacuna no CED. A ficha qualifica a proposta da T-01: repor o critério do DL 82/2019 não resolve o animal sem dono."),
    ("1.10", "8.10.2026", "Recolha de errantes por particulares e estatuto de quem acolhe. Fichas novas: T-20 (quem acolhe um animal errante pode ficar sem saída lícita), C-18 (a definição de animal errante passa a abranger qualquer animal não identificado) e C-19 (a Lei 75/2013 ainda atribui às câmaras o abate de canídeos e gatídeos). Fichas T-14 e T-15 completadas: o RGAC omite a entrega pelo particular prevista no n.º 2 do art. 7.º da Portaria 146/2017, torna a captura exclusiva das câmaras e tem duas alíneas contraditórias no art. 140.º, n.º 2. Fontes novas: Lei 75/2013, regulamentos de Setúbal e Coimbra, acórdão do TRP de 8.5.2024."),
    ("1.11", "8.10.2026", "Fichas novas P-01 (a amarração no domicílio fica sem duração máxima nem requisitos verificáveis, com a condenação confirmada pelo TRP em 8.5.2024 por amarração diária de um cão) e A-01 (duas normas diferentes sobre que espécies são animais de companhia, arts. 2.º e 4.º). Lapso L-10 no art. 19.º. Acórdão do TRP de 8.5.2024 acrescentado às fichas T-03, T-04 e T-13. Bibliografia: Projeto de Lei n.º 612/XVII/1.ª."),
    ("1.12", "9.10.2026", "Fichas C-01 e C-08 completadas com a proposta de resposta da DGAV à MIAR (24.10.2025): não analisa o art. 4.º da Lei 27/2016 e admite que o CRO ou a associação sejam titulares dos gatos CED, ao contrário da nota jurídica sobre a titularidade e do RGAC. Anexo B: posições da DGAV (24.10.2025) e da MIAR. O Projeto de Lei n.º 612/XVII/1.ª passa para o grupo de projetos e iniciativas legislativas da bibliografia."),
    ("1.13", "9.10.2026", "Ficha C-01: a proposta passa a registar a posição desta análise. A leitura que trata o CED como mera faculdade municipal, adotada pela DGAV nas respostas à MIAR de 20.10.2025 e 24.10.2025, é um erro de interpretação face ao art. 4.º da Lei 27/2016 e ao art. 143.º, n.º 1 do CPA."),
]
