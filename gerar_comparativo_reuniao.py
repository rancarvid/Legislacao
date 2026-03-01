"""
Gera ficheiro Excel + HTML comparativo para reunião artigo a artigo do @regulamento.
Exemplo com 3 artigos: Identificação, Bem-estar/Detenção, Reprodução.
"""

import openpyxl
from openpyxl.styles import (
    PatternFill, Font, Alignment, Border, Side, GradientFill
)
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
import json
import os

# ---------------------------------------------------------------------------
# DADOS — verbatim dos documentos
# ---------------------------------------------------------------------------

ARTIGOS = [
    {
        "id": "ART-17",
        "tema": "Identificação e Registo",
        "regulamento": {
            "ref": "Art.º 17.º do Regulamento 2023/0447",
            "texto": (
                "All dogs and cats kept in establishments placed on the market or owned by pet owners "
                "or by any other natural or legal persons, shall be individually identified by means of "
                "a single injectable transponder containing a readable microchip compliant with Annex II.\n\n"
                "1a. Operators shall ensure that dogs and cats born in their establishments are individually "
                "identified within 3 months after their birth and in any event before the date of their "
                "placing on the market.\n\n"
                "Operators of selling establishments, shelters and those placing and being responsible for "
                "dogs and cats in foster homes shall ensure that dogs and cats that enter their establishments "
                "or come under their responsibility are individually identified within 30 days after their "
                "arrival at the establishment and in any event before the date of their placing on the market.\n\n"
                "Pet owners and any other natural or legal persons, other than operators, who own dogs or cats, "
                "shall ensure that the dogs or cats are individually identified at the latest when the dog or cat "
                "reaches 3 months of age or, in case the dog or cat is placed on the market, before the date "
                "of their placing on the market."
            ),
            "traducao": (
                "Todos os cães e gatos mantidos em estabelecimentos colocados no mercado ou detidos por "
                "donos de animais de companhia ou por qualquer outra pessoa singular ou coletiva devem ser "
                "identificados individualmente por meio de um único transponder injetável contendo um microchip "
                "legível em conformidade com o Anexo II.\n\n"
                "1a. Os operadores devem assegurar que os cães e gatos nascidos nos seus estabelecimentos sejam "
                "identificados individualmente no prazo de 3 meses após o nascimento e, em qualquer caso, antes "
                "da data da sua colocação no mercado.\n\n"
                "Os operadores de estabelecimentos de venda, abrigos e os que colocam e são responsáveis por "
                "cães e gatos em famílias de acolhimento devem assegurar que os cães e gatos que entrem nos seus "
                "estabelecimentos sejam identificados individualmente no prazo de 30 dias após a chegada.\n\n"
                "Os donos de animais de companhia e quaisquer outras pessoas singulares ou coletivas que detenham "
                "cães ou gatos devem assegurar que os animais sejam identificados individualmente o mais tardar "
                "quando o animal atingir os 3 meses de idade."
            ),
        },
        "rgbeac": {
            "ref": "Art.º 17.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "1 — A identificação dos animais de companhia, pela sua marcação, quando aplicável, e registo "
                "no SIAC, deve ser realizada:\n\n"
                "a) Relativamente aos cães, gatos e furões nascidos em alojamentos, até aos três meses de idade "
                "ou, em qualquer caso, antes da sua colocação no mercado;\n\n"
                "b) Relativamente aos cães, gatos e furões que entrem em alojamentos, nos termos dos artigos "
                "12.º a 15.º, até trinta dias após a sua chegada ao alojamento ou, em qualquer caso, antes da "
                "data de colocação no mercado;\n\n"
                "c) Relativamente aos cães, gatos e furões detidos por pessoas singulares, exceto nos casos "
                "previstos nas alíneas anteriores, até aos três meses de idade ou, no caso de colocação no "
                "mercado, antes da data de colocação no mercado."
            ),
        },
        "codigo": {
            "ref": "Art.º 53.º do Código do Animal (DL n.º 214/2013)",
            "texto": (
                "1 — Todos os cães devem ser identificados e registados, entre os três e os seis meses de idade.\n\n"
                "2 — Os gatos em exposição, para fins comerciais ou lucrativos, em estabelecimentos de venda, "
                "locais de criação, feiras ou concursos, provas funcionais, publicidade ou fins similares, devem "
                "ser identificados e registados entre os três e os seis meses de idade.\n\n"
                "4 — Os cães e gatos são identificados através de método electrónico e registados na base de dados "
                "nacional.\n\n"
                "5 — A identificação electrónica é efetuada através da aplicação subcutânea de um microchip no "
                "centro da face lateral esquerda do pescoço."
            ),
        },
        "legislacao": {
            "ref": "n.ºs 1, 2 e 3 do art.º 5.º do DL n.º 82/2019, de 27 de junho",
            "texto": (
                "1 — A identificação dos animais de companhia, pela sua marcação e registo no SIAC, deve ser "
                "realizada até 120 dias após o seu nascimento.\n\n"
                "2 — Na impossibilidade de determinar a data de nascimento exata, para efeitos de contagem do "
                "prazo referido no número anterior, a identificação deve ser efetuada até à perda dos dentes "
                "incisivos de leite.\n\n"
                "3 — Sem prejuízo dos números anteriores, e relativamente aos cães, gatos e furões que sejam "
                "cedidos e ou comercializados a partir de um criador ou de um estabelecimento autorizado para a "
                "detenção de animais de companhia, nomeadamente os centros de hospedagem com ou sem fins lucrativos "
                "e os centros de recolha oficiais, deve ser assegurada a sua marcação e registo no SIAC antes de "
                "abandonarem a instalação de nascimento ou de alojamento, independentemente da sua idade."
            ),
        },
        "divergencia": (
            "O @regulamento fixa o prazo de identificação em 3 meses para nascimentos e 30 dias para entrada em "
            "estabelecimentos. A @legislacao (DL n.º 82/2019, art.º 5.º) prevê um prazo geral de 120 dias após "
            "o nascimento, sem distinguir o contexto de estabelecimento — prazo superior ao fixado pelo "
            "@regulamento e que exigirá redução. O @codigo fixa entre 3 e 6 meses, igualmente sem distinção de "
            "contexto. O @rgbeac alinha com o @regulamento nos prazos, mas aplica-se apenas a cães, gatos e "
            "furões. Nenhum dos diplomas nacionais vigentes distingue o prazo de 30 dias aplicável a animais que "
            "entram em estabelecimentos, previsto no @regulamento."
        ),
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
    {
        "id": "ART-06",
        "tema": "Bem-Estar e Detenção",
        "regulamento": {
            "ref": "Art.º 6.º do Regulamento 2023/0447",
            "texto": (
                "Operators shall be responsible for the welfare of dogs or cats kept in the establishments "
                "under their responsibility and under their control and to minimise any risks to their welfare.\n\n"
                "1a. In the case of foster homes, the responsibility shall lie with the operator on whose behalf "
                "dogs or cats are kept. Such operators shall not place more than a total of five dogs or cats or "
                "one litter with or without mother in a foster home at any given time and shall provide the foster "
                "family with adequate information on the animal welfare obligations as well as the individual needs "
                "of the dogs or cats, and shall ensure that the relevant obligations set out by this Regulation "
                "are complied with in foster homes."
            ),
            "traducao": (
                "Os operadores são responsáveis pelo bem-estar dos cães ou gatos mantidos nos estabelecimentos "
                "sob a sua responsabilidade e controlo e devem minimizar quaisquer riscos para o seu bem-estar.\n\n"
                "1a. No caso de famílias de acolhimento, a responsabilidade recai sobre o operador em nome de quem "
                "os cães ou gatos são mantidos. Esses operadores não devem colocar mais do que um total de cinco "
                "cães ou gatos ou uma ninhada com ou sem mãe numa família de acolhimento em qualquer momento e "
                "devem fornecer à família de acolhimento informação adequada sobre as obrigações de bem-estar "
                "animal, bem como as necessidades individuais dos animais."
            ),
        },
        "rgbeac": {
            "ref": "Art.º 10.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "1 — O detentor do animal de companhia deve:\n\n"
                "a) Assegurar o bem-estar do animal, de acordo com a sua espécie, raça, idade e necessidades "
                "físicas e etológicas, proporcionando-lhe:\n"
                "— Atenção, supervisão, controlo, exercício físico e estímulo mental;\n"
                "— Alimentos saudáveis, adequados e convenientes ao seu normal desenvolvimento e acesso permanente "
                "a água potável;\n"
                "— Condições higiossanitárias que atendam, no mínimo, ao estabelecido no presente decreto-lei e "
                "na demais legislação aplicável;\n"
                "— Liberdade de movimento, sendo proibidos todos os sistemas de contenção permanentes."
            ),
        },
        "codigo": {
            "ref": "Art.º 5.º do Código do Animal (DL n.º 214/2013)",
            "texto": (
                "1 — As condições de detenção e de alojamento para reprodução, criação, manutenção e acomodação "
                "dos animais de companhia devem salvaguardar os cinco domínios do bem-estar animal (Nutrição, "
                "Ambiente, Saúde, Comportamento e Psicológico), estabelecidos pela Organização Mundial da Saúde "
                "Animal (OMSA).\n\n"
                "2 — Nenhum animal deve ser detido como animal de companhia se não estiverem asseguradas as "
                "condições referidas no número anterior ou as demais previstas no presente diploma.\n\n"
                "3 — É proibida a violência contra animais, considerando-se como tal todos os atos que, sem "
                "necessidade, infligem a morte, o sofrimento, a dor, a angústia ou ferimentos a um animal."
            ),
        },
        "legislacao": {
            "ref": "n.ºs 1, 2 e 3 do art.º 7.º do DL n.º 276/2001, de 17 de outubro",
            "texto": (
                "1 — As condições de detenção e de alojamento para reprodução, criação, manutenção e acomodação "
                "dos animais de companhia devem salvaguardar os seus parâmetros de bem-estar animal, "
                "nomeadamente nos termos dos artigos seguintes.\n\n"
                "2 — Nenhum animal deve ser detido como animal de companhia se não estiverem asseguradas as "
                "condições referidas no número anterior ou se não se adaptar ao cativeiro.\n\n"
                "3 — São proibidas todas as violências contra animais, considerando-se como tais os atos "
                "consistentes em, sem necessidade, se infligir a morte, o sofrimento ou lesões a um animal."
            ),
        },
        "divergencia": (
            "O @regulamento especifica o limite de 5 animais por família de acolhimento e atribui responsabilidade "
            "ao operador (não à família). A @legislacao (DL n.º 276/2001, art.º 7.º) centra a responsabilidade no "
            "detentor, sem distinguir o contexto de acolhimento temporário nem fixar limites numéricos — posição "
            "idêntica à do @rgbeac e do @codigo. Nenhum dos diplomas nacionais, incluindo a legislação vigente, "
            "prevê o conceito de família de acolhimento nem o limite numérico de 5 animais estabelecido pelo "
            "@regulamento. A lacuna é transversal a toda a legislação nacional."
        ),
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
    {
        "id": "ART-07",
        "tema": "Reprodução e Criação",
        "regulamento": {
            "ref": "Art.º 7.º do Regulamento 2023/0447",
            "texto": (
                "Operators shall notify the competent authorities of their activity, providing at least the "
                "following information:\n\n"
                "(a) name, address and contact details of the operator;\n"
                "(b) the location(s) of the establishment(s);\n"
                "(c) the type(s) of establishment: breeding establishment, selling establishment, shelter or "
                "foster home;\n"
                "(d) the species and, for breeding establishments, the breeds of the dogs or cats kept in the "
                "establishment(s);\n"
                "(e) the capacity of the establishment expressed as the maximum number of dogs and cats which can "
                "be kept in the establishment(s);\n"
                "(ea) for breeding establishments, the estimated number of litters to be placed on the market "
                "per year."
            ),
            "traducao": (
                "Os operadores devem notificar as autoridades competentes da sua atividade, fornecendo pelo menos "
                "as seguintes informações:\n\n"
                "(a) nome, morada e contactos do operador;\n"
                "(b) a(s) localização(ões) do(s) estabelecimento(s);\n"
                "(c) o tipo de estabelecimento: criação, venda, abrigo ou família de acolhimento;\n"
                "(d) as espécies e, para os estabelecimentos de criação, as raças dos cães ou gatos mantidos;\n"
                "(e) a capacidade do estabelecimento, expressa no número máximo de cães e gatos que podem ser "
                "alojados;\n"
                "(ea) para os estabelecimentos de criação, o número estimado de ninhadas a colocar no mercado "
                "por ano."
            ),
        },
        "rgbeac": {
            "ref": "Art.º 43.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "1 — Os centros de bem-estar animal procedem à esterilização dos animais recolhidos que se "
                "presuma terem sido abandonados, nos termos do artigo 41.º.\n\n"
                "2 — As câmaras municipais devem, sempre que necessário e sob a responsabilidade do médico "
                "veterinário municipal, incentivar e promover programas de esterilização de animais de companhia, "
                "nomeadamente os cães e gatos, em complementaridade com os centros de bem-estar animal.\n\n"
                "3 — Os requisitos mínimos das instalações adequadas à realização de esterilizações nos centros "
                "de bem-estar animal são estabelecidos em portaria do membro do Governo responsável pela área "
                "da agricultura."
            ),
        },
        "codigo": {
            "ref": "Art.º 8.º do Código do Animal (DL n.º 214/2013)",
            "texto": (
                "1 — A reprodução de animais deve ser realizada de forma planeada.\n\n"
                "2 — A reprodução de animais obedece ao seguinte:\n\n"
                "a) Os animais só devem ser utilizados na reprodução depois de atingida a maturidade reprodutiva "
                "para a espécie e raça devendo, no caso de cães e gatos, as fêmeas ter pelo menos dois anos de "
                "idade no momento da primeira cobertura;\n\n"
                "b) Deve ser respeitada a regra do porte semelhante dos progenitores, para prevenir a possibilidade "
                "de distócia;\n\n"
                "c) Devem ser excluídos da reprodução os animais que revelem defeitos genéticos e malformações, "
                "designadamente monorquidia e displasia."
            ),
        },
        "legislacao": {
            "ref": "n.º 1 do art.º 3.º-A do DL n.º 276/2001, de 17 de outubro",
            "texto": (
                "1 — A mera comunicação prévia a que se refere a alínea a) do n.º 1 do artigo anterior é "
                "dirigida à DGAV e deve conter os seguintes elementos, quando aplicáveis:\n\n"
                "a) O nome ou a denominação social do interessado;\n"
                "b) A localização do alojamento e a sua designação comercial;\n"
                "c) O número de identificação fiscal ou de pessoa coletiva do interessado;\n"
                "d) Municípios integrantes, no caso dos centros de recolha intermunicipais;\n"
                "e) Caracterização das atividades a exercer;\n"
                "f) Indicação do médico veterinário responsável pelo alojamento;\n"
                "g) O número de celas de quarentena para isolamento de animais por suspeita de raiva, "
                "no caso dos centros de recolha;\n"
                "h) A capacidade máxima de animais e respetivas espécies a alojar;\n"
                "i) O número de animais detidos, espécies e raças;\n"
                "j) Declaração de responsabilidade, subscrita pelo interessado, relativa ao cumprimento "
                "da legislação aplicável aos animais de companhia, nomeadamente em matéria de instalações, "
                "equipamentos, higiene, saúde e bem-estar dos animais."
            ),
        },
        "divergencia": (
            "O @regulamento exige notificação prévia com dados detalhados, incluindo o número estimado de ninhadas "
            "a colocar no mercado por ano (al. ea)). A @legislacao (DL n.º 276/2001, art.º 3.º-A) já prevê "
            "comunicação prévia à DGAV com elementos parcialmente equivalentes (capacidade máxima, espécies, raças "
            "— als. h) e i)), mas não exige a estimativa de ninhadas, constituindo lacuna parcial face ao "
            "@regulamento. O @codigo regula condições de reprodução mas não prevê notificação ou registo de "
            "estabelecimentos criadores. O @rgbeac trata exclusivamente da esterilização de errantes, sem qualquer "
            "norma sobre notificação de criadores. A @legislacao vigente é, dos diplomas nacionais, o mais próximo "
            "do @regulamento neste eixo, ainda que com lacuna relevante."
        ),
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
    {
        "id": "ART-05",
        "tema": "Princípios Gerais de Bem-Estar",
        "regulamento": {
            "ref": "Art.º 5.º do Regulamento 2023/0447",
            "texto": (
                "Operators shall apply the following general welfare principles with respect to dogs or cats "
                "bred or kept in their establishment:\n\n"
                "(a) dogs and cats are provided with water and feed of a quality and of a quantity that enables "
                "them to have appropriate nutrition and hydration;\n\n"
                "(b) dogs and cats are kept in an appropriate and regularly cleaned physical environment which is "
                "secure and comfortable, especially in terms of space, air quality, temperature, light, protection "
                "against adverse climatic conditions and ease of movement, preventing overcrowding;\n\n"
                "(c) dogs and cats are kept safe, clean and in good health by preventing diseases, injuries, and "
                "pain, due in particular to management, handling practices and breeding practices;\n\n"
                "(d) dogs and cats are kept in an environment that enables them to exhibit species-specific and "
                "social non-harmful behaviour, and to establish a positive relationship with human beings;\n\n"
                "(e) dogs and cats are kept in such a way as to optimise their mental state by preventing or "
                "reducing negative stimuli in duration and intensity, as well as by maximising opportunities for "
                "positive stimuli in duration and intensity, preventing the development of abnormal repetitive and "
                "other behaviours indicative of negative animal welfare, and taking into consideration the "
                "individual dog's or cat's needs in the different domains referred to in points (a) to (d)."
            ),
            "traducao": (
                "Os operadores devem aplicar os seguintes princípios gerais de bem-estar aos cães e gatos criados "
                "ou detidos nos seus estabelecimentos:\n\n"
                "(a) os cães e gatos são alimentados e abebeirados com água e ração de qualidade e quantidade "
                "adequadas a uma nutrição e hidratação apropriadas;\n\n"
                "(b) os cães e gatos são mantidos num ambiente físico adequado, regularmente limpo, seguro e "
                "confortável, especialmente em termos de espaço, qualidade do ar, temperatura, iluminação, "
                "proteção face a condições climáticas adversas e facilidade de movimentação, prevenindo a "
                "sobrelotação;\n\n"
                "(c) os cães e gatos são mantidos seguros, limpos e com boa saúde, prevenindo doenças, lesões e "
                "dor, nomeadamente através de práticas de maneio, manuseamento e reprodução adequadas;\n\n"
                "(d) os cães e gatos são mantidos num ambiente que lhes permite exibir comportamentos específicos "
                "da espécie e comportamentos sociais não nocivos, e estabelecer uma relação positiva com os seres "
                "humanos;\n\n"
                "(e) os cães e gatos são mantidos de forma a otimizar o seu estado mental, prevenindo ou "
                "reduzindo estímulos negativos em duração e intensidade, maximizando oportunidades de estímulos "
                "positivos, prevenindo o desenvolvimento de comportamentos repetitivos anormais, tendo em conta as "
                "necessidades individuais do animal nos domínios referidos nas alíneas (a) a (d)."
            ),
        },
        "rgbeac": {
            "ref": "al. a) do n.º 1 do art.º 10.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "1 — O detentor do animal de companhia deve:\n\n"
                "a) Assegurar o bem-estar do animal, de acordo com sua espécie, raça, idade e necessidades "
                "físicas e etológicas, proporcionando-lhe:\n"
                "— Atenção, supervisão, controlo, exercício físico e estímulo mental;\n"
                "— Alimentos saudáveis, adequados e convenientes ao seu normal desenvolvimento e acesso "
                "permanente a água potável;\n"
                "— Condições higiossanitárias que atendam, no mínimo, ao estabelecido no presente decreto-lei "
                "e na demais legislação aplicável;\n"
                "— Liberdade de movimento, sendo proibidos todos os sistemas de contenção permanentes;\n"
                "— Abrigo adequado, em termos de tamanho e qualidade, com vista a proteger de condições "
                "atmosféricas adversas, incluindo frio, chuva, sol ou calor excessivos, com cama seca, limpa "
                "e confortável;\n"
                "— Contato social adequado a cada espécie, de acordo com a sua idade e atividade."
            ),
        },
        "codigo": {
            "ref": "n.ºs 1, 2 e 3 do art.º 5.º do Código do Animal (DL n.º 214/2013)",
            "texto": (
                "1 — As condições de detenção e de alojamento para reprodução, criação, manutenção e acomodação "
                "dos animais de companhia devem salvaguardar os seus parâmetros de bem-estar animal.\n\n"
                "2 — Nenhum animal deve ser detido como animal de companhia se não estiverem asseguradas as "
                "condições referidas no número anterior ou se não se adaptar ao cativeiro.\n\n"
                "3 — É proibida a violência contra animais, considerando-se como tal todos os atos que, sem "
                "necessidade, infligem a morte, o sofrimento, abuso ou lesões a um animal."
            ),
        },
        "legislacao": {
            "ref": "n.º 1 do art.º 7.º e n.º 1 do art.º 9.º do DL n.º 276/2001, de 17 de outubro",
            "texto": (
                "Artigo 7.º, n.º 1 — As condições de detenção e de alojamento para reprodução, criação, "
                "manutenção e acomodação dos animais de companhia devem salvaguardar os seus parâmetros de "
                "bem-estar animal, nomeadamente nos termos dos artigos seguintes.\n\n"
                "Artigo 9.º, n.º 1 — A temperatura, a ventilação e a luminosidade e obscuridade das instalações "
                "devem ser as adequadas à manutenção do conforto e bem-estar das espécies que albergam."
            ),
        },
        "divergencia": (
            "O @regulamento enuncia explicitamente 5 domínios de bem-estar — nutrição, ambiente, saúde, "
            "comportamento e estado mental — como obrigação vinculativa dos operadores de estabelecimentos. "
            "A @legislacao (DL n.º 276/2001, art.ºs 7.º e 9.º) e o @codigo (art.º 5.º) consagram os mesmos "
            "parâmetros de bem-estar, mas sem formulação sistemática nos 5 domínios: o @codigo refere 'parâmetros "
            "de bem-estar animal' genericamente; o DL n.º 276/2001 desenvolve cada parâmetro em artigos separados "
            "(alojamento, alimentação, ambiente) mas sem os denominar domínios. O @rgbeac (art.º 10.º, n.º 1, "
            "al. a)) articula obrigações equivalentes ao nível do detentor mas de forma descritiva, não "
            "sistematizada nos 5 domínios. Nenhum diploma nacional adota formalmente a nomenclatura dos 5 domínios "
            "OMSA como o @regulamento."
        ),
        "necessidade_alteracao": "Não",
        "notas": "",
    },
    {
        "id": "ART-06a",
        "tema": "Estratégias de Criação — Conformação e Consanguinidade",
        "regulamento": {
            "ref": "Art.º 6.a do Regulamento 2023/0447",
            "texto": (
                "Operators of breeding establishments shall ensure that their breeding strategies minimise the "
                "risk of producing dogs or cats with genotypes associated with detrimental effects on their health "
                "and welfare.\n\n"
                "Operators of breeding establishments shall not use for reproduction dogs or cats that have "
                "excessive conformational traits leading to a high risk of detrimental effects on the welfare of "
                "these dogs or cats, or of their offspring. Before selection for breeding of a dog or cat that may "
                "be concerned by an excessive conformational trait the operator shall consult a veterinarian or an "
                "independent qualified person under the responsibility of a veterinarian.\n\n"
                "The following shall be prohibited in the management of the reproduction of dogs and cats:\n"
                "(a) the breeding between parents and offspring, between siblings, between half-siblings or "
                "between grandparents and grandchildren, unless approved by the competent authority based on a "
                "specific need to preserve local breeds with a limited genetic pool;\n"
                "(b) the breeding to produce hybrids."
            ),
            "traducao": (
                "Os operadores de estabelecimentos de criação devem assegurar que as suas estratégias de criação "
                "minimizam o risco de produzir cães ou gatos com genótipos associados a efeitos prejudiciais para "
                "a sua saúde e bem-estar.\n\n"
                "Os operadores de estabelecimentos de criação não devem utilizar para reprodução cães ou gatos "
                "que apresentem traços conformacionais excessivos que conduzam a um risco elevado de efeitos "
                "prejudiciais para o bem-estar desses animais ou das suas crias. Antes da seleção para reprodução "
                "de um animal potencialmente afetado por traço conformacional excessivo, o operador deve consultar "
                "um médico veterinário ou uma pessoa qualificada independente sob responsabilidade veterinária.\n\n"
                "São proibidos na gestão da reprodução de cães e gatos:\n"
                "(a) o cruzamento entre progenitores e descendentes, entre irmãos, entre meios-irmãos ou entre "
                "avós e netos, exceto com aprovação da autoridade competente por razão de necessidade específica "
                "de preservação de raças locais com reserva genética limitada;\n"
                "(b) o cruzamento para produção de híbridos."
            ),
        },
        "rgbeac": {
            "ref": "n.ºs 1 e 2 do art.º 34.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "1 — As intervenções cirúrgicas com o objetivo da modificação da aparência ou com fins não "
                "curativos ou não destinados a impedir a reprodução dos animais são proibidas, nos termos do "
                "disposto na alínea i) do n.º 1 do artigo 12.º.\n\n"
                "2 — O detentor de animal sujeito a intervenção curativa que modifique a sua aparência deve "
                "possuir documento comprovativo da necessidade da mesma, passado pelo médico veterinário que "
                "a ela procedeu, sob a forma de atestado do qual constem a identificação do médico veterinário, "
                "o número da cédula profissional e a sua assinatura, ou, no caso de animais importados, documento "
                "comprovativo da necessidade dessa intervenção, emitida pelo médico veterinário que a ela "
                "procedeu, legalizado pela autoridade competente do respetivo país."
            ),
        },
        "codigo": {
            "ref": "n.º 2, als. a), b) e c) do art.º 8.º do Código do Animal (DL n.º 214/2013)",
            "texto": (
                "2 — A reprodução de animais obedece ao seguinte:\n\n"
                "a) Os animais só devem ser utilizados na reprodução depois de atingida a maturidade reprodutiva "
                "para a espécie e raça devendo, no caso dos cães e gatos, seguir os parâmetros referidos no "
                "anexo I ao presente diploma, do qual faz parte integrante, não sendo autorizado, no caso das "
                "fêmeas, o acasalamento em cios sucessivos;\n\n"
                "b) Deve ser respeitada a regra do porte semelhante dos progenitores, para prevenir a "
                "possibilidade de distócia;\n\n"
                "c) Devem ser excluídos da reprodução, os animais que revelem defeitos genéticos e malformações, "
                "designadamente monorquidia e displasia da anca nos cães e rim poliquístico nos gatos, ou "
                "alterações comportamentais."
            ),
        },
        "legislacao": {
            "ref": "art.º 17.º e n.º 1 do art.º 18.º do DL n.º 276/2001, de 17 de outubro",
            "texto": (
                "Artigo 17.º — As intervenções cirúrgicas, nomeadamente as destinadas ao corte de caudas nos "
                "canídeos, têm de ser executadas por um médico veterinário.\n\n"
                "Artigo 18.º, n.º 1 — Os detentores de animais de companhia que os apresentem com quaisquer "
                "amputações que modifiquem a aparência dos animais ou com fins não curativos devem possuir "
                "documento comprovativo, passado pelo médico veterinário que a elas procedeu, da necessidade "
                "dessa amputação, nomeadamente discriminando que as mesmas foram feitas por razões "
                "médico-veterinárias ou no interesse particular do animal ou para impedir a reprodução."
            ),
        },
        "divergencia": (
            "O @regulamento proíbe traços conformacionais excessivos e impõe consulta veterinária prévia ao "
            "acasalamento de animais potencialmente afetados, além de proibir consanguinidade próxima (pais/filhos, "
            "irmãos, avós/netos) e produção de híbridos. Estas exigências são inteiramente novas no direito "
            "nacional: a @legislacao (DL n.º 276/2001, art.ºs 17.º e 18.º) limita-se a exigir intervenção "
            "veterinária em cirurgias e documentação para amputações, sem abordar conformação ou consanguinidade. "
            "O @codigo (art.º 8.º, n.º 2) exclui da reprodução animais com defeitos genéticos e malformações, e "
            "proíbe acasalamento em cios sucessivos, mas não prevê o conceito de traços conformacionais excessivos "
            "nem proíbe consanguinidade. O @rgbeac (art.º 34.º) proíbe apenas intervenções cirúrgicas de "
            "modificação da aparência, sem norma sobre estratégia genética. Lacuna normativa transversal a toda "
            "a legislação nacional quanto ao núcleo central do art.º 6.a do @regulamento."
        ),
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
    {
        "id": "ART-13",
        "tema": "Saúde e Monitorização Sanitária",
        "regulamento": {
            "ref": "Art.º 13.º do Regulamento 2023/0447",
            "texto": (
                "Operators shall ensure that:\n\n"
                "(a) dogs or cats under their responsibility are inspected by animal caretakers at least once a "
                "day and vulnerable dogs and cats, such as newborns, ill or injured dogs and cats, and "
                "peri-partum bitches and queens, are inspected more frequently;\n\n"
                "(b) dogs or cats with compromised welfare are, where necessary, transferred without undue delay "
                "to a separate area and, where needed, receive appropriate treatment;\n\n"
                "(c) where the recovery of a dog or a cat with compromised welfare is not achievable and the dog "
                "or cat experiences severe pain or suffering, a veterinarian is consulted without undue delay, to "
                "decide whether the dog or cat shall be euthanised to end its suffering, and, if that is the "
                "case, to perform the euthanasia using anesthesia and analgesia;\n\n"
                "(d) measures to prevent and control external and internal parasites, and vaccinations to prevent "
                "common diseases to which dogs or cats are likely to be exposed are implemented.\n\n"
                "Operators of breeding establishments shall additionally ensure that:\n"
                "(-a) bitches or queens are only bred if they have reached a minimum age and skeletal maturity "
                "in accordance with point 3 of Annex I, and they have no diagnosed disease, clinical sign of "
                "diseases or physical conditions which could negatively impact their pregnancy and welfare;\n"
                "(-b) litter-giving pregnancies of bitches or queens follows a maximum frequency in accordance "
                "with point 3 of Annex I;\n"
                "(-c) lactating queens are not mated or inseminated."
            ),
            "traducao": (
                "Os operadores devem assegurar que:\n\n"
                "(a) os cães e gatos sob a sua responsabilidade são inspecionados por cuidadores pelo menos uma "
                "vez por dia, e os animais vulneráveis, como recém-nascidos, doentes, lesionados, fêmeas em "
                "período peri-parto, são inspecionados com maior frequência;\n\n"
                "(b) os cães e gatos com bem-estar comprometido são transferidos, quando necessário, sem demora "
                "injustificada para área separada e, se necessário, recebem tratamento adequado;\n\n"
                "(c) quando a recuperação de um animal com bem-estar comprometido não seja alcançável e o animal "
                "experiencie dor ou sofrimento severo, um médico veterinário é consultado sem demora injustificada "
                "para decidir sobre a eutanásia, que, se realizada, é executada com anestesia e analgesia;\n\n"
                "(d) são implementadas medidas de prevenção e controlo de parasitas externos e internos, bem como "
                "vacinações para prevenção de doenças comuns.\n\n"
                "Os operadores de estabelecimentos de criação devem adicionalmente assegurar que:\n"
                "(-a) as cadelas ou gatas só são reproduzidas se tiverem atingido a idade mínima e maturidade "
                "esquelética nos termos do Anexo I, e não apresentem doença diagnosticada, sinais clínicos ou "
                "condições físicas que possam impactar negativamente a gestação e o bem-estar;\n"
                "(-b) a frequência de gestações com ninhadas respeita o máximo fixado no Anexo I;\n"
                "(-c) as gatas a lactar não são acasaladas nem inseminadas."
            ),
        },
        "rgbeac": {
            "ref": "n.ºs 1, 2 e 3 do art.º 33.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "1 — Os detentores dos animais de companhia devem assegurar-lhes os cuidados de saúde adequados, "
                "nomeadamente seguindo as orientações da DGAV em matéria de vacinação e tratamentos obrigatórios, "
                "bem como consultas regulares junto de médico veterinário.\n\n"
                "2 — Os animais que apresentem sinais que levem a suspeitar de poderem estar doentes ou "
                "lesionados devem receber os primeiros cuidados pelo detentor e, se não houver indícios de "
                "recuperação, devem ser tratados por médico veterinário.\n\n"
                "3 — Os médicos veterinários e os centros de atendimento médico-veterinário (CAMV) devem manter "
                "um arquivo com os dados clínicos de cada animal, pelo período mínimo de cinco anos, que ficará "
                "à disposição das autoridades competentes."
            ),
        },
        "codigo": {
            "ref": "art.º 6.º do Código do Animal (DL n.º 214/2013)",
            "texto": (
                "O detentor do animal deve assegurar ao animal ferido ou doente os cuidados médico-veterinários "
                "adequados, designadamente retirando o mesmo do alojamento sempre que este seja um local de venda."
            ),
        },
        "legislacao": {
            "ref": "n.ºs 1 e 3 do art.º 13.º e n.ºs 1 e 2 do art.º 16.º do DL n.º 276/2001, de 17 de outubro",
            "texto": (
                "Artigo 13.º, n.º 1 — A observação diária dos animais e o seu maneio, a organização da dieta e "
                "o tratamento médico-veterinário devem ser assegurados por pessoal técnico competente e em número "
                "adequado à quantidade e espécies animais que alojam.\n\n"
                "Artigo 13.º, n.º 3 — Todos os animais devem ser alvo de inspeção diária, sendo de imediato "
                "prestados os primeiros cuidados aos que tiverem sinais que levem a suspeitar estarem doentes, "
                "lesionados ou com alterações comportamentais.\n\n"
                "Artigo 16.º, n.º 1 — Sem prejuízo de quaisquer medidas determinadas pela DGAV, deve existir um "
                "programa de profilaxia médica e sanitária devidamente elaborado e supervisionado pelo médico "
                "veterinário responsável e executado por profissionais competentes.\n\n"
                "Artigo 16.º, n.º 2 — No âmbito do número anterior, os animais devem ser sujeitos a exames "
                "médico-veterinários de rotina, vacinações e desparasitações sempre que aconselhável."
            ),
        },
        "divergencia": (
            "O @regulamento impõe inspeção diária por cuidadores, isolamento imediato de animais com bem-estar "
            "comprometido e condições específicas para reprodução em criadores (idade mínima da fêmea, frequência "
            "máxima de partos por ninhada, proibição de cobrição de gatas a lactar). A @legislacao (DL n.º "
            "276/2001, art.ºs 13.º e 16.º) prevê inspeção diária e programa de profilaxia supervisionado por "
            "veterinário — alinhamento parcial com o @regulamento — mas não fixa condições sanitárias específicas "
            "para a reprodução em criadores. O @rgbeac (art.º 33.º) centra os cuidados de saúde no detentor em "
            "geral, sem distinguir obrigações reforçadas para operadores de criação. O @codigo (art.º 6.º) limita "
            "o dever de cuidados médico-veterinários ao animal ferido ou doente, sem obrigação de inspeção "
            "sistemática nem regras sanitárias de criação. A @legislacao vigente é a mais próxima do @regulamento "
            "neste eixo, mas apresenta lacuna relevante nas condições sanitárias específicas da reprodução."
        ),
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
]

# ---------------------------------------------------------------------------
# CORES (sistema cromático por diploma)
# ---------------------------------------------------------------------------

COR = {
    "regulamento_header": "1A3A5C",   # azul escuro
    "regulamento_body":   "D6E4F0",   # azul claro
    "regulamento_trad":   "EBF5FB",   # azul muito claro (tradução)
    "rgbeac_header":      "1E5631",   # verde escuro
    "rgbeac_body":        "D5E8D4",   # verde claro
    "codigo_header":      "7E4C00",   # castanho escuro
    "codigo_body":        "FFE6CC",   # castanho claro
    "legislacao_header":  "006064",   # verde-azul escuro (teal)
    "legislacao_body":    "E0F7FA",   # verde-azul muito claro
    "divergencia_header": "5D2A8A",   # roxo escuro
    "divergencia_body":   "EAD7F7",   # roxo claro
    "notas_header":       "4A4A4A",   # cinza escuro
    "notas_body":         "F5F5F5",   # cinza muito claro
    "tema_header":        "1A1A2E",   # quase preto
    "alternado_a":        "FAFAFA",
    "alternado_b":        "F0F4FF",
}

def fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def font_white_bold(size=10):
    return Font(color="FFFFFF", bold=True, size=size, name="Calibri")

def font_normal(size=10, bold=False, color="000000"):
    return Font(size=size, bold=bold, color=color, name="Calibri")

def border_thin():
    s = Side(style="thin", color="CCCCCC")
    return Border(left=s, right=s, top=s, bottom=s)

def wrap_align(horizontal="left", vertical="top"):
    return Alignment(horizontal=horizontal, vertical=vertical, wrap_text=True)

# ---------------------------------------------------------------------------
# EXCEL
# ---------------------------------------------------------------------------

def criar_excel(path):
    wb = openpyxl.Workbook()

    # --- Folha 1: Vista de Reunião (dados completos) ---
    ws = wb.active
    ws.title = "Vista de Reunião"
    ws.sheet_view.showGridLines = False

    # Cabeçalhos
    headers = [
        ("Tema", 18),
        ("Art. @regulamento", 22),
        ("Texto @regulamento (EN)", 55),
        ("Tradução @regulamento (PT)", 55),
        ("Art. @rgbeac", 22),
        ("Texto @rgbeac", 55),
        ("Art. @codigo", 22),
        ("Texto @codigo", 55),
        ("Art. @legislacao", 22),
        ("Texto @legislacao (vigente)", 55),
        ("Divergência face ao Regulamento", 42),
        ("Necessidade de Alteração", 14),
        ("Notas de Reunião", 40),
    ]

    for col_idx, (header, width) in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.fill = fill(COR["tema_header"])
        cell.font = font_white_bold(11)
        cell.alignment = wrap_align("center", "center")
        cell.border = border_thin()
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    ws.row_dimensions[1].height = 30

    # Dados
    bg_toggle = [COR["alternado_a"], COR["alternado_b"]]
    for row_idx, art in enumerate(ARTIGOS, start=2):
        bg = bg_toggle[(row_idx) % 2]
        valores = [
            art["tema"],
            art["regulamento"]["ref"],
            art["regulamento"]["texto"],
            art["regulamento"]["traducao"],
            art["rgbeac"]["ref"],
            art["rgbeac"]["texto"],
            art["codigo"]["ref"],
            art["codigo"]["texto"],
            art["legislacao"]["ref"],
            art["legislacao"]["texto"],
            art["divergencia"],
            art["necessidade_alteracao"],
            art["notas"],
        ]
        for col_idx, valor in enumerate(valores, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=valor)
            cell.alignment = wrap_align()
            cell.border = border_thin()
            # Cor por coluna
            if col_idx in (1,):
                cell.fill = fill(COR["tema_header"])
                cell.font = font_white_bold()
                cell.alignment = wrap_align("center", "center")
            elif col_idx in (2, 3, 4):
                cell.fill = fill(COR["regulamento_body"] if col_idx != 4 else COR["regulamento_trad"])
                cell.font = font_normal()
            elif col_idx in (5, 6):
                cell.fill = fill(COR["rgbeac_body"])
                cell.font = font_normal()
            elif col_idx in (7, 8):
                cell.fill = fill(COR["codigo_body"])
                cell.font = font_normal()
            elif col_idx in (9, 10):
                cell.fill = fill(COR["legislacao_body"])
                cell.font = font_normal()
            elif col_idx == 11:
                cell.fill = fill(COR["divergencia_body"])
                cell.font = font_normal(bold=True)
            elif col_idx == 12:
                cell.fill = fill(COR["divergencia_body"])
                cell.font = Font(bold=True, color="8B0000", size=10, name="Calibri")
                cell.alignment = wrap_align("center", "center")
            elif col_idx == 13:
                cell.fill = fill(COR["notas_body"])
                cell.font = font_normal(color="4A4A4A")
        ws.row_dimensions[row_idx].height = 120

    # Freeze panes
    ws.freeze_panes = "B2"

    # --- Folha 2: Legenda / Sistema de Cores ---
    ws2 = wb.create_sheet("Legenda")
    ws2.sheet_view.showGridLines = False
    ws2.column_dimensions["A"].width = 30
    ws2.column_dimensions["B"].width = 50

    legenda_items = [
        ("DIPLOMA", "COR", True),
        ("@regulamento (texto EN)", COR["regulamento_body"], False),
        ("@regulamento (tradução PT)", COR["regulamento_trad"], False),
        ("@rgbeac", COR["rgbeac_body"], False),
        ("@codigo", COR["codigo_body"], False),
        ("@legislacao (legislação vigente)", COR["legislacao_body"], False),
        ("Divergência", COR["divergencia_body"], False),
        ("Notas de Reunião", COR["notas_body"], False),
    ]
    for i, (label, cor_ou_header, is_header) in enumerate(legenda_items, start=1):
        a = ws2.cell(row=i, column=1, value=label)
        b = ws2.cell(row=i, column=2, value="" if is_header else f"Cor de fundo: #{cor_ou_header}")
        if is_header:
            for c in (a, b):
                c.fill = fill(COR["tema_header"])
                c.font = font_white_bold(12)
                c.alignment = wrap_align("center", "center")
        else:
            a.fill = fill(cor_ou_header)
            b.fill = fill(cor_ou_header)
            a.font = font_normal(bold=True)
            b.font = font_normal()
        for c in (a, b):
            c.border = border_thin()
        ws2.row_dimensions[i].height = 22

    wb.save(path)
    print(f"Excel guardado: {path}")


# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------

def criar_html(path, artigos):
    """Gera visualizador HTML interativo para reunião."""

    # Serializar artigos para JSON (injetado no HTML)
    dados_json = json.dumps(artigos, ensure_ascii=False, indent=2)

    html = f"""<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Comparativo Artigo a Artigo — Regulamento 2023/0447</title>
<style>
  :root {{
    --reg:    #1A3A5C;
    --reg-bg: #D6E4F0;
    --reg-tr: #EBF5FB;
    --rgb:    #1E5631;
    --rgb-bg: #D5E8D4;
    --cod:    #7E4C00;
    --cod-bg: #FFE6CC;
    --leg:    #006064;
    --leg-bg: #E0F7FA;
    --div:    #5D2A8A;
    --div-bg: #EAD7F7;
    --nota:   #4A4A4A;
    --nota-bg:#F5F5F5;
    --dark:   #1A1A2E;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', Calibri, sans-serif; background: #ECEFF4; color: #222; }}

  /* HEADER */
  header {{
    background: var(--dark);
    color: #fff;
    padding: 18px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky; top: 0; z-index: 100;
    box-shadow: 0 2px 8px rgba(0,0,0,0.4);
  }}
  header h1 {{ font-size: 1.1rem; font-weight: 700; letter-spacing: .5px; }}
  header span {{ font-size: .85rem; opacity: .7; }}

  /* LAYOUT */
  .layout {{ display: flex; min-height: calc(100vh - 60px); }}

  /* SIDEBAR */
  nav {{
    width: 220px; min-width: 220px;
    background: var(--dark);
    padding: 24px 0;
    position: sticky; top: 60px;
    height: calc(100vh - 60px);
    overflow-y: auto;
  }}
  nav h2 {{ color: #aaa; font-size: .7rem; text-transform: uppercase;
            letter-spacing: 1.5px; padding: 0 20px 12px; }}
  nav button {{
    display: block; width: 100%;
    background: none; border: none;
    color: #ccc; text-align: left;
    padding: 12px 20px; cursor: pointer;
    font-size: .88rem; line-height: 1.35;
    border-left: 3px solid transparent;
    transition: all .15s;
  }}
  nav button:hover {{ background: rgba(255,255,255,.06); color: #fff; }}
  nav button.active {{
    background: rgba(255,255,255,.1);
    color: #fff; font-weight: 700;
    border-left-color: #7EC8E3;
  }}
  nav button small {{ display: block; font-size: .74rem; opacity: .55; margin-top: 2px; }}

  /* MAIN */
  main {{ flex: 1; padding: 28px 32px; overflow-x: auto; }}

  /* BADGE DE ARTIGO */
  .art-badge {{
    display: inline-block;
    background: var(--dark); color: #fff;
    border-radius: 6px; padding: 4px 14px;
    font-size: .8rem; font-weight: 700;
    margin-bottom: 18px; letter-spacing: .5px;
  }}
  .tema-title {{
    font-size: 1.4rem; font-weight: 700;
    color: var(--dark); margin-bottom: 22px;
    padding-bottom: 10px;
    border-bottom: 3px solid var(--reg);
  }}

  /* GRID 3 COLUNAS (diplomas nacionais) */
  .grid {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-bottom: 20px; }}
  @media (max-width: 1100px) {{ .grid {{ grid-template-columns: 1fr 1fr; }} }}
  @media (max-width: 700px)  {{ .grid {{ grid-template-columns: 1fr; }} }}

  /* CARD */
  .card {{ border-radius: 8px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,.12); }}
  .card-header {{
    padding: 10px 16px; font-size: .78rem;
    font-weight: 700; text-transform: uppercase; letter-spacing: .8px;
    color: #fff; display: flex; align-items: center; gap: 10px;
  }}
  .card-header-ref {{
    font-size: .7rem; font-weight: 400; opacity: .7;
    text-transform: none; letter-spacing: 0;
  }}
  .card-body {{ padding: 14px 16px; font-size: .88rem; line-height: 1.65; }}
  .card-ref {{ font-size: .75rem; font-weight: 700; margin-bottom: 10px; opacity: .75; }}

  .card.reg .card-header {{ background: var(--reg); }}
  .card.reg .card-body   {{ background: var(--reg-bg); }}
  .card.reg-tr .card-header {{ background: #2471A3; }}
  .card.reg-tr .card-body   {{ background: var(--reg-tr); font-style: italic; }}
  .card.rgb .card-header {{ background: var(--rgb); }}
  .card.rgb .card-body   {{ background: var(--rgb-bg); }}
  .card.cod .card-header {{ background: var(--cod); }}
  .card.cod .card-body   {{ background: var(--cod-bg); }}
  .card.leg .card-header {{ background: var(--leg); }}
  .card.leg .card-body   {{ background: var(--leg-bg); }}

  /* DIVERGÊNCIA */
  .div-box {{
    background: var(--div-bg);
    border-left: 5px solid var(--div);
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    margin-bottom: 20px;
    font-size: .88rem; line-height: 1.6;
  }}
  .div-box strong {{ color: var(--div); display: block; margin-bottom: 6px;
                     font-size: .78rem; text-transform: uppercase; letter-spacing: .8px; }}
  .badge-alt {{
    display: inline-block;
    background: #8B0000; color: #fff;
    border-radius: 4px; padding: 2px 10px;
    font-size: .75rem; font-weight: 700; margin-left: 10px;
  }}

  /* NOTAS */
  .notas-box {{ margin-top: 4px; }}
  .notas-box label {{
    display: block; font-size: .78rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: .8px;
    color: var(--nota); margin-bottom: 6px;
  }}
  .notas-box textarea {{
    width: 100%; min-height: 90px;
    border: 2px solid #ccc; border-radius: 6px;
    padding: 10px; font-size: .88rem; font-family: inherit;
    resize: vertical; background: var(--nota-bg);
    transition: border-color .2s;
  }}
  .notas-box textarea:focus {{ outline: none; border-color: var(--div); }}

  /* NAVEGAÇÃO INFERIOR */
  .nav-btns {{
    display: flex; gap: 12px; margin-top: 24px; justify-content: flex-end;
  }}
  .btn {{
    padding: 9px 22px; border: none; border-radius: 6px;
    cursor: pointer; font-size: .9rem; font-weight: 700;
    transition: opacity .15s;
  }}
  .btn:hover {{ opacity: .82; }}
  .btn-prev {{ background: #ddd; color: #333; }}
  .btn-next {{ background: var(--reg); color: #fff; }}
  .btn-export {{ background: var(--rgb); color: #fff; }}

  /* EXPORTAÇÃO */
  #export-msg {{
    display: none; background: #D5E8D4; border: 1px solid var(--rgb);
    border-radius: 6px; padding: 10px 16px; margin-top: 12px;
    font-size: .85rem; color: var(--rgb);
  }}
  pre {{ white-space: pre-wrap; word-break: break-word; }}
  mark {{ background: #FFE066; color: #000; border-radius: 2px; padding: 0 2px; }}

  /* BARRA DE PESQUISA */
  .search-wrap {{ position: relative; }}
  .search-wrap input {{
    padding: 7px 32px 7px 12px;
    border-radius: 6px; border: none;
    font-size: .88rem; width: 240px;
    background: rgba(255,255,255,.14); color: #fff;
    outline: none; transition: background .2s;
  }}
  .search-wrap input::placeholder {{ color: rgba(255,255,255,.4); }}
  .search-wrap input:focus {{ background: rgba(255,255,255,.24); }}
  .search-wrap .clear-btn {{
    position: absolute; right: 8px; top: 50%; transform: translateY(-50%);
    background: none; border: none; color: rgba(255,255,255,.55);
    cursor: pointer; font-size: 1rem; line-height: 1; padding: 0;
    display: none;
  }}
  .search-count {{ color: #90b0c8; font-size: .73rem; padding: 2px 20px 8px; }}
</style>
</head>
<body>

<header>
  <h1>Comparativo Artigo a Artigo — Regulamento 2023/0447 (Cães e Gatos)</h1>
  <div style="display:flex;align-items:center;gap:16px;">
    <div class="search-wrap">
      <input id="search-input" type="search"
             placeholder="🔍 Pesquisar palavra-chave…"
             oninput="pesquisar(this.value)"
             autocomplete="off">
      <button class="clear-btn" id="clear-btn"
              onclick="limparPesquisa()" title="Limpar pesquisa">✕</button>
    </div>
    <span id="progresso"></span>
  </div>
</header>

<div class="layout">
  <nav id="sidebar">
    <h2>Artigos</h2>
  </nav>
  <main id="main-content"></main>
</div>

<script>
const ARTIGOS = {dados_json};

let atual = 0;
let searchTerm = '';

/* ---- PESQUISA ---- */
function pesquisar(q) {{
  searchTerm = q.trim().toLowerCase();
  const clearBtn = document.getElementById('clear-btn');
  if (clearBtn) clearBtn.style.display = searchTerm ? 'block' : 'none';
  if (searchTerm) {{
    const primeiroIdx = ARTIGOS.findIndex(a => artMatch(a, searchTerm));
    if (primeiroIdx >= 0 && !artMatch(ARTIGOS[atual], searchTerm)) {{
      atual = primeiroIdx;
    }}
  }}
  render();
}}

function limparPesquisa() {{
  searchTerm = '';
  const inp = document.getElementById('search-input');
  if (inp) inp.value = '';
  const clearBtn = document.getElementById('clear-btn');
  if (clearBtn) clearBtn.style.display = 'none';
  render();
}}

function artMatch(art, q) {{
  const campos = [
    art.id, art.tema,
    art.regulamento.ref, art.regulamento.texto, art.regulamento.traducao,
    art.rgbeac.ref, art.rgbeac.texto,
    art.codigo.ref, art.codigo.texto,
    art.legislacao.ref, art.legislacao.texto,
    art.divergencia
  ];
  return campos.some(c => (c || '').toLowerCase().includes(q));
}}

function getSnippet(art, q) {{
  const campos = [
    art.regulamento.texto, art.regulamento.traducao,
    art.rgbeac.texto, art.codigo.texto,
    art.legislacao.texto, art.divergencia
  ];
  for (const c of campos) {{
    const idx = (c || '').toLowerCase().indexOf(q);
    if (idx >= 0) {{
      const s = Math.max(0, idx - 28);
      const e = Math.min(c.length, idx + q.length + 40);
      return (s > 0 ? '…' : '') +
             c.slice(s, e).replace(/\\n/g, ' ') +
             (e < c.length ? '…' : '');
    }}
  }}
  return '';
}}

function highlight(str) {{
  if (!searchTerm || !str) return nl2br(str || '');
  const re = new RegExp(searchTerm.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&'), 'gi');
  return nl2br(str.replace(re, m => `<mark>${{m}}</mark>`));
}}

/* ---- SIDEBAR ---- */
function renderSidebar() {{
  const nav = document.getElementById('sidebar');
  nav.innerHTML = '<h2>Artigos</h2>';
  let nResultados = 0;
  ARTIGOS.forEach((art, i) => {{
    const mostrar = !searchTerm || artMatch(art, searchTerm);
    if (!mostrar) return;
    nResultados++;
    const btn = document.createElement('button');
    const snippet = searchTerm ? getSnippet(art, searchTerm) : '';
    btn.innerHTML =
      `<b>${{art.id}}</b><small>${{art.tema}}</small>` +
      (snippet ? `<em style="font-size:.7rem;opacity:.65;display:block;margin-top:3px;font-style:normal;">${{
        snippet.replace(new RegExp(searchTerm.replace(/[.*+?^${{}}()|[\\]\\\\]/g,'\\\\$&'),'gi'),
                        m => `<mark>${{m}}</mark>`)
      }}</em>` : '');
    btn.className = i === atual ? 'active' : '';
    btn.onclick = () => {{ atual = i; render(); }};
    nav.appendChild(btn);
  }});
  if (searchTerm) {{
    const ct = document.createElement('div');
    ct.className = 'search-count';
    ct.textContent = nResultados > 0
      ? `${{nResultados}} resultado(s) para "${{searchTerm}}"`
      : 'Sem resultados.';
    nav.insertBefore(ct, nav.children[1]);
  }}
}}

/* ---- UTILIDADES ---- */
function nl2br(str) {{
  return (str || '').replace(/\\n/g, '<br>');
}}

function render() {{
  const art = ARTIGOS[atual];
  renderSidebar();
  document.getElementById('progresso').textContent =
    `${{atual + 1}} / ${{ARTIGOS.length}}`;

  document.getElementById('main-content').innerHTML = `
    <div class="art-badge">${{art.id}}</div>
    <div class="tema-title">${{art.tema}}</div>

    <div class="card reg-tr" style="margin-bottom:14px;">
      <div class="card-header">
        @regulamento — Tradução PT-PT
        <span class="card-header-ref">${{art.regulamento.ref}}</span>
      </div>
      <div class="card-body">
        <pre>${{highlight(art.regulamento.traducao)}}</pre>
      </div>
    </div>

    <div class="card reg" style="margin-bottom:20px;">
      <div class="card-header">@regulamento — Texto original EN</div>
      <div class="card-body">
        <pre>${{highlight(art.regulamento.texto)}}</pre>
      </div>
    </div>

    <div class="grid">
      <div class="card rgb">
        <div class="card-header">@rgbeac (proposta jun. 2025)</div>
        <div class="card-body">
          <div class="card-ref">${{art.rgbeac.ref}}</div>
          <pre>${{highlight(art.rgbeac.texto)}}</pre>
        </div>
      </div>
      <div class="card cod">
        <div class="card-header">@codigo (DL n.º 214/2013)</div>
        <div class="card-body">
          <div class="card-ref">${{art.codigo.ref}}</div>
          <pre>${{highlight(art.codigo.texto)}}</pre>
        </div>
      </div>
      <div class="card leg">
        <div class="card-header">@legislacao (legislação vigente)</div>
        <div class="card-body">
          <div class="card-ref">${{art.legislacao.ref}}</div>
          <pre>${{highlight(art.legislacao.texto)}}</pre>
        </div>
      </div>
    </div>

    <div class="div-box">
      <strong>Divergência face ao Regulamento
        <span class="badge-alt">Necessidade de alteração: ${{art.necessidade_alteracao}}</span>
      </strong>
      ${{highlight(art.divergencia)}}
    </div>

    <div class="notas-box">
      <label>Notas de Reunião</label>
      <textarea id="notas-input" placeholder="Escreve aqui as decisões ou observações da reunião..."
        oninput="ARTIGOS[${{atual}}].notas = this.value">${{art.notas}}</textarea>
    </div>

    <div class="nav-btns">
      ${{atual > 0 ? '<button class="btn btn-prev" onclick="navegar(-1)">← Anterior</button>' : ''}}
      <button class="btn btn-export" onclick="exportarNotas()">Exportar Notas (CSV)</button>
      ${{atual < ARTIGOS.length - 1 ? '<button class="btn btn-next" onclick="navegar(1)">Próximo →</button>' : ''}}
    </div>
    <div id="export-msg"></div>
  `;
}}

function navegar(dir) {{
  atual = Math.max(0, Math.min(ARTIGOS.length - 1, atual + dir));
  render();
  window.scrollTo({{top: 0, behavior: 'smooth'}});
}}

function exportarNotas() {{
  const linhas = [['ID', 'Tema', 'Art. Regulamento', 'Art. RGBEAC', 'Art. Código', 'Art. Legislação Vigente', 'Notas de Reunião']];
  ARTIGOS.forEach(a => {{
    linhas.push([
      a.id, a.tema,
      a.regulamento.ref, a.rgbeac.ref, a.codigo.ref,
      a.legislacao.ref,
      a.notas
    ]);
  }});
  const csv = linhas.map(r => r.map(c => `"${{String(c).replace(/"/g,'""')}}"`).join(',')).join('\\n');
  const blob = new Blob([csv], {{type: 'text/csv;charset=utf-8;'}});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = 'notas_reuniao_regulamento.csv';
  document.body.appendChild(a); a.click(); document.body.removeChild(a);
  const msg = document.getElementById('export-msg');
  if (msg) {{ msg.style.display = 'block'; msg.textContent = 'CSV exportado com as notas da reunião.'; }}
}}

// Iniciar
render();
</script>
</body>
</html>
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML guardado: {path}")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    criar_excel(os.path.join(base, "comparativo_reuniao_exemplo.xlsx"))
    criar_html(os.path.join(base, "comparativo_reuniao_exemplo.html"), ARTIGOS)
    print("Concluído.")
