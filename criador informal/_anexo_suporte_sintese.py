import re, zipfile, shutil
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

DR314 = "Decreto-Lei n.º 314/2003, de 17 de dezembro, Diário da República, I série-A, n.º 290, de 17.12.2003"
DR276 = "Decreto-Lei n.º 276/2001, de 17 de outubro, Diário da República, I série-A, n.º 241, de 17.10.2001"
DR315 = "Decreto-Lei n.º 315/2003, de 17 de dezembro, Diário da República, I série-A, n.º 290, de 17.12.2003"
DR260 = "Decreto-Lei n.º 260/2012, de 12 de dezembro, Diário da República, 1.ª série, n.º 240, de 12.12.2012"

C = []  # (tipo, texto)
def t(x): C.append(("t", x))
def s(x): C.append(("s", x))
def r(x): C.append(("r", x))
def p(x): C.append(("p", x))
def q(x, fonte): C.append(("q", "«" + x + "»")); C.append(("f", fonte))

t("Anexo de suporte à síntese «Limites de detenção por fogo e lotação dos alojamentos registados»")
p("Este anexo acompanha a síntese em dez pontos. Para cada ponto, reproduz o texto legal em que assenta, explica-o com mais detalhe e indica o capítulo do estudo «Os limites de detenção por fogo e a lotação dos alojamentos registados» onde a matéria está desenvolvida. Não substitui o estudo.")
p("Os textos legais foram conferidos no Diário da República e citam-se com a página. Nas transcrições omite-se o número que antecede cada n.º, indicado na referência.")

# 1
s("Ponto 1. A unidade de contagem é o fogo, não o prédio")
r("Texto legal")
q("Nos prédios urbanos podem ser alojados até três cães ou quatro gatos adultos por cada fogo, não podendo no total ser excedido o número de quatro animais, excepto se, a pedido do detentor, e mediante parecer vinculativo do médico veterinário municipal e do delegado de saúde, for autorizado alojamento até ao máximo de seis animais adultos, desde que se verifiquem todos os requisitos hígio-sanitários e de bem-estar animal legalmente exigidos.",
  "N.º 2 do artigo 3.º do " + DR314 + ", p. 8445")
q("a) Área bruta (Ab) é a superfície total do fogo, medida pelo perímetro exterior das paredes exteriores e eixos das paredes separadoras dos fogos, e inclui varandas privativas, locais acessórios e a quota-parte que lhe corresponda nas circulações comuns do edifício; b) Área útil (Au) é a soma das áreas de todos os compartimentos da habitação, incluindo […]",
  "Alíneas a) e b) do n.º 2 do artigo 67.º do Regulamento Geral das Edificações Urbanas, aprovado pelo Decreto-Lei n.º 38 382, de 7 de agosto de 1951")
q("c) Programa de utilização das edificações, incluindo a área total de construção a afetar aos diversos usos e o número de fogos e outras unidades de utilização, com identificação das áreas acessórias, técnicas e de serviço;",
  "Alínea c) do n.º 2 do artigo 14.º do Regime Jurídico da Urbanização e Edificação, aprovado pelo Decreto-Lei n.º 555/99, de 16 de dezembro, na redação do Decreto-Lei n.º 108/2026, de 29 de maio")
r("Explicação")
p("O Decreto-Lei n.º 314/2003 não define «fogo», e a palavra aparece uma única vez em todo o diploma, no n.º 2 do artigo 3.º. O conceito colhe-se no direito do edificado. O Regulamento Geral das Edificações Urbanas usa «fogo» e «habitação» para o mesmo objeto: a alínea a) mede o fogo e a alínea b), logo a seguir, mede a habitação. O Regime Jurídico da Urbanização e Edificação distingue os «fogos» das «outras unidades de utilização». O fogo é, assim, a unidade de utilização destinada a habitação, e o que decide o uso de cada unidade é o respetivo título de utilização.")
p("Daqui resultam três consequências. O limite é de cada fogo e não do prédio: um prédio urbano com dez fogos comporta dez vezes o limite. Num prédio urbano sem fogo, a norma não tem unidade a que se aplicar. E o Decreto-Lei n.º 276/2001 nunca usa a palavra fogo: a sua unidade é o alojamento.")
r("No estudo: capítulo 5 e ponto 7.1.")

# 2
s("Ponto 2. Um alojamento registado não é um fogo")
r("Texto legal")
q("Os alojamentos no âmbito deste capítulo devem possuir instalações individualizadas destinadas à armazenagem de alimentos e equipamento limpo e à lavagem e recolha de material.",
  "N.º 1 do artigo 25.º do " + DR276 + ", p. 6577")
q("Os alojamentos para a reprodução/criação, para além do disposto no número anterior, devem possuir instalações individualizadas destinadas à maternidade e à criação até à idade adulta, a quarentena, a enfermaria, o manuseamento de alimentos e à higienização dos animais.",
  "N.º 2 do artigo 25.º do " + DR276 + ", p. 6577")
r("Explicação")
p("O artigo 25.º impõe ao alojamento um conjunto de instalações individualizadas que uma habitação não tem: armazenagem de alimentos e equipamento limpo, lavagem e recolha de material, maternidade, criação até à idade adulta, quarentena, enfermaria, manuseamento de alimentos e higienização dos animais. Cumprir esta norma é constituir um conjunto distinto da casa, ainda que no mesmo prédio.")
p("O critério prático não é, por isso, a área do prédio nem a sua classificação matricial, mas o lugar onde os animais estão. Os animais mantidos nas instalações do artigo 25.º estão no alojamento. Os animais mantidos dentro de casa, como animais do agregado, estão no fogo (ver ponto 8).")
r("No estudo: pontos 7.2 e 7.6 e capítulo 10.")

# 3
s("Ponto 3. A lotação do alojamento tem regime próprio e completo")
r("Texto legal")
q("h) A capacidade máxima de animais e respetivas espécies a alojar;",
  "Alínea h) do n.º 1 do artigo 3.º-A do Decreto-Lei n.º 276/2001, aditado pelo " + DR260 + ", p. 6972")
q("O alojamento de cães e gatos deve obedecer às dimensões mínimas indicadas no anexo III ao presente diploma, do qual faz parte integrante.",
  "N.º 1 do artigo 27.º do " + DR276 + ", p. 6577")
q("d.2) Em grupo: […] Recinto fechado exterior […] 10 […] 23 […] 28 […] 37",
  "Anexo III, alínea d.2), última linha da tabela, do " + DR276 + ", p. 6586")
r("Explicação")
p("A capacidade do alojamento é declarada pelo interessado na mera comunicação prévia. Essa declaração não é livre: está limitada pelas superfícies mínimas do anexo III, que o artigo 27.º torna obrigatórias. Para cães em grupo, a tabela da alínea d.2) fixa a superfície de base de cada recinto em função do número de animais e do peso vivo. Num recinto fechado exterior, por exemplo, dez cães exigem 23 m² até 16 kg, 28 m² entre 16 e 28 kg e 37 m² acima de 28 kg.")
p("O regime está completo: há declaração da capacidade, limite material por superfície e controlo pela autoridade competente. Não há lacuna que deva ser preenchida com uma norma de outro diploma e com outro objeto. A própria tabela do anexo III prevê grupos de até dez animais por recinto, o que seria incompatível com um teto de seis por prédio urbano.")
r("No estudo: pontos 7.3 e 7.9.")

# 4
s("Ponto 4. A norma sancionatória confirma o objeto doméstico do artigo 3.º")
r("Texto legal")
q("c) A permanência de cães e gatos em habitações e terrenos anexos em desrespeito pelas condições previstas no artigo 3.º;",
  "Alínea c) do n.º 3 do artigo 14.º do " + DR314 + ", p. 8448")
q("f) O comércio de cães e gatos em desrespeito das condições previstas no artigo 5.º;",
  "Alínea f) do n.º 3 do artigo 14.º do " + DR314 + ", p. 8448")
q("Os cães e gatos que se encontrem em estabelecimentos destinados ao seu comércio devem estar acompanhados do respectivo boletim sanitário de cães e gatos […]",
  "N.º 1 do artigo 5.º do " + DR314 + ", p. 8446")
r("Explicação")
p("Quando o legislador descreve o facto punível por violação do artigo 3.º, descreve-o como permanência «em habitações e terrenos anexos». Não usa «alojamento», «estabelecimento» nem «canil». E quando quer tratar estabelecimentos, fá-lo em artigo próprio, o 5.º, com alínea sancionatória própria, a f). O diploma sabe distinguir a habitação do estabelecimento, e não tem artigo sobre estabelecimentos de criação.")
p("A expressão «terrenos anexos» alarga o âmbito do artigo 3.º ao quintal, e é por isso que o dever de salubridade do n.º 1 alcança também o logradouro. Não altera a unidade de contagem do n.º 2, que continua a ser o fogo.")
p("A única doutrina localizada que trata o artigo 3.º na perspetiva da fiscalização arruma-o sob a epígrafe «Limite de cães e gatos por habitação» e descreve o tipo da alínea c) como «exceder o n.º de animais por fogo urbano» (Bruno Branco, «A detenção de animais de companhia: uma análise do ponto de vista contraordenacional», Revista Jurídica Luso-Brasileira, ano 5, 2019, n.º 2, pp. 229-260).")
r("No estudo: pontos 7.4, 7.5, 9.3 e 11.4.")

# 5
s("Ponto 5. O desenho é do próprio legislador e está documentado")
r("Texto legal")
q("Os alojamentos para hospedagem sem fins lucrativos, com fins comerciais, com excepção dos destinados exclusivamente à venda, e os centros de recolha carecem de licença de funcionamento a emitir pelo director-geral de Veterinária, sob parecer da DRA da área de localização e do médico veterinário municipal, no caso dos centros de recolha.",
  "N.º 1 do artigo 3.º do Decreto-Lei n.º 276/2001, na redação do " + DR315 + ", p. 8450")
q("p) «Hospedagem sem fins lucrativos», alojamento, permanente ou temporário, de animais de companhia que não vise a obtenção de rendimentos, com excepção das referidas no n.º 3 do artigo 3.º do diploma que aprova o Plano Nacional de Luta e Vigilância da Raiva Animal e outras Zoonoses;",
  "Alínea p) do n.º 1 do artigo 2.º do Decreto-Lei n.º 276/2001, na redação do " + DR315 + ", p. 8450")
q("Em caso de não cumprimento do disposto nos números anteriores, as câmaras municipais, após vistoria conjunta do delegado de saúde e do médico veterinário municipal, notificam o detentor para retirar os animais para o canil ou gatil municipal no prazo estabelecido por aquelas entidades, caso o detentor não opte por outro destino que reúna as condições estabelecidas pelo presente diploma.",
  "N.º 5 do artigo 3.º do " + DR314 + ", p. 8445")
r("Explicação")
p("Entre 2001 e 2003, o título de funcionamento dos alojamentos era uma licença municipal. No Diário da República n.º 290, de 17 de dezembro de 2003, o legislador fez três coisas ao mesmo tempo. O Decreto-Lei n.º 315/2003 entregou o título dos alojamentos ao diretor-geral de Veterinária. O Decreto-Lei n.º 314/2003 criou os limites por fogo e entregou às câmaras municipais a vistoria e a remoção. E a alínea p) abriu uma única passagem entre os dois regimes: excluiu da hospedagem sem fins lucrativos as frações autónomas em propriedade horizontal, referidas no n.º 3 do artigo 3.º do Decreto-Lei n.º 314/2003.")
p("No mesmo dia, a atividade subiu para a autoridade nacional e a densidade doméstica ficou no município. Desde o Decreto-Lei n.º 260/2012, o título passou a ser a mera comunicação prévia à DGAV, e o município deixou de intervir no acesso à atividade. Os dois regimes foram entregues a autoridades diferentes, com procedimentos que não se cruzam.")
r("No estudo: pontos 13.4 e 14.1 a 14.5.")

# 6
s("Ponto 6. A leitura contrária conduz ao absurdo")
r("Texto legal")
q("Os hotéis para animais, para além do disposto no n.º 1, devem possuir instalações individualizadas para enfermaria, manuseamento de alimentos e higienização dos animais.",
  "N.º 3 do artigo 25.º do " + DR276 + ", p. 6577, hoje n.º 4")
q("[…] notificam o detentor para retirar os animais para o canil ou gatil municipal […]",
  "N.º 5 do artigo 3.º do " + DR314 + ", p. 8445")
r("Explicação")
p("Se o n.º 2 fosse um teto aplicável a todo o prédio urbano, nenhum hotel para animais instalado num prédio urbano poderia ter mais de seis animais adultos. O mesmo valeria para os centros de atendimento médico-veterinário, para as lojas de venda e para os centros de recolha oficial, cujo alojamento em grupo o anexo III regula. E o próprio n.º 5 do artigo 3.º manda retirar os animais em excesso para o canil ou gatil municipal, que ficaria impedido de os receber.")
p("Ninguém sustenta estas consequências, e a razão é sempre a mesma: nenhum destes locais é um fogo. O teste confirma, por via independente, a leitura do ponto 1.")
r("No estudo: capítulo 8.")

# 7
s("Ponto 7. Registar não isenta do dever de salubridade")
r("Texto legal")
q("O alojamento de cães e gatos em prédios urbanos, rústicos ou mistos, fica sempre condicionado à existência de boas condições do mesmo e ausência de riscos hígio-sanitários relativamente à conspurcação ambiental e doenças transmissíveis ao homem.",
  "N.º 1 do artigo 3.º do " + DR314 + ", p. 8445")
q("j) Declaração de responsabilidade, subscrita pelo interessado, relativa ao cumprimento da legislação aplicável aos animais de companhia, nomeadamente em matéria de instalações, equipamentos, higiene, saúde e bem-estar dos animais.",
  "Alínea j) do n.º 1 do artigo 3.º-A do Decreto-Lei n.º 276/2001, aditado pelo " + DR260 + ", p. 6972")
q("Os detentores de animais de companhia que se dediquem à sua reprodução, criação, manutenção ou venda devem cumprir, sem prejuízo das demais disposições aplicáveis, as condições previstas no presente capítulo.",
  "Artigo 24.º do " + DR276 + ", p. 6577")
r("Explicação")
p("O n.º 1 do artigo 3.º aplica-se a todos os prédios, urbanos, rústicos ou mistos, e a quem quer que aloje cães e gatos, incluindo o titular de um alojamento registado. O registo não dispensa este dever. Pelo contrário, pressupõe o seu cumprimento: o interessado declara na comunicação prévia que cumpre toda a legislação aplicável em matéria de higiene e saúde, e o artigo 24.º manda cumprir o regime dos alojamentos «sem prejuízo das demais disposições aplicáveis».")
p("O n.º 1 tem aplicação prática a instalações que são de facto canis. O Tribunal da Relação de Lisboa deferiu a remoção de animais «alojados num canil clandestino, instalado no logradouro de um prédio urbano, de onde emana um cheiro nauseabundo, ladrando os 30 canídeos dia e noite», com fundamento no n.º 1 do artigo 3.º (acórdão de 28.6.2007, processo n.º 1692/2007-8).")
r("No estudo: pontos 7.8, 7.9, 9.2 e 11.2.")

# 8
s("Ponto 8. O caso em que a resposta é afirmativa")
r("Texto legal")
p("N.º 2 do artigo 3.º do Decreto-Lei n.º 314/2003, transcrito no ponto 1.")
r("Explicação")
p("O critério é o lugar onde os animais estão, e não o facto de existir registo. O titular de um alojamento registado que mantém os animais dentro de casa, integrados no agregado, tem-nos no fogo. Aplica-se-lhe o n.º 2: quatro animais adultos, ou até seis mediante parecer vinculativo do médico veterinário municipal e do delegado de saúde. Acima de seis, dentro do fogo, a lei não oferece caminho, e o registo não o cria.")
p("Os três casos possíveis são estes. Animais dentro de casa: aplica-se o n.º 2. Animais nas instalações do artigo 25.º, ainda que no quintal da mesma moradia: a lotação é a declarada, dentro dos limites do anexo III. Em qualquer dos dois casos: aplica-se sempre o n.º 1.")
r("No estudo: capítulos 10 e 16.")

# 9
s("Ponto 9. A dimensão do alojamento não fica sem controlo")
r("Texto legal")
q("O diretor-geral de Alimentação e Veterinária pode, mediante despacho, determinar a suspensão da atividade ou o encerramento do alojamento, designadamente quando se verifique uma das seguintes situações: a) Existência de riscos higiossanitários que ponham em causa a saúde das pessoas e ou dos animais; b) Maus tratos aos animais; c) Existência de graves problemas de saúde e bem-estar dos animais; […]",
  "N.º 1 do artigo 3.º-G do Decreto-Lei n.º 276/2001, aditado pelo " + DR260 + ", p. 6975")
q("Compete às câmaras municipais executar as medidas necessárias ao cumprimento da decisão a que se referem os n.os 3 e 4, nomeadamente proceder, quando necessário, à recolha dos animais.",
  "N.º 6 do mesmo artigo, p. 6976")
q("As instalações para alojamento de animais somente poderão ser consentidas nas áreas habitadas ou suas imediações quando construídas e exploradas em condições de não originarem, directa ou indirectamente, qualquer prejuízo para a salubridade e conforto das habitações.",
  "Artigo 115.º do Regulamento Geral das Edificações Urbanas")
q("Na área que o art.º 12.º n.º1 al. a) do PDM de Palmela […] classifica como “Espaço urbanizável de baixa densidade […]”, definida como área destinada “dominantemente ao uso residencial, incluindo os respectivos equipamentos colectivos, comércio e serviços de apoio”, a autorização de fazer uma edificação destinada a um canil com capacidade para cem cães viola o Plano, sendo nula nos termos do art.º 103.º do DL 380/99, de 22 de Set.",
  "Acórdão do Supremo Tribunal Administrativo de 7.3.2006, processo n.º 0794/05, sumário")
r("Explicação")
p("Afastar o n.º 2 não deixa o alojamento sem limite de dimensão. Há cinco vias de controlo. A primeira é o anexo III, que fixa a superfície por animal (ponto 3). A segunda é o n.º 1 do artigo 3.º, que vale sempre (ponto 7). A terceira é o poder do diretor-geral de Alimentação e Veterinária de suspender ou encerrar o alojamento, cuja execução, incluindo a recolha dos animais, cabe às câmaras municipais. A quarta é o ordenamento do território e o artigo 115.º do Regulamento Geral das Edificações Urbanas. A quinta é o ruído, sujeito ao Regulamento Geral do Ruído.")
p("O acórdão de Palmela mostra a quarta via em funcionamento: a capacidade de cem cães pesou na decisão, por fazer do canil «uma unidade de prestação de serviços de dimensão relevante e que tem efeitos necessários no ambiente circundante». No caso de Santo Tirso, o instrumento que o município mobilizou contra os abrigos foi também o regime da urbanização e edificação, com coimas por operações urbanísticas não licenciadas.")
r("No estudo: pontos 9.5, 11.6 e 15.7.")

# 10
s("Ponto 10. A posição da Administração")
r("Texto")
q("De todos exposto e salvo melhor entendimento, não há lugar para a aplicação do Decreto-Lei nº314/2003 em conjugação do Decreto-Lei nº 276/2001, relativamente à limitação do número de animais imposta pelo artigo 3º do Decreto-lei nº 314/2003.",
  "ICNF, I. P., Gabinete de Apoio Jurídico e Contencioso, Informação interna n.º I-013109/2022, de 16.5.2022, processo P-020019/2022, conclusão, p. 7")
q("O Anexo III ao Decreto-Lei nº 276/2001 estipula que, no caso de alojamento de cães em recintos fechados no exterior, o número de animais permitidos dentro de cada recinto, consoante a dimensão, pode chegar até dez animais. Pelo que, se fosse entendimento do legislador a limitação do número de animais por conjugação do artigo 3º do Decreto-Lei nº 314/2003, esta estipulação de alojamento não constaria do Decreto-lei nº 276/2001.",
  "Mesma informação, p. 6")
r("Explicação")
p("A informação foi emitida pelo gabinete jurídico do ICNF, I. P., quando este instituto era a autoridade competente para os alojamentos, a pedido do seu Departamento de Bem-Estar dos Animais de Companhia, no âmbito dos planos de controlo de alojamentos. Conclui no mesmo sentido da síntese, com base na capacidade declarada na comunicação prévia e no anexo III. Não usa o conceito de fogo. Não está publicada, e não se sabe se obteve despacho de concordância.")
p("Os serviços do mesmo instituto sustentaram o entendimento contrário, considerando os dois diplomas «complementares e não autónomas» e propondo rever o Decreto-Lei n.º 314/2003 «para diferenciar os tipos de prédios urbanos e a sua lotação máxima». Esse entendimento lê o limite como limite do prédio, sem discutir a unidade de contagem. A sua premissa sanitária fica satisfeita pelo n.º 1 do artigo 3.º, que se aplica sempre ao alojamento (ponto 7).")
r("No estudo: capítulo 12 e ponto 6.8.")

# Publicação
s("Lugar de publicação dos textos citados")
for x in [
    DR314 + ": artigo 3.º, p. 8445; artigo 5.º, p. 8446; artigo 14.º, p. 8448. O artigo 3.º nunca foi alterado.",
    DR276 + ": artigos 24.º, 25.º e 27.º, p. 6577; anexo III, pp. 6585 e 6586.",
    DR315 + ": nova redação do artigo 3.º e da alínea p) do n.º 1 do artigo 2.º do Decreto-Lei n.º 276/2001, p. 8450.",
    DR260 + ": artigo 3.º-A, p. 6972; artigo 3.º-G, pp. 6975 e 6976.",
    "Regulamento Geral das Edificações Urbanas, aprovado pelo Decreto-Lei n.º 38 382, de 7 de agosto de 1951, em vigor por força do artigo 25.º do Decreto-Lei n.º 10/2024, de 8 de janeiro, na redação do Decreto-Lei n.º 108/2026, de 29 de maio.",
    "Regime Jurídico da Urbanização e Edificação, aprovado pelo Decreto-Lei n.º 555/99, de 16 de dezembro, na redação do Decreto-Lei n.º 108/2026, de 29 de maio.",
    "Acórdãos: Supremo Tribunal Administrativo, 7.3.2006, processo n.º 0794/05; Tribunal da Relação de Lisboa, 28.6.2007, processo n.º 1692/2007-8.",
    "ICNF, I. P., Informação interna n.º I-013109/2022, de 16.5.2022, e documento interno dos serviços «Dúvidas alojamento animais», cópias na pasta «criador informal» do repositório.",
]:
    C.append(("l", x))

# ---------------- verificação de travessões
txt = " ".join(x for _, x in C)
assert "—" not in txt and "–" not in txt, "travessão"

d = Document()
sec = d.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
sec.left_margin = sec.right_margin = Cm(2.5); sec.top_margin = sec.bottom_margin = Cm(2.2)
st = d.styles["Normal"]; st.font.name = "Aptos"; st.font.size = Pt(11); st.font.color.rgb = RGBColor(0, 0, 0)
rf = st.element.get_or_add_rPr().find(qn("w:rFonts"))
for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"): rf.set(qn(a), "Aptos")
pf = st.paragraph_format; pf.space_before = Pt(0); pf.space_after = Pt(6); pf.line_spacing = 1.0
for kind, x in C:
    par = d.add_paragraph(x)
    f = par.paragraph_format
    if kind in ("p", "q", "l"): par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if kind == "t": f.space_after = Pt(12)
    if kind == "s": f.space_before = Pt(12); f.keep_with_next = True
    if kind == "r": f.space_before = Pt(4); f.space_after = Pt(3); f.keep_with_next = True
    if kind == "q": f.left_indent = Cm(1); f.space_after = Pt(1)
    if kind == "f": f.left_indent = Cm(1); f.space_after = Pt(6)
    if kind == "l": f.left_indent = Cm(0.5)
out = "Anexo_Suporte_Sintese_Limites_por_Fogo_2026-10-09.docx"
d.save(out)
tmp = out + ".tmp"
with zipfile.ZipFile(out) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
    for it in zi.infolist():
        data = zi.read(it.filename)
        if it.filename == "word/settings.xml":
            data = re.sub(r'<w:zoom(?![^>]*w:percent)([^>]*)/>', r'<w:zoom w:percent="100"\1/>', data.decode()).encode()
        zo.writestr(it, data)
shutil.move(tmp, out)
print(out, "palavras:", len(txt.split()))
