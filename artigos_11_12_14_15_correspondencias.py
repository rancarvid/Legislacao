#!/usr/bin/env python3
"""
Artigos 11, 12, 14, 15 do Regulamento 2023/0447
Com correspondências portuguesas (@rgbeac, @codigo, @legislacao) e análise de divergências
Data: 2026-03-02
Correspondências encontradas por agente de pesquisa
"""

ARTICLES_11_12_14_15_COMPLETE = [
    {
        "id": "ART-11",
        "tema": "Alimentação e Hidratação",
        "regulamento": "Art.º 11.º - Feeding and watering",
        "correspondencias": {
            "codigo": {
                "ref": "Art.º 46.º do Código do Animal (DL 214/2013)",
                "titulo": "Alimentação e abeberamento",
                "texto": (
                    "A alimentação dos animais de companhia, nos locais de criação, manutenção e venda bem como nos "
                    "centros de recolha e instalações de hospedagem, deve obedecer a um programa de alimentação bem definido, "
                    "de valor nutritivo adequado e distribuído em quantidade suficiente para satisfazer as necessidades alimentares "
                    "das espécies.\n\n"
                    "Os animais devem dispor de água potável e sem qualquer restrição, salvo por razões médico-veterinárias."
                ),
                "divergencia_sumario": "COBERTURA COMPLETA - Art. 46.º implementa integralmente os requisitos do Art. 11.º"
            },
            "rgbeac": {
                "ref": "Arts. 7.º (n.º 1, al. a) e 10.º (n.º 1, al. a) do RGBEAC (proposta, jun. 2025)",
                "titulo": "Princípios fundamentais e Obrigações especiais dos detentores",
                "texto": (
                    "Art. 7.º: Não passem fome ou sede, nem sejam sujeitos a malnutrição.\n\n"
                    "Art. 10.º: Alimentos saudáveis, adequados e convenientes ao seu normal desenvolvimento e "
                    "acesso permanente a água potável. Ênfase em necessidades nutricionais adequadas ao estado de saúde."
                ),
                "divergencia_sumario": "COBERTURA COMPLETA - Linguagem modernizada e alinhada com Regulamento europeu"
            },
            "legislacao": {
                "ref": "DL 82/2019",
                "titulo": "Bem-estar de animais de companhia - não específico",
                "texto": (
                    "DL 82/2019 regulamenta identificação de animais. Não aborda especificamente requisitos de alimentação."
                ),
                "divergencia_sumario": "NÃO APLICÁVEL"
            }
        },
        "analise_divergencias": {
            "necessidade_alteracao": "Não",
            "observacoes": "Legislação portuguesa cobre completamente. RGBEAC (2025) alinha perfeitamente com Regulamento europeu."
        }
    },
    {
        "id": "ART-12",
        "tema": "Alojamento (Housing)",
        "regulamento": "Art.º 12.º - Housing",
        "correspondencias": {
            "codigo": {
                "ref": "Arts. 3.º, 14.º, 18.º, 28.º do Código do Animal (DL 214/2013)",
                "titulo": "Definições, Fatores ambientais e Instalações",
                "texto": (
                    "Art. 3.º: Define 'Alojamento' como qualquer instalação, edifício ou local onde animais se encontram mantidos.\n\n"
                    "Art. 14.º: A temperatura, ventilação, luminosidade e obscuridade devem ser adequadas ao conforto e bem-estar.\n\n"
                    "Art. 18.º: Alojamentos devem possuir instalações para armazenagem, lavagem, quarentena, enfermaria e higienização.\n\n"
                    "Art. 28.º: Define separação por espécie e requisitos de estrutura para hospedagem."
                ),
                "divergencia_sumario": "COBERTURA COMPLETA - Código implementa requisitos principais do Art. 12.º"
            },
            "rgbeac": {
                "ref": "Arts. 7.º, 10.º, 11.º, 47-57 do RGBEAC (proposta, jun. 2025)",
                "titulo": "Princípios, Obrigações especiais e Condições de alojamentos",
                "texto": (
                    "Art. 7.º: Condições de detenção e alojamento salvaguardam bem-estar animal.\n\n"
                    "Art. 10.º: Liberdade de movimento, proibição de contenção permanente, espaço adequado, "
                    "enriquecimento ambiental e abrigo protetor.\n\n"
                    "Art. 11.º: Obrigações especiais relativas ao alojamento doméstico.\n\n"
                    "Arts. 47-57: Regulação detalhada de alojamentos para hospedagem (estruturas, proteção, "
                    "maneio, responsabilidades veterinárias)."
                ),
                "divergencia_sumario": "COBERTURA EXPANDIDA - RGBEAC especifica detalhes técnicos e alinha com Regulamento europeu"
            },
            "legislacao": {
                "ref": "Lei 27/2016, DL 82/2019",
                "titulo": "Legislação adicional - não específica para alojamento",
                "texto": (
                    "Lei 27/2016 aborda recolha de animais errantes. DL 82/2019 regulamenta identificação. "
                    "Nenhum diploma específico complementar para condições detalhadas de alojamento."
                ),
                "divergencia_sumario": "NÃO APLICÁVEL"
            }
        },
        "analise_divergencias": {
            "necessidade_alteracao": "Sim - Portaria complementar com especificações técnicas detalhadas (temperatura, ventilação, iluminação)",
            "observacoes": "@CODIGO e @RGBEAC cobrem princípios; faltam normas técnicas pormenorizadas como valores mínimos de temperatura/ventilação"
        }
    },
    {
        "id": "ART-14",
        "tema": "Necessidades Comportamentais (Behavioural needs)",
        "regulamento": "Art.º 14.º - Behavioural needs",
        "correspondencias": {
            "codigo": {
                "ref": "Arts. 5.º e 13.º do Código do Animal (DL 214/2013)",
                "titulo": "Princípios de bem-estar e condições de alojamento",
                "texto": (
                    "Art. 5.º - Princípios que proíbem violência e maus-tratos, garantem bem-estar.\n\n"
                    "Art. 13.º - Espaço para exercício físico e expressão de comportamentos naturais.\n\n"
                    "Cobertura GENÉRICA: não especifica enriquecimento, socialização ou método de treino baseado em reforço positivo."
                ),
                "divergencia_sumario": "COBERTURA PARCIAL/GENÉRICA - Faltam especificações sobre socialização, enriquecimento, métodos"
            },
            "rgbeac": {
                "ref": "RGBEAC (proposta, jun. 2025)",
                "titulo": "Obrigações especiais e Proibições gerais",
                "texto": (
                    "Especificação clara: 'exercício físico e estímulo mental'.\n"
                    "'Contato social adequado'.\n"
                    "Métodos de 'reforço positivo' (OBRIGATÓRIO).\n"
                    "Proibição explícita de 'métodos aversivos, punitivos ou violentos'.\n"
                    "Documentação obrigatória de estratégia de socialização (criadores)."
                ),
                "divergencia_sumario": "COBERTURA SIGNIFICATIVAMENTE EXPANDIDA - Alinha bem com Regulamento europeu"
            },
            "legislacao": {
                "ref": "Lei 27/2016, DL 82/2019",
                "titulo": "Legislação de recolha e identificação",
                "texto": (
                    "Lei 27/2016 - Rede de centros de recolha (não cobre necessidades comportamentais).\n"
                    "DL 82/2019 - Identificação (não cobre necessidades comportamentais)."
                ),
                "divergencia_sumario": "NÃO APLICÁVEL"
            }
        },
        "analise_divergencias": {
            "necessidade_alteracao": "Sim - RGBEAC necessita regulamentação específica sobre métodos de treino",
            "observacoes": "RGBEAC (2025) oferece avanço substancial. Falta ainda regulamentação pormenorizada sobre socialização e enriquecimento."
        }
    },
    {
        "id": "ART-15",
        "tema": "Práticas Dolorosas (Painful practices)",
        "regulamento": "Art.º 15.º - Painful practices",
        "correspondencias": {
            "codigo": {
                "ref": "Arts. 51.º e 52.º do Código do Animal (DL 214/2013)",
                "titulo": "Intervenções cirúrgicas e proibição de mutilações",
                "texto": (
                    "Art. 51.º - Intervenções cirúrgicas exclusivamente por médico veterinário.\n\n"
                    "Art. 52.º - Proibição específica de mutilações:\n"
                    "- Corte de orelhas (exceto fins medicinais)\n"
                    "- Corte de cauda (revogado em 2015)\n"
                    "- Ressecção de cordas vocais\n"
                    "- Remoção de unhas/dentes\n"
                    "- Exceções: reprodução e interesse do animal (com documentação)"
                ),
                "divergencia_sumario": "COBERTURA COMPLETA - Arts. 51.º-52.º implementam integralmente Art. 15.º Regulamento"
            },
            "rgbeac": {
                "ref": "RGBEAC (proposta, jun. 2025)",
                "titulo": "Artigo 12.º - Proibições gerais",
                "texto": (
                    "Lista idêntica de mutilações proibidas ao Código.\n"
                    "Referência a 'boas práticas internacionais' (alinhamento com Reg. 2023/0447).\n"
                    "Alargamento: 'qualquer amputação sem razão médica veterinária'.\n"
                    "Ênfase em anestesia e analgesia prolongada.\n"
                    "Documentação obrigatória de indicação médica."
                ),
                "divergencia_sumario": "COBERTURA COMPLETA + EXPANSÃO - Alinha substancialmente com Regulamento europeu"
            },
            "legislacao": {
                "ref": "Lei 27/2016, DL 82/2019",
                "titulo": "Legislação adicional",
                "texto": (
                    "Lei 27/2016 - Recolha de animais errantes (não cobre mutilações).\n"
                    "DL 82/2019 - Identificação (não cobre mutilações).\n"
                    "Nenhum diploma específico adicional necessário."
                ),
                "divergencia_sumario": "NÃO APLICÁVEL"
            }
        },
        "analise_divergencias": {
            "necessidade_alteracao": "Não",
            "observacoes": "Legislação portuguesa (Código + RGBEAC) cobre COMPLETAMENTE. RGBEAC alinha bem com Regulamento europeu."
        }
    }
]

if __name__ == "__main__":
    print("Artigos 11, 12, 14, 15 - Correspondências Portuguesas e Divergências")
    print(f"Total de artigos: {len(ARTICLES_11_12_14_15_COMPLETE)}")
    for art in ARTICLES_11_12_14_15_COMPLETE:
        print(f"  ✓ {art['id']}: {art['tema']}")
        print(f"    Alteração necessária: {art['analise_divergencias']['necessidade_alteracao']}")
