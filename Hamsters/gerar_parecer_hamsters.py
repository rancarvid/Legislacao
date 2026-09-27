# -*- coding: utf-8 -*-
"""Gera o parecer técnico-jurídico sobre a criação comercial de hamsters sírios (pedido de 10.9.2026)."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

AZUL = RGBColor(0x1F, 0x3A, 0x5F)
CINZA = RGBColor(0x55, 0x55, 0x55)

doc = Document()
for s in doc.sections:
    s.left_margin = s.right_margin = Cm(2.2)
    s.top_margin = s.bottom_margin = Cm(2)
st = doc.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(10.5)


def sombra(cell, cor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), cor)
    tcPr.append(shd)


def h(txt, n=1):
    p = doc.add_heading(txt, level=n)
    for r in p.runs:
        r.font.color.rgb = AZUL
    return p


def par(txt, bold=False, italic=False, cor=None, size=None, align=None):
    p = doc.add_paragraph()
    r = p.add_run(txt)
    r.bold, r.italic = bold, italic
    if cor:
        r.font.color.rgb = cor
    if size:
        r.font.size = Pt(size)
    if align:
        p.alignment = align
    return p


def bullet(txt, bold_prefix=None):
    p = doc.add_paragraph(style="List Bullet")
    if bold_prefix:
        p.add_run(bold_prefix).bold = True
    p.add_run(txt)
    return p


def citacao(ref, linhas, lingua=None):
    """Citação verbatim em caixa (tabela 1x1 sombreada)."""
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    c = t.rows[0].cells[0]
    sombra(c, "EEF3F8")
    p = c.paragraphs[0]
    r = p.add_run(ref + (f"  [{lingua}]" if lingua else ""))
    r.bold = True
    r.font.size = Pt(9)
    r.font.color.rgb = AZUL
    for l in linhas:
        q = c.add_paragraph()
        rr = q.add_run(l)
        rr.italic = True
        rr.font.size = Pt(9.5)
    doc.add_paragraph()


def tabela(cab, linhas, larguras=None, cor_cab="1F3A5F"):
    t = doc.add_table(rows=1, cols=len(cab))
    t.style = "Table Grid"
    for i, c in enumerate(cab):
        cell = t.rows[0].cells[i]
        sombra(cell, cor_cab)
        r = cell.paragraphs[0].add_run(c)
        r.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    for lin in linhas:
        cells = t.add_row().cells
        for i, v in enumerate(lin):
            r = cells[i].paragraphs[0].add_run(v)
            r.font.size = Pt(9)
    if larguras:
        for row in t.rows:
            for i, w in enumerate(larguras):
                row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return t


# ---------------------------------------------------------------- capa
par("DIREÇÃO DE SERVIÇOS DE BEM-ESTAR ANIMAL", bold=True, cor=AZUL, size=9)
par("Divisão de Bem-Estar dos Animais para Fins Experimentais, Companhia e Zoológicos", cor=CINZA, size=9)
doc.add_paragraph()
par("INFORMAÇÃO / PROPOSTA DE RESPOSTA", bold=True, size=16, cor=AZUL)
par("Criação e venda de hamsters sírios (Mesocricetus auratus) em pequena escala — "
    "enquadramento legal, divergência entre as informações prestadas pelo ICNF e pela DGAV "
    "e proposta de atuação", bold=True, size=12)
par("Pedido: e-mail de Ana Filipa Santos (Porto), de 10.9.2026 — reencaminhado pela DSPA/DESA em 16.9.2026 "
    "e distribuído pela Chefe de Divisão em 16.9.2026 para análise e preparação de resposta.", cor=CINZA, size=9)
par("Data da informação: 27.9.2026", cor=CINZA, size=9)

# ---------------------------------------------------------------- 1
h("1. Síntese")
tabela(
    ["Questão", "Resposta curta", "Base legal"],
    [
        ["O hamster sírio é animal de companhia?",
         "Sim. Está abrangido pelo DL 276/2001, que tem até normas próprias para pequenos roedores.",
         "Al. a) do n.º 1 do art.º 2.º e art.º 26.º do DL 276/2001; anexo I, parte B, do Reg. (UE) 2016/429"],
        ["É obrigatório o microchip e o registo no SIAC?",
         "Não. A obrigação abrange só cães, gatos e furões; para os roedores a identificação é facultativa.",
         "Art.º 2.º e n.º 1 do art.º 4.º do DL 82/2019"],
        ["É necessária licença do ICNF (espécies exóticas)?",
         "O ICNF informou a requerente de que não é. A matéria é da competência do ICNF. Ver ponto 4.2: convém obter confirmação escrita do ICNF.",
         "Art.º 5.º do DL 92/2019"],
        ["A atividade pretendida carece de algum procedimento?",
         "Sim. Ter fêmeas reprodutoras cujas crias se destinam a venda, ainda que por valor simbólico, é «criação comercial». "
         "Por isso, exige mera comunicação prévia à DGAV antes do início da atividade.",
         "Als. y) e aa) do n.º 1 do art.º 2.º; al. a) do n.º 1 do art.º 3.º; art.º 3.º-A do DL 276/2001"],
        ["Que obrigações se aplicam à venda?",
         "Anúncio com os elementos legais, documentos na entrega, venda só no local de criação e declaração médico-veterinária.",
         "Art.os 53.º, 53.º-A, 54.º e 57.º do DL 276/2001"],
        ["O Regulamento (UE) 2026/1818 aplica-se?",
         "Não. Aplica-se só a cães e gatos.",
         "Art.os 1.º e 2.º do Regulamento (UE) 2026/1818"],
    ],
    [4.2, 7.3, 5.5],
)
par("Conclusão: a informação prestada pela DSPA («a legislação nacional não estabelece a obrigatoriedade de "
    "identificação eletrónica de Hamsters») está correta, mas é incompleta. Não refere que a atividade pretendida "
    "depende de mera comunicação prévia à DGAV, nem quais as regras de venda. A indicação do ICNF sobre a "
    "obrigatoriedade de registo no SIAC e de microchip não tem base legal. É provável que resulte de uma leitura "
    "literal da al. c) do n.º 1 do art.º 53.º do DL 276/2001 (ver ponto 4.3).", bold=True)

# ---------------------------------------------------------------- 2
h("2. Factos")
bullet("A requerente pretende criar hamsters sírios em casa, com 1 a 2 casais, 2 a 3 ninhadas por fêmea "
       "ao longo da vida e alojamento individual em terrários de 100×50×60 cm. As crias seriam vendidas "
       "«por valores relativamente simbólicos», para reinvestir nos cuidados dos animais.")
bullet("O ICNF informou a requerente de que a detenção, criação e comercialização de hamster sírio não carece "
       "de licença de espécies exóticas ao abrigo do DL 92/2019. Informou também que a requerente «deve assegurar "
       "que os animais estão registados no SIAC e têm microchip».")
bullet("A DSPA/DESA da DGAV informou que «a legislação nacional não estabelece a obrigatoriedade de "
       "identificação eletrónica de Hamsters».")
bullet("A requerente manifesta preocupação com a dor que a aplicação de um microchip pode causar num animal "
       "tão pequeno.")

# ---------------------------------------------------------------- 3
h("3. Enquadramento legal (legislação vigente)")
par("Fontes: o DL 276/2001 foi confrontado com a versão consolidada em linha (PGDL). A última alteração é o DL "
    "n.º 9/2021, de 29 de janeiro, e o texto coincide com o ficheiro «10a DL 276_2001 – versão atualizada e "
    "consolidada» do repositório. O DL 82/2019 foi lido na redação dada pela Lei n.º 2/2020. O DL 92/2019 foi "
    "lido na redação dada pela Lei n.º 25/2023. O Regulamento (UE) 2026/1818 foi lido no texto publicado no JO "
    "(EN e PT).", italic=True, cor=CINZA, size=9)

h("3.1 Qualificação do hamster sírio como animal de companhia", 2)
citacao("al. a), do n.º 1, do art.º 2.º do Decreto-Lei n.º 276/2001", [
    "a) «Animal de companhia» qualquer animal detido ou destinado a ser detido pelo homem, designadamente no seu lar, "
    "para seu entretenimento e companhia;"])
citacao("n.º 1, do art.º 26.º do Decreto-Lei n.º 276/2001 — Condições particulares para a manutenção de pequenos roedores e coelhos", [
    "1 - As caixas onde os animais são colocados devem estar providas com material de cama em quantidade suficiente, "
    "adaptada às espécies em causa, o qual deve ser renovado regularmente.",
    "2 - As medidas das caixas para pequenos roedores e coelhos devem obedecer aos parâmetros mínimos adequados à "
    "espécie, nomeadamente os constantes do anexo ii do presente diploma, do qual faz parte integrante.",
    "3 - Ao planear a criação e ou manutenção deverá ter-se em conta o crescimento potencial dos animais, a fim de "
    "lhes assegurar um espaço apropriado, em conformidade com as medidas das caixas previstas no anexo ii, durante "
    "todas as suas fases de desenvolvimento."])
citacao("Anexo I, parte B, do Regulamento (UE) 2016/429 (Lei da Saúde Animal)", [
    "Mammals: rodents and rabbits other than those intended for food production"], "EN")
par("Tradução: «Mamíferos: roedores e coelhos, com exceção dos destinados à produção de alimentos». "
    "Nota: não foi possível obter o texto PT oficial no EUR-Lex (acesso bloqueado nesta sessão). Deve ser confirmado "
    "antes de citar em documento externo.", italic=True, size=9, cor=CINZA)

h("3.2 Identificação eletrónica e registo no SIAC", 2)
citacao("art.º 2.º do Decreto-Lei n.º 82/2019 — Âmbito de aplicação", [
    "O presente decreto-lei aplica-se à identificação de animais de companhia das espécies referidas no anexo I do "
    "Regulamento (UE) n.º 576/2013, do Parlamento Europeu e do Conselho, de 12 de junho de 2013, e no anexo I do "
    "Regulamento (UE) n.º 2016/429, do Parlamento Europeu e do Conselho, de 9 de março de 2016, nascidos ou presentes "
    "no território nacional."])
citacao("n.os 1 e 2, do art.º 4.º do Decreto-Lei n.º 82/2019 — Obrigação de identificação", [
    "1 - A identificação de animais de companhia é obrigatória para cães, gatos e furões, nos termos da parte A do "
    "anexo I do Regulamento (UE) n.º 576/2013, do Parlamento Europeu e do Conselho, de 12 de junho de 2013, e a parte A "
    "do anexo I do Regulamento (UE) n.º 2016/429, do Parlamento Europeu e do Conselho, de 9 de março de 2016, sendo "
    "facultativa para as espécies abrangidas na parte B do anexo I dos referidos Regulamentos.",
    "2 - Por despacho do diretor-geral de Alimentação e Veterinária, pode ser determinada a obrigatoriedade de "
    "identificação, nos termos do presente decreto-lei, de qualquer das espécies referidas na parte B do anexo I dos "
    "Regulamentos mencionados no número anterior ou de outras espécies de animais detidos para fins de companhia, com "
    "fundamento na necessidade de implementar medidas de natureza sanitária para combate a surtos de doenças "
    "epizoóticas ou zoonoses."])
citacao("n.º 3, do art.º 5.º do Decreto-Lei n.º 82/2019", [
    "3 - Sem prejuízo dos números anteriores, e relativamente aos cães, gatos e furões que sejam cedidos e ou "
    "comercializados a partir de um criador ou de um estabelecimento autorizado para a detenção de animais de "
    "companhia, nomeadamente os centros de hospedagem com ou sem fins lucrativos e os centros de recolha oficiais, "
    "deve ser assegurada a sua marcação e registo no SIAC antes de abandonarem a instalação de nascimento ou de "
    "alojamento, independentemente da sua idade."])
par("Os hamsters são roedores da parte B do anexo I do Regulamento (UE) 2016/429. Por isso, a sua identificação é "
    "facultativa. A obrigação de marcar as crias antes de saírem do criador (n.º 3 do art.º 5.º) também se limita a "
    "cães, gatos e furões. Só por despacho do Diretor-Geral, e com fundamento sanitário, poderia ser imposta a "
    "identificação de outras espécies (n.º 2 do art.º 4.º). Não se conhece despacho desse tipo para roedores, o que "
    "deve ser confirmado internamente pela DSPA.")

h("3.3 Procedimento para o exercício da atividade", 2)
citacao("als. y), z) e aa), do n.º 1, do art.º 2.º do Decreto-Lei n.º 276/2001", [
    "y) 'Venda de animal de companhia', a transmissão a título oneroso de um animal de companhia;",
    "z) 'Vendedor de animal de companhia', qualquer pessoa que, sendo ou não proprietário ou mero detentor eventual "
    "de fêmea reprodutora, exerce a atividade de venda de animais de companhia;",
    "aa) 'Criação comercial de animais de companhia', a atividade que consiste em possuir uma ou mais fêmeas "
    "reprodutoras cujas crias sejam destinadas ao comércio;"])
citacao("al. a), do n.º 1, e n.os 11 e 13, do art.º 3.º do Decreto-Lei n.º 276/2001", [
    "1 - Sem prejuízo do disposto no Decreto-Lei n.º 10/2015, de 16 de janeiro, quanto aos estabelecimentos de "
    "comércio a retalho de animais de companhia, o exercício da atividade de exploração de alojamentos, bem como a "
    "atividade de criação comercial de animais de companhia depende de:",
    "a) Mera comunicação prévia, no caso dos centros de recolha, alojamentos para hospedagem, com ou sem fins "
    "lucrativos, criação comercial de animais de companhia, em qualquer caso com exceção dos destinados "
    "exclusivamente à venda, sem prejuízo do disposto na alínea seguinte;",
    "[…]",
    "11 - A comunicação prévia ou a permissão administrativa dão lugar a um número de identificação, o qual é pessoal "
    "e intransmissível.",
    "13 - O disposto nos números anteriores não prejudica as obrigações devidas junto da Autoridade Tributária e "
    "Aduaneira."])
par("A lei não fixa limiar mínimo: basta uma fêmea reprodutora cujas crias se destinem ao comércio. Também não "
    "distingue valores simbólicos, porque a venda é qualquer «transmissão a título oneroso». O projeto da requerente "
    "é, por isso, criação comercial e depende de mera comunicação prévia à DGAV. A comunicação é feita por via "
    "eletrónica, através do balcão único (ePortugal), com os elementos do n.º 1 do art.º 3.º-A. Entre eles estão o "
    "médico veterinário responsável (al. f)), a capacidade máxima e as espécies (al. h)) e a declaração de "
    "responsabilidade (al. j)). A falta de comunicação prévia é contraordenação económica grave (al. a) do n.º 1 do "
    "art.º 68.º).")
par("Da mera comunicação prévia decorrem, entre outras, as seguintes obrigações:")
bullet("ter um médico veterinário responsável pelo alojamento (art.º 4.º);", "Art.º 4.º — ")
bullet("manter registos durante 1 ano: identificação dos animais, número por espécie e movimento mensal de "
       "nascimentos, mortes, saídas e destino (art.º 5.º);", "Art.º 5.º — ")
bullet("cumprir as normas gerais de bem-estar, alojamento, ambiente, alimentação, maneio, higiene e saúde "
       "(art.os 6.º a 18.º), incluindo um programa de profilaxia supervisionado pelo médico veterinário "
       "(art.º 16.º);", "Art.os 6.º a 18.º — ")
bullet("dispor das instalações individualizadas do art.º 25.º: armazenagem, lavagem, maternidade, criação, "
       "quarentena, enfermaria, manuseamento de alimentos e higienização. Numa criação doméstica de roedores, esta "
       "exigência é desproporcionada (ver Observações);", "Art.º 25.º — ")
bullet("cumprir o art.º 26.º e o anexo II (caixas para pequenos roedores, incluindo roedores em reprodução).",
       "Art.º 26.º — ")

h("3.4 Regras de anúncio, venda e transmissão", 2)
citacao("n.º 1, do art.º 53.º do Decreto-Lei n.º 276/2001", [
    "1 - Qualquer anúncio de transmissão, a título oneroso, de animais de companhia deve conter as seguintes informações:",
    "a) A idade dos animais;",
    "b) Tratando-se de cão ou gato, a indicação se é animal de raça pura ou indeterminada, sendo que, tratando-se de "
    "animal de raça pura, deve obrigatoriamente ser referido o número de registo no livro de origens português;",
    "c) Número de identificação eletrónica da cria e da fêmea reprodutora;",
    "d) Número de inscrição de criador nos termos do artigo 3.º do presente diploma;",
    "e) Número de animais da ninhada."])
citacao("art.º 54.º do Decreto-Lei n.º 276/2001", [
    "Qualquer transmissão de propriedade, gratuita ou onerosa, de animal de companhia deve ser acompanhada, no "
    "momento da transmissão, dos seguintes documentos entregues ao adquirente:",
    "a) Declaração de cedência ou contrato de compra e venda do animal e respetiva fatura, ou documento comprovativo "
    "da doação;",
    "b) Comprovativo de identificação eletrónica do animal, desde que se trate de cão ou gato;",
    "c) Declaração médico-veterinária, com prazo de pelo menos 15 dias, que ateste que o animal se encontra de boa "
    "saúde e apto a ser vendido;",
    "d) Informação de vacinas e historial clínico do animal."])
citacao("n.º 1, do art.º 57.º do Decreto-Lei n.º 276/2001", [
    "1 - Os animais de companhia podem ser publicitados na Internet mas a compra e venda dos mesmos apenas é admitida "
    "no local de criação ou em estabelecimentos devidamente licenciados para o efeito, sendo expressamente proibida a "
    "venda de animais por entidade transportadora."])

h("3.5 Regulamento (UE) 2026/1818 — inaplicabilidade", 2)
citacao("art.º 2.º, n.º 1, do Regulamento (UE) 2026/1818", [
    "1. This Regulation applies to the breeding, keeping, tracing, placing on the market and entry into the Union of "
    "dogs and cats."], "EN — JO")
citacao("art.º 2.º, n.º 1, do Regulamento (UE) 2026/1818", [
    "1. O presente regulamento é aplicável à criação, à detenção, à rastreabilidade, à colocação no mercado e à "
    "entrada na União de cães e gatos."], "PT — JO")
par("O Regulamento aplica-se só a cães e gatos. Não abrange hamsters, nem sequer a título supletivo.")

# ---------------------------------------------------------------- 4
h("4. Análise da divergência ICNF / DGAV")
tabela(
    ["Matéria", "Posição do ICNF (segundo a requerente)", "Posição da DGAV (DSPA)", "Apreciação"],
    [
        ["Licença de espécies exóticas (DL 92/2019)",
         "Não carece de licença.",
         "Não se pronunciou.",
         "É matéria da competência exclusiva do ICNF (art.º 4.º do DL 92/2019). A DGAV não deve contrariar esta "
         "posição, que favorece a requerente. Convém, contudo, obter confirmação escrita (ver 4.2)."],
        ["Registo no SIAC",
         "Obrigatório.",
         "Não obrigatório (implícito).",
         "Sem base legal. O SIAC e a identificação são competência da DGAV (DL 82/2019), e a identificação dos "
         "roedores é facultativa (n.º 1 do art.º 4.º)."],
        ["Microchip",
         "Obrigatório.",
         "«A legislação nacional não estabelece a obrigatoriedade de identificação eletrónica de Hamsters».",
         "A DGAV tem razão. A única norma que poderia sugerir o contrário é a al. c) do n.º 1 do art.º 53.º do "
         "DL 276/2001, que respeita ao conteúdo dos anúncios e não impõe marcação (ver 4.3)."],
        ["Mera comunicação prévia (criador)",
         "Não referida.",
         "Não referida.",
         "Ambas as respostas são omissas. É o ponto juridicamente mais relevante para a requerente."],
    ],
    [3.2, 3.6, 3.6, 6.6],
)

h("4.1 Origem provável da posição do ICNF", 2)
par("O Manual de Normas e Procedimentos da Divisão de Aplicação de Normativos do ICNF (rev. 01.2023), no "
    "ponto 3.3.23, aplica aos animais do seu âmbito os requisitos do art.º 53.º do DL 276/2001 «com as devidas "
    "adaptações». Entre esses requisitos inclui a «Marcação do espécime e respetivos progenitores». O ICNF terá "
    "estendido esta lógica aos animais de companhia em geral e tê-la associado ao SIAC. O SIAC, porém, é um sistema "
    "da DGAV e só é obrigatório para cães, gatos e furões.")

h("4.2 Licença ICNF — fragilidade da fundamentação", 2)
citacao("n.os 1 e 2, do art.º 5.º do Decreto-Lei n.º 92/2019", [
    "1 - É sujeita a licença a detenção, cultivo ou criação, por pessoas singulares ou coletivas, de espécimes de "
    "espécies exóticas para fins comerciais, científicos ou pedagógicos, nomeadamente em:",
    "[…]",
    "c) Aquários, lojas e outros locais de venda de animais;",
    "d) Instalações para criação de animais.",
    "2 - São isentas da licença referida no número anterior as situações de:",
    "a) Detenção, cultivo ou criação de espécimes de espécies exóticas identificadas nos termos do n.º 4 do artigo "
    "1.º, quando circunscritos a um determinado território, ou parte dele, onde a introdução dessa espécie está "
    "confirmada;",
    "[…]"])
par("A definição de «espécie exótica» da al. i) do art.º 2.º do DL 92/2019 abrange, em sentido literal, o hamster "
    "sírio, que não é autóctone. O Mesocricetus auratus não consta da lista do ICNF prevista no n.º 4 do art.º 1.º "
    "(«Espécies exóticas ocorrentes em Portugal Continental…»), que é quase só de flora. A dispensa de licença "
    "comunicada pelo ICNF assenta, assim, numa interpretação administrativa: a exclusão das espécies domesticadas "
    "tradicionalmente detidas como animais de companhia. Não assenta numa isenção expressa. Esta interpretação é "
    "razoável, mas convém que a requerente disponha da posição do ICNF por escrito.")

h("4.3 Interpretação da al. c) do n.º 1 do art.º 53.º do DL 276/2001", 2)
par("Em leitura literal, a al. c) aplicar-se-ia a «qualquer anúncio de transmissão, a título oneroso, de animais de "
    "companhia». A leitura sistemática afasta esse resultado (art.º 9.º do Código Civil), por três razões:")
bullet("a al. b) do mesmo número restringe-se expressamente a cão ou gato, o que mostra que o legislador tinha "
       "em mente sobretudo estas espécies;")
bullet("a al. b) do art.º 54.º, aprovada na mesma revisão (Lei n.º 95/2017), limita o comprovativo de "
       "identificação eletrónica a cão ou gato;")
bullet("o DL 82/2019, posterior e especial em matéria de identificação, torna-a facultativa para roedores. Não é "
       "coerente que uma norma sobre o conteúdo de anúncios obrigue a marcar animais que a lei da identificação "
       "dispensa.")
par("Conclusão: a al. c) do n.º 1 do art.º 53.º deve ler-se «quando aplicável», isto é, só para as espécies "
    "sujeitas a identificação obrigatória. Há, no entanto, um risco residual. Um anúncio sem esse elemento pode ser "
    "visto como contraordenação económica grave (al. e) do n.º 1 do art.º 68.º), e as plataformas podem recusá-lo "
    "(art.º 53.º-A). Justifica-se, por isso, um esclarecimento interpretativo da DGAV.")

h("4.4 Outra dúvida: o hamster sírio seria «animal selvagem»?", 2)
par("A al. dd) do n.º 1 do art.º 2.º do DL 276/2001 define «animal selvagem» de forma ampla («todo o animal cuja "
    "espécie existe na natureza…»). Nessa leitura, o hamster sírio poderia ficar abrangido pela proibição de anúncio "
    "e venda na Internet do art.º 55.º. Esta leitura é de afastar, por quatro razões: o próprio DL 276/2001 regula "
    "a criação de pequenos roedores como animais de companhia (art.º 26.º e anexo II); a espécie consta da parte B "
    "do anexo I do Reg. (UE) 2016/429; o ICNF, que é a autoridade para a fauna selvagem, não a trata como tal; e o "
    "@rgac inclui expressamente essas espécies (n.º 2 do art.º 2.º).")

# ---------------------------------------------------------------- 5
h("5. Diploma final @rgac (trabalho em curso — não é legislação vigente)")
par("Versão analisada: diploma final @rgac (versão: RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO — Revisto 30-06-2026 "
    "18h00 Grupo). A leitura foi confirmada contra a versão RGAC_Rev. DAJA _V1_06_2026, que tem o mesmo "
    "conteúdo nesta matéria.", italic=True, cor=CINZA, size=9)
citacao("n.º 2, do art.º 2.º do diploma final @rgac", [
    "2 - Para efeitos do presente decreto-lei, são animais de companhia os animais das espécies constantes da Parte A "
    "do Anexo I do Regulamento (UE) 2016/429 do Parlamento Europeu e do Conselho, de 9 de março de 2016, e, quando "
    "detidos para fins de companhia, os das espécies constantes da Parte B do mesmo anexo."])
bullet("O hamster fica incluído de forma expressa (n.º 2 do art.º 2.º). A identificação obrigatória com registo no "
       "SIAC mantém-se só para cães, gatos e furões (n.º 1 do art.º 65.º).")
bullet("A dúvida da al. c) do n.º 1 do art.º 53.º do DL 276/2001 fica resolvida. No anúncio de «outros animais de "
       "companhia», o número de identificação só é exigido «quando aplicável» (n.º 4 do art.º 106.º). Na "
       "transmissão, estes animais devem ser acompanhados de «documento que ateste a origem, emitido pelo criador» "
       "(n.º 7 do art.º 105.º).")
bullet("Lacuna a corrigir: o anúncio de outras espécies exige o «N.º de registo do estabelecimento de criação» "
       "(n.º 4 do art.º 106.º). Porém, «Estabelecimento de criação» (art.º 3.º) está definido só para a instalação "
       "onde são mantidos «cães ou gatos». Assim, não fica claro se os criadores de roedores estão sujeitos a mera "
       "comunicação prévia (al. a) do n.º 1 do art.º 42.º). Sugere-se alargar a definição, ou prever expressamente "
       "os estabelecimentos de criação de outras espécies.")
bullet("O n.º 9 do art.º 2.º repete a exclusão das espécies da «fauna selvagem autóctone e exótica». Convém "
       "esclarecer que as espécies da parte B do anexo I do Reg. (UE) 2016/429 detidas para fins de companhia, como "
       "os roedores domesticados, não ficam abrangidas por essa exclusão.")
bullet("Os parâmetros das caixas para pequenos roedores passam para portaria (n.º 2 do art.º 35.º). Esta é a sede "
       "adequada para uma solução proporcional à pequena escala.")

# ---------------------------------------------------------------- 6
h("6. Proposta de atuação")
tabela(
    ["#", "Ação", "Responsável", "Prioridade"],
    [
        ["1", "Responder à requerente com a minuta do ponto 7: sem microchip nem SIAC obrigatórios, com mera "
              "comunicação prévia e regras de venda.", "DSBEA/DBEAFECZ", "Imediata"],
        ["2", "Ofício ou e-mail ao ICNF (DAN) para harmonizar a informação prestada ao público: a identificação e o "
              "registo no SIAC dos roedores são facultativos (DL 82/2019, competência DGAV); pedir confirmação "
              "escrita do fundamento da dispensa de licença (DL 92/2019) para roedores domesticados; sugerir revisão "
              "do ponto 3.3.23 do Manual do ICNF.", "DSBEA, em articulação com a DSPA", "Alta"],
        ["3", "Confirmar com a DSPA que não existe despacho ao abrigo do n.º 2 do art.º 4.º do DL 82/2019 para "
              "roedores.", "DSPA", "Alta"],
        ["4", "Publicar uma FAQ ou orientação da DGAV sobre a criação de pequenos mamíferos não sujeitos a "
              "identificação: mera comunicação prévia; al. c) do n.º 1 do art.º 53.º «quando aplicável»; documentos "
              "de transmissão.", "DSBEA", "Média"],
        ["5", "@rgac: alargar a definição de «estabelecimento de criação» (art.º 3.º) a outras espécies ou prever norma própria; clarificar o n.º 9 do art.º 2.º; "
              "prever um regime proporcional para a pequena escala (equivalência funcional das instalações do "
              "art.º 25.º), como no memorando sobre criação em pequena escala de 14.9.2026.", "Grupo RGAC / DAJA", "Média"],
    ],
    [0.7, 10.3, 3.8, 2.2],
)

h("Observações", 2)
par("As deduções, inferências e opiniões desta informação concentram-se aqui.", italic=True, size=9, cor=CINZA)
bullet("Bem-estar: a preocupação da requerente com o microchip é legítima. Existem transponders miniatura, mas "
       "num animal de cerca de 100–150 g a implantação implica contenção e dor aguda, com riscos de migração e de "
       "reação local. Como a lei não impõe a marcação, não se recomenda a identificação eletrónica voluntária para "
       "fins comerciais. Se for feita, tem de ser aplicada por médico veterinário (al. c) do art.º 3.º do "
       "DL 82/2019) e implica cumprir o DL 82/2019 a partir desse momento.")
bullet("Proporcionalidade: exigir a uma criação doméstica de 1 a 2 casais de hamsters as instalações "
       "individualizadas do art.º 25.º do DL 276/2001 (maternidade, quarentena, enfermaria, etc.) é "
       "desproporcionado. Na fiscalização deve admitir-se a equivalência funcional, como preconizado para a "
       "pequena escala em cães e gatos.")
bullet("Capacidade: cada ninhada de hamster sírio pode ter muitas crias. A capacidade máxima declarada (al. h) do "
       "n.º 1 do art.º 3.º-A) e o espaço (n.º 3 do art.º 26.º) devem prever a separação das crias por sexo e o "
       "alojamento individual dos adultos, próprio desta espécie solitária, até à venda.")
bullet("Adquirentes: recomenda-se entregar ao adquirente informação escrita sobre as necessidades da espécie. "
       "O @rgac vai nesse sentido.")

# ---------------------------------------------------------------- 7
h("7. Minuta de resposta à requerente")
t = doc.add_table(rows=1, cols=1)
t.style = "Table Grid"
c = t.rows[0].cells[0]
sombra(c, "F7F7F7")
minuta = [
    "Assunto: Criação de Hamsters Sírios — esclarecimento",
    "",
    "Exma. Senhora,",
    "",
    "Em resposta ao seu pedido de esclarecimento sobre a criação e venda de hamsters sírios (Mesocricetus auratus), "
    "informamos o seguinte:",
    "",
    "1. Identificação eletrónica e registo no SIAC — Nos termos do n.º 1 do artigo 4.º do Decreto-Lei n.º 82/2019, "
    "de 27 de junho, a identificação eletrónica (transponder/microchip) e o registo no Sistema de Informação de "
    "Animais de Companhia (SIAC) são obrigatórios apenas para cães, gatos e furões, sendo facultativos para os "
    "roedores. Os hamsters não estão, assim, sujeitos a identificação eletrónica nem a registo obrigatório no SIAC.",
    "",
    "2. Licença de espécies exóticas — Quanto ao Decreto-Lei n.º 92/2019, de 10 de julho, a competência é do "
    "Instituto da Conservação da Natureza e das Florestas, I. P. (ICNF), cuja informação de que a atividade não "
    "carece de licença se recomenda que conserve por escrito.",
    "",
    "3. Registo como criador — A detenção de uma ou mais fêmeas reprodutoras cujas crias se destinem a venda, "
    "independentemente do número de animais ou do preço praticado, constitui «criação comercial de animais de "
    "companhia» (alíneas y) e aa) do n.º 1 do artigo 2.º do Decreto-Lei n.º 276/2001, de 17 de outubro). Esta "
    "atividade depende de mera comunicação prévia à DGAV (alínea a) do n.º 1 do artigo 3.º e artigo 3.º-A do mesmo "
    "diploma), efetuada eletronicamente no portal ePortugal antes do início da atividade. Na comunicação deve "
    "indicar, entre outros elementos, o local do alojamento, as espécies, a capacidade máxima e o médico veterinário "
    "responsável. Da comunicação resulta um número de criador, pessoal e intransmissível. O exercício da atividade "
    "sem esta comunicação constitui contraordenação.",
    "",
    "4. Principais obrigações — Deverá, designadamente:",
    "a) Dispor de médico veterinário responsável, que acompanhe o programa de saúde e bem-estar dos animais "
    "(artigos 4.º e 16.º);",
    "b) Manter, durante um ano, registos dos animais e do movimento mensal: nascimentos, mortes, saídas e destino "
    "(artigo 5.º);",
    "c) Assegurar as condições de alojamento, ambiente, alimentação, maneio e higiene previstas nos artigos 7.º a "
    "14.º e as condições particulares para pequenos roedores do artigo 26.º e do anexo II do Decreto-Lei "
    "n.º 276/2001, incluindo nas fases de reprodução e crescimento das crias.",
    "",
    "5. Anúncio e venda — Os anúncios de venda devem indicar, pelo menos, a idade dos animais, o seu número de "
    "criador e o número de animais da ninhada (artigo 53.º). Não sendo os hamsters sujeitos a identificação "
    "eletrónica, não lhes é exigível a indicação de número de identificação eletrónica. A venda só pode concretizar-"
    "se no local de criação ou em estabelecimento licenciado, não podendo ser feita por entidade transportadora "
    "(artigo 57.º). No momento da entrega, devem ser facultados ao adquirente a declaração de cedência ou o contrato "
    "de compra e venda e a respetiva fatura, uma declaração médico-veterinária que ateste que o animal se encontra "
    "de boa saúde e apto a ser vendido, e a informação sobre o historial clínico (artigo 54.º).",
    "",
    "6. Obrigações fiscais — O exposto não prejudica as obrigações devidas junto da Autoridade Tributária e "
    "Aduaneira (n.º 13 do artigo 3.º do Decreto-Lei n.º 276/2001).",
    "",
    "7. Regulamento (UE) 2026/1818 — O novo Regulamento europeu relativo ao bem-estar e à rastreabilidade aplica-se "
    "apenas a cães e gatos, não abrangendo hamsters.",
    "",
    "Com os melhores cumprimentos,",
]
first = True
for l in minuta:
    p = c.paragraphs[0] if first else c.add_paragraph()
    first = False
    r = p.add_run(l)
    r.font.size = Pt(9.5)
    if l.startswith("Assunto"):
        r.bold = True

doc.add_paragraph()
h("8. Fontes", 2)
for f in [
    "Decreto-Lei n.º 276/2001, de 17 de outubro, na redação do DL n.º 9/2021 — versão consolidada PGDL "
    "(https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=347&tabela=leis) e ficheiro do repositório.",
    "Decreto-Lei n.º 82/2019, de 27 de junho, na redação da Lei n.º 2/2020 — ficheiro @legislacao do repositório.",
    "Decreto-Lei n.º 92/2019, de 10 de julho, na redação da Lei n.º 25/2023 — PGDL "
    "(https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3100&tabela=leis) e ficheiro do repositório.",
    "Regulamento (UE) 2016/429, anexo I — texto EN (legislation.gov.uk, versão originalmente adotada).",
    "Regulamento (UE) 2026/1818 — texto publicado no JO (EN e PT), ficheiros do repositório.",
    "ICNF — Manual de Normas e Procedimentos da DAN, rev. 01.2023 (https://www.icnf.pt/api/file/doc/6b74c5b3f05d24b6).",
    "ICNF — Espécies exóticas ocorrentes em Portugal Continental não incluídas na LNEI "
    "(https://www.icnf.pt/api/file/doc/1fb57e0009a04d41).",
    "SIAC — Perguntas frequentes (https://siac.pt/pt/faq).",
    "Diploma final @rgac (versão: RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO — Revisto 30-06-2026 18h00 Grupo) — trabalho em curso.",
]:
    bullet(f)

out = "Hamsters/Informacao_Criacao_Hamsters_Sirios.docx"
doc.save(out)
print("OK", out)
