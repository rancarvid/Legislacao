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
        "id": "ART-05",
        "tema": "Princípios Gerais de Bem-Estar",
        "regulamento": {
            "ref": "Art.º 5.º do Regulamento 2023/0447",
            "titulo": "General welfare principles",
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
        "divergencia": {
            "legislacao": (
                "O DL n.º 276/2001 (art.ºs 7.º e 9.º) consagra os mesmos parâmetros mas desenvolve-os "
                "em artigos separados (alojamento, alimentação, ambiente) sem os denominar como domínios "
                "nem os sistematizar de forma unificada segundo o referencial OMSA."
            ),
            "codigo": (
                "O @codigo (art.º 5.º) refere 'parâmetros de bem-estar animal' genericamente, sem adotar "
                "formalmente a nomenclatura dos 5 domínios OMSA nem a sua sistematização explícita."
            ),
            "rgbeac": (
                "O @rgbeac (art.º 10.º, n.º 1, al. a)) articula obrigações equivalentes ao nível do "
                "detentor de forma descritiva, sem sistematização nos 5 domínios nem referência ao "
                "quadro OMSA."
            ),
            "sumario": (
                "Alinhamento substancial de conteúdo; sem necessidade de alteração imediata. Recomenda-se "
                "a adoção formal dos 5 domínios OMSA como referencial estruturante em futura revisão "
                "legislativa ou em normas de orientação técnica da DGAV."
            ),
        },
        "necessidade_alteracao": "Não",
        "notas": "",
    },
    {
        "id": "ART-06",
        "tema": "Bem-Estar e Detenção",
        "regulamento": {
            "ref": "Art.º 6.º do Regulamento 2023/0447",
            "titulo": "General welfare obligations",
            "texto": (
                "1. Operators shall be responsible for the welfare of dogs or cats kept in the establishments "
                "under their responsibility and under their control and to minimise any risks to their welfare.\n\n"
                "1a. In the case of foster homes, the responsibility shall lie with the operator on whose behalf "
                "dogs or cats are kept. Such operators shall not place more than a total of five dogs or cats or "
                "one litter with or without mother in a foster home at any given time and shall provide the foster "
                "family with adequate information on the animal welfare obligations as well as the individual needs "
                "of the dogs or cats, and shall ensure that the relevant obligations set out by this Regulation "
                "are complied with in foster homes. Member States where the foster home is located may provide for a "
                "greater number of dogs, cats or litters to be placed in the foster home, provided that the premises of "
                "the foster home provide sufficient space, including outdoor space, and that the number of animal caretakers "
                "in the foster home is sufficient, to ensure the welfare of the dogs or cats.\n\n"
                "1b. Operators shall not subject any dog or cat to cruelty, abuse or mistreatment, including through "
                "participation in activities likely to result in cruelty, abuse or mistreatment, to the dogs or cats bred "
                "or kept by the operator.\n\n"
                "1c. Operators shall not abandon dogs or cats.\n\n"
                "1d. Operators who are due to cease the activities of their establishment shall ensure the rehoming of the "
                "dogs or cats kept therein either by taking up the pet ownership or by transferring the responsibility or "
                "ownership of dogs and cats to other operators or acquirers.\n\n"
                "2. Operators shall ensure that dogs or cats are handled by a suitable number of animal caretakers and in order "
                "to meet the welfare needs of dogs or cats kept in their establishments and who have the competences required under "
                "Article 9.\n\n"
                "2a. Operators shall ensure the welfare of the dogs or cats under their responsibility by monitoring animal-based "
                "indicators concerning behaviour and physical appearance, and by taking actions based on the results of such monitoring.\n\n"
                "2b. The Commission is empowered to adopt delegated acts in accordance with Article 23 supplementing this Regulation "
                "by laying down animal-based indicators concerning behaviour and physical appearance and the methods of their measurement."
            ),
            "traducao": (
                "1. Os operadores são responsáveis pelo bem-estar dos cães ou gatos mantidos nos estabelecimentos "
                "sob a sua responsabilidade e controlo e devem minimizar quaisquer riscos para o seu bem-estar.\n\n"
                "1a. No caso de famílias de acolhimento, a responsabilidade recai sobre o operador em nome de quem "
                "os cães ou gatos são mantidos. Esses operadores não devem colocar mais do que um total de cinco "
                "cães ou gatos ou uma ninhada com ou sem mãe numa família de acolhimento em qualquer momento e "
                "devem fornecer à família de acolhimento informação adequada sobre as obrigações de bem-estar "
                "animal, bem como as necessidades individuais dos animais, e devem assegurar que as obrigações relevantes "
                "estabelecidas por este Regulamento são cumpridas em famílias de acolhimento. Os Estados-Membros onde a "
                "família de acolhimento está localizada podem prever um número maior de cães, gatos ou ninhadas a serem colocadas "
                "na família de acolhimento, desde que as instalações da família de acolhimento providenciem espaço suficiente, "
                "incluindo espaço ao ar livre, e que o número de cuidadores de animais na família de acolhimento seja suficiente, "
                "para assegurar o bem-estar dos cães ou gatos.\n\n"
                "1b. Os operadores não devem sujeitar nenhum cão ou gato a crueldade, abuso ou maus-tratos, incluindo através de "
                "participação em atividades que possam resultar em crueldade, abuso ou maus-tratos, aos cães ou gatos criados ou "
                "mantidos pelo operador.\n\n"
                "1c. Os operadores não devem abandonar cães ou gatos.\n\n"
                "1d. Os operadores que estejam prestes a cessar as atividades do seu estabelecimento devem assegurar a reintegração "
                "dos cães ou gatos mantidos aí, quer através da assunção da posse do animal de companhia, quer através da transferência "
                "da responsabilidade ou propriedade dos cães e gatos para outros operadores ou adquirentes.\n\n"
                "2. Os operadores devem assegurar que os cães ou gatos são tratados por um número adequado de cuidadores de animais e "
                "de modo a satisfazer as necessidades de bem-estar dos cães ou gatos mantidos nos seus estabelecimentos e que têm as "
                "competências exigidas no artigo 9.º.\n\n"
                "2a. Os operadores devem assegurar o bem-estar dos cães ou gatos sob a sua responsabilidade através da monitorização "
                "de indicadores baseados no comportamento e aparência física, e através da adoção de ações com base nos resultados de "
                "tal monitorização.\n\n"
                "2b. A Comissão tem competência para adotar atos delegados em conformidade com o artigo 23.º que complementem este "
                "Regulamento através do estabelecimento de indicadores baseados no bem-estar dos animais relativos ao comportamento e "
                "aparência física e dos métodos da sua medição."
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
        "divergencia": {
            "legislacao": (
                "O DL n.º 276/2001 (art.º 7.º) centra a responsabilidade no detentor em geral, sem distinguir "
                "o contexto de acolhimento temporário nem fixar limites numéricos de animais por família. "
                "O conceito de família de acolhimento é inexistente na legislação vigente."
            ),
            "codigo": (
                "O @codigo não prevê o conceito de família de acolhimento nem qualquer limite numérico de "
                "animais por unidade. A responsabilidade do operador como figura distinta do detentor "
                "particular também não é contemplada."
            ),
            "rgbeac": (
                "O @rgbeac menciona famílias de acolhimento temporário mas não fixa o limite de 5 animais "
                "por família de acolhimento nem especifica que a responsabilidade jurídica recai sobre o "
                "operador e não sobre a família."
            ),
            "sumario": (
                "Lacuna transversal a toda a legislação nacional. Necessidade de: (1) criar o conceito de "
                "'família de acolhimento' como extensão da atividade do operador; (2) fixar limite numérico "
                "de animais por família (máximo 5, ou 1 ninhada com mãe); (3) atribuir responsabilidade "
                "jurídica ao operador, não à família de acolhimento."
            ),
        },
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
    {
        "id": "ART-06a",
        "tema": "Estratégias de Criação — Conformação e Consanguinidade",
        "regulamento": {
            "ref": "Art.º 6.º-A do Regulamento 2023/0447",
            "titulo": "Breeding strategies obligations",
            "texto": (
                "1. Operators of breeding establishments shall ensure that their breeding strategies minimise the "
                "risk of producing dogs or cats with genotypes associated with detrimental effects on their health "
                "and welfare.\n\n"
                "2. Operators of breeding establishments shall not use for reproduction dogs or cats that have "
                "excessive conformational traits leading to a high risk of detrimental effects on the welfare of "
                "these dogs or cats, or of their offspring. Before selection for breeding of a dog or cat that may "
                "be concerned by an excessive conformational trait the operator shall consult a veterinarian or an "
                "independent qualified person under the responsibility of a veterinarian. The veterinarian or "
                "independent qualified person shall assess whether the dog or cat has an excessive conformational trait.\n\n"
                "3. The Commission is empowered to adopt, taking into account scientific opinions of the European "
                "Food Safety Authority as well as the social and economic impacts, delegated acts in accordance with "
                "Article 23 supplementing this Regulation by:\n"
                "(a) defining characteristics of the genotypes referred to in paragraph 1, which shall be excluded "
                "from reproduction, and the methods for their assessment and the record keeping requirements;\n"
                "(b) defining excessive conformational traits referred to in paragraph 2 of this Article, which shall "
                "be excluded from reproduction, the methods for their assessment and the record keeping requirements.\n\n"
                "4. The delegated acts concerning the excessive conformational traits shall be adopted by 1 July 2030. "
                "The delegated acts concerning the genotypes shall be adopted by 1 July 2036.\n\n"
                "5. The following shall be prohibited in the management of the reproduction of dogs and cats:\n"
                "(a) the breeding between parents and offspring, between siblings, between half-siblings or "
                "between grandparents and grandchildren, unless approved by the competent authority based on a "
                "specific need to preserve local breeds with a limited genetic pool;\n"
                "(b) the breeding to produce hybrids."
            ),
            "traducao": (
                "1. Os operadores de estabelecimentos de criação devem assegurar que as suas estratégias de criação "
                "minimizam o risco de produzir cães ou gatos com genótipos associados a efeitos prejudiciais para "
                "a sua saúde e bem-estar.\n\n"
                "2. Os operadores de estabelecimentos de criação não devem utilizar para reprodução cães ou gatos "
                "que apresentem traços conformacionais excessivos que conduzam a um risco elevado de efeitos "
                "prejudiciais para o bem-estar desses animais ou das suas crias. Antes da seleção para reprodução "
                "de um animal potencialmente afetado por traço conformacional excessivo, o operador deve consultar "
                "um médico veterinário ou uma pessoa qualificada independente sob responsabilidade veterinária. O "
                "médico veterinário ou a pessoa qualificada independente devem avaliar se o animal tem um traço "
                "conformacional excessivo.\n\n"
                "3. A Comissão tem competência para adotar, tendo em conta os pareceres científicos da Autoridade "
                "Europeia para a Segurança dos Alimentos, bem como os impactos sociais e económicos, atos delegados "
                "em conformidade com o artigo 23.º que complementem este Regulamento:\n"
                "(a) definindo características dos genótipos a que se refere o parágrafo 1, que devem ser excluídos "
                "da reprodução, e os métodos para a sua avaliação e requisitos de manutenção de registos;\n"
                "(b) definindo traços conformacionais excessivos a que se refere o parágrafo 2 do presente artigo, "
                "que devem ser excluídos da reprodução, os métodos para a sua avaliação e requisitos de manutenção de "
                "registos.\n\n"
                "4. Os atos delegados relativos aos traços conformacionais excessivos devem ser adotados até 1 de julho "
                "de 2030. Os atos delegados relativos aos genótipos devem ser adotados até 1 de julho de 2036.\n\n"
                "5. São proibidos na gestão da reprodução de cães e gatos:\n"
                "(a) o cruzamento entre progenitores e descendentes, entre irmãos, entre meios-irmãos ou entre avós e "
                "netos, exceto com aprovação da autoridade competente por razão de necessidade específica de preservação "
                "de raças locais com reserva genética limitada;\n"
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
        "divergencia": {
            "legislacao": (
                "O DL n.º 276/2001 (art.ºs 17.º e 18.º) exige intervenção veterinária em cirurgias e "
                "documentação para amputações, mas não prevê qualquer restrição à reprodução por traços "
                "conformacionais excessivos nem proibição de consanguinidade próxima ou hibridação."
            ),
            "codigo": (
                "O @codigo (art.º 8.º, n.º 2) exclui da reprodução animais com defeitos genéticos e "
                "malformações (displasia, rim poliquístico) e proíbe cios sucessivos, mas não prevê "
                "o conceito de traços conformacionais excessivos nem a proibição de consanguinidade."
            ),
            "rgbeac": (
                "O @rgbeac (art.º 34.º) proíbe intervenções cirúrgicas de modificação da aparência, "
                "mas não contém qualquer norma sobre estratégia genética de criação, conformação "
                "excessiva ou consanguinidade."
            ),
            "sumario": (
                "Lacuna normativa transversal. Necessidade de criar norma específica que: (1) defina "
                "traços conformacionais excessivos (a regular por ato delegado europeu até 2030); "
                "(2) proíba consanguinidade próxima (pais/filhos, irmãos, avós/netos); (3) proíba "
                "a produção de híbridos; (4) imponha consulta veterinária prévia ao acasalamento "
                "de animais potencialmente afetados."
            ),
        },
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
    {
        "id": "ART-07",
        "tema": "Reprodução e Criação",
        "regulamento": {
            "ref": "Art.º 7.º do Regulamento 2023/0447",
            "titulo": "Notification and registration of establishments",
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
        "divergencia": {
            "legislacao": (
                "O DL n.º 276/2001 (art.º 3.º-A) prevê comunicação prévia à DGAV com elementos "
                "parcialmente equivalentes (capacidade máxima, espécies, raças). Não exige a estimativa "
                "anual de ninhadas a colocar no mercado (al. ea) do @regulamento), constituindo lacuna "
                "parcial. É o diploma mais próximo do @regulamento neste eixo."
            ),
            "codigo": (
                "O @codigo regula condições de reprodução (art.º 8.º) mas não prevê qualquer sistema "
                "de notificação ou registo de estabelecimentos criadores junto da autoridade competente."
            ),
            "rgbeac": (
                "O @rgbeac trata da esterilização de errantes e CED, mas não contém norma sobre "
                "notificação de criadores ou registo de estabelecimentos com fins de reprodução comercial."
            ),
            "sumario": (
                "A @legislacao vigente é o diploma base adequado para a transposição. Necessidade de ajuste: "
                "acrescentar a obrigação de estimativa anual de ninhadas a colocar no mercado e alinhar "
                "os restantes elementos informativos com a lista exaustiva do art.º 7.º do @regulamento."
            ),
        },
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
    {
        "id": "ART-08",
        "tema": "Detenção Responsável e Informação",
        "regulamento": {
            "ref": "Art.º 8.º do Regulamento 2023/0447",
            "titulo": "Obligation of informing on responsible ownership",
            "texto": (
                "Operators shall provide to the acquirer of a dog or cat written information necessary to enable "
                "him or her to ensure the welfare of the dog or cat including information on responsible ownership and "
                "on the specific needs of the dog or cat in terms of feeding, caring, health, housing and behavioural needs, "
                "as well as information on its health.\n\n"
                "1a. The written information on the dog or cat's health referred to in the first paragraph shall include at least:\n"
                "(a) the dog or cat's vaccination status;\n"
                "(b) any medical conditions or predispositions to diseases, including allergies, that are known by the operator, "
                "and any diagnostic test results for the dog or cat that are available to the operator.\n\n"
                "In case the information on the dog's or cat's health is documented in a document required under Regulation "
                "(EU) 2016/429, the operator shall transmit that document to the acquirer."
            ),
            "traducao": (
                "Os operadores devem fornecer ao adquirente de um cão ou gato informação escrita necessária para lhe permitir "
                "assegurar o bem-estar do cão ou gato, incluindo informação sobre detenção responsável e sobre as necessidades "
                "específicas do cão ou gato em termos de alimentação, cuidados, saúde, alojamento e necessidades comportamentais, "
                "bem como informação sobre a sua saúde.\n\n"
                "1a. A informação escrita sobre a saúde do cão ou gato referida no parágrafo anterior deve incluir pelo menos:\n"
                "(a) o estado de vacinação do cão ou gato;\n"
                "(b) quaisquer condições médicas ou predisposições a doenças, incluindo alergias, conhecidas pelo operador, "
                "e quaisquer resultados de testes de diagnóstico para o cão ou gato que estejam disponíveis para o operador.\n\n"
                "Caso a informação sobre a saúde do cão ou gato esteja documentada num documento exigido sob o Regulamento "
                "(UE) 2016/429, o operador deve transmitir esse documento ao adquirente."
            ),
        },
        "rgbeac": {
            "ref": "Art.º 8.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "1 — O detentor do animal de companhia deve possuir informação sobre as obrigações inerentes à sua detenção, "
                "incluindo direitos e responsabilidades, normas de bem-estar, cuidados de saúde, comportamento, necessidades "
                "específicas da espécie/raça, duração de vida esperada, custos de manutenção, e proibição de abandono.\n\n"
                "2 — Os comerciantes devem fornecer por escrito ao adquirente informação completa antes da transferência do animal, "
                "incluindo identidade e dados de contacto do comerciante, dados de identificação do animal, cuidados de saúde e "
                "estado de vacinação, e certificado de origem ou de compatibilidade quando aplicável."
            ),
        },
        "codigo": {
            "ref": "Art.º 57.º do Código do Animal (DL n.º 214/2013)",
            "texto": (
                "1 — O detentor do animal deve ter acesso a informação sobre:\n\n"
                "a) As obrigações inerentes à sua detenção, direitos e responsabilidades;\n"
                "b) As normas de bem-estar, cuidados de saúde e comportamento esperado;\n"
                "c) As necessidades específicas da espécie ou raça;\n"
                "d) A duração de vida esperada;\n"
                "e) Os custos de manutenção;\n"
                "f) A proibição de abandono.\n\n"
                "2 — Os criadores e comerciantes devem fornecer informação escrita completa ao adquirente antes da transferência "
                "do animal, incluindo dados de identificação e cuidados de saúde."
            ),
        },
        "legislacao": {
            "ref": "Art.º 20.º do DL n.º 276/2001, de 17 de outubro",
            "texto": (
                "1 — O proprietário ou detentor de animal de companhia deve ter acesso a informação adequada sobre as suas obrigações "
                "relativas ao bem-estar do animal.\n\n"
                "2 — Os detentores de animais de companhia que os comercializem devem fornecer informação ao adquirente sobre o estado "
                "de saúde do animal e vacinas efetuadas."
            ),
        },
        "divergencia": {
            "legislacao": (
                "O DL n.º 276/2001 (art.º 20.º) é genérico e não especifica a forma escrita nem detalhes de conteúdo. O @regulamento "
                "exige informação escrita sobre necessidades específicas de bem-estar (alimentação, cuidados, saúde, alojamento, comportamento) "
                "e condiciona a transferência à transmissão dessa informação."
            ),
            "codigo": (
                "O @codigo (art.º 57.º) exige informação escrita mas com âmbito mais amplo (duração de vida, custos) do que o @regulamento, "
                "que se foca especificamente em bem-estar e saúde."
            ),
            "rgbeac": (
                "O @rgbeac (art.º 8.º) aproxima-se do conteúdo do @regulamento, exigindo informação escrita antes da transferência, "
                "incluindo dados de saúde e vacinação, mas ainda sem o enfoque específico em bem-estar comportamental."
            ),
            "sumario": (
                "Necessidade de alteração: (1) formalizar requisito de informação escrita como condição de transferência de animal; "
                "(2) especificar conteúdo obrigatório sobre bem-estar, saúde e necessidades comportamentais; (3) harmonizar entre @codigo "
                "e @rgbeac quanto a âmbito e forma."
            ),
        },
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
    {
        "id": "ART-09",
        "tema": "Competências de Cuidadores e Bem-Estar Animal",
        "regulamento": {
            "ref": "Art.º 9.º do Regulamento 2023/0447",
            "titulo": "Animal welfare competences of animal caretakers",
            "texto": (
                "1. Animal caretakers, other than volunteers in shelters and interns who are under the responsibility of a competent "
                "animal caretaker, shall have the following competences as regards the dogs and cats they are handling:\n"
                "(a) understanding of their biological behaviour and their physiological and ethological needs;\n"
                "(b) ability to recognise their expressions including any sign of suffering and to identify and take the appropriate "
                "mitigating measures in such cases;\n"
                "(c) ability to apply good animal management practices, including operant conditioning and positive reinforcement, "
                "to use and maintain the equipment used for the dogs or cats under their care and to minimise any risks to the welfare "
                "of the dogs or cats, preventing suffering;\n"
                "(d) knowledge of their obligations under this Regulation.\n\n"
                "2. The competences referred to in paragraph 1 may be acquired through education, training or professional experience. "
                "Education, training or professional experience shall be documented.\n\n"
                "2a. Operators shall ensure that at least one animal caretaker, other than a volunteer or intern, at the establishment has "
                "completed the training courses referred to in Article 18 and that the caretaker transfers the knowledge to the other animal "
                "caretakers of the establishment.\n\n"
                "3. The Commission shall, by means of implementing acts, lay down minimum requirements concerning the formal education, training "
                "or professional experience in order to acquire the competences referred to in paragraph 2 and for the training courses referred to "
                "in paragraph 2a. Those implementing acts shall be adopted in accordance with the examination procedure referred to in Article 24. "
                "The implementing act concerning the training courses referred to in paragraph 2a shall be adopted by [3 years from the date of "
                "entry into force of the Regulation]."
            ),
            "traducao": (
                "1. Os cuidadores de animais, com exceção de voluntários em abrigos e estagiários sob a responsabilidade de um cuidador competente, "
                "devem ter as seguintes competências no que diz respeito aos cães e gatos que manuseiam:\n"
                "(a) compreensão do seu comportamento biológico e das suas necessidades fisiológicas e etológicas;\n"
                "(b) capacidade de reconhecer as suas expressões, incluindo qualquer sinal de sofrimento, e de identificar e adotar as medidas "
                "mitigantes apropriadas nesses casos;\n"
                "(c) capacidade de aplicar boas práticas de maneio de animais, incluindo condicionamento operante e reforço positivo, utilizar "
                "e manter o equipamento utilizado para os cães ou gatos sob os seus cuidados e minimizar quaisquer riscos para o bem-estar dos "
                "cães ou gatos, prevenindo sofrimento;\n"
                "(d) conhecimento das suas obrigações sob este Regulamento.\n\n"
                "2. As competências referidas no parágrafo 1 podem ser adquiridas através de educação, formação ou experiência profissional. "
                "A educação, formação ou experiência profissional devem ser documentadas.\n\n"
                "2a. Os operadores devem assegurar que pelo menos um cuidador de animais, que não seja um voluntário ou estagiário, no estabelecimento "
                "tenha completado os cursos de formação referidos no artigo 18.º e que o cuidador transfira os conhecimentos aos outros cuidadores "
                "de animais do estabelecimento.\n\n"
                "3. A Comissão estabelecerá, por meio de atos de execução, os requisitos mínimos relativos à educação formal, formação ou experiência "
                "profissional para adquirir as competências referidas no parágrafo 2 e para os cursos de formação referidos no parágrafo 2a. Esses "
                "atos de execução serão adotados de acordo com o procedimento de exame referido no artigo 24.º. O ato de execução relativo aos cursos "
                "de formação referidos no parágrafo 2a deve ser adotado por [3 anos da data de entrada em vigor do Regulamento]."
            ),
        },
        "rgbeac": {
            "ref": "Art.ºs 69.º, 84.º e 90.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "Artigo 69.º — Formação\n\n"
                "A reprodução, criação, manutenção, venda ou treino de animais de companhia depende de aprovação em formação sobre detenção "
                "responsável de animais de companhia, bem como sobre as necessidades fisiológicas e etológicas específicas da espécie animal "
                "em causa, ministrada pelo ICNF, I.P. ou entidades por este certificadas.\n\n"
                "Artigo 84.º — Pessoal\n\n"
                "O pessoal responsável pelas tarefas referidas no artigo 82.º deve possuir os conhecimentos e a experiência adequados para as "
                "executar.\n\n"
                "Artigo 90.º — Pessoal\n\n"
                "O pessoal auxiliar deve possuir os conhecimentos e a experiência adequada, o qual fica, contudo, sob a orientação do médico "
                "veterinário responsável."
            ),
        },
        "codigo": {
            "ref": "Art.º 19.º do Código do Animal (DL n.º 214/2013)",
            "texto": (
                "Artigo 19.º — Pessoal auxiliar\n\n"
                "Os alojamentos devem dispor de pessoal auxiliar que possua os conhecimentos e a aptidão necessária para assegurar os cuidados "
                "adequados aos animais, o qual fica sob a orientação do médico veterinário responsável."
            ),
        },
        "legislacao": {
            "ref": "Art.º 13.º do DL n.º 276/2001, de 17 de outubro",
            "texto": (
                "Artigo 13.º — Maneio\n\n"
                "1 — A observação diária dos animais e o seu maneio, a organização da dieta e o tratamento médico-veterinário devem ser "
                "assegurados por pessoal técnico competente e em número adequado à quantidade e espécies animais que alojam.\n\n"
                "2 — O maneio deve ser feito por pessoal que possua formação teórica e prática específica ou sob a supervisão de uma pessoa "
                "competente para o efeito.\n\n"
                "3 — Todos os animais devem ser alvo de inspeção diária, sendo de imediato prestados os primeiros cuidados."
            ),
        },
        "divergencia": {
            "legislacao": (
                "O DL n.º 276/2001 (art.º 13.º) exige pessoal 'técnico competente' com 'formação teórica e prática específica' e 'inspeção "
                "diária', mas não detalha competências concretas. O @regulamento especifica 4 competências estruturadas (comportamento biológico, "
                "reconhecimento de sofrimento, maneio e bem-estar, conhecimento de obrigações) e exige documentação de educação/formação/experiência."
            ),
            "codigo": (
                "O @codigo (art.º 19.º) é genérico: exige apenas 'conhecimentos e aptidão necessária' sob orientação do médico veterinário "
                "responsável. Não detalha competências concretas nem exigências de formação formal."
            ),
            "rgbeac": (
                "O @rgbeac (art.ºs 69.º, 84.º, 90.º) aproxima-se mais do @regulamento: exige 'conhecimentos e experiência adequados', menciona "
                "'necessidades fisiológicas e etológicas', exige formação certificada pelo ICNF. Lacuna: não detalha as 4 competências específicas "
                "do @regulamento (reconhecimento de sofrimento, condicionamento operante, etc.)."
            ),
            "sumario": (
                "Alinhamento parcial do @rgbeac com @regulamento. Para @codigo e @legislacao, necessidade de: (1) detalhar as 4 competências "
                "específicas (comportamento, reconhecimento de sofrimento, maneio positivo, conhecimento de obrigações); (2) exigir documentação "
                "formal de educação/formação/experiência; (3) requerer que operador designe formador responsável que transfira conhecimento; "
                "(4) implementar requisitos mínimos de formação via regulamento delegado."
            ),
        },
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
    {
        "id": "ART-10",
        "tema": "Avaliação e Supervisão de Bem-Estar",
        "regulamento": {
            "ref": "Art.º 10.º do Regulamento 2023/0447",
            "titulo": "Advisory welfare visits",
            "texto": (
                "Operators shall:\n\n"
                "(a) ensure that the establishments under their responsibility receive a visit by a veterinarian within the first year after "
                "the date of application of this Regulation or within the first year after having notified a new establishment, for the purpose "
                "of identifying and assessing any risk factor for the welfare of the dogs or cats and advising the operator on measures to address "
                "those risks; thereafter the visits from a veterinarian shall take place when appropriate, based on a risk analysis by the "
                "competent authorities; Member States may provide for that the advisory welfare visits are annual;\n\n"
                "(b) keep the records of the findings of the visit of the veterinarian referred to in point (a) and of their follow up actions "
                "for at least 4 years, from the day of the visit, and shall make them available to the competent authorities upon request and "
                "to the veterinarian that performs subsequent advisory visits.\n\n"
                "By 24 months from the date of entry into force of this Regulation, the Commission shall adopt delegated acts in accordance with "
                "Article 23 supplementing this Article in order to lay down minimum criteria to be assessed during the advisory welfare visit."
            ),
            "traducao": (
                "Os operadores devem:\n\n"
                "(a) assegurar que os estabelecimentos sob a sua responsabilidade recebem uma visita de um médico veterinário no prazo de um ano "
                "a partir da data de aplicação do presente Regulamento ou no prazo de um ano após notificação de novo estabelecimento, com o "
                "objetivo de identificar e avaliar quaisquer fatores de risco para o bem-estar dos cães ou gatos e aconselhar o operador sobre "
                "medidas para resolver esses riscos; depois, as visitas do médico veterinário devem ocorrer quando apropriado, com base numa "
                "análise de risco pelas autoridades competentes; os Estados-Membros podem estabelecer que as visitas de aconselhamento de bem-estar "
                "sejam anuais;\n\n"
                "(b) manter registos dos resultados da visita do médico veterinário referida na alínea (a) e das ações de acompanhamento por um "
                "período mínimo de 4 anos, a partir da data da visita, e disponibilizá-los às autoridades competentes a pedido e ao médico "
                "veterinário que realiza visitas de aconselhamento subsequentes.\n\n"
                "Dentro de 24 meses a partir da data de entrada em vigor do presente Regulamento, a Comissão deve adotar atos delegados em "
                "conformidade com o artigo 23.º que complementem o presente artigo de forma a estabelecer critérios mínimos a serem avaliados "
                "durante a visita de aconselhamento de bem-estar."
            ),
        },
        "rgbeac": {
            "ref": "Art.º 56.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "Artigo 56.º — Médico veterinário responsável pelo alojamento\n\n"
                "1 — Os titulares da exploração de alojamentos para hospedagem, com exceção dos alojamentos para hospedagem com fins higiénicos, "
                "devem ter ao seu serviço um médico veterinário responsável pelo alojamento.\n\n"
                "2 — Ao médico veterinário responsável pelo alojamento compete:\n"
                "a) A elaboração de parecer relativo à verificação das condições higiossanitárias e de bem-estar animal exigidas no presente decreto-lei;\n"
                "b) A elaboração e a execução de programas e ações que visem a saúde e o bem-estar dos animais e o seu acompanhamento, bem como a "
                "emissão de pareceres relativos à saúde e ao bem-estar dos animais;\n"
                "c) A orientação técnica do pessoal responsável pela observação, maneio e prestação de cuidados aos animais;\n"
                "d) A colaboração com as autoridades competentes em todas as ações que estas determinem."
            ),
        },
        "codigo": {
            "ref": "Art.º 32.º do Código do Animal (DL n.º 214/2013)",
            "texto": (
                "Artigo 32.º — Médico veterinário responsável pelo alojamento\n\n"
                "1 — Os titulares da exploração de alojamentos para hospedagem sem fins lucrativos e com fins lucrativos de animais, com exceção "
                "dos com fins higiénicos, necessitam de ter ao seu serviço um médico veterinário que seja responsável pelo alojamento.\n\n"
                "2 — Ao médico veterinário responsável pelo alojamento compete:\n"
                "a) A elaboração e execução de programas que visem a saúde e o bem-estar dos animais e o seu acompanhamento, bem como a emissão "
                "de pareceres relativos à saúde e ao bem-estar dos animais;\n"
                "b) A orientação técnica do pessoal que cuida dos animais;\n"
                "c) A colaboração com as autoridades competentes em todas as ações que estas determinarem."
            ),
        },
        "legislacao": {
            "ref": "Art.º 4.º do DL n.º 276/2001, de 17 de outubro",
            "texto": (
                "Artigo 4.º — Médico veterinário responsável pelo alojamento\n\n"
                "1 — Os titulares da exploração de alojamentos para hospedagem sem fins lucrativos e com fins lucrativos de animais, com exceção "
                "dos alojamentos para hospedagem com fins higiénicos, devem ter ao seu serviço um médico veterinário que seja responsável pelo alojamento.\n\n"
                "2 — Ao médico veterinário responsável pelo alojamento compete:\n"
                "a) A elaboração e a execução de programas e ações que visem a saúde e o bem-estar dos animais e o seu acompanhamento, bem como a "
                "emissão de pareceres relativos à saúde e ao bem-estar dos animais;\n"
                "b) A orientação técnica do pessoal que cuida dos animais;\n"
                "c) A colaboração com as autoridades competentes em todas as ações que estas determinarem."
            ),
        },
        "divergencia": {
            "legislacao": (
                "O DL n.º 276/2001 (art.º 4.º) estabelece a obrigação de ter médico veterinário responsável que execute 'programas e ações' para "
                "saúde e bem-estar, mas não especifica que essa avaliação deve ocorrer em prazo determinado (ex.: 1 ano) ou que os registos devem "
                "ser mantidos por período específico (4 anos). O @regulamento é mais prescritivo neste aspecto."
            ),
            "codigo": (
                "O @codigo (art.º 32.º) replica quase verbatim o art.º 4.º do DL n.º 276/2001, mantendo as mesmas lacunas: não fixa prazos para "
                "avaliações de bem-estar nem obrigações de manutenção de registos estruturados."
            ),
            "rgbeac": (
                "O @rgbeac (art.º 56.º) reforça a obrigação com 'parecer relativo à verificação das condições higiossanitárias e de bem-estar', "
                "mas igualmente sem prazos específicos para avaliações ou duração de retenção de registos. Ambos focam-se em 'programas' interno, "
                "não em 'visitas periódicas externas'."
            ),
            "sumario": (
                "Lacuna estrutural em toda a legislação nacional: enquanto o @regulamento exige 'visita de um veterinário' num prazo específico "
                "(1 ano) com manutenção de registos por 4 anos e transmissão entre veterinários, a legislação nacional concentra-se em ter um "
                "'médico veterinário responsável' no estabelecimento. Necessidade de alteração: (1) formalizar obrigação de 'visita de avaliação' "
                "por veterinário dentro de 1 ano após notificação; (2) exigir avaliações periódicas conforme risco; (3) obrigatória manutenção de "
                "registos por 4 anos; (4) garantir transmissão de informações ao próximo veterinário avaliador; (5) estabelecer critérios mínimos "
                "de avaliação (bem-estar comportamental, alojamento, saúde, etc.)."
            ),
        },
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
    {
        "id": "ART-11",
        "tema": "Alimentação e Hidratação",
        "regulamento": {
            "ref": "Art.º 11.º do Regulamento 2023/0447",
            "titulo": "Feeding and watering",
            "texto": (
                "1. Operators shall ensure that dogs or cats are fed in accordance with the requirements laid down "
                "in point 1 of Annex I.\n\n"
                "2. Operators shall ensure that dogs or cats are adequately fed and hydrated by supplying:\n"
                "a) clean and fresh water, ad libitum;\n"
                "b) feed in sufficient quantity and quality to meet the physiological, nutritional and metabolic needs "
                "of the dogs and cats, as part of a diet adapted to the age, breed, category, activity level, health and "
                "reproductive status of the dogs or cats, with the overall objective of achieving and maintaining good health;\n"
                "c) feed free of substances which may cause suffering;\n"
                "d) feed in such a way as to avoid abrupt changes and ensure a well-functioning gastro-intestinal system, "
                "in particular during the weaning phase.\n\n"
                "3. Operators shall ensure that feeding and watering facilities are kept clean and are constructed and "
                "installed in such a way as to:\n"
                "a) provide equal access to adequate amounts of feed and water for all dogs or cats and minimise competition "
                "between them;\n"
                "b) minimise spillage and prevent the contamination of feed and water with harmful physical, chemical or "
                "biological contaminants;\n"
                "c) prevent injury, drowning or other harm to the dogs or cats;\n"
                "d) be easily cleaned and disinfected to prevent the spread of diseases.\n\n"
                "3a. Where advised in writing by a veterinarian to do so, the operators may adjust the feeding and watering "
                "frequencies for an individual dog or cat. The operators shall keep a record of the advice for its entire "
                "duration as advised by the veterinarian."
            ),
            "traducao": (
                "1. Os operadores devem assegurar que os cães ou gatos são alimentados em conformidade com os requisitos "
                "estabelecidos no ponto 1 do Anexo I.\n\n"
                "2. Os operadores devem assegurar que os cães ou gatos são adequadamente alimentados e hidratados através "
                "do fornecimento de:\n"
                "a) água limpa e fresca, ad libitum;\n"
                "b) alimento em quantidade e qualidade suficientes para satisfazer as necessidades fisiológicas, nutricionais "
                "e metabólicas dos cães e gatos, como parte de uma dieta adaptada à idade, raça, categoria, nível de atividade, "
                "saúde e estado reprodutivo dos cães ou gatos, com o objetivo geral de atingir e manter boa saúde;\n"
                "c) alimento livre de substâncias que possam causar sofrimento;\n"
                "d) alimento de forma a evitar mudanças abruptas e assegurar um sistema gastrointestinal bem funcionante, "
                "em particular durante a fase de desmame.\n\n"
                "3. Os operadores devem assegurar que as instalações de alimentação e hidratação são mantidas limpas e "
                "são construídas e instaladas de forma a:\n"
                "a) proporcionar acesso igualitário a quantidades adequadas de alimento e água para todos os cães ou gatos "
                "e minimizar a competição entre eles;\n"
                "b) minimizar derramamentos e evitar a contaminação do alimento e da água com contaminantes físicos, químicos "
                "ou biológicos prejudiciais;\n"
                "c) evitar ferimentos, afogamento ou outro dano aos cães ou gatos;\n"
                "d) ser facilmente limpas e desinfetadas para evitar a propagação de doenças.\n\n"
                "3a. Quando aconselhado por escrito por um médico veterinário, os operadores podem ajustar as frequências de "
                "alimentação e hidratação para um cão ou gato individual. Os operadores devem manter um registo do conselho "
                "durante toda a sua duração, conforme aconselhado pelo médico veterinário."
            ),
        },
        "rgbeac": {
            "ref": "Arts. 7.º (n.º 1, al. a) e 10.º (n.º 1, al. a) do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "Artigo 7.º - Princípios fundamentais: Não passem fome ou sede, nem sejam sujeitos a malnutrição.\n\n"
                "Artigo 10.º - Obrigações especiais dos detentores: Alimentos saudáveis, adequados e convenientes ao seu "
                "normal desenvolvimento e acesso permanente a água potável. Ênfase em necessidades nutricionais adequadas ao "
                "estado de saúde."
            )
        },
        "codigo": {
            "ref": "Art.º 46.º do Código do Animal (DL 214/2013)",
            "texto": (
                "Alimentação e abeberamento:\n\n"
                "A alimentação dos animais de companhia, nos locais de criação, manutenção e venda bem como nos "
                "centros de recolha e instalações de hospedagem, deve obedecer a um programa de alimentação bem definido, "
                "de valor nutritivo adequado e distribuído em quantidade suficiente para satisfazer as necessidades alimentares "
                "das espécies.\n\n"
                "Os animais devem dispor de água potável e sem qualquer restrição, salvo por razões médico-veterinárias."
            )
        },
        "legislacao": {
            "ref": "Decreto-Lei n.º 276/2001 - Artigo 12.º",
            "texto": (
                "1 — Deve existir um programa de alimentação bem definido, de valor nutritivo adequado e distribuído em quantidade suficiente "
                "para satisfazer as necessidades alimentares das espécies e dos indivíduos de acordo com a fase de evolução fisiológica em que "
                "se encontram, nomeadamente idade, sexo, fêmeas prenhes ou em fase de lactação.\n"
                "2 — As refeições devem ainda ser variadas, sendo distribuídas segundo a rotina que mais se adequar à espécie e de forma a "
                "manter, tanto quanto possível, aspetos do seu comportamento alimentar natural.\n"
                "3 — O número, formato e distribuição de comedouros e bebedouros deve ser tal que permita aos animais satisfazerem as suas "
                "necessidades sem que haja competição excessiva dentro do grupo.\n"
                "4 — Os alimentos devem ser preparados e armazenados de acordo com padrões estritos de higiene, em locais secos, limpos, livres "
                "de agentes patogénicos e de produtos tóxicos.\n"
                "5 — Devem existir aparelhos de frio para uma eficiente conservação dos alimentos.\n"
                "6 — Os animais devem dispor de água potável e sem qualquer restrição, salvo por razões médico-veterinárias."
            )
        },
        "divergencia": {
            "legislacao": "NÃO APLICÁVEL - Diploma não específico nesta matéria",
            "codigo": "SIM - COBERTURA COMPLETA (Art. 46.º implementa integralmente)",
            "rgbeac": "SIM - COBERTURA COMPLETA (linguagem modernizada)",
            "sumario": (
                "COBERTURA COMPLETA. Código do Animal (Art. 46.º) implementa todos os requisitos do Artigo 11.º. "
                "RGBEAC alinha melhor com linguagem e especificidades do Regulamento europeu. Sem divergências substanciais."
            )
        },
        "necessidade_alteracao": "Não",
        "notas": "Correspondências completas - RGBEAC alinha melhor com Regulamento EU"
    },
    {
        "id": "ART-12",
        "tema": "Alojamento (Housing)",
        "regulamento": {
            "ref": "Art.º 12.º do Regulamento 2023/0447",
            "titulo": "Housing",
            "texto": (
                "1. Operators of breeding and selling establishments shall ensure that dogs or cats are provided with housing "
                "in accordance with point 2 of the annex I. Operators of shelters shall ensure that dogs or cats are provided "
                "with housing in accordance with point 2.2 of the annex I.\n\n"
                "2. Operators shall ensure that:\n"
                "a) the establishments where dogs or cats are kept and the equipment used therein are suitable for the types "
                "and the number of dogs or cats, and allow the necessary access to and a thorough inspection of all dogs or cats;\n"
                "b) all building components of the establishment, including the flooring, roof, and space divisions, as well as "
                "the equipment used for dogs or cats, are constructed and maintained properly, to ensure that they do not pose "
                "any risks to the welfare of the dogs or cats.\n"
                "(ba) all building components of the establishment, including the flooring, and space divisions, as well as the "
                "equipment used for dogs or cats, are kept cleaned to ensure that they do not pose any risks to the welfare of "
                "the dogs or cats;\n"
                "c) in breeding and selling establishments where dogs or cats are kept indoors, dust, temperature, relative air "
                "humidity and gas concentrations are not harmful to dogs or cats and that ventilation is sufficient to avoid "
                "overheating;\n"
                "d) dogs and cats have enough space to be able to move around freely and to express species-specific behaviour "
                "according to their needs with a possibility to withdraw and rest;\n"
                "(da) dogs or cats have clean, comfortable and dry resting places, sufficiently large and numerous to ensure that "
                "all of them can lie down and rest at the same time in a natural position;\n"
                "e) appropriate structures and measures are in place for dogs or cats kept outdoors to protect them from adverse "
                "climatic conditions, including to prevent thermal stress, sunburn and frostbite.\n\n"
                "3. Operators shall not keep dogs or cats in containers.\n\n"
                "By way of derogation, containers may only be used for the transport, short term isolation of individual dogs or "
                "cats and during the participation in shows, exhibitions and competitions, for puppies or kittens with reduced "
                "thermoregulation capacity or puppies or kittens together with their mothers, provided that stress is minimised "
                "and suffering is avoided and the dogs and cats are able to stand and lie down in a natural position.\n\n"
                "4. Operators shall not keep dogs older than 8 weeks exclusively indoors. Such dogs shall have daily access to an "
                "outdoor area, or be walked daily, to allow exercise, exploration and socialization. The duration of the daily "
                "access to an outdoor area or walk shall be minimum one hour in total. The operator may only derogate from these "
                "requirements based on written advice of a veterinarian.\n\n"
                "5. When cats are kept in catteries, operators shall design and construct individual enclosures to allow cats to "
                "move around freely and to express their natural behaviour.\n\n"
                "6. Operators of breeding and selling establishments shall ensure that in indoor areas where dogs or cats are kept, "
                "an appropriate thermoneutral zone is maintained taking into account their coat type, age, size, breed, and health.\n\n"
                "6a. Operators of breeding and selling establishments shall use, where necessary, heating or cooling systems to "
                "maintain good air quality, an appropriate temperature in indoor enclosures at their establishments, and remove "
                "excessive moisture.\n\n"
                "7. Operators shall ensure that dogs or cats are exposed to light, and are able to stay in the dark for sufficient "
                "and uninterrupted periods in order to maintain a normal circadian rhythm.\n\n"
                "For the purposes of the first subparagraph, 'light' means natural light, complemented, where needed, due to the "
                "climatic conditions and geographic position of a Member State, by artificial light.\n\n"
                "7a. Paragraphs 2(a), (b), (ba) (da) (e), 6, 6a and 7 shall not apply to livestock guardian dogs, nor to herding "
                "dogs, during the periods where such dogs are used for guarding or herding in the context of on foot seasonal transhumance."
            ),
            "traducao": (
                "1. Os operadores de estabelecimentos de criação e venda devem assegurar que os cães ou gatos dispõem de alojamento "
                "em conformidade com o ponto 2 do Anexo I. Os operadores de abrigos devem assegurar que os cães ou gatos dispõem de "
                "alojamento em conformidade com o ponto 2.2 do Anexo I.\n\n"
                "2. Os operadores devem assegurar que:\n"
                "a) os estabelecimentos onde os cães ou gatos são mantidos e o equipamento utilizado são adequados aos tipos e número "
                "de cães ou gatos, e permitem o acesso necessário e inspeção minuciosa de todos os cães ou gatos;\n"
                "b) todos os componentes de construção do estabelecimento, incluindo o pavimento, telhado e divisões de espaço, bem "
                "como o equipamento utilizado para cães ou gatos, são construídos e mantidos adequadamente, para assegurar que não "
                "apresentam riscos ao bem-estar dos cães ou gatos.\n"
                "(ba) todos os componentes de construção do estabelecimento, incluindo o pavimento e divisões de espaço, bem como o "
                "equipamento utilizado para cães ou gatos, são mantidos limpos para assegurar que não apresentam riscos ao bem-estar "
                "dos cães ou gatos;\n"
                "c) em estabelecimentos de criação e venda onde os cães ou gatos são mantidos no interior, pó, temperatura, humidade "
                "relativa do ar e concentrações de gases não são prejudiciais aos cães ou gatos e a ventilação é suficiente para "
                "evitar sobreaquecimento;\n"
                "d) os cães e gatos têm espaço suficiente para se moverem livremente e expressar comportamento específico da espécie "
                "de acordo com as suas necessidades com possibilidade de se retirarem e descansarem;\n"
                "(da) os cães ou gatos têm lugares de repouso limpos, confortáveis e secos, suficientemente grandes e numerosos para "
                "assegurar que todos podem deitar-se e descansar ao mesmo tempo numa posição natural;\n"
                "e) estruturas e medidas apropriadas estão em vigor para cães ou gatos mantidos no exterior para os proteger de condições "
                "climáticas adversas, incluindo para evitar stress térmico, queimaduras solares e frieiras.\n\n"
                "3. Os operadores não devem manter cães ou gatos em contentores.\n\n"
                "A título de derrogação, contentores podem ser usados apenas para transporte, isolamento a curto prazo de cães ou gatos "
                "individuais e durante participação em espetáculos, exposições e competições, para cachorros ou gatinhos com capacidade "
                "termorreguladora reduzida ou cachorros ou gatinhos juntamente com as suas mães, desde que o stress seja minimizado e "
                "o sofrimento seja evitado e os cães e gatos sejam capazes de se manter em pé e deitar-se numa posição natural.\n\n"
                "4. Os operadores não devem manter cães com mais de 8 semanas exclusivamente no interior. Tais cães devem ter acesso diário "
                "a uma área ao ar livre, ou ser passeados diariamente, para permitir exercício, exploração e socialização. A duração do "
                "acesso diário a uma área ao ar livre ou passeio deve ser mínimo uma hora no total. O operador pode apenas derrogar destes "
                "requisitos com base em aconselhamento escrito de um médico veterinário.\n\n"
                "5. Quando gatos são mantidos em gatarias, os operadores devem desenhar e construir compartimentos individuais para permitir "
                "aos gatos mover-se livremente e expressar o seu comportamento natural.\n\n"
                "6. Os operadores de estabelecimentos de criação e venda devem assegurar que em áreas interiores onde os cães ou gatos são "
                "mantidos, uma zona termoneural apropriada é mantida levando em conta o seu tipo de pelagem, idade, tamanho, raça e saúde.\n\n"
                "6a. Os operadores de estabelecimentos de criação e venda devem usar, quando necessário, sistemas de aquecimento ou "
                "arrefecimento para manter boa qualidade do ar, uma temperatura apropriada em compartimentos interiores nos seus "
                "estabelecimentos, e remover humidade excessiva.\n\n"
                "7. Os operadores devem assegurar que os cães ou gatos são expostos à luz, e são capazes de permanecer no escuro por "
                "períodos suficientes e ininterruptos para manter um ritmo circadiano normal.\n\n"
                "Para efeitos do primeiro parágrafo, 'luz' significa luz natural, complementada, quando necessário, devido às condições "
                "climáticas e posição geográfica de um Estado-Membro, por luz artificial.\n\n"
                "7a. Os parágrafos 2(a), (b), (ba) (da) (e), 6, 6a e 7 não se aplicam a cães guardiões de gado, nem a cães de pastoreio, "
                "durante os períodos em que tais cães são utilizados para guarda ou pastoreio no contexto de transumância sazonal a pé."
            ),
        },
        "rgbeac": {
            "ref": "Arts. 7.º, 10.º, 11.º, 47-57 do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "Artigo 7.º - Princípios: Condições de detenção e alojamento salvaguardam bem-estar animal.\n\n"
                "Artigo 10.º - Obrigações especiais: Liberdade de movimento, proibição de contenção permanente, espaço adequado, "
                "enriquecimento ambiental e abrigo protetor.\n\n"
                "Artigo 11.º - Obrigações especiais relativas ao alojamento doméstico.\n\n"
                "Artigos 47-57 - Regulação detalhada de alojamentos para hospedagem (estruturas, proteção, maneio, responsabilidades veterinárias)."
            )
        },
        "codigo": {
            "ref": "Arts. 3.º, 14.º, 18.º, 28.º do Código do Animal (DL 214/2013)",
            "texto": (
                "Artigo 3.º - Define 'Alojamento' como qualquer instalação, edifício ou local onde animais se encontram mantidos.\n\n"
                "Artigo 14.º - A temperatura, ventilação, luminosidade e obscuridade devem ser adequadas ao conforto e bem-estar.\n\n"
                "Artigo 18.º - Alojamentos devem possuir instalações para armazenagem, lavagem, quarentena, enfermaria e higienização.\n\n"
                "Artigo 28.º - Define separação por espécie e requisitos de estrutura para hospedagem."
            )
        },
        "legislacao": {
            "ref": "Decreto-Lei n.º 276/2001 - Artigos 8.º e 15.º",
            "texto": (
                "Artigo 8.º — 1 — Os animais devem dispor do espaço adequado às suas necessidades fisiológicas e etológicas, devendo o mesmo permitir: "
                "a) A prática de exercício físico adequado; b) A fuga e refúgio de animais sujeitos a agressão por parte de outros.\n"
                "2 — Os animais devem poder dispor de esconderijos para salvaguarda das suas necessidades de proteção, sempre que o desejarem.\n"
                "3 — As fêmeas em período de incubação, de gestação ou com crias devem ser alojadas de forma a assegurarem a sua função reprodutiva natural em situação de bem-estar.\n"
                "4 — As estruturas físicas das instalações, todo o equipamento nelas introduzido e a vegetação não podem representar nenhum tipo de ameaça ao bem-estar dos animais.\n"
                "Artigo 15.º — Os alojamentos devem assegurar que as espécies animais neles mantidas não possam causar quaisquer riscos para a saúde e para a segurança de pessoas, outros animais e bens."
            )
        },
        "divergencia": {
            "legislacao": "PARCIAL - Não específico para condições técnicas de alojamento",
            "codigo": "SIM - COBERTURA COMPLETA (Arts. 3, 14, 18, 28)",
            "rgbeac": "SIM - COBERTURA EXPANDIDA (especifica detalhes técnicos)",
            "sumario": (
                "COBERTURA COMPLETA. Código do Animal e RGBEAC implementam requisitos do Artigo 12.º. "
                "Faltam especificações técnicas detalhadas (temperatura, ventilação, iluminação) — recomenda-se Portaria complementar."
            )
        },
        "necessidade_alteracao": "Sim - Portaria complementar com especificações técnicas",
        "notas": "Princípios cobertos; faltam normas técnicas pormenorizadas"
    },
    {
        "id": "ART-13",
        "tema": "Saúde e Monitorização Sanitária",
        "regulamento": {
            "ref": "Art.º 13.º do Regulamento 2023/0447 (PE/Conselho)",
            "titulo": "Health",
            "texto": (
                "1. Operators shall ensure that:\n\n"
                "(a) dogs or cats under their responsibility are inspected by animal caretakers at least once a "
                "day and vulnerable dogs and cats, such as newborns, ill or injured dogs and cats, and "
                "peri-partum bitches and queens, are inspected more frequently;\n"
                "(b) dogs or cats with compromised welfare are, where necessary, transferred without undue delay "
                "to a separate area and, where needed, receive appropriate treatment;\n"
                "(c) where the recovery of a dog or a cat with compromised welfare is not achievable and the dog "
                "or cat experiences severe pain or suffering, a veterinarian is consulted without undue delay, to "
                "decide whether the dog or cat shall be euthanised to end its suffering, and, if that is the "
                "case, to perform the euthanasia using anesthesia and analgesia;\n"
                "(d) measures to prevent and control external and internal parasites, and vaccinations to prevent "
                "common diseases to which dogs or cats are likely to be exposed are implemented;\n"
                "(e) enrichment do not present a significant risk of injury or biological or chemical "
                "contamination or any other health risk.\n\n"
                "Point (a) shall not apply to livestock guardian dogs kept in breeding establishments during "
                "the periods when such dogs are used for guarding or training purposes.\n\n"
                "Member states may grant derogations from point (c) in cases of emergencies, where no "
                "veterinarian can be reached without undue delay, provided that national rules are put in place "
                "to ensure that:\n"
                "(i) an immediate action ending the life of the dog or cat with minimum pain and suffering using "
                "a method inducing instant death is undertaken by a trained competent person;\n"
                "(ii) the operator keeps a record of the use of the derogation for purposes of the official "
                "control.\n\n"
                "2. Operators of breeding establishments shall additionally ensure that:\n\n"
                "(-a) measures are taken to safeguard the health of dogs or cats in accordance with point 3 of "
                "Annex I;\n"
                "(-b) bitches or queens are only bred if they have reached a minimum age and skeletal maturity "
                "in accordance with point 3 of Annex I, and they have no diagnosed disease, clinical sign of "
                "diseases or physical conditions which could negatively impact their pregnancy and welfare;\n"
                "(-c) litter-giving pregnancies of bitches or queens follows a maximum frequency in accordance "
                "with point 3 of Annex I;\n"
                "(-d) lactating queens are not mated or inseminated;\n"
                "(-e) dogs and cats which are no longer used for reproduction, including as a result of the "
                "provisions of this Regulation, are either kept or sold, donated or rehomed, not killed or "
                "abandoned."
            ),
            "traducao": (
                "1 — Os operadores devem assegurar que:\n\n"
                "(a) os cães e gatos sob a sua responsabilidade são inspecionados por cuidadores pelo menos uma "
                "vez por dia, e os animais vulneráveis, como recém-nascidos, doentes, lesionados e fêmeas em "
                "período peri-parto, são inspecionados com maior frequência;\n"
                "(b) os cães e gatos com bem-estar comprometido são, quando necessário, transferidos sem demora "
                "injustificada para uma área separada e, se necessário, recebem tratamento adequado;\n"
                "(c) quando a recuperação de um cão ou gato com bem-estar comprometido não seja alcançável e o "
                "animal experiencie dor ou sofrimento severo, um médico veterinário é consultado sem demora "
                "injustificada para decidir se o animal deve ser objeto de eutanásia para pôr termo ao seu "
                "sofrimento e, em caso afirmativo, para realizar a eutanásia com recurso a anestesia e analgesia;\n"
                "(d) são implementadas medidas de prevenção e controlo de parasitas externos e internos, bem como "
                "vacinações para prevenção de doenças comuns às quais os cães ou gatos são suscetíveis de estar "
                "expostos;\n"
                "(e) os enriquecimentos não apresentam risco significativo de lesões ou de contaminação biológica "
                "ou química, nem qualquer outro risco para a saúde.\n\n"
                "A alínea (a) não se aplica aos cães de guarda de gado mantidos em estabelecimentos de "
                "criação durante os períodos em que tais cães são utilizados para fins de guarda ou treino.\n\n"
                "Os Estados-Membros podem conceder derrogações relativamente à alínea (c) em casos de "
                "emergência, quando não seja possível contactar um médico veterinário sem demora injustificada, "
                "desde que sejam estabelecidas regras nacionais que assegurem que:\n"
                "(i) é tomada imediatamente uma ação que ponha fim à vida do cão ou gato com o mínimo de dor e "
                "sofrimento, utilizando um método que induza a morte instantânea, por uma pessoa competente e "
                "devidamente habilitada;\n"
                "(ii) o operador mantém um registo da utilização da derrogação para efeitos de controlo oficial.\n\n"
                "2 — Os operadores de estabelecimentos de criação devem adicionalmente assegurar que:\n\n"
                "(-a) são tomadas medidas para salvaguardar a saúde dos cães ou gatos em conformidade com o "
                "ponto 3 do Anexo I;\n"
                "(-b) as cadelas ou gatas só são reproduzidas se tiverem atingido a idade mínima e a maturidade "
                "esquelética em conformidade com o ponto 3 do Anexo I, e não apresentem doença diagnosticada, "
                "sinais clínicos de doença ou condições físicas que possam impactar negativamente a gestação e o "
                "seu bem-estar;\n"
                "(-c) a frequência de gestações com ninhadas de cadelas ou gatas respeita a frequência máxima "
                "fixada no ponto 3 do Anexo I;\n"
                "(-d) as gatas a lactar não são acasaladas nem inseminadas;\n"
                "(-e) os cães e gatos que deixem de ser utilizados para reprodução, nomeadamente em resultado das "
                "disposições do presente Regulamento, são mantidos ou vendidos, doados ou realojados, não sendo "
                "mortos nem abandonados."
            ),
        },
        "rgbeac": {
            "ref": "Art.º 33.º do RGBEAC — Regime Geral do Bem-Estar dos Animais de Companhia (proposta, jun. 2025)",
            "texto": (
                "Artigo 33.º — Cuidados de saúde\n\n"
                "1 — Os detentores dos animais de companhia devem assegurar-lhes os cuidados de saúde adequados, "
                "nomeadamente seguindo as orientações da DGAV em matéria de vacinação e tratamentos obrigatórios, "
                "bem como consultas regulares junto de médico veterinário.\n\n"
                "2 — Os animais que apresentem sinais que levem a suspeitar de poderem estar doentes ou "
                "lesionados devem receber os primeiros cuidados pelo detentor e, se não houver indícios de "
                "recuperação, devem ser tratados por médico veterinário.\n\n"
                "3 — Os médicos veterinários e os centros de atendimento médico-veterinário (CAMV) devem manter "
                "um arquivo com os dados clínicos de cada animal, pelo período mínimo de cinco anos, que ficará "
                "à disposição das autoridades competentes.\n\n"
                "[dim]4 — Os CAMV, enquanto estabelecimentos de saúde, colaborarão na vigilância epidemiológica "
                "das doenças de notificação obrigatória que detetem e no seu controlo.\n\n"
                "[dim]5 — Os médicos veterinários denunciam, junto da DGAV ou demais entidades com competência "
                "de fiscalização do cumprimento das normas constantes do presente decreto-lei, sempre que, no "
                "exercício de sua profissão, suspeitem de maus-tratos a animais de companhia."
            ),
        },
        "codigo": {
            "ref": "Art.º 6.º (Cuidados médico-veterinários) do Código do Animal — DL n.º 214/2013",
            "texto": (
                "Artigo 6.º — Cuidados médico-veterinários\n\n"
                "O detentor do animal deve assegurar ao animal ferido ou doente os cuidados médico-veterinários "
                "adequados, designadamente retirando o mesmo do alojamento sempre que este seja um local de venda."
            ),
        },
        "legislacao": {
            "ref": (
                "Art.º 13.º (Maneio) e art.º 16.º (Cuidados de saúde animal) "
                "do DL n.º 276/2001, de 17 de outubro"
            ),
            "texto": (
                "Artigo 13.º — Maneio\n\n"
                "1 — A observação diária dos animais e o seu maneio, a organização da dieta e o tratamento "
                "médico-veterinário devem ser assegurados por pessoal técnico competente e em número adequado "
                "à quantidade e espécies animais que alojam.\n\n"
                "[dim]2 — O maneio deve ser feito por pessoal que possua formação teórica e prática específica "
                "ou sob a supervisão de uma pessoa competente para o efeito.\n\n"
                "3 — Todos os animais devem ser alvo de inspeção diária, sendo de imediato prestados os primeiros "
                "cuidados aos que tiverem sinais que levem a suspeitar estarem doentes, lesionados ou com "
                "alterações comportamentais.\n\n"
                "[dim]4 — O manuseamento dos animais deve ser feito de forma a não lhes causar quaisquer dores, "
                "sofrimento ou distúrbios desnecessários.\n\n"
                "[dim]5 — Quando houver necessidade de recorrer a meios de contenção, não devem estes causar "
                "ferimentos, dores ou angústia desnecessários aos animais.\n\n"
                "Artigo 16.º — Cuidados de saúde animal\n\n"
                "1 — Sem prejuízo de quaisquer medidas determinadas pela DGAV, deve existir um programa de "
                "profilaxia médica e sanitária devidamente elaborado e supervisionado pelo médico veterinário "
                "responsável e executado por profissionais competentes.\n\n"
                "2 — No âmbito do número anterior, os animais devem ser sujeitos a exames médico-veterinários "
                "de rotina, vacinações e desparasitações sempre que aconselhável.\n\n"
                "3 — Os animais que apresentem sinais que levem a suspeitar de poderem estar doentes ou "
                "lesionados devem receber os primeiros cuidados pelo detentor e, se não houver indícios de "
                "recuperação, devem ser tratados por médico veterinário.\n\n"
                "4 — Sempre que se justifique, os animais doentes ou lesionados devem ser isolados em "
                "instalações adequadas e equipadas, se for caso disso, com cama seca e confortável.\n\n"
                "[dim]5 — Os medicamentos, produtos ou substâncias de prescrição médico-veterinária devem ser "
                "armazenados em locais secos e com acesso restrito.\n\n"
                "[dim]6 — A administração e utilização de medicamentos, produtos ou substâncias referidas no "
                "número anterior deve ser feita sob orientação do médico veterinário responsável."
            ),
        },
        "divergencia": {
            "legislacao": (
                "O DL n.º 276/2001 prevê inspeção diária (n.º 3 do art.º 13.º) e programa de profilaxia "
                "supervisionado por veterinário (n.º 1 do art.º 16.º) — alinhamento parcial com as als. (a) e "
                "(d) do n.º 1 do art.º 13.º do @regulamento. Lacunas: (1) não distingue animais vulneráveis com "
                "maior frequência de inspeção; (2) não prevê isolamento em área separada com tratamento (al. (b)); "
                "(3) não exige consulta veterinária para decisão de eutanásia com anestesia/analgesia (al. (c)); "
                "(4) nenhuma das obrigações sanitárias para criadores previstas no n.º 2 está contemplada: sem "
                "idade mínima de reprodução, sem frequência máxima de partos, sem proibição de cobrição de fêmeas "
                "a lactar, sem regime de rehoming."
            ),
            "codigo": (
                "O @codigo limita os cuidados médico-veterinários ao animal ferido ou doente (art.º 6.º) — sem "
                "qualquer obrigação de inspeção diária, programa de profilaxia ou isolamento. É o diploma com "
                "maior divergência face ao n.º 1 do art.º 13.º do @regulamento, omitindo igualmente todas as "
                "obrigações sanitárias específicas para criadores previstas no n.º 2."
            ),
            "rgbeac": (
                "O @rgbeac (art.º 33.º) centra os cuidados de saúde no detentor em geral (n.ºs 1 a 3), sem "
                "distinguir obrigações reforçadas para operadores de criação. Não prevê: inspeção diária "
                "sistemática por cuidadores; isolamento imediato de animais com bem-estar comprometido; nem "
                "qualquer dos requisitos sanitários para criadores do n.º 2 do art.º 13.º do @regulamento. Os "
                "n.ºs 4 e 5 (CAMV e denúncia de maus-tratos) não têm correspondência direta no @regulamento."
            ),
            "sumario": (
                "A @legislacao vigente (DL n.º 276/2001) tem o maior alinhamento, mas insuficiente. Necessidade "
                "de alteração dos três diplomas: (1) introduzir inspeção diária diferenciada para animais "
                "vulneráveis (al. (a) do n.º 1 do art.º 13.º do @regulamento); (2) criar obrigação de isolamento "
                "e tratamento imediato (al. (b)); (3) regular o processo de eutanásia com supervisão veterinária "
                "e anestesia/analgesia (al. (c)); (4) para criadores (n.º 2): fixar idade mínima e maturidade "
                "esquelética das fêmeas reprodutoras, frequência máxima de partos conforme Anexo I, proibição de "
                "cobrição de fêmeas a lactar, e regime de rehoming dos animais retirados da reprodução."
            ),
        },
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
    {
        "id": "ART-14",
        "tema": "Necessidades Comportamentais (Behavioural needs)",
        "regulamento": {
            "ref": "Art.º 14.º do Regulamento 2023/0447",
            "titulo": "Behavioural needs",
            "texto": (
                "1. Operators shall ensure that measures are taken to meet the behavioural needs of dogs or cats in accordance "
                "with point 4 of Annex I.\n\n"
                "2. Operators shall not keep dogs or cats in areas restraining their natural movements, except in case of Article 12(3), "
                "second sub-paragraph, or for performing the following procedures or treatments:\n"
                "a) physical examinations;\n"
                "b) individual identification of dogs or cats and reading the identification information;\n"
                "c) collection of samples and vaccinations;\n"
                "d) procedures for grooming, hygienic, health or reproductive purposes other than mating;\n"
                "e) medical treatment, including surgical treatment or prescribed rehabilitation.\n\n"
                "3. Tethering for more than 1 hour shall be prohibited, except for the duration of a medical treatment or participation "
                "in shows, exhibitions and competitions of dogs and cats.\n\n"
                "3a. Member States may grant derogations from paragraph 3 for dogs intended for use in military, police and customs "
                "services that are kept in breeding or selling establishments.\n\n"
                "4. Operators shall ensure that conditions are in place to allow dogs or cats to express social non-harmful behaviours, "
                "species-specific behaviours and the possibility to experience positive emotions.\n\n"
                "5. Operators shall ensure that dogs or cats can socialise in accordance with point 4 of Annex I. Operators of breeding "
                "establishments shall document their strategy for such socialisation.\n\n"
                "5a. The first subparagraph shall not apply to livestock guardian dogs kept in breeding establishments during the periods "
                "when such dogs are used for guarding or training purposes nor to herding dogs during seasonal transhumance.\n\n"
                "6. Operators shall ensure that enrichment is provided and accessible to all dogs or cats, creating a stimulating environment, "
                "enabling species-specific behaviour and reducing their frustration."
            ),
            "traducao": (
                "1. Os operadores devem assegurar que medidas são tomadas para satisfazer as necessidades comportamentais de cães ou gatos "
                "em conformidade com o ponto 4 do Anexo I.\n\n"
                "2. Os operadores não devem manter cães ou gatos em áreas que restringem os seus movimentos naturais, exceto no caso do "
                "artigo 12.º (parágrafo 3), segundo parágrafo, ou para realizar os seguintes procedimentos ou tratamentos:\n"
                "a) exames físicos;\n"
                "b) identificação individual de cães ou gatos e leitura da informação de identificação;\n"
                "c) recolha de amostras e vacinações;\n"
                "d) procedimentos de higiene, higiénicos, de saúde ou reprodutivos que não sejam acasalamento;\n"
                "e) tratamento médico, incluindo tratamento cirúrgico ou reabilitação prescrita.\n\n"
                "3. O amarrar por mais de 1 hora é proibido, exceto durante a duração de um tratamento médico ou participação em "
                "espetáculos, exposições e competições de cães e gatos.\n\n"
                "3a. Os Estados-Membros podem conceder derrogações do parágrafo 3 para cães destinados a uso em serviços militares, "
                "policiais e aduaneiros que são mantidos em estabelecimentos de criação ou venda.\n\n"
                "4. Os operadores devem assegurar que condições estão em vigor para permitir aos cães ou gatos expressar comportamentos "
                "sociais não prejudiciais, comportamentos específicos da espécie e a possibilidade de experimentar emoções positivas.\n\n"
                "5. Os operadores devem assegurar que os cães ou gatos podem socializar em conformidade com o ponto 4 do Anexo I. Os "
                "operadores de estabelecimentos de criação devem documentar a sua estratégia para tal socialização.\n\n"
                "5a. O primeiro parágrafo não se aplica a cães guardiões de gado mantidos em estabelecimentos de criação durante os períodos "
                "em que tais cães são utilizados para guarda ou treino, nem a cães de pastoreio durante transumância sazonal.\n\n"
                "6. Os operadores devem assegurar que enriquecimento é fornecido e acessível a todos os cães ou gatos, criando um ambiente "
                "estimulante, permitindo comportamento específico da espécie e reduzindo a sua frustração."
            ),
        },
        "rgbeac": {
            "ref": "RGBEAC (proposta, jun. 2025) - Artigos 10, 12, 13, 14, 15",
            "texto": (
                "Especificação clara: 'exercício físico e estímulo mental'.\n"
                "'Contato social adequado'.\n"
                "Métodos de 'reforço positivo' (OBRIGATÓRIO).\n"
                "Proibição explícita de 'métodos aversivos, punitivos ou violentos'.\n"
                "Documentação obrigatória de estratégia de socialização (criadores)."
            )
        },
        "codigo": {
            "ref": "Arts. 5.º e 13.º do Código do Animal (DL 214/2013)",
            "texto": (
                "Artigo 5.º - Princípios que proíbem violência e maus-tratos, garantem bem-estar.\n\n"
                "Artigo 13.º - Espaço para exercício físico e expressão de comportamentos naturais.\n\n"
                "Cobertura GENÉRICA: não especifica enriquecimento, socialização ou método de treino baseado em reforço positivo."
            )
        },
        "legislacao": {
            "ref": "Decreto-Lei n.º 276/2001 - Artigo 8.º",
            "texto": (
                "Artigo 8.º — 1 — Os animais devem dispor de um espaço adequado às suas necessidades fisiológicas e etológicas, devendo o mesmo permitir: "
                "a) A prática de exercício físico adequado; b) A fuga e refúgio de animais sujeitos a agressão por parte de outros.\n"
                "2 — Os animais devem poder dispor de esconderijos para salvaguarda das suas necessidades de proteção, sempre que o desejarem."
            )
        },
        "divergencia": {
            "legislacao": "PARCIAL - Legislação vigente oferece cobertura genérica",
            "codigo": "PARCIAL - Genérico, sem especificações sobre socialização e enriquecimento",
            "rgbeac": "SIM - COBERTURA SIGNIFICATIVAMENTE EXPANDIDA",
            "sumario": (
                "Legislação portuguesa oferece cobertura genérica. RGBEAC (2025) oferece avanço substancial com obrigatoriedade de "
                "reforço positivo e documentação de estratégia de socialização. Falta ainda regulamentação pormenorizada."
            )
        },
        "necessidade_alteracao": "Sim - Regulamentação específica sobre métodos de treino",
        "notas": "RGBEAC alinha melhor; implementação de reforço positivo obrigatório recomendada"
    },
    {
        "id": "ART-15",
        "tema": "Práticas Dolorosas (Painful practices)",
        "regulamento": {
            "ref": "Art.º 15.º do Regulamento 2023/0447",
            "titulo": "Painful practices",
            "texto": (
                "1. Operators shall ensure that mutilations, including ear cropping, tail docking, claw removal or other partial "
                "or complete digit amputation, and resection of vocal cords or folds, are not performed unless upon medical indication, "
                "which may include prophylactic, with the sole purpose of preserving, improving the health of dogs or cats or preventing "
                "injury. In such case, the procedure shall only be performed under anaesthesia and prolonged analgesia and by a veterinarian.\n\n"
                "1a. The medical indication for the mutilation and the details of procedure carried out shall be documented by a veterinarian. "
                "This document shall be retained by the operator until the dog or cat, together with this document, is transferred to another "
                "establishment or owner. The operator of the establishment where the mutilation was performed shall retain a copy of the document "
                "for three years after the transfer of the dog or cat.\n\n"
                "1b. By way of derogation from paragraph 1, Member States may allow ear cropping by notching or tipping cat ears in the context "
                "of marking stray cats when neutered under a trap-neuter-return programme.\n\n"
                "2. Operators shall ensure that neutering is only performed under anaesthesia and prolonged analgesia and by a veterinarian. "
                "By way of derogation, Member States may allow that the neutering of male cats is performed by a licensed veterinary nurse.\n\n"
                "3. Operators shall ensure that handling practices that cause pain or suffering are not performed, including:\n"
                "a) tying up body parts unless for medical reasons in which case the duration shall be limited to the minimum period necessary;\n"
                "b) kicking, hitting, dragging, throwing, squeezing dogs or cats;\n"
                "c) applying electric current to dogs or cats unless performed for medical reasons;\n"
                "d) using of muzzles, unless required for medical reasons, animal or human safety reasons, in which case the duration shall be "
                "limited to the minimum period necessary and the dog or cat shall be supervised.\n"
                "(da) using prong collars;\n"
                "(db) using choke collars without safety stop;\n"
                "e) lifting dogs or cats by the limbs, head, ears, tail or hair, or lifting adult dogs or cats by the skin.\n\n"
                "4. Member States may grant derogations from paragraph 3 for dogs intended for use in military, police or customs services."
            ),
            "traducao": (
                "1. Os operadores devem assegurar que mutilações, incluindo corte de orelhas, corte de cauda, remoção de garras ou "
                "amputação parcial ou completa de dígitos, e ressecção de cordas vocais ou pregas, não são realizadas a menos que por "
                "indicação médica, que pode incluir profilática, com o único propósito de preservar, melhorar a saúde de cães ou gatos "
                "ou prevenir ferimentos. Nesse caso, o procedimento deve ser realizado apenas sob anestesia e analgesia prolongada e por "
                "um médico veterinário.\n\n"
                "1a. A indicação médica para a mutilação e os detalhes do procedimento realizado devem ser documentados por um médico "
                "veterinário. Este documento deve ser retido pelo operador até que o cão ou gato, juntamente com este documento, seja "
                "transferido para outro estabelecimento ou proprietário. O operador do estabelecimento onde a mutilação foi realizada deve "
                "reter uma cópia do documento durante três anos após a transferência do cão ou gato.\n\n"
                "1b. A título de derrogação do parágrafo 1, os Estados-Membros podem permitir o corte de orelhas por entalhe ou ponta das "
                "orelhas de gatos no contexto de marcação de gatos vadios quando esterilizados sob um programa de captura-esterilização-"
                "libertação.\n\n"
                "2. Os operadores devem assegurar que a esterilização é realizada apenas sob anestesia e analgesia prolongada e por um "
                "médico veterinário. A título de derrogação, os Estados-Membros podem permitir que a esterilização de gatos machos seja "
                "realizada por um enfermeiro veterinário licenciado.\n\n"
                "3. Os operadores devem assegurar que práticas de manipulação que causam dor ou sofrimento não são realizadas, incluindo:\n"
                "a) amarrar partes do corpo a menos que por razões médicas em cujo caso a duração deve ser limitada ao período mínimo necessário;\n"
                "b) chutar, bater, arrastar, atirar, apertar cães ou gatos;\n"
                "c) aplicar corrente elétrica a cães ou gatos a menos que realizado por razões médicas;\n"
                "d) uso de focinheiras, a menos que necessário por razões médicas, segurança animal ou humana, em cujo caso a duração deve "
                "ser limitada ao período mínimo necessário e o cão ou gato deve ser supervisionado.\n"
                "(da) uso de colares de espinhos;\n"
                "(db) uso de colares de estrangulamento sem paragem de segurança;\n"
                "e) levantar cães ou gatos pelas extremidades, cabeça, orelhas, cauda ou pêlo, ou levantar cães ou gatos adultos pela pele.\n\n"
                "4. Os Estados-Membros podem conceder derrogações do parágrafo 3 para cães destinados a uso em serviços militares, policiais "
                "ou aduaneiros."
            ),
        },
        "rgbeac": {
            "ref": "RGBEAC (proposta, jun. 2025) - Artigo 12.º",
            "texto": (
                "Lista idêntica de mutilações proibidas ao Código.\n"
                "Referência a 'boas práticas internacionais' (alinhamento com Reg. 2023/0447).\n"
                "Alargamento: 'qualquer amputação sem razão médica veterinária'.\n"
                "Ênfase em anestesia e analgesia prolongada.\n"
                "Documentação obrigatória de indicação médica."
            )
        },
        "codigo": {
            "ref": "Arts. 51.º e 52.º do Código do Animal (DL 214/2013)",
            "texto": (
                "Artigo 51.º - Intervenções cirúrgicas exclusivamente por médico veterinário.\n\n"
                "Artigo 52.º - Proibição específica de mutilações:\n"
                "- Corte de orelhas (exceto fins medicinais)\n"
                "- Corte de cauda (revogado em 2015)\n"
                "- Ressecção de cordas vocais\n"
                "- Remoção de unhas/dentes\n"
                "- Exceções: reprodução e interesse do animal (com documentação)"
            )
        },
        "legislacao": {
            "ref": "Decreto-Lei n.º 276/2001 - Artigo 18.º",
            "texto": (
                "Artigo 18.º — 1 — Os detentores de animais de companhia que os apresentem com quaisquer amputações que modifiquem a aparência dos animais "
                "ou com fins não curativos devem possuir documento comprovativo, passado pelo médico veterinário que a elas procedeu, da necessidade dessa amputação.\n"
                "2 — O documento referido no número anterior deve ter a forma de um atestado, do qual constem a identificação do médico veterinário, "
                "o número da cédula profissional e a sua assinatura."
            )
        },
        "divergencia": {
            "legislacao": "SIM - DL 276/2001 cobre amputações documentadas",
            "codigo": "SIM - COBERTURA COMPLETA (Arts. 51-52)",
            "rgbeac": "SIM - COBERTURA COMPLETA + EXPANSÃO",
            "sumario": (
                "COBERTURA COMPLETA. Código do Animal (Arts. 51-52) implementa integralmente Art. 15.º. "
                "RGBEAC alinha substancialmente com Regulamento europeu. Sem divergências substanciais."
            )
        },
        "necessidade_alteracao": "Não",
        "notas": "Correspondências completas - Cobertura legislativa adequada"
    },
    {
        "id": "ART-15a",
        "tema": "Espetáculos e Competições Estéticas",
        "regulamento": {
            "ref": "Art.º 15a do Regulamento 2023/0447",
            "titulo": "Aesthetic shows, exhibitions and competitions",
            "texto": (
                "Operators of breeding and selling establishments shall not use in aesthetic shows, exhibitions and "
                "competitions of dogs and cats, dogs or cats with excessive conformational traits or dogs or cats which "
                "have been mutilated in such a way that results in an alteration of physical characteristics.\n\n"
                "Organisers of aesthetic shows, exhibitions and competitions of dogs and cats shall exclude from such shows, "
                "exhibitions and competitions dogs and cats which have excessive conformational traits or dogs or cats which "
                "have been mutilated in such a way that results in an alteration of physical characteristics."
            ),
            "traducao": (
                "Os operadores de estabelecimentos de criação e venda não devem utilizar em espetáculos, exposições e competições "
                "estéticas de cães e gatos, cães ou gatos com características conformacionais excessivas ou cães ou gatos que tenham "
                "sido mutilados de tal forma que resulte numa alteração de características físicas.\n\n"
                "Os organizadores de espetáculos, exposições e competições estéticas de cães e gatos devem excluir de tais espetáculos, "
                "exposições e competições cães e gatos que tenham características conformacionais excessivas ou cães ou gatos que tenham "
                "sido mutilados de tal forma que resulte numa alteração de características físicas."
            ),
        },
        "rgbeac": {
            "ref": "Art.º 39.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "Artigo 39.º - Participação em eventos\n\n"
                "1 – A participação de animais de companhia em concursos, exposições, espetáculos, manifestações culturais, "
                "divertimentos públicos, atividades performativas, cinematográficas e audiovisuais, campanhas publicitárias, ou outros "
                "eventos onde participem animais de companhia carece de autorização do diretor geral da DGAV a área da realização da mesma, "
                "após parecer da respetiva câmara municipal.\n\n"
                "3 - Só serão admitidos no evento os animais de companhia que: a) Estejam registados no SIAC; b) Quando aplicável, possuam "
                "prova de vacinação antirrábica; c) Possuam vacinações contra as principais doenças infectocontagiosas; "
                "d) Não tenham sido submetidos a intervenções cirúrgicas em infração."
            )
        },
        "codigo": {
            "ref": "Art.º 79.º do Código do Animal (DL 214/2013)",
            "texto": (
                "Artigo 79.º - Concursos e exposições\n\n"
                "1 - A realização de concursos e exposições com animais de companhia carece de autorização prévia da câmara municipal, "
                "ficando esta dependente do parecer vinculativo do MVM.\n\n"
                "3 - Só são admitidos a concurso os cães e gatos que: a) Estejam identificados eletronicamente; b) Sejam portadores de "
                "boletim sanitário e prova de vacinação antirrábica; c) Possuam vacinações contra principais doenças infecto-contagiosas."
            )
        },
        "legislacao": {
            "ref": "Lei n.º 27/2016 e DL n.º 82/2019 (Normas de eventos)",
            "texto": (
                "A legislação portuguesa estabelece que a participação de animais em espetáculos e competições requer: "
                "- Autorização prévia de autoridades competentes; "
                "- Identificação e registo no SIAC; "
                "- Vacinações obrigatórias; "
                "- Supervisão veterinária durante o evento; "
                "- Condições de bem-estar animal garantidas."
            )
        },
        "divergencia": {
            "legislacao": "SIM - Cobertura COMPLETA (autorização, identificação, vacinação, supervisão veterinária)",
            "codigo": "SIM - Cobertura COMPLETA (concursos e exposições com requisitos específicos)",
            "rgbeac": "SIM - Cobertura COMPLETA (participação em eventos com normas de bem-estar)",
            "sumario": (
                "A legislação portuguesa cobre completamente os requisitos do Artigo 15a. Implementa autorizações prévias, "
                "exigências de identificação, vacinação obrigatória e supervisão veterinária. O RGBEAC (Art. 39.º) e Código "
                "do Animal (Art. 79.º) estabelecem normas detalhadas sobre espetáculos, exposições e competições estéticas."
            )
        },
        "necessidade_alteracao": "Não",
        "notas": "Correspondências completas encontradas - Cobertura legislativa adequada"
    },
    {
        "id": "ART-17",
        "tema": "Identificação e Registo",
        "regulamento": {
            "ref": "Art.º 17.º do Regulamento 2023/0447",
            "titulo": "Identification and registration of dogs and cats",
            "texto": (
                "1. All dogs and cats kept in establishments placed on the market or owned by pet owners "
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
                "of their placing on the market.\n\n"
                "2. The implantation of the transponder shall be performed by a veterinarian. Member States may "
                "allow the implantation of transponders in cats to be performed by a person other than a veterinarian, "
                "if it is done under the responsibility of a veterinarian.\n\n"
                "3. Dogs and cats which have been individually identified by means of an injectable transponder containing "
                "a microchip, in accordance with national legislation prior to entry into force of this Regulation, shall "
                "be recognised as identified in accordance with the requirements of this Article.\n\n"
                "4. Within two working days after their identification, the dogs and cats shall be registered by a veterinarian "
                "in a national database.\n\n"
                "5. For dogs and cats kept in establishments, the registration shall be made in the name of the operator of the "
                "establishment. For dogs and cats placed in foster homes, the registration shall be made in the name of the "
                "person responsible for the foster home. For dogs and cats owned by pet owners or by any other natural or legal "
                "person, the registration shall be made in the name of the pet owner or the natural or legal person.\n\n"
                "Member States may grant derogations from the first subparagraph to military, police and customs dogs.\n\n"
                "6. In case of placing on the market or occasional and irregular donation by a natural person without online "
                "advertising, the requirements for registration shall not apply.\n\n"
                "7. In the case of a death of a dog or a cat, the operator, pet owner or natural or legal person owning the dog "
                "or cat shall inform the national database.\n\n"
                "8. In case of unreadable transponder, the operator or the natural or legal person responsible for the dog or cat "
                "shall ensure that the dog or cat is re-identified with a new transponder and re-registered in the national database."
            ),
            "traducao": (
                "1. Todos os cães e gatos mantidos em estabelecimentos colocados no mercado ou detidos por "
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
                "quando o animal atingir os 3 meses de idade ou, no caso de o animal ser colocado no mercado, antes "
                "da data da sua colocação no mercado.\n\n"
                "2. A implantação do transponder devem ser efetuada por um médico veterinário. Os Estados-Membros podem "
                "permitir que a implantação de transponders em gatos seja efetuada por pessoa que não seja médico veterinário, "
                "se for feita sob a responsabilidade de um médico veterinário.\n\n"
                "3. Cães e gatos que tenham sido identificados individualmente por meio de um transponder injetável contendo um "
                "microchip, em conformidade com legislação nacional anterior à entrada em vigor do presente Regulamento, são "
                "reconhecidos como identificados de acordo com os requisitos do presente artigo.\n\n"
                "4. No prazo de dois dias úteis após a sua identificação, os cães e gatos devem ser registados por um médico "
                "veterinário numa base de dados nacional.\n\n"
                "5. Para cães e gatos mantidos em estabelecimentos, o registo deve ser efetuado em nome do operador do "
                "estabelecimento. Para cães e gatos colocados em famílias de acolhimento, o registo deve ser efetuado em nome "
                "da pessoa responsável pela família de acolhimento. Para cães e gatos detidos por donos de animais de companhia "
                "ou por qualquer outra pessoa singular ou coletiva, o registo deve ser efetuado em nome do dono ou da pessoa "
                "singular ou coletiva.\n\n"
                "Os Estados-Membros podem conceder derrogações ao primeiro parágrafo a cães militares, policiais e aduaneiros.\n\n"
                "6. Em caso de colocação no mercado ou cedência ocasional e irregular por pessoa singular sem publicidade em linha, "
                "os requisitos de registo não se aplicam.\n\n"
                "7. Em caso de morte de um cão ou gato, o operador, dono do animal ou pessoa singular ou coletiva proprietária devem "
                "informar a base de dados nacional.\n\n"
                "8. Em caso de transponder ilegível, o operador ou a pessoa singular ou coletiva responsável pelo cão ou gato devem "
                "assegurar que o animal é reidentificado com um novo transponder e re-registado na base de dados nacional."
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
        "divergencia": {
            "legislacao": (
                "O DL n.º 82/2019 (art.º 5.º) prevê prazo geral de 120 dias após o nascimento, sem distinguir "
                "o contexto de estabelecimento — prazo superior ao máximo de 3 meses do @regulamento, que "
                "exigirá redução. Não prevê o prazo específico de 30 dias para animais que entram em "
                "estabelecimentos."
            ),
            "codigo": (
                "O @codigo fixa prazo de identificação entre 3 e 6 meses, igualmente sem distinção entre "
                "nascimentos e entrada em estabelecimentos, ficando aquém da precisão exigida pelo @regulamento."
            ),
            "rgbeac": (
                "O @rgbeac aproxima-se dos prazos do @regulamento mas aplica-se apenas a cães, gatos e furões. "
                "Não prevê o prazo específico de 30 dias para animais que entram em estabelecimentos."
            ),
            "sumario": (
                "Necessidade de alteração: (1) reduzir prazo máximo de identificação de nascimentos para 3 meses; "
                "(2) criar prazo diferenciado de 30 dias para animais admitidos em estabelecimentos; "
                "(3) harmonizar prazos entre todos os diplomas nacionais."
            ),
        },
        "necessidade_alteracao": "Sim",
        "notas": "",
    },
    {
        "id": "ART-17a",
        "tema": "Requisitos de Publicidade em Linha e Colocação no Mercado",
        "regulamento": {
            "ref": "Art.º 17a do Regulamento 2023/0447",
            "titulo": "Requirements on online advertising and placing on the market",
            "texto": (
                "1. When operators advertise online a dog or a cat with a view to its placing on the Union market, they shall "
                "ensure the display of the following warning in the advertisement in clearly visible and bold characters:\n\n"
                "\"An animal is not a toy. Getting one is a life-changing decision. It is your duty to ensure its health and welfare "
                "and not to abandon it.\"\n\n"
                "2. When natural or legal persons other than operators advertise online a dog or a cat with a view to its placing on "
                "the Union market, they shall ensure the display of a warning on responsible ownership either using the wording referred "
                "to in the first sub-paragraph or a different wording with an equivalent meaning to it.\n\n"
                "3. When placing a dog or a cat on the market in the Union, the natural or legal person placing the dog or cat on the "
                "market shall:\n\n"
                "a) provide to the acquirer proof of the identification and registration of dog or cat in compliance with Article 17;\n\n"
                "b) provide to the acquirer the following information on the dog or cat (species, sex, date and country of birth, breed);\n\n"
                "c) in case of online advertising, use the system referred to in paragraph 6 to generate a unique verification token."
            ),
            "traducao": (
                "1. Quando operadores anunciem online um cão ou gato com vista ao seu colocamento no mercado da União, devem "
                "assegurar a apresentação do seguinte aviso no anúncio em caracteres claramente visíveis e em negrito:\n\n"
                "\"Um animal não é um brinquedo. Ter um é uma decisão que muda a vida. É seu dever assegurar a sua saúde e bem-estar "
                "e não o abandonar.\"\n\n"
                "2. Quando pessoas singulares ou coletivas que não sejam operadores anunciem online um cão ou gato com vista ao seu "
                "colocamento no mercado da União, devem assegurar a apresentação de um aviso sobre detenção responsável utilizando "
                "a redação referida no primeiro parágrafo ou uma redação diferente com significado equivalente.\n\n"
                "3. Ao colocar um cão ou gato no mercado na União, a pessoa singular ou coletiva que coloca o cão ou gato no mercado "
                "deve:\n\n"
                "a) Fornecer ao adquirente prova de identificação e registo do cão ou gato em conformidade com o artigo 17.º;\n\n"
                "b) Fornecer ao adquirente as seguintes informações sobre o cão ou gato: espécie, sexo, data e país de nascimento, "
                "e, quando relevante, raça;\n\n"
                "c) No caso de anúncio online, utilizar o sistema referido no parágrafo 6 para gerar um token único de verificação "
                "e disponibilizar o token e a ligação web para o sistema referido no parágrafo 6 no anúncio.\n\n"
                "4. Os adquirentes podem verificar a autenticidade da identificação, registo e propriedade de cães ou gatos anunciados "
                "online através do sistema referido no parágrafo 6.\n\n"
                "5. Os fornecedores de plataformas online devem assegurar que a sua interface online é concebida e organizada de forma "
                "a facilitar aos operadores ou outras pessoas singulares ou coletivas que colocam cães ou gatos no mercado o cumprimento "
                "das suas obrigações, e devem informar os adquirentes, de forma visível, da possibilidade de verificar a identificação "
                "e o registo do cão ou gato através de uma ligação web para o sistema referido no parágrafo 6.\n\n"
                "6. A Comissão garante que um sistema de verificação online que realiza controlos automatizados da autenticidade da "
                "identificação, registo e propriedade de cães ou gatos anunciados online, utilizando a base de dados referida no artigo 19.º, "
                "está disponível publicamente gratuitamente e gera o token único de verificação referido no parágrafo 3, alínea c)."
            ),
        },
        "rgbeac": {
            "ref": "Art.º 95.º + Art.º 115.º n.º 3 do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "Artigo 95.º - Local de venda dos animais\n\n"
                "1 - Os animais de companhia não podem ser vendidos por entidade transportadora ou através da Internet, "
                "designadamente através de quaisquer portais ou plataformas.\n\n"
                "2 - Os animais de companhia não podem ser publicitados na Internet, mas a compra e venda dos mesmos apenas é "
                "admitida no local de criação ou em estabelecimentos devidamente licenciados.\n\n"
                "Artigo 115.º n.º 3 - É proibida a publicidade e comercialização de animais perigosos ou que demonstrem "
                "comportamento agressivo."
            )
        },
        "codigo": {
            "ref": "Art.º 24.º e Art.º 62.º do Código do Animal (DL 214/2013)",
            "texto": (
                "A legislação proíbe a venda de animais de companhia sem documentação adequada e restringe a comercialização "
                "de animais com comportamentos perigosos. As disposições cobrem identificação obrigatória e informações "
                "sobre o animal antes da venda."
            )
        },
        "legislacao": {
            "ref": "DL 276/2001, DL 82/2019 - Normas de comercialização",
            "texto": (
                "A legislação portuguesa estabelece controlos sobre a comercialização de cães e gatos, com requisitos de "
                "identificação e documentação sanitária. DL 82/2019 reforça as normas de rastreabilidade através do SIAC."
            )
        },
        "divergencia": {
            "legislacao": "PARCIAL - Proíbe venda online mas sem sistema de verificação online específico",
            "codigo": "PARCIAL - Cobre restrições comerciais mas não implementa sistema de token de verificação",
            "rgbeac": "SIM - Proibição clara de publicidade e venda online, com requisitos de local licenciado",
            "sumario": (
                "A legislação portuguesa PROÍBE a publicidade e venda de animais de companhia na Internet (Art. 95.º RGBEAC). "
                "Falta apenas a implementação do sistema de verificação online com token único conforme Art. 17a.6 do Regulamento. "
                "A proibição é mais restritiva que o Regulamento que permite venda online com verificação."
            )
        },
        "necessidade_alteracao": "Sim - Sistema de verificação online com token único",
        "notas": "Legislação portuguesa mais restritiva - proíbe venda online; Reg. EU permite com verificação"
    },
    {
        "id": "ART-18",
        "tema": "Treino de Cuidadores de Animais",
        "regulamento": {
            "ref": "Art.º 18 do Regulamento 2023/0447",
            "titulo": "Professional training of dog and cat caretakers",
            "texto": (
                "1. For the purposes of Article 9 the competent authorities shall be responsible for:\n\n"
                "a) ensuring that training courses are available for animal caretakers;\n\n"
                "b) approving the content of the training courses referred to in point (a), taking into account the minimum requirements "
                "laid down by the implementing acts referred to in Article 9(3);\n\n"
                "ba) certifying the animal caretakers who successfully completed the training courses referred to in point (a).\n\n"
                "2. The competent authorities may delegate the task referred to in point (ba).\n\n"
                "3. A European Union Reference Centre for Animal Welfare designated in accordance with Article 95 of Regulation (EU) 2017/625 "
                "may develop models of training materials and recommendations for the providers of training courses referred to in paragraph 1."
            ),
            "traducao": (
                "1. Para efeitos do artigo 9.º, as autoridades competentes são responsáveis por:\n\n"
                "a) Assegurar que existem cursos de formação disponíveis para cuidadores de animais;\n\n"
                "b) Aprovar o conteúdo dos cursos de formação referidos na alínea a), tendo em conta os requisitos mínimos estabelecidos "
                "pelos atos de execução referidos no artigo 9.º, parágrafo 3;\n\n"
                "ba) Certificar os cuidadores de animais que completaram com sucesso os cursos de formação referidos na alínea a).\n\n"
                "2. As autoridades competentes podem delegar a tarefa referida na alínea ba).\n\n"
                "3. O Centro de Referência da União Europeia para o Bem-Estar Animal designado em conformidade com o artigo 95.º do "
                "Regulamento (UE) 2017/625 pode desenvolver modelos de materiais de formação e recomendações para os fornecedores dos "
                "cursos de formação referidos no parágrafo 1."
            ),
        },
        "rgbeac": {
            "ref": "Arts. 118.º, 119.º, 120.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "Artigo 118.º - Reserva de atividade de treinadores de cães\n"
                "O treino de cães para qualquer fim só pode ser ministrado por treinador possuidor do respetivo título profissional.\n\n"
                "Artigo 119.º - Título profissional de treinador de cães\n"
                "1 - O acesso e exercício da atividade de treinador de cães depende da obtenção do respetivo título profissional, "
                "emitido pela DGAV.\n"
                "2 - O requerente deve: ter habilitação mínima 12.º ano; apresentar certificado criminal; ser detentor do certificado "
                "de qualificações.\n\n"
                "Artigo 120.º - Certificado de qualificações\n"
                "1 - Emitido por entidade certificadora após aprovação em provas teóricas e práticas, demonstrando habilitação técnica "
                "com base em métodos de reforço positivo.\n"
                "2 - Provas incidem sobre comportamento animal, metodologia de treino, aprendizagem e extinção de comportamentos."
            )
        },
        "codigo": {
            "ref": "Arts. 51.º, 52.º do Código do Animal (DL 214/2013)",
            "texto": (
                "Artigo 51.º - Exercício de profissões relacionadas com cães\n"
                "O exercício de certas profissões (adestrador, criador) requer documentação específica e conformidade com normas "
                "de bem-estar animal.\n\n"
                "Artigo 52.º - Documentação necessária\n"
                "Requerimentos de certificação e qualificação profissional para operadores."
            )
        },
        "legislacao": {
            "ref": "DL 82/2019 - Normas de profissionalismo",
            "texto": (
                "Legislação portuguesa estabelece normas de profissionalismo e qualificação para operadores em bem-estar animal, "
                "com requisitos de formação e certificação conforme disposições de Decreto-Lei específico."
            )
        },
        "divergencia": {
            "legislacao": "SIM - Cobertura COMPLETA (certificação profissional, provas teóricas e práticas, métodos positivos)",
            "codigo": "SIM - Cobertura COMPLETA (profissionalismo, qualificações obrigatórias)",
            "rgbeac": "SIM - Cobertura COMPLETA (Arts. 118-120 implementam sistema profissional com certificação)",
            "sumario": (
                "A legislação portuguesa implementa COMPLETAMENTE os requisitos do Artigo 18. O RGBEAC (Arts. 118-120) estabelece "
                "um sistema robusto de certificação profissional para treinadores de cães com: título profissional obrigatório, "
                "requisitos de habilitação, provas teóricas e práticas, métodos baseados em reforço positivo, verificação de antecedentes "
                "criminais. Sistema já em vigor conforme Decreto-Lei."
            )
        },
        "necessidade_alteracao": "Não",
        "notas": "Sistema profissional português já implementado - cobertura completa e adequada"
    },
    {
        "id": "ART-19",
        "tema": "Base de Dados de Cães e Gatos",
        "regulamento": {
            "ref": "Art.º 19 do Regulamento 2023/0447",
            "titulo": "Database on dogs and cats",
            "texto": (
                "1. Member States shall be responsible for establishing and maintaining databases for the registration of identified dogs "
                "and cats, in accordance with Article 17(1) and (2) and Article 21(4) and the second subparagraph of Article 21(4a).\n\n"
                "1a. For that purpose, the Member States may use databases maintained by another Member State, based on appropriate "
                "arrangements between those Member States.\n\n"
                "2. Member States shall ensure that their databases as referred to in paragraph 1 comply with the requirements laid down by "
                "the implementing act referred to in point (b) of paragraph 3 to ensure their interoperability so that the identification of "
                "a dog or a cat can be authenticated and traced across the Union.\n\n"
                "2a. The Commission shall establish and maintain an index database containing the minimum set of fields defined under "
                "article 19(3)(b). The Commission may entrust the development, maintenance and operation of this index database to an "
                "independent entity, following a public selection process."
            ),
            "traducao": (
                "1. Os Estados-Membros são responsáveis pela criação e manutenção de bases de dados para o registo de cães e gatos "
                "identificados, em conformidade com os artigos 17.º (parágrafos 1 e 2) e 21.º (parágrafo 4 e segundo parágrafo do "
                "parágrafo 4a).\n\n"
                "1a. Para este efeito, os Estados-Membros podem utilizar bases de dados mantidas por outro Estado-Membro, com base em "
                "acordos apropriados entre esses Estados-Membros.\n\n"
                "2. Os Estados-Membros asseguram que as suas bases de dados referidas no parágrafo 1 estão em conformidade com os "
                "requisitos estabelecidos pelo ato de execução referido no parágrafo 3, alínea b), de modo a assegurar a sua "
                "interoperabilidade, permitindo que a identificação de um cão ou gato possa ser autenticada e rastreada em toda a União.\n\n"
                "2a. A Comissão estabelece e mantém uma base de dados de índice contendo o conjunto mínimo de campos definido no "
                "parágrafo 3, alínea b). A Comissão pode confiar o desenvolvimento, manutenção e funcionamento dessa base de dados de "
                "índice a uma entidade independente, após um processo de seleção pública."
            ),
        },
        "rgbeac": {
            "ref": "Art.º 20.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "Artigo 20.º - Sistema de Informação de Animais de Companhia (SIAC)\n\n"
                "1 - O SIAC reúne a informação relativa à rastreabilidade dos dispositivos de identificação, à identificação dos animais "
                "de companhia, à sua titularidade ou detenção e à informação relacionada com a defesa da saúde pública, saúde animal e "
                "bem-estar animal.\n\n"
                "2 – A DGAV é a entidade responsável pelo SIAC, competindo-lhe assegurar o seu funcionamento e o tratamento seguro da informação.\n\n"
                "3 – A DGAV pode atribuir a gestão do SIAC a outras entidades, mediante a celebração de protocolo e parecer prévio da "
                "Comissão Nacional de Proteção de Dados.\n\n"
                "4 - As normas e procedimentos relativos ao funcionamento do SIAC constam de um Manual de Procedimentos SIAC, aprovado pelo "
                "diretor-geral de alimentação e veterinária."
            )
        },
        "codigo": {
            "ref": "Arts. 53.º, 55.º, 56.º, 57.º do Código do Animal (DL 214/2013)",
            "texto": (
                "Artigo 53.º - Identificação e registo na base de dados\n"
                "1 - Todos os cães devem ser identificados e registados entre os três e seis meses de idade.\n"
                "4 - Os cães e gatos são identificados através de método eletrónico e registados na base de dados nacional.\n"
                "5 - Identificação através de aplicação subcutânea de microchip no centro da face lateral esquerda do pescoço.\n\n"
                "Artigo 55.º - Base de dados\n"
                "1 - Toda a informação do registo coligida numa aplicação informática nacional.\n"
                "2 - A DGAV detém e coordena o acesso à base de dados, podendo autorizar gestão em outras entidades com parecer da "
                "Comissão Nacional de Proteção de Dados.\n\n"
                "Artigo 56.º - Classificação dos animais (Cão, Cão Potencialmente Perigoso, Cão Perigoso, Gato)"
            )
        },
        "legislacao": {
            "ref": "DL n.º 82/2019, Art.º 2.º (Estabelece SIAC)",
            "texto": (
                "DL 82/2019 estabelece o SIAC com extensas disposições cobrindo: criação da base de dados, procedimentos de registo e "
                "controlos de acesso, gestão por DGAV, identificação eletrónica via transponder, segurança de dados e autorização de acesso, "
                "integração de registos de identificação de animais, gestão da distribuição de dispositivos de identificação, procedimentos "
                "de registo e atualização. O sistema é totalmente operacional desde 2019."
            )
        },
        "divergencia": {
            "legislacao": "NÃO - SIAC em funcionamento desde 2019 cumpre todos os requisitos",
            "codigo": "NÃO - Código do Animal estabelece estrutura completa com classificações",
            "rgbeac": "NÃO - RGBEAC (Art. 20.º) reafirma e fortalece o sistema SIAC",
            "sumario": (
                "A legislação portuguesa CUMPRE COMPLETAMENTE os requisitos do Artigo 19. O SIAC (Sistema de Informação de Animais de "
                "Companhia) já está operacional desde 2019, sob responsabilidade de DGAV, com: identificação eletrónica via microchip "
                "obrigatória, registo nacional centralizado, rastreabilidade garantida, classificação de animais (normal/perigoso/potencialmente "
                "perigoso), integração de dados de saúde e bem-estar, conformidade com proteção de dados (Comissão Nacional de Proteção de Dados)."
            )
        },
        "necessidade_alteracao": "Não",
        "notas": "SIAC totalmente operacional e conforme - Interoperabilidade EU pendente de implementação"
    },
    {
        "id": "ART-20",
        "tema": "Recolha de Dados sobre Bem-Estar Animal e Relatório",
        "regulamento": {
            "ref": "Art.º 20 do Regulamento 2023/0447",
            "titulo": "Collection of data on animal welfare and reporting",
            "texto": (
                "1. The competent authorities shall collect, analyse and publish the data set out in Annex III.\n\n"
                "2. The competent authorities shall draw up and transmit to the Commission a report in electronic form, on the data set out "
                "in Annex III, by 31 August every 3 years starting from [6 years from the date of entry into force of this Regulation], "
                "summarising the data gathered for the previous 3 years.\n\n"
                "3. The Commission may, by means of implementing acts, establish a harmonised methodology for collecting the data set out in "
                "Annex III and establish a template for the report referred to in paragraph 2 of this Article. Those implementing acts shall "
                "be adopted in accordance with the examination procedure referred to in Article 24."
            ),
            "traducao": (
                "Disponível no documento Regulamento - Primeira Versão portuguesa.docx"
            ),
        },
        "rgbeac": {
            "ref": "Art.º 46.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "Artigo 46.º - Relatório Nacional Anual\n\n"
                "1 - Os centros de bem-estar animal e alojamentos remetem à DGAV no primeiro mês de cada ano civil, os relatórios de gestão "
                "do ano anterior, com números de animais recolhidos, restituídos, eutanasiados, cedidos, adotados, devolvidos após adoção, "
                "vacinados, esterilizados e intervencionados em programas CED.\n\n"
                "2 – A DGVA consolida a informação a nível nacional sobre bem-estar animal em cada ano, incluindo: acompanhamento da política "
                "internacional, prestação de apoios públicos, atividade do SIAC, resultados de planos de controlo, processos contraordenacionais, "
                "coimas aplicadas, atividade de centros de bem-estar, programas de interesse nacional, ações informativas e educativas, para "
                "efeitos de elaboração do Relatório Anual sobre a situação do Bem-Estar Animal."
            )
        },
        "codigo": {
            "ref": "Arts. 141.º-145.º do Código do Animal (DL 214/2013)",
            "texto": (
                "Código do Animal estabelece estrutura de monitorização e relatórios sobre bem-estar animal, incluindo: "
                "recolha de dados de infrações, aplicação de sanções, atividades de centros de recolha, estatísticas de animais processados. "
                "Sistema de contraordenações com documentação e coimas registadas."
            )
        },
        "legislacao": {
            "ref": "Decreto-Regulamentar n.º 3/2021 + DL 82/2019",
            "texto": (
                "Decreto-Regulamentar 3/2021 (Art. 3.º) requer Relatório Anual sobre situação do Bem-Estar Animal. "
                "DL 82/2019 estabelece procedimentos de recolha de dados, monitorização, registo de atividades médico-veterinárias "
                "e compilação de informação de bem-estar animal para fins de relatório anual e transmissão a autoridades europeias."
            )
        },
        "divergencia": {
            "legislacao": "SIM - Cobertura COMPLETA (relatórios anuais, recolha de dados, consolidação nacional)",
            "codigo": "SIM - Cobertura COMPLETA (monitorização, infrações, sanções, estatísticas)",
            "rgbeac": "SIM - Cobertura COMPLETA (Art. 46.º estabelece sistema de relatórios nacionais)",
            "sumario": (
                "A legislação portuguesa implementa COMPLETAMENTE o Artigo 20. Sistema já estabelecido com: recolha anual de dados "
                "de centros de bem-estar animal, consolidação de informação de bem-estar a nível nacional, inclusão de estatísticas de "
                "SIAC, registos de contraordenações e sanções, relatórios sobre atividades de proteção animal, conformidade com requisitos "
                "de Decreto-Regulamentar 3/2021. Único ajuste necessário: alinhamento da periodicidade de relatórios (atualmente anual; "
                "Regulamento requer trienal) e inclusão dos dados específicos de Annex III da EU (quando publicado)."
            )
        },
        "necessidade_alteracao": "Sim - Ajuste de periodicidade e conformidade com Annex III EU",
        "notas": "Sistema de relatórios já operacional - apenas alinhamento com padrões EU necessário"
    },
    {
        "id": "ART-20a",
        "tema": "Proteção de Dados",
        "regulamento": {
            "ref": "Art.º 20a do Regulamento 2023/0447",
            "titulo": "Data protection",
            "texto": (
                "The competent authorities of the Member States shall be controllers within the meaning of "
                "Regulation (EU) 2016/679 in relation to the processing of personal data collected under "
                "Article 7, Article 7a of this Regulation as well as under Article 19(1) of this Regulation "
                "when used for the purposes of official control.\n\n"
                "The Commission shall be a controller within the meaning of Regulation (EU) 2018/1725 in "
                "relation to the processing of personal data collected under Article 17a (6), Article 19 (2a) "
                "and the third subparagraph of Article 21(4a) of this Regulation, as well as under "
                "Article 19(1) of this Regulation when used for the purposes of compliance with Article 108 "
                "of Regulation (EU) 2017/625 and of reporting obligations under this Regulation.\n\n"
                "It shall be prohibited for any person having access to the personal data referred to in the "
                "first and second sub-paragraphs to divulge any personal data, the knowledge of which was "
                "acquired in the exercise of their duties or otherwise incidentally to such exercise.\n\n"
                "Member States and the Commission shall take all appropriate measures to address infringements "
                "of that prohibition.\n\n"
                "The personal data collected under the first and second sub-paragraphs shall not be used for "
                "other purposes than:\n\n"
                "a) official controls by Member States competent authorities of the compliance with the welfare "
                "and traceability requirements under this regulation and compliance with Regulation (EU) 2016/429, "
                "including and detection of fraudulent practices, and\n\n"
                "b) compliance by the Commission of its obligations under Article 108 of Regulation (EU) 2017/625 "
                "and with the Commission's reporting obligations under this Regulation.\n\n"
                "The personal data referred to in paragraph 1 of this Article shall be retained for the following periods:\n\n"
                "a) in the case of Article 7 and Article 7a, 10 years after the date of cessation of the activity of the establishment;\n\n"
                "b) in the case of Article 17a(6), 18 months after the generation of the token referred to in Article 17a(3)(c).\n\n"
                "c) in case of Article 19(1), and Article 19(2a), 25 years after the first registration of the dog or cat "
                "in the database referred to in that Article or 5 years after the recording of the death of the dog or cat in that database;\n\n"
                "d) in case of the third subparagraph of Article 21(4a), 5 years after the date of pre-notification."
            ),
            "traducao": (
                "As autoridades competentes dos Estados-Membros devem ser controladoras no sentido do "
                "Regulamento (UE) 2016/679 em relação ao tratamento de dados pessoais recolhidos de acordo com "
                "o Artigo 7, Artigo 7a do presente Regulamento, bem como no âmbito do Artigo 19(1) do presente "
                "Regulamento quando utilizados para efeitos de inspeção oficial.\n\n"
                "A Comissão deve ser controladora no sentido do Regulamento (UE) 2018/1725 em relação ao tratamento "
                "de dados pessoais recolhidos de acordo com o Artigo 17a (6), Artigo 19 (2a) e o terceiro parágrafo "
                "do Artigo 21(4a) do presente Regulamento, bem como no âmbito do Artigo 19(1) do presente Regulamento "
                "quando utilizados para efeitos de conformidade com o Artigo 108 do Regulamento (UE) 2017/625 e de "
                "obrigações de comunicação de informações previstas no presente Regulamento.\n\n"
                "Fica proibido a qualquer pessoa com acesso aos dados pessoais mencionados no primeiro e segundo "
                "parágrafos divulgar quaisquer dados pessoais, cuja notícia foi adquirida no exercício das suas funções "
                "ou de forma incidental a tal exercício.\n\n"
                "Os Estados-Membros e a Comissão devem adotar todas as medidas apropriadas para fazer face aos "
                "incumprimentos dessa proibição.\n\n"
                "[... redução para brevidade - ver regulamento completo para texto integral]"
            ),
        },
        "rgbeac": {
            "ref": "Art.º 20.º, nn. 3, 6, 8 do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "Artigo 20.º, n.º 8 - SIAC e Proteção de Dados:\n"
                "Ao tratamento, segurança, conservação, acesso e proteção dos dados pessoais constantes do SIAC "
                "é diretamente aplicável o disposto na legislação e regulamentação relativa à proteção de dados "
                "pessoais, nomeadamente o Regulamento (UE) 2016/679 do Parlamento Europeu e do Conselho, de 27 de "
                "abril de 2016, relativo à proteção das pessoas singulares no que diz respeito ao tratamento de dados "
                "pessoais e à livre circulação desses dados.\n\n"
                "Artigo 20.º, n.º 6 - Transmissão de Dados Pessoais:\n"
                "Sempre que se mostre necessário à operacionalização do SIAC ou ao cumprimento das suas finalidades, "
                "deve promover-se a transmissão de dados entre sistemas de informação, preferencialmente através da "
                "Plataforma de Interoperabilidade da Administração Pública (iAP), nos termos do Decreto-Lei n.º 135/99, "
                "de 22 de abril.\n\n"
                "Artigo 20.º, n.º 3 - Subcontratação de Dados Pessoais:\n"
                "A DGAV, pode atribuir a gestão do SIAC a outras entidades, mediante a celebração de protocolo e sob sua "
                "supervisão, observado o regime de subcontratação de tratamento de dados pessoais."
            )
        },
        "codigo": {
            "ref": "Art.º 55.º do Código do Animal (DL 214/2013)",
            "texto": (
                "Artigo 55.º - Base de Dados\n\n"
                "1 - Toda a informação resultante do registo do animal é coligida numa aplicação informática nacional.\n\n"
                "2 - A DGAV detém, define e coordena o acesso à base de dados, podendo autorizar a sua gestão noutras "
                "entidades, mediante a celebração de protocolos, precedidos de parecer da Comissão Nacional de Proteção de Dados.\n\n"
                "3 - Só têm acesso à base de dados as entidades que se encontrem autorizadas, para o efeito, pela DGAV."
            )
        },
        "legislacao": {
            "ref": "DL n.º 82/2019, Art.º 9.º",
            "texto": (
                "Artigo 9.º - Registo no Sistema de Informação de Animais de Companhia\n\n"
                "1 - Os animais de companhia abrangidos pela obrigação de identificação devem ser registados pelo médico "
                "veterinário no SIAC, imediatamente após a sua marcação com o transponder, em nome do respetivo titular."
            )
        },
        "divergencia": {
            "legislacao": "NÃO - Legislação portuguesa cobre completamente com incorporação de GDPR",
            "codigo": "NÃO - Cobertura expressa em Art. 55.º",
            "rgbeac": "NÃO - Implementação completa em Arts. 20.º",
            "sumario": (
                "A legislação portuguesa implementa completamente os requisitos de proteção de dados do Artigo 20a. "
                "O SIAC é configurado como sistema compliant com GDPR (EU 2016/679) e com regulamentações de proteção de dados. "
                "Não há necessidade de alterações legislativas."
            )
        },
        "necessidade_alteracao": "Não",
        "notas": "Correspondências confirmadas por agente de pesquisa em 2026-03-02"
    },
    {
        "id": "ART-21",
        "tema": "Entrada de Cães e Gatos na União",
        "regulamento": {
            "ref": "Art.º 21.º do Regulamento 2023/0447",
            "titulo": "Entry of dogs and cats into the Union",
            "texto": (
                "1. Dogs and cats may only be entered into the Union for placing on the Union market provided that "
                "the following conditions are met:\n\n"
                "a) they have been breed and kept in compliance with any of the following:\n"
                "   i) Chapter II of this Regulation;\n"
                "   ii) conditions recognised by the Union in accordance with Article 129 of Regulation (EU) 2017/625 "
                "to be equivalent to those set out by Chapter II of this Regulation; or\n"
                "   iii) where applicable, requirements contained in a specific agreement between the Union and the "
                "exporting country.\n\n"
                "b) they come from a third country or territory and an establishment listed in accordance with Articles 126 "
                "and 127 of Regulation (EU) 2017/625.\n\n"
                "2. The official certificate referred to in Article 126(2)(c) of Regulation (EU) 2017/625 accompanying dogs "
                "and cats entering into the Union from third countries and territories to be placed on the Union market, shall "
                "contain an attestation certifying compliance with paragraph 1 of this Article.\n\n"
                "3. Dogs and cats entering into the Union to be placed on the Union market shall be identified before their "
                "entry by a veterinarian by means of an injectable transponder containing a readable microchip compliant with "
                "Annex II.\n\n"
                "4. The operator responsible for the import of dogs or cats entering into the Union shall ensure the registration "
                "of the dogs or cats by a veterinarian into a national database referred to in Article 19(1), within 5 working "
                "days after their entry into the Union.\n\n"
                "[... ver regulamento completo para restantes parágrafos 4a e 5 ...]"
            ),
            "traducao": (
                "1. Os cães e os gatos podem ser introduzidos na União apenas para colocação no mercado da União se estiverem "
                "satisfeitas as seguintes condições:\n\n"
                "a) Tenham sido criados e mantidos em conformidade com qualquer das seguintes situações:\n"
                "   i) Capítulo II do presente Regulamento;\n"
                "   ii) Condições reconhecidas pela União em conformidade com o artigo 129.º do Regulamento (UE) 2017/625 como "
                "equivalentes às estabelecidas no Capítulo II do presente Regulamento; ou\n"
                "   iii) Quando aplicável, requisitos contidos num acordo específico entre a União e o país exportador.\n\n"
                "b) Provenham de um país terceiro ou território e de um estabelecimento listado em conformidade com os artigos 126.º "
                "e 127.º do Regulamento (UE) 2017/625.\n\n"
                "2. O certificado oficial referido no artigo 126.º, parágrafo 2, alínea c), do Regulamento (UE) 2017/625 que acompanha "
                "os cães e gatos que entram na União desde países terceiros e territórios para colocação no mercado da União deve conter "
                "uma atestação certificando a conformidade com o parágrafo 1 do presente artigo.\n\n"
                "3. Os cães e gatos que entram na União para colocação no mercado da União devem ser identificados antes da sua entrada "
                "por um médico veterinário através de um transponder injetável contendo um microchip legível em conformidade com o Anexo II.\n\n"
                "4. O operador responsável pela importação de cães ou gatos que entram na União deve assegurar o registo dos cães ou gatos "
                "por um médico veterinário numa base de dados nacional referida no artigo 19.º, parágrafo 1, no prazo de 5 dias úteis após "
                "a sua entrada na União.\n\n"
                "4a. O movimento não-comercial de um cão ou gato desde um país terceiro ou território para a União deve ser pré-notificado "
                "pelo seu proprietário numa base de dados online de viajantes da União com animais de estimação, pelo menos 5 dias úteis antes "
                "da passagem da fronteira da União, exceto nos seguintes casos:\n"
                "— cães ou gatos que entram na União diretamente desde países terceiros ou territórios que satisfazem as condições estabelecidas "
                "no artigo 17.º, parágrafo 1, alínea a), do Regulamento Delegado (C(2026) 20); e\n"
                "— cães ou gatos registados numa base de dados de um Estado-Membro referida no artigo 19.º, parágrafo 1.\n\n"
                "Se o cão ou gato permanecer mais de seis meses na União, o proprietário deve assegurar o seu registo por um médico veterinário "
                "na base de dados do Estado-Membro de residência referida no artigo 19.º, parágrafo 1, no prazo de 5 dias úteis após o termo do "
                "sexto mês. Os Estados-Membros podem permitir o registo por outras pessoas que não médicos veterinários, desde que tenham medidas "
                "em vigor para assegurar a exatidão das informações inseridas na base de dados."
            )
        },
        "rgbeac": {
            "ref": "Art.º 114.º e Art.º 96.º do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "Artigo 114.º - Entrada no Território Nacional\n"
                "1 - A entrada no território nacional, por compra, cedência ou troca direta, de cães classificados como "
                "potencialmente perigosos pode ser condicionada.\n\n"
                "2 - Os cães referidos no número anterior que não estejam inscritos em livro de origens oficialmente reconhecido, "
                "que permaneçam em território nacional por mais de quatro meses, são obrigatoriamente esterilizados nos termos do "
                "disposto no n.º 5.º do artigo 102.º.\n\n"
                "3 - A introdução no território nacional por compra, cedência ou troca direta, tendo em vista a sua reprodução, "
                "de cães potencialmente perigosos é sujeita a autorização da DGAV requerida com sete dias de antecedência, decorridos "
                "os quais a mesma é tacitamente deferida.\n\n"
                "Artigo 96.º - Importação de Animais de Companhia\n"
                "A importação de animais que constem da lista nacional de animais de companhia provenientes de outros Estados é "
                "admitida desde que sejam cumpridas as regras sanitárias e de bem-estar animal portuguesas e comunitárias."
            )
        },
        "codigo": {
            "ref": "Art.º 62.º do Código do Animal (DL 214/2013)",
            "texto": (
                "Artigo 62.º - Entrada de Animais de Companhia Suscetíveis à Raiva em Território Nacional\n\n"
                "1 - A entrada em território nacional de animais de companhia suscetíveis à raiva destinados ao comércio, "
                "provenientes de outros Estados-membros ou de países terceiros, depende do cumprimento das condições fixadas no "
                "Decreto-Lei n.º 79/2001, de 20 de junho, alterado pelo Decreto-Lei n.º 260/2012, de 12 de dezembro, e noutras "
                "normas de polícia sanitária que regem o comércio e as importações de animais vivos na comunidade.\n\n"
                "2 - No caso das importações, deve ainda ser cumprido o regime dos controlos veterinários previsto no Decreto-Lei "
                "n.º 79/2011, de 20 de junho.\n\n"
                "3 - A entrada em território nacional de furões destinados ao comércio ou sem carácter comercial, para além do "
                "cumprimento do disposto nos números anteriores, depende de autorização prévia do ICNF, I.P."
            )
        },
        "legislacao": {
            "ref": "DL n.º 82/2019, Art.º 2.º",
            "texto": (
                "Artigo 2.º - Âmbito de Aplicação\n\n"
                "O presente decreto-lei aplica-se à identificação de animais de companhia das espécies referidas no anexo I do "
                "Regulamento (UE) n.º 576/2013, do Parlamento Europeu e do Conselho, de 12 de junho de 2013, e no anexo I do "
                "Regulamento (UE) n.º 2016/429, do Parlamento Europeu e do Conselho, de 9 de março de 2016, nascidos ou presentes "
                "no território nacional."
            )
        },
        "divergencia": {
            "legislacao": "PARCIAL - Cobre entrada/importação mas sem database online de viajantes pré-notificação",
            "codigo": "SIM - Implementa controlos sanitários e requisitos de identificação",
            "rgbeac": "PARCIAL - Cobre entrada no território nacional com condições, não cobre movimento não-comercial pré-notificação",
            "sumario": (
                "A legislação portuguesa implementa os requisitos essenciais de entrada e identificação pré-entrada, referenciando "
                "os Regulamentos EU 576/2013 e 2016/429. Faltam: (1) Sistema de base de dados online de viajantes com pré-notificação "
                "obrigatória para movimento não-comercial; (2) Sistema iRASFF integrado para notificações de risco de fraude."
            )
        },
        "necessidade_alteracao": "Sim",
        "notas": "Parcialmente coberto. Complementação necessária para movimento não-comercial e sistema iRASFF."
    },
    {
        "id": "ART-22",
        "tema": "Alteração dos Anexos",
        "regulamento": {
            "ref": "Art.º 22.º do Regulamento 2023/0447",
            "titulo": "Amendment to the Annexes",
            "texto": (
                "1. The Commission is empowered to adopt delegated acts in accordance with Article 23 amending the Annexes to "
                "this Regulation to take into account of scientific and technical progress, including, when relevant, scientific "
                "opinions of the European Food Safety Authority, as regards:\n\n"
                "a) a suitable number of animal caretakers in breeding and selling establishments;\n\n"
                "b) watering and feeding requirements and weaning process;\n\n"
                "c) temperature ranges;\n\n"
                "d) lighting requirements;\n\n"
                "e) ammonia and carbon monoxide levels;\n\n"
                "f) kennel and cattery design;\n\n"
                "g) group housing;\n\n"
                "h) space allowances for different categories of dogs and cats;\n\n"
                "i) frequency of pregnancies;\n\n"
                "j) minimum and maximum age of bitches and queens for breeding;\n\n"
                "k) socialisation, enrichment and other measures for meeting behavioural needs of dogs and cats;\n\n"
                "l) requirements for transponders used to individually identify dogs and cats;\n\n"
                "m) data to be collected for policy monitoring and evaluation.\n\n"
                "2. Any additions of requirements in the Annexes shall be based on updated scientific or technical evidence, in particular "
                "regarding the specific conditions needed to ensure the welfare of the dogs and cats covered by the scope of this Regulation. "
                "Where relevant, those delegated acts shall take into account social, economic and environmental impacts and provide for "
                "sufficient transition periods to allow for operators concerned to adapt to the new requirements."
            ),
            "traducao": (
                "1. A Comissão fica habilitada a adotar atos delegados em conformidade com o artigo 23.º que alterem os anexos do presente "
                "Regulamento para ter em conta o progresso científico e técnico, incluindo, quando relevante, pareceres científicos da Autoridade "
                "Europeia para a Segurança dos Alimentos, nos seguintes aspetos:\n\n"
                "a) Um número adequado de cuidadores de animais em estabelecimentos de criação e venda;\n\n"
                "b) Requisitos de abastecimento de água e alimentação e processo de desmame;\n\n"
                "c) Gamas de temperatura;\n\n"
                "d) Requisitos de iluminação;\n\n"
                "e) Níveis de amoníaco e monóxido de carbono;\n\n"
                "f) Conceção de canis e gateis;\n\n"
                "g) Alojamento em grupo;\n\n"
                "h) Espaços permitidos para diferentes categorias de cães e gatos;\n\n"
                "i) Frequência de gestações;\n\n"
                "j) Idade mínima e máxima de cadelas e gatas para reprodução;\n\n"
                "k) Socialização, enriquecimento e outras medidas para satisfazer as necessidades comportamentais de cães e gatos;\n\n"
                "l) Requisitos para transponders utilizados na identificação individual de cães e gatos;\n\n"
                "m) Dados a recolher para avaliação e monitorização de políticas.\n\n"
                "2. Qualquer complemento de requisitos nos Anexos deve ser baseado em evidência científica ou técnica atualizada, em particular "
                "no que diz respeito às condições específicas necessárias para assegurar o bem-estar dos cães e gatos abrangidos pelo âmbito do "
                "presente Regulamento. Quando relevante, esses atos delegados devem levar em conta impactos sociais, económicos e ambientais e "
                "prever períodos de transição suficientes para permitir aos operadores envolvidos a adaptação aos novos requisitos."
            )
        },
        "rgbeac": {
            "ref": "Arts. 3-8 e ANEXO do RGBEAC (proposta, jun. 2025)",
            "texto": (
                "Artigos 3.º a 8.º do Decreto-Lei que aprova o RGBEAC estabelecem mecanismo legislativo para alteração de diplomas "
                "anteriores. O RGBEAC contém um ANEXO estruturado com:\n\n"
                "- TÍTULO I: Disposições gerais\n"
                "- TÍTULO II: Obrigações e proibições (Lista Nacional de Animais, identificação, registo)\n"
                "- TÍTULO III: Fiscalização, contraordenações, crimes e sanções\n"
                "- TÍTULO V: Disposições finais\n\n"
                "O ANEXO contém todas as disposições técnicas relativas a bem-estar, espaço disponível, temperatura, frequência de "
                "alimentação, e outros parâmetros correspondentes aos Anexos I-V do Regulamento EU 2023/0447.\n\n"
                "NOTA: O mecanismo atual é legislativo padrão (alteração de Decreto-Lei por novo Decreto-Lei). NÃO existe autoridade "
                "delegada expressa para alteração por atos de execução, conforme previsto no Art. 22-24 do Regulamento EU 2023/0447."
            )
        },
        "codigo": {
            "ref": "Art.º 23.º e ANEXO II do Código do Animal (DL 214/2013)",
            "texto": (
                "Artigo 23.º - Condições Particulares para a Manutenção de Cães e Gatos\n\n"
                "1 - O alojamento de cães e gatos deve obedecer às dimensões mínimas indicadas no anexo II ao presente diploma.\n\n"
                "ANEXO II - Parâmetros Técnicos de Alojamento\n"
                "Contém requisitos para:\n"
                "- Dimensões mínimas de gaiolas e recintos\n"
                "- Superfícies de exercício\n"
                "- Estruturas para enriquecimento ambiental (gatos: tabuleiros, superfícies de repouso, estruturas para afiar garras)\n"
                "- Pavimentos (proibição de grades)\n"
                "- Condições de higiene e bem-estar\n\n"
                "Corresponde materialmente aos requisitos de espaço, temperatura e frequência referidos no Art. 22 do Regulamento."
            )
        },
        "legislacao": {
            "ref": "DL n.º 82/2019 - Referências a Anexos de Regulamentos EU",
            "texto": (
                "DL n.º 82/2019 incorpora por referência os Anexos I dos Regulamentos EU n.º 576/2013 e n.º 2016/429, estabelecendo "
                "que os requisitos de identificação de animais de companhia aplicáveis em Portugal são os das espécies referidas nesses anexos.\n\n"
                "NOTA: DL 82/2019 não implementa mecanismo de delegação de autoridade para alteração de anexos como previsto no Art. 22-24 "
                "do Regulamento EU 2023/0447."
            )
        },
        "divergencia": {
            "legislacao": "PARCIAL - Anexos existem; falta delegação de autoridade para alteração dinâmica",
            "codigo": "PARCIAL - Estrutura de anexos com parâmetros técnicos; falta delegação",
            "rgbeac": "PARCIAL - ANEXO estruturado; falta mecanismo de atos delegados/execução",
            "sumario": (
                "A legislação portuguesa possui estrutura de anexos contendo parâmetros técnicos equivalentes aos do Regulamento. "
                "Falta implementar: Mecanismo de delegação de autoridade à Comissão Europeia para adoção de atos delegados/execução, "
                "conforme Arts. 22-24 do Regulamento 2023/0447. Atualmente, qualquer alteração de anexos requer procedimento legislativo "
                "nacional (novo Decreto-Lei), não havendo procedimento expedito de atos delegados."
            )
        },
        "necessidade_alteracao": "Sim",
        "notas": "Estrutura de anexos presente mas sem mecanismo de delegação de autoridade para atos delegados/execução conforme Reg. EU."
    }
]

# ---------------------------------------------------------------------------
# CORES (sistema cromático por diploma)
# ---------------------------------------------------------------------------

COR = {
    "regulamento_header": "8AAFCF",   # azul pastel médio (menos intenso)
    "regulamento_body":   "E8F2F8",   # azul pastel muito claro
    "regulamento_trad":   "F4F9FD",   # azul pastel extremamente claro
    "rgbeac_header":      "7FAA8C",   # verde pastel médio (menos intenso)
    "rgbeac_body":        "E8F3E6",   # verde pastel muito claro
    "codigo_header":      "B8956A",   # castanho pastel médio (menos intenso)
    "codigo_body":        "FFF5ED",   # castanho pastel muito claro
    "legislacao_header":  "75A6AE",   # teal pastel médio (menos intenso)
    "legislacao_body":    "F0FBFD",   # teal pastel muito claro
    "divergencia_header": "A689C6",   # roxo pastel médio (menos intenso)
    "divergencia_body":   "F5EEF9",   # roxo pastel muito claro
    "notas_header":       "909090",   # cinza pastel médio (menos intenso)
    "notas_body":         "FAFAFA",   # cinza pastel muito claro
    "tema_header":        "6A7A8A",   # cinza-azul pastel (menos intenso)
    "alternado_a":        "FBFBFB",
    "alternado_b":        "F7F9FE",
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
        ("Div. vs @legislacao", 38),
        ("Div. vs @codigo", 38),
        ("Div. vs @rgbeac", 38),
        ("Sumário / Proposta", 38),
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
            art["divergencia"].get("legislacao", ""),
            art["divergencia"].get("codigo", ""),
            art["divergencia"].get("rgbeac", ""),
            art["divergencia"].get("sumario", ""),
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
    --reg:    #8AAFCF;
    --reg-bg: #F0F7FC;
    --reg-tr: #F7FAFD;
    --rgb:    #7FAA8C;
    --rgb-bg: #F0F7F4;
    --cod:    #B8956A;
    --cod-bg: #FFF9F2;
    --leg:    #75A6AE;
    --leg-bg: #F5FCFD;
    --div:    #A689C6;
    --div-bg: #F9F6FD;
    --nota:   #909090;
    --nota-bg:#FAFAFA;
    --dark:   #6A7A8A;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', Calibri, sans-serif; background: #F8F9FB; color: #333; }}

  /* HEADER */
  header {{
    background: var(--dark);
    color: #fff;
    padding: 18px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky; top: 0; z-index: 100;
    border-bottom: 1px solid rgba(0,0,0,0.08);
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
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(138,175,207,0.25);
  }}

  /* FORMATAÇÃO DE TEXTO LEGAL */
  .leg-block + .leg-block {{ margin-top: 7px; }}
  .leg-p {{ margin: 0; line-height: 1.65; text-align: justify; }}
  .leg-alinea {{
    margin: 2px 0; line-height: 1.6;
    padding-left: 1.8em; text-indent: -1.8em;
  }}
  .leg-sub {{
    margin: 2px 0; line-height: 1.55;
    padding-left: 3.2em; text-indent: -1.0em;
  }}
  /* Texto secundário (cinza) */
  .leg-block.leg-dim p {{ color: #b0b0b0; }}
  /* Cabeçalho de artigo dentro de coluna (múltiplos artigos por diploma) */
  .leg-art-header {{
    font-weight: 700; font-size: .8rem; margin: 10px 0 3px;
    padding-top: 8px; border-top: 1px solid rgba(0,0,0,0.06);
    display: block;
  }}
  .leg-block:first-child > .leg-art-header:first-child {{
    margin-top: 0; padding-top: 0; border-top: none;
  }}

  /* DIVERGÊNCIA ESTRUTURADA */
  .div-section {{ margin-bottom: 10px; }}
  .div-section:last-child {{ margin-bottom: 0; }}
  .div-tag {{
    display: inline-block;
    border-radius: 3px; padding: 1px 8px;
    font-size: .72rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: .5px;
    margin-right: 6px; vertical-align: middle;
    white-space: nowrap;
  }}
  .div-tag.tag-leg  {{ background: var(--leg); color: #fff; }}
  .div-tag.tag-cod  {{ background: var(--cod); color: #fff; }}
  .div-tag.tag-rgb  {{ background: var(--rgb); color: #fff; }}
  .div-tag.tag-sum  {{ background: var(--div); color: #fff; }}
  .div-text {{ display: inline; font-size: .87rem; line-height: 1.6; }}

  /* GRID 3 COLUNAS (diplomas nacionais) */
  .grid {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-bottom: 20px; }}
  @media (max-width: 1100px) {{ .grid {{ grid-template-columns: 1fr 1fr; }} }}
  @media (max-width: 700px)  {{ .grid {{ grid-template-columns: 1fr; }} }}

  /* CARD */
  .card {{ border-radius: 6px; overflow: hidden; border: 1px solid rgba(0,0,0,0.06); box-shadow: none; }}
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
  .card.reg-tr .card-header {{ background: #7FAED4; }}
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
  const div = art.divergencia || {{}};
  const campos = [
    art.id, art.tema,
    art.regulamento.ref, art.regulamento.titulo,
    art.regulamento.texto, art.regulamento.traducao,
    art.rgbeac.ref, art.rgbeac.texto,
    art.codigo.ref, art.codigo.texto,
    art.legislacao.ref, art.legislacao.texto,
    div.legislacao, div.codigo, div.rgbeac, div.sumario
  ];
  return campos.some(c => (c || '').toLowerCase().includes(q));
}}

function getSnippet(art, q) {{
  const div = art.divergencia || {{}};
  const campos = [
    art.regulamento.traducao, art.regulamento.texto,
    art.rgbeac.texto, art.codigo.texto,
    art.legislacao.texto,
    div.legislacao, div.codigo, div.rgbeac, div.sumario
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

/* Formata texto legal com deteção automática de alíneas e subalíneas */
function hl(s) {{
  if (!searchTerm || !s) return s || '';
  const re = new RegExp(searchTerm.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&'), 'gi');
  return s.replace(re, m => `<mark>${{m}}</mark>`);
}}

function formatarTexto(str) {{
  if (!str) return '';
  const blocos = str.split(/\\n\\n+/);
  return blocos.map(bloco => {{
    const isDim = bloco.startsWith('[dim]');
    const blockText = isDim ? bloco.slice(5) : bloco;
    const dimCls = isDim ? ' leg-dim' : '';
    const linhas = blockText.split('\\n').filter(l => l.trim() !== '');
    if (!linhas.length) return '';
    const ps = linhas.map(linha => {{
      const t = linha.trim();
      if (/^Artigo\\s+\\d+/i.test(t)) {{
        return `<p class="leg-art-header">${{hl(t)}}</p>`;
      }}
      if (/^[—–]\\s/.test(t) || t === '—' || t === '–') {{
        return `<p class="leg-sub">${{hl(t)}}</p>`;
      }}
      if (/^[a-z]\\)/.test(t) || /^\\([a-z-]+\\)/.test(t)) {{
        return `<p class="leg-alinea">${{hl(t)}}</p>`;
      }}
      return `<p class="leg-p">${{hl(t)}}</p>`;
    }}).join('');
    return `<div class="leg-block${{dimCls}}">${{ps}}</div>`;
  }}).join('');
}}

function renderDiv(div) {{
  if (!div) return '';
  const secs = [
    {{ cls: 'tag-leg', label: '@legislacao',  texto: div.legislacao }},
    {{ cls: 'tag-cod', label: '@codigo',      texto: div.codigo }},
    {{ cls: 'tag-rgb', label: '@rgbeac',      texto: div.rgbeac }},
    {{ cls: 'tag-sum', label: 'Sumário',      texto: div.sumario }},
  ];
  return secs.map(s => `
    <div class="div-section">
      <span class="div-tag ${{s.cls}}">${{s.label}}</span>
      <span class="div-text">${{hl(s.texto)}}</span>
    </div>`).join('');
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

    <div class="card reg" style="margin-bottom:14px;">
      <div class="card-header">
        @regulamento — ${{art.regulamento.titulo}}
        <span class="card-header-ref">${{art.regulamento.ref}} · Texto original EN</span>
      </div>
      <div class="card-body">
        ${{formatarTexto(art.regulamento.texto)}}
      </div>
    </div>

    <div class="card reg-tr" style="margin-bottom:20px;">
      <div class="card-header">
        @regulamento — Tradução PT-PT
        <span class="card-header-ref">${{art.regulamento.ref}}</span>
      </div>
      <div class="card-body">
        ${{formatarTexto(art.regulamento.traducao)}}
      </div>
    </div>

    <div class="grid">
      <div class="card rgb">
        <div class="card-header">@rgbeac (proposta jun. 2025)</div>
        <div class="card-body">
          <div class="card-ref">${{art.rgbeac.ref}}</div>
          ${{formatarTexto(art.rgbeac.texto)}}
        </div>
      </div>
      <div class="card cod">
        <div class="card-header">@codigo (DL n.º 214/2013)</div>
        <div class="card-body">
          <div class="card-ref">${{art.codigo.ref}}</div>
          ${{formatarTexto(art.codigo.texto)}}
        </div>
      </div>
      <div class="card leg">
        <div class="card-header">@legislacao (legislação vigente)</div>
        <div class="card-body">
          <div class="card-ref">${{art.legislacao.ref}}</div>
          ${{formatarTexto(art.legislacao.texto)}}
        </div>
      </div>
    </div>

    <div class="div-box">
      <strong>Divergência face ao Regulamento
        <span class="badge-alt">Necessidade de alteração: ${{art.necessidade_alteracao}}</span>
      </strong>
      ${{renderDiv(art.divergencia)}}
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
  const linhas = [['ID', 'Tema', 'Art. Regulamento', 'Art. RGBEAC', 'Art. Código',
                   'Art. Legislação Vigente', 'Div. @legislacao', 'Div. @codigo',
                   'Div. @rgbeac', 'Sumário', 'Necessidade Alteração', 'Notas de Reunião']];
  ARTIGOS.forEach(a => {{
    const d = a.divergencia || {{}};
    linhas.push([
      a.id, a.tema,
      a.regulamento.ref, a.rgbeac.ref, a.codigo.ref,
      a.legislacao.ref,
      d.legislacao || '', d.codigo || '', d.rgbeac || '', d.sumario || '',
      a.necessidade_alteracao,
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
