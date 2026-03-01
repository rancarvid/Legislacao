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
            "estabelecimentos. O @codigo fixa entre 3 e 6 meses, sem distinguir o contexto de estabelecimento. "
            "O @rgbeac alinha com o @regulamento mas aplica-se apenas a cães, gatos e furões."
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
            "ao operador (não à família). O @rgbeac e o @codigo centram a responsabilidade no detentor individual, "
            "sem distinguir o contexto de acolhimento temporário nem fixar limites numéricos."
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
            "O @regulamento exige notificação prévia das autoridades com dados detalhados (capacidade, raças, "
            "ninhadas estimadas). O @codigo regula condições de reprodução mas não prevê registo ou notificação "
            "de estabelecimentos criadores. O @rgbeac trata da esterilização de errantes, não da notificação de "
            "criadores — há uma lacuna normativa face ao @regulamento."
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

  /* GRID 4 COLUNAS */
  .grid {{ display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 16px; margin-bottom: 20px; }}
  @media (max-width: 1400px) {{ .grid {{ grid-template-columns: 1fr 1fr; }} }}
  @media (max-width: 800px)  {{ .grid {{ grid-template-columns: 1fr; }} }}

  /* CARD */
  .card {{ border-radius: 8px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,.12); }}
  .card-header {{
    padding: 10px 16px; font-size: .78rem;
    font-weight: 700; text-transform: uppercase; letter-spacing: .8px;
    color: #fff;
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
</style>
</head>
<body>

<header>
  <h1>Comparativo Artigo a Artigo — Regulamento 2023/0447 (Cães e Gatos)</h1>
  <span id="progresso"></span>
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

function renderSidebar() {{
  const nav = document.getElementById('sidebar');
  nav.innerHTML = '<h2>Artigos</h2>';
  ARTIGOS.forEach((art, i) => {{
    const btn = document.createElement('button');
    btn.innerHTML = `<b>${{art.id}}</b><small>${{art.tema}}</small>`;
    btn.className = i === atual ? 'active' : '';
    btn.onclick = () => {{ atual = i; render(); }};
    nav.appendChild(btn);
  }});
}}

function nl2br(str) {{
  return str.replace(/\\n/g, '<br>');
}}

function render() {{
  const art = ARTIGOS[atual];
  renderSidebar();
  document.getElementById('progresso').textContent =
    `${{atual + 1}} / ${{ARTIGOS.length}}`;

  document.getElementById('main-content').innerHTML = `
    <div class="art-badge">${{art.id}}</div>
    <div class="tema-title">${{art.tema}}</div>

    <div class="grid">
      <div class="card reg">
        <div class="card-header">@regulamento (texto original EN)</div>
        <div class="card-body">
          <div class="card-ref">${{art.regulamento.ref}}</div>
          <pre>${{nl2br(art.regulamento.texto)}}</pre>
        </div>
      </div>
      <div class="card rgb">
        <div class="card-header">@rgbeac (proposta jun. 2025)</div>
        <div class="card-body">
          <div class="card-ref">${{art.rgbeac.ref}}</div>
          <pre>${{nl2br(art.rgbeac.texto)}}</pre>
        </div>
      </div>
      <div class="card cod">
        <div class="card-header">@codigo (DL n.º 214/2013)</div>
        <div class="card-body">
          <div class="card-ref">${{art.codigo.ref}}</div>
          <pre>${{nl2br(art.codigo.texto)}}</pre>
        </div>
      </div>
      <div class="card leg">
        <div class="card-header">@legislacao (legislação vigente)</div>
        <div class="card-body">
          <div class="card-ref">${{art.legislacao.ref}}</div>
          <pre>${{nl2br(art.legislacao.texto)}}</pre>
        </div>
      </div>
    </div>

    <div class="card reg-tr" style="margin-bottom:20px;">
      <div class="card-header">Tradução do @regulamento (PT-PT)</div>
      <div class="card-body">
        <pre>${{nl2br(art.regulamento.traducao)}}</pre>
      </div>
    </div>

    <div class="div-box">
      <strong>Divergência face ao Regulamento
        <span class="badge-alt">Necessidade de alteração: ${{art.necessidade_alteracao}}</span>
      </strong>
      ${{nl2br(art.divergencia)}}
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
