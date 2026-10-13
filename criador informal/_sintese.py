# -*- coding: utf-8 -*-
"""Gera a síntese em dez pontos (314 vs alojamentos). Aptos 11, preto, sem negrito nem travessões."""
import re, zipfile, shutil
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

OUT = "Sintese_Limites_por_Fogo_2026-10-09.docx"
T = [
    ('t', 'Limites de detenção por fogo e lotação dos alojamentos registados'),
    ('s', 'Questão'),
    ('p', 'Os limites de animais fixados no n.º 2 do artigo 3.º do Decreto-Lei n.º 314/2003, de 17 de dezembro, fixam a lotação de um alojamento registado por mera comunicação prévia nos termos do artigo 3.º-A do Decreto-Lei n.º 276/2001, de 17 de outubro?'),
    ('s', 'Resposta'),
    ('p', 'Não. Os limites do n.º 2 contam por fogo, e um alojamento registado não é um fogo. A lotação do alojamento rege-se pelo Decreto-Lei n.º 276/2001. O dever geral de salubridade do n.º 1 do mesmo artigo aplica-se sempre, incluindo ao alojamento registado.'),
    ('s', 'Fundamentos'),
    ('p', '1. A unidade de contagem é o fogo, não o prédio. «Nos prédios urbanos podem ser alojados até três cães ou quatro gatos adultos por cada fogo, não podendo no total ser excedido o número de quatro animais, excepto se, a pedido do detentor, e mediante parecer vinculativo do médico veterinário municipal e do delegado de saúde, for autorizado alojamento até ao máximo de seis animais adultos» (n.º 2 do artigo 3.º do Decreto-Lei n.º 314/2003). Fogo é a unidade de habitação. Um prédio com dez fogos comporta dez vezes o limite. Onde não há fogo, a norma não tem a que se aplicar.'),
    ('p', '2. Um alojamento registado não é um fogo. A lei impõe-lhe uma estrutura que a habitação não tem: «Os alojamentos para a reprodução/criação […] devem possuir instalações individualizadas destinadas à maternidade e à criação até à idade adulta, a quarentena, a enfermaria, o manuseamento de alimentos e à higienização dos animais» (n.º 2 do artigo 25.º do Decreto-Lei n.º 276/2001). Cumprir esta norma é constituir um conjunto distinto da casa.'),
    ('p', '3. A lotação do alojamento tem regime próprio e completo. A comunicação prévia indica «A capacidade máxima de animais e respetivas espécies a alojar» (alínea h) do n.º 1 do artigo 3.º-A), capacidade limitada materialmente pelas «dimensões mínimas indicadas no anexo iii» (n.º 1 do artigo 27.º). Havendo regime especial, não há lacuna a preencher com norma de outro diploma.'),
    ('p', '4. A norma sancionatória confirma o objeto doméstico do artigo 3.º. Pune-se «A permanência de cães e gatos em habitações e terrenos anexos em desrespeito pelas condições previstas no artigo 3.º» (alínea c) do n.º 3 do artigo 14.º do Decreto-Lei n.º 314/2003). Para os estabelecimentos, o mesmo diploma tem artigo e alínea sancionatória próprios (artigo 5.º e alínea f) do mesmo número). Os terrenos anexos alargam o n.º 1 ao quintal; não convertem o fogo do n.º 2 em prédio.'),
    ('p', '5. O desenho é do próprio legislador e está documentado. No Diário da República, I série-A, n.º 290, de 17 de dezembro de 2003, o Decreto-Lei n.º 315/2003 entregou o título de acesso dos alojamentos ao diretor-geral, o Decreto-Lei n.º 314/2003 criou os limites por fogo e entregou às câmaras a vistoria e a remoção, e a alínea p) do primeiro excluiu as frações autónomas da hospedagem sem fins lucrativos. No mesmo dia, a atividade subiu para a autoridade nacional e a densidade doméstica ficou no município.'),
    ('p', '6. A leitura contrária conduz ao absurdo. Se o n.º 2 fosse teto do prédio urbano, nenhum hotel para animais, centro de atendimento médico-veterinário, loja ou centro de recolha oficial instalado em prédio urbano poderia ter mais de seis animais. E o próprio n.º 5 manda remover animais «para o canil ou gatil municipal», que ficaria impedido de os receber.'),
    ('s', 'Ressalvas, que fazem parte da resposta'),
    ('p', '7. Registar não isenta do dever de salubridade. «O alojamento de cães e gatos em prédios urbanos, rústicos ou mistos, fica sempre condicionado à existência de boas condições do mesmo e ausência de riscos hígio-sanitários relativamente à conspurcação ambiental e doenças transmissíveis ao homem» (n.º 1 do artigo 3.º do Decreto-Lei n.º 314/2003). O próprio registo obriga a declarar o cumprimento da legislação aplicável (alínea j) do n.º 1 do artigo 3.º-A do Decreto-Lei n.º 276/2001).'),
    ('p', '8. Há um caso em que a resposta é afirmativa. O titular de alojamento registado que mantém os animais dentro de casa, como animais do agregado, está no fogo. Aplica-se-lhe o n.º 2, com o máximo de seis animais mediante parecer vinculativo do médico veterinário municipal e do delegado de saúde.'),
    ('s', 'A dimensão do alojamento não fica sem controlo'),
    ('p', '9. Controlam-na o anexo III; o n.º 1 do artigo 3.º do Decreto-Lei n.º 314/2003; o encerramento por despacho do diretor-geral de Alimentação e Veterinária, designadamente por «Maus tratos aos animais» ou por «graves problemas de saúde e bem-estar dos animais», com execução pelas câmaras (n.ºs 1 e 6 do artigo 3.º-G do Decreto-Lei n.º 276/2001); o uso do solo, tendo o Supremo Tribunal Administrativo declarado nulo o licenciamento de um canil para cem cães em zona de uso dominantemente residencial (acórdão de 7.3.2006, processo n.º 0794/05); e o ruído. A lotação de um canil de grande dimensão em zona habitacional controla-se por estas vias, e não pelo limite por fogo.'),
    ('s', 'Posição da Administração'),
    ('p', '10. A autoridade então competente concluiu no mesmo sentido. A Informação interna n.º I-013109/2022 do Gabinete de Apoio Jurídico e Contencioso do ICNF, I. P., de 16 de maio de 2022, conclui que «não há lugar para a aplicação do Decreto-Lei nº314/2003 em conjugação do Decreto-Lei nº 276/2001, relativamente à limitação do número de animais imposta pelo artigo 3º do Decreto-lei nº 314/2003». Os serviços do mesmo instituto sustentaram entendimento contrário, que não discute a unidade de contagem e cuja premissa sanitária é satisfeita pelo n.º 1, aplicável sempre.'),
]
txt = " ".join(t for _, t in T)
assert "\u2014" not in txt and "\u2013" not in txt, "travessão"
d = Document()
s = d.sections[0]
s.page_width, s.page_height = Cm(21), Cm(29.7)
s.left_margin = s.right_margin = Cm(2.5); s.top_margin = s.bottom_margin = Cm(2.2)
st = d.styles["Normal"]; st.font.name = "Aptos"; st.font.size = Pt(11); st.font.color.rgb = RGBColor(0, 0, 0)
rf = st.element.get_or_add_rPr().find(qn("w:rFonts"))
for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"): rf.set(qn(a), "Aptos")
pf = st.paragraph_format; pf.space_before = Pt(0); pf.space_after = Pt(6); pf.line_spacing = 1.0
for kind, t in T:
    p = d.add_paragraph(t)
    if kind == "p": p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if kind == "s": p.paragraph_format.space_before = Pt(6)
    if kind == "t": p.paragraph_format.space_after = Pt(10)
d.save(OUT)
tmp = OUT + ".tmp"
with zipfile.ZipFile(OUT) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
    for it in zi.infolist():
        data = zi.read(it.filename)
        if it.filename == "word/settings.xml":
            data = re.sub(r'<w:zoom(?![^>]*w:percent)([^>]*)/>', r'<w:zoom w:percent="100"\1/>', data.decode()).encode()
        zo.writestr(it, data)
shutil.move(tmp, OUT)
print(OUT, "palavras:", len(txt.split()))
