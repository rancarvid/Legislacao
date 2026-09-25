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

VERSAO_MEMORANDO = "1.2"
DATA_MEMORANDO = "25.9.2026"
VERSAO_RGAC = ("RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO - Revisto 30-06-2026 18h00 Grupo.docx "
               "(revisão formal DAJA V1, revista pelo grupo em 30.6.2026, 18h00)")

# Valores admitidos
ORIGENS = {
    "RGAC": "Criado pelo RGAC",
    "VIGENTE": "Já existia no regime vigente e o RGAC não resolve",
    "PARCIAL": "Já existia; o RGAC resolve em parte",
}
ESTADOS = ("Aberto", "Parcialmente resolvido", "Resolvido")

INTRODUCAO = [
    "Este memorando serve para acompanhar o trabalho sobre o RGAC. Regista os problemas que vamos "
    "encontrando no texto, os que já existem na legislação em vigor e continuam por resolver, e as "
    "críticas feitas por entidades externas. É um documento vivo: cada nova versão acrescenta fichas "
    "ou muda o estado das que já existem.",
    "Cada problema tem uma ficha com um código fixo. As fichas do tema titular, detentor, proprietário e "
    "operador começam por T. As fichas dos programas CED, colónias e animais errantes começam por C. "
    "Os códigos não se reutilizam. Quando um problema fica resolvido, a ficha mantém-se com o estado "
    "Resolvido.",
    "As referências a artigos são sempre à versão do RGAC indicada acima, salvo indicação em contrário. "
    "A legislação vigente citada foi confirmada online (DRE e PGDL), na pasta Legislação vigente e nos "
    "ficheiros do repositório.",
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
            "levantado": ["Acórdão do TRL de 30.4.2025", "Análise interna", "PCP, proposta ao OE2026 (registo informativo sem responsabilidade, 5.11.2025)"],
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
            ],
            "proposta": "Art. 76.º, n.º 2: «O titular e o detentor, ou os seus representantes, devem comunicar a "
                        "morte ou o desaparecimento do animal de companhia ao SIAC […]».",
            "levantado": ["Análise interna"],
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
            "levantado": ["Análise interna", "Teresa Quintela de Brito, RJLB 2019 (o crime de abandono só abrange quem já tem dever de guarda)"],
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
            "levantado": ["Contributos dos médicos veterinários municipais (6.3.2026)", "Tribunal da Relação de Coimbra, proc. 281/10.1TBCV.C1 (11.7.2012)", "Tribunal da Relação do Porto (11.11.2024)", "CDU (resposta de 2024)"],
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
            ],
            "proposta": "Decidir se a família de acolhimento informal fica proibida ou se passa a ter um registo "
                        "simples no SIAC, como detentor, com limite de animais e dever de comunicação.",
            "levantado": ["Estratégia Nacional para os Animais Errantes (ENAE), pp. 30-31",
                          "Contributos dos médicos veterinários municipais (6.3.2026)", "PAN (estatuto da família de acolhimento, 2024)", "Iniciativa Liberal (programa 2024)", "SNMV (contra registos provisórios no SIAC)"],
            "estado": "Parcialmente resolvido",
            "rel": ["T-13", "C-02"],
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
            ],
            "proposta": "Articular o art. 91.º, n.º 9 com o art. 1323.º do Código Civil: permitir a guarda "
                        "provisória pelo achador, com dever de comunicação e leitura do transponder num prazo curto.",
            "levantado": ["Análise interna"],
            "estado": "Aberto",
            "rel": ["C-02", "C-16"],
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
            "levantado": ["Contributos dos médicos veterinários municipais (6.3.2026)", "ANVETEM (falta de regulação das entidades privadas de proteção animal, 2020)"],
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
            "levantado": ["OMV, parecer sobre abandono de animais em centros veterinários (nov. 2015)"],
            "estado": "Aberto",
            "rel": ["T-05", "T-06"],
        },
    ],
}

# ---------------------------------------------------------------------------
# Tema C: programas CED, colonias e animais errantes
# ---------------------------------------------------------------------------
TEMA_C = {
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
            ],
            "proposta": "Manter pelo menos o nível da Lei 27/2016: «as câmaras municipais asseguram, diretamente ou "
                        "por protocolo, programas CED para gatos, sempre que se justifique».",
            "levantado": ["ENAE, p. 35 («Os programas CED não estão instituídos em todo o território»)",
                          "Livre e PAN (respostas de 2024)", "ARPA (o CED é dever legal dos municípios, dez. 2022)", "Chega (programa 2024)", "Animais de Rua (18.11.2024)"],
            "estado": "Aberto",
            "rel": ["C-02"],
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
                          "PAN (figura do animal comunitário, PJL 662/XV)", "BE, Chega e Livre (animal comunitário, programas 2024)", "Assembleia Municipal de Coimbra (regulamento de cuidadores, 30.6.2026)", "Câmara Municipal do Porto (gestão diária pelas associações, 2021)"],
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
                          "alimentadores, posição contrária)", "Regulamentos municipais de Lisboa, Porto, Oeiras, Cascais e outros (excecionam cuidadores registados)"],
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
            "levantado": ["Relatório final do GTBEA (DGAV, 2021)", "Projeto de revisão da Portaria 146/2017 (ANMP, 2021)", "ANMP (2018)", "Provedora do Animal (cerca de 80 mil animais nos CRO, 25.10.2023)"],
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
            "levantado": ["OMV (25.11.2025)", "APMVEAC (parecer set. 2023)", "PAN e BE (2024)",
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
            ],
            "proposta": "Definir as duas entidades no art. 3.º ou no próprio art. 86.º, e dizer que o município, "
                        "como titular, responde nos termos gerais, com direito de regresso sobre a entidade responsável.",
            "levantado": ["CDU (resposta de 2024)", "Análise interna", "Câmara Municipal do Porto (2021)", "PCP (proposta ao OE2026)", "ARPA (dez. 2022)"],
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
                          "colónias»)", "ENAE, §33 (número de registo nacional da colónia)", "Assembleia Municipal de Coimbra (mapeamento georreferenciado, 30.6.2026)", "Provedoria dos Animais de Lisboa (sinalização de colónias, 10.9.2024)"],
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
            "levantado": ["SPEA", "RGBEAC (jun. 2025), art. 44.º, n.º 3", "SPEA, parecer Açores 2020 (84% da predação de cagarros por gatos)", "Projeto de alteração da Portaria 146/2017 (articulação com o ICNF)"],
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
                          "Inventário interno de zonas cinzentas do CED (zona 20)", "DGAV (140 médicos veterinários reconhecidos para 138 municípios, 8.1.2026)", "OMV (cerca de 45% dos municípios com médico veterinário municipal, 22.8.2026)", "Provedoria dos Animais de Lisboa (9.1.2026)", "PCP (2021)", "ANMP (OE2025 sem verbas próprias para CRO)"],
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
                "A Provedora do Animal diz que os dados anuais não permitem definir políticas.",
            ],
            "proposta": "Fixar os dados mínimos (colónias, número de gatos esterilizados, capturas, entradas e saídas "
                        "do CRO), retirá-los do SIAC sempre que possível e ligar o acesso a apoios públicos à entrega "
                        "do plano.",
            "levantado": ["Comentário do grupo de trabalho ao art. 85.º («prever sanções para os Municípios que não "
                          "informam a DGAV»)", "Provedora do Animal (25.10.2023)", "Paulo Afonso (21.4.2026)"],
            "estado": "Aberto",
            "rel": ["C-09"],
        },
    ],
}

# ---------------------------------------------------------------------------
# Pontos ja resolvidos pelo RGAC (para registo)
# ---------------------------------------------------------------------------
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
    ("Administração pública", "DGAV, diretora-geral (audição na Comissão de Agricultura)", "8.1.2026", "C",
     "Defende que todos os concelhos tenham autoridade sanitária veterinária concelhia. Indica 140 médicos veterinários reconhecidos para 138 municípios.",
     "https://sapo.pt/artigo/diretora-da-dgav-defende-que-todos-os-municipios-tenham-medico-veterinario-concelhio-69600006ab728f90f0c5c2cf"),
    ("Administração pública", "Provedora do Animal (audição parlamentar)", "25.10.2023", "C",
     "Cerca de 80 mil animais a viver nos CRO, com tendência para 100 mil, e custos muito elevados. Os dados anuais não permitem definir políticas.",
     "https://observador.pt/2023/10/25/ha-80-000-animais-habitantes-nos-centros-de-recolha-alerta-provedora-do-animal/"),
    ("Administração pública", "Provedora do Animal", "24.7.2026", "C",
     "Defende a esterilização obrigatória com vales de livre escolha do centro veterinário e equipas nacionais de resgate.",
     "https://www.veterinaria-atual.pt/na-gestao/word-spay-day-esterilizacao/"),
    ("Administração pública", "Provedoria dos Animais de Lisboa", "9.1.2026", "C",
     "Recomenda a nomeação do médico veterinário municipal em Lisboa, que não existe. Sem ele ficam comprometidos a direção técnica do CRO, o destino dos animais e o parecer exigido para os CED.",
     "https://www.veterinaria-atual.pt/na-gestao/veterinario-municipal/"),
    ("Administração pública", "Provedoria dos Animais de Lisboa", "10.9.2024", "C",
     "Propõe sinalização das colónias CED (cerca de 12 000 gatos em mais de 1 500 colónias em Lisboa) e contactos de cuidadores para emergências.",
     "https://www.publico.pt/2024/09/10/local/noticia/provedoria-animais-lisboa-propoe-nova-sinaletica-proteger-animais-casos-emergencias-2103558"),
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
     "Contributos MVM.docx (repositório)"),
    # --- Ordens e associacoes profissionais
    ("Ordens e associações profissionais", "OMV, comunicado sobre CED em cães", "21.11.2025", "C",
     "Contra o CED em cães, que considera tecnicamente infundado e socialmente perigoso e uma desistência da administração local. Apoia o CED em gatos. Propõe reforço da captura e do alojamento em CRO.",
     "https://www.veterinaria-atual.pt/na-gestao/omv-programa-ced-caes/"),
    ("Ordens e associações profissionais", "OMV, bastonário", "22.8.2026", "T e C",
     "Esterilização obrigatória com financiamento público, registo SIAC com rastreio de ninhadas e um médico veterinário municipal por concelho. Refere que só cerca de 45% dos municípios têm médico veterinário municipal.",
     "https://observador.pt/2026/08/22/veterinarios-e-associacoes-defendem-mais-investimento-na-esterilizacao-de-animais/"),
    ("Ordens e associações profissionais", "OMV, parecer sobre abandono em centros veterinários", "nov. 2015", "T",
     "A lei é omissa sobre animais que os donos não vão buscar depois do tratamento. Propõe termo de responsabilidade com prazo a partir do qual se presume o abandono. Citação: «A legislação é omissa quanto à situação de animais abandonados, após tratamento, em CAMV's».",
     "https://www.omv.pt/dmdocuments/vi_formacao_omv/abandono_animais_camv_ultimoparecer_nov2015.pdf"),
    ("Ordens e associações profissionais", "OMV e SNMV, comentários nos documentos de trabalho do RGBEAC e do RGAC", "2025-2026", "T",
     "Prazo para comunicar desaparecimento: SNMV propõe 48 horas, OMV propõe 72 horas. SNMV opõe-se a registos provisórios no SIAC por gerarem dúvidas sobre a responsabilidade pelos atos do animal.",
     "Documentos de trabalho do RGBEAC e do RGAC (repositório)"),
    ("Ordens e associações profissionais", "APMVEAC, revisão crítica da legislação", "9.4.2021", "T e C",
     "Critica que a lei ponha autarquias e sociedades zoófilas em pé de igualdade no abandono, sem definir estas últimas. Citação: «a lei pode estar a passar responsabilidades elevadas para um sector que os legisladores foram até agora incapazes de caracterizar e definir cabalmente.» Sobre a Portaria 146/2017, sugere rever a adoção de animais com menos de 6 meses sem esterilização.",
     "https://apmveac.pt/wp-content/uploads/2021/04/Legislacao.Animais.Companhia_09-04-2021-amarelo-final-.pdf"),
    ("Ordens e associações profissionais", "APMVEAC, parecer à ENAE", "set. 2023", "C",
     "Contra a dispersão de tutelas e contra o CED em cães. Diz que o enquadramento legal é parte do problema e que a eutanásia é ato clínico da responsabilidade exclusiva do médico veterinário.",
     "https://apmveac.pt/wp-content/uploads/2023/09/Parecer-APMVEAC-Consulta-Publica-ENAE.pdf"),
    ("Ordens e associações profissionais", "ANVETEM", "2020", "C",
     "Diz que a Lei 27/2016 assentou em pressupostos errados e que os CRO estão sobrelotados. Aponta a falta de regulação das entidades privadas de proteção animal. Refere que só 172 dos 308 municípios tinham médico veterinário municipal.",
     "https://observador.pt/2020/03/08/associacao-de-veterinarios-diz-que-situacao-nos-canis-municipais-e-dramatica/"),
    # --- Juristas, academia e tribunais
    ("Juristas, academia e tribunais", "Teresa Quintela de Brito, «O abandono de animais de companhia», RJLB", "2019", "T",
     "O crime de abandono só pode ser cometido por quem já tem o dever de guardar, vigiar ou assistir o animal. Citação: «Não é possível a imputação de responsabilidade por estes crimes a associações ou sociedades zoófilas ou a quaisquer outras pessoas colectivas».",
     "https://www.cidp.pt/revistas/rjlb/2019/2/2019_02_0077_0095.pdf"),
    ("Juristas, academia e tribunais", "Tribunal da Relação de Coimbra, proc. 281/10.1TBCV.C1", "11.7.2012", "T",
     "O dever de vigilância do art. 493.º, n.º 1 do Código Civil decorre do poder de facto sobre o animal e não tem de recair sobre o dono.",
     "https://trc.pt/responsabilidade-civil-danos-causados-por-animais-dever-de-vigilancia/"),
    ("Juristas, academia e tribunais", "Tribunal da Relação do Porto", "11.11.2024", "T",
     "O detentor que mantinha o cão em sua casa responde pelos danos, ainda que não seja proprietário.",
     "https://www.lexpoint.pt/conteudos/987/133651/noticias/responsabilidade-por-danos-causados-por-animal"),
    ("Juristas, academia e tribunais", "Tribunal da Relação de Lisboa, proc. 1642/24.4T8AMD.L1-8", "30.4.2025", "T",
     "O registo no SIAC pode relevar para presumir a propriedade, mas não afasta a prova da posse. O tribunal revogou uma decisão que se apoiava só no registo.",
     "https://www.dgsi.pt/jtrl.nsf/33182fc732316039802565fa00497eec/7462ba7a0546bac680258c8b0049a31e?OpenDocument"),
    ("Juristas, academia e tribunais", "Tribunal Constitucional, Acórdãos 70/2024 e 478/2024", "2024", "T",
     "Não julgam inconstitucionais os arts. 387.º e 388.º do Código Penal (maus-tratos e abandono), invertendo a jurisprudência anterior.",
     "https://www.tribunalconstitucional.pt/tc/acordaos/20240070.html"),
    ("Juristas, academia e tribunais", "Paulo Afonso, docente e médico veterinário", "21.4.2026", "C",
     "A Lei 27/2016 ficou aquém: os CRO recolhem o mesmo número de animais que antes, sem coordenação nacional nem identificação suficiente.",
     "https://greensavers.sapo.pt/problema-dos-animais-errantes-persiste-uma-decada-depois-da-proibicao-de-abate/"),
    # --- ONG
    ("ONG e associações de proteção animal", "ARPA, parecer sobre o DL 82/2019", "dez. 2022", "T e C",
     "Registar gatos de colónia em nome do cuidador torna-o responsável por animais que não controla, desincentiva a esterilização e cria falsas presunções de abandono. Defende o registo em nome do município nos CED municipais e que o CED é um dever legal dos municípios. Citação: «o que não podem é onerá-las com responsabilidades que além de não estarem legamente previstas, apenas as desencorajam a agir».",
     "https://www.arpa-associacao.pt/media/attachments/2022/12/14/parecer-arpa-versAo-4-final.pdf"),
    ("ONG e associações de proteção animal", "FEDRA (federação de associações)", "22.8.2026", "C",
     "Esterilização obrigatória como serviço público, financiamento estável e CED para cães. Diz que as associações suportam as falhas do sistema.",
     "https://observador.pt/2026/08/22/veterinarios-e-associacoes-defendem-mais-investimento-na-esterilizacao-de-animais/"),
    ("ONG e associações de proteção animal", "FEDRA, plano de políticas públicas", "2024", "C",
     "Diz que o microchip nos gatos de colónia não é viável na maioria dos casos e pede exceções. Propõe CED para cães e parques de matilhas.",
     "FEDRA - Plano de políticas públcias.pdf (repositório)"),
    ("ONG e associações de proteção animal", "Animais de Rua", "18.11.2024", "C",
     "Pede mais pressão sobre os municípios para cumprirem o CED e colaboração com as ONG. Contra o corte de apoios no OE2025.",
     "https://jornaleconomico.sapo.pt/noticias/estamos-perante-um-retrocesso-inaceitavel-se-bem-estar-animal-nao-for-incluido-no-oe2025-diz-animais-de-rua/"),
    ("ONG e associações de proteção animal", "SOS Animal e ANIMAL", "25.10.2019", "T",
     "O Estado não cumpre a lei: CRO lotados e listas de espera, com os animais a ficarem a cargo das associações.",
     "https://tvi.iol.pt/noticias/sociedade/canis/associacoes-culpam-o-estado-nao-ha-capacidade-para-receber-os-animais"),
    ("ONG e associações de proteção animal", "Abraços de 4 Patas (Entroncamento)", "14.9.2025", "C",
     "O CED municipal perdeu eficácia, as esterilizações caíram e os voluntários fazem trabalho do médico veterinário municipal.",
     "https://omirante.pt/sociedade/2025-09-14-associacao-do-entroncamento-critica-falta-de-controlo-de-colonias-de-gatos-1a4940a3"),
    ("ONG e associações de proteção animal", "Movimento de Intervenção pelas Matilhas (Coimbra)", "s/d", "C",
     "Defende o CED em cães, com devolução ao território acompanhada por cuidadores, vacinação e microchip.",
     "https://matilhascoimbra.pt/pages/projecto-2"),
    ("ONG e associações de proteção animal", "Associação São Francisco de Assis (Cascais)", "29.1.2021", "C",
     "Defendeu a proibição de alimentar animais na via pública para gerir uma matilha no Guincho.",
     "https://poligrafo.sapo.pt/fact-check/proibido-alimentar-os-animais-punivel-com-coima-imagem-deste-cartaz-em-cascais-e-autentica"),
    # --- Partidos
    ("Partidos", "PAN", "2021 a 2025", "T e C",
     "Figura do animal comunitário (projeto aprovado na generalidade em 2021, caducado, retomado nos PJL 662/XV e 88/XVI). Estatuto da família de acolhimento temporário (2024). Critica o OE2026 por nenhum avanço para animais comunitários e matilhas.",
     "https://www.pan.com.pt/pan-destaca-vitorias-no-bem-estar-animal-mas-denuncia-retrocesso-grave-no-orcamento-do-estado-para-2026/"),
    ("Partidos", "PAN, Inês Sousa Real", "1.9.2026", "C",
     "A execução da Lei 27/2016 fica aquém: esterilizações em queda, pelo menos 96 municípios sem CRO e só 45% com médico veterinário municipal.",
     "https://pit.nit.pt/animais/10-anos-sem-abate-nos-canis-ha-leis-que-salvam-vidas"),
    ("Partidos", "PCP, proposta ao OE2026", "5.11.2025", "T e C",
     "Campanha nacional de esterilização com CED para cães não perigosos, registados no SIAC sem responsabilidade do município. Citação: «a título exclusivamente informativo, mediante a identificação genérica ‘Cães CED’ e com a exclusão das responsabilidades desses municípios inerentes à propriedade ou detenção desses animais».",
     "https://www.pcp.pt/campanha-nacional-de-esterilizacao-de-animais-errantes-0"),
    ("Partidos", "PCP", "12.11.2021", "C",
     "Contra criar novas figuras legais sem meios: a solução é a esterilização e uma rede pública de médicos veterinários.",
     "https://www.pcp.pt/solucao-prevencao-pela-esterilizacao-rede-publica-de-veterinarios-nao-abate-de-animais-abandonados"),
    ("Partidos", "Livre, programa eleitoral", "2024", "C",
     "Reforço dos CED e alargamento a cães errantes, valorização do animal comunitário, protocolos com associações com metas e financiamento.",
     "https://programa.partidolivre.pt/propostas/N.13/"),
    ("Partidos", "Bloco de Esquerda, programa eleitoral", "2024", "C",
     "CED, figura do animal comunitário e um médico veterinário municipal a tempo inteiro por município.",
     "https://pit.nit.pt/animais/legislativas-estao-ai-prometem-os-partidos-defesa-do-bem-estar-animal"),
    ("Partidos", "Chega, programa eleitoral", "2024", "C",
     "Garantir o CED em todos os municípios e criar o estatuto do animal comunitário.",
     "https://pit.nit.pt/animais/legislativas-estao-ai-prometem-os-partidos-defesa-do-bem-estar-animal"),
    ("Partidos", "PS, programa eleitoral", "2024", "C",
     "Programas de esterilização e vacinação para matilhas errantes. Não se pronuncia sobre CED de gatos.",
     "https://pit.nit.pt/animais/legislativas-estao-ai-prometem-os-partidos-defesa-do-bem-estar-animal"),
    ("Partidos", "PSD/AD e Iniciativa Liberal, programas eleitorais", "2024", "T",
     "PSD/AD: campanhas contra o abandono e reforço dos CRO. IL: permitir que os CRO entreguem animais a particulares com apoio do Estado e financiar as associações em função dos animais a cargo.",
     "https://pit.nit.pt/animais/legislativas-estao-ai-prometem-os-partidos-defesa-do-bem-estar-animal"),
    ("Partidos", "Respostas dos partidos (Maratona pelos Animais)", "mar. 2024", "C",
     "Sobre o CED em cães: PAN e BE a favor; Chega a favor em local circunscrito com cuidadores designados; CDU prudente por questões práticas e de responsabilidade civil; AD disponível para refletir; PS e IL não responderam.",
     "https://maratonapelosanimais.pt/wp-content/uploads/2024/03/respostas-completas.pdf"),
    # --- Municipios
    ("Municípios e ANMP", "ANMP", "2018 e 2024", "C",
     "Em 2018 disse ser impossível cumprir ao mesmo tempo a recolha obrigatória e a proibição do abate. Em 2024 lamentou que o OE2025 deixasse de prever verbas próprias para os CRO.",
     "https://www.rtp.pt/noticias/economia/anmp-lamenta-que-orcamento-do-estado-nao-contemple-verbas-para-centros-de-recolha-animal_n1612994"),
    ("Municípios e ANMP", "Representante dos municípios (audição parlamentar)", "25.10.2023", "C",
     "Só cerca de 200 dos 308 municípios têm CRO, mas todos estão obrigados a recolher.",
     "https://observador.pt/2023/10/25/ha-80-000-animais-habitantes-nos-centros-de-recolha-alerta-provedora-do-animal/"),
    ("Municípios e ANMP", "Câmara Municipal do Porto", "6.8.2021", "T e C",
     "Os gatos das colónias CED estão registados no SIAC em nome da câmara, mas a gestão diária cabe às associações. Mais de 70 colónias.",
     "https://poligrafo.sapo.pt/fact-check/colonia-de-gatos-sinalizada-por-placa-no-porto-esta-legalizada-e-os-animais-sao-propriedade-da-autarquia/"),
    ("Municípios e ANMP", "Câmara Municipal do Entroncamento", "14.9.2025", "C",
     "O médico veterinário municipal está sob grande pressão; a câmara vai contratar clínicas para esterilizações.",
     "https://omirante.pt/sociedade/2025-09-14-associacao-do-entroncamento-critica-falta-de-controlo-de-colonias-de-gatos-1a4940a3"),
    ("Municípios e ANMP", "Assembleia Municipal de Coimbra (proposta aprovada)", "30.6.2026", "C",
     "Mapeamento georreferenciado das colónias, regulamento municipal de cuidadores com formação, identificação, direitos e deveres, metas anuais de CED e apoio alimentar aos cuidadores.",
     "https://www.diariocoimbra.pt/2026/06/30/municipio-planeia-fazer-uma-melhor-gestao-das-colonias-de-gatos/"),
    ("Municípios e ANMP", "Regulamentos municipais (Lisboa, Porto, Oeiras, Cascais, Sintra, Leiria, entre outros)", "vários", "C",
     "Proíbem alimentar animais na via pública, com coimas que em Oeiras chegam a 8 000 euros. Em regra excecionam os cuidadores registados.",
     "https://www.oeiras.pt/-/alimentacao-animais-via-publica"),
    # --- Conservacao
    ("Conservação da natureza", "SPEA, parecer aos planos de gestão dos parques naturais dos Açores", "2020", "C",
     "Prioridade ao controlo de predadores introduzidos. Citação: «com prioridade para o controlo e esterilização de gatos (84% da predação é da responsabilidade dos gatos, Hervías et al., 2013)».",
     "https://www.spea.pt/wp-content/uploads/2020/09/ParecerSPEA_Planos-Gestao-Parques-Naturais-Ilha-2020.pdf"),
    ("Conservação da natureza", "SPEA", "27.12.2021", "C",
     "Recomenda gestão responsável dos gatos com dono, incluindo recolhimento noturno, para reduzir a predação de aves.",
     "https://spea.pt/um-gato-feliz-e-alimentado-mantem-o-passarinho-afastado/"),
    ("Conservação da natureza", "Miguel Clavero, Estação Biológica de Doñana (Espanha), entrevista ao DN", "14.4.2023", "C",
     "Cientista espanhol. Defende que os gatos sem dono sejam retirados do meio natural, por métodos não letais sempre que possível, porque as colónias alimentadas continuam a caçar.",
     "https://www.dn.pt/sociedade/ha-que-manter-os-gatos-sem-dono-fora-do-meio-ambiente-16178512.html"),
]

FONTES = [
    "RGAC: RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO - Revisto 30-06-2026 18h00 Grupo.docx (repositório).",
    "RGBEAC (jun. 2025) e versões comentadas de out. 2025 e fev. 2026 (repositório).",
    "DL 82/2019, DL 276/2001, DL 314/2003, DL 315/2009, Portaria 146/2017: versões consolidadas no DRE "
    "(diariodarepublica.pt), confirmadas na pasta Legislação vigente e no repositório.",
    "Código Civil e Código Penal: versões em vigor na PGDL (pgdlisboa.pt).",
    "Lei 27/2016 (repositório e DRE).",
    "Regulamento (UE) 2026/1818, JO L de 10.8.2026 (versões PT e EN no repositório).",
    "Estratégia Nacional para os Animais Errantes, ICNF, consulta pública de 2023: "
    "https://www.icnf.pt/api/file/doc/41f8f44aee23be1a",
    "Relatório final do GTBEA, DGAV, 2021: "
    "https://www.dgav.pt/wp-content/uploads/2021/08/Relatorio-FINAL-avaliacao-da-implementacao-da-Lei-27-2016.pdf",
    "Projeto de revisão da Portaria 146/2017 (ANMP, 2021): https://anmp.pt/file-viewer/?pstid=41508",
    "Contributos dos médicos veterinários municipais, reunião de 6.3.2026 (Contributos MVM.docx, repositório).",
    "Acórdão do Tribunal da Relação de Lisboa de 30.4.2025, proc. 1642/24.4T8AMD.L1-8 (dgsi.pt).",
]

REGISTO_ALTERACOES = [
    ("1", "25.9.2026", "Primeira versão. Tema T (18 fichas) e tema C (17 fichas). Anexo B com posições de entidades externas recolhidas no repositório e online."),
    ("1.1", "25.9.2026", "Correção de formatação: larguras fixas das colunas em todas as tabelas; anexos A e B em páginas na horizontal. Sem alterações de conteúdo."),
    ("1.2", "25.9.2026", "Correção das tabelas: as propriedades de largura estavam fora da ordem exigida pelo Word e eram ignoradas. Ficheiro validado contra o esquema. Sem alterações de conteúdo."),
]
