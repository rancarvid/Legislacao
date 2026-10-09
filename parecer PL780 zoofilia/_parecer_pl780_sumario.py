# -*- coding: utf-8 -*-
"""Parecer DGAV sobre o PL n.º 780/XVII/2.ª — versão sumária, 2 páginas.

Registo institucional, incidência restrita ao bem-estar dos animais de companhia.
"""
from _memo_engine import *
from docx.shared import Cm


def construir(doc):
    enquadramento(doc, [
        '**DIREÇÃO-GERAL DE ALIMENTAÇÃO E VETERINÁRIA** · Bem-estar dos animais de companhia · Processo '
        'n.º ____ · Data ____',
        '**Projeto de Lei n.º 780/XVII/2.ª (PAN)** — «Criminaliza a prática da zoofilia reforçando a '
        'proteção animal e a tutela penal e contraordenacional». Altera o artigo 387.º do Código Penal e '
        'adita a alínea h) ao n.º 3 do artigo 1.º da Lei n.º 92/95, de 12 de setembro.',
        'O presente parecer incide sobre o bem-estar dos animais de companhia, matéria da competência desta '
        'divisão, formulando-se as observações sobre as demais matérias a título de sinalização, sem '
        'prejuízo da pronúncia das unidades competentes. **Sentido: favorável, condicionado à correção '
        'referida no ponto 3.**'])

    h1(doc, '1.', 'O que a iniciativa acrescenta')
    para(doc,
         'O n.º 3 do artigo 387.º passa a comportar duas alíneas, sob o elemento comum «sem motivo '
         'legítimo»: a alínea a) reproduz o crime de maus tratos vigente e a alínea b) acrescenta «Ofender '
         'sexualmente um animal de companhia através de cópula, coito anal, coito oral ou a introdução '
         'vaginal, anal ou oral de partes do corpo ou de objetos», mantendo-se a moldura vigente. Na Lei '
         'n.º 92/95 adita-se a alínea h) com fórmula equivalente, referida a «animais» sem qualificação de '
         'espécie.')
    destaque(doc, [
        'O efeito útil é um só, e importa fixá-lo: **a conduta passa a ser punível sem dependência da prova '
        'de dor, sofrimento ou lesão**. É o que a legislação vigente não assegura.'])

    h1(doc, '2.', 'A insuficiência que a iniciativa supre')
    para(doc,
         'Toda a tutela hoje disponível é de resultado: o n.º 3 do artigo 387.º do Código Penal exige dor, '
         'sofrimento ou maus tratos físicos provados, e o n.º 1 do artigo 1.º da Lei n.º 92/95 exige a '
         'morte, ou o sofrimento cruel e prolongado, ou graves lesões.')
    para(doc,
         'Acresce — e é este o ponto de maior relevo para a competência desta divisão — que o dever especial '
         'de cuidado consagrado no artigo 6.º do Decreto-Lei n.º 276/2001, de 17 de outubro, que impõe ao '
         'detentor cuidar do animal «de forma a não pôr em causa os parâmetros de bem-estar», não se '
         'encontra sancionado quando o perigo recaia sobre o próprio animal. As contraordenações que o '
         'sancionam são apenas duas: a alínea j) do n.º 1 do artigo 68.º, quando a violação «crie perigo '
         'para a vida ou integridade física de outro animal», e a alínea b) do n.º 2, quando crie perigo '
         '«de outrem». **A ofensa sexual não põe em perigo terceiro nem outro animal: situa-se precisamente '
         'no espaço não sancionado.**')
    para(doc,
         'Assinala-se ainda que o ordenamento já qualificou o motivo sexual como especialmente censurável, '
         'na alínea c) do n.º 5 do artigo 387.º — «para excitação» —, sem que exista o tipo que essa '
         'agravante pressupõe.')
    nota(doc, [
        '**Sinalização, fora da competência desta divisão.** A conduta envolve contacto directo de mucosas '
        'entre espécies, com relevância higiossanitária e zoonótica documentada — associação epidemiológica '
        'apurada em estudo caso-controlo multicêntrico (Zequi SC, et al., J Sex Med. 2012;9(7):1860-67) e '
        'transmissão sexual de brucelose descrita (Li N, et al., IDCases. 2020;21:e00871). Matéria de saúde '
        'pública veterinária, que se sinaliza para pronúncia da unidade competente e cuja inclusão na '
        'fundamentação da iniciativa se sugere.'])

    h1(doc, '3.', 'Correção premente: sobreinclusão sobre actos médico-veterinários')
    para(doc,
         'A alínea h) proposta para a Lei n.º 92/95 abrange «a introdução vaginal, anal ou oral de partes do '
         'corpo ou de objetos». Diferentemente da norma penal, que subordina ambas as alíneas ao elemento '
         '«sem motivo legítimo», a norma contraordenacional não comporta qualquer elemento limitador. O '
         'n.º 1 do mesmo artigo não supre a falta: é autodefinido e o n.º 3 abre com «São também proibidos», '
         'acrescentando e não especificando — sendo a demonstração interna ao artigo, porquanto as alíneas '
         'a), b), c), e) e f) carregam limitadores próprios, que seriam redundantes se o n.º 1 se '
         'transmitisse. Ficam assim abrangidos, na letra, actos correntes da prática clínica e zootécnica: '
         'termometria rectal, palpação e ecografia transrectais, inseminação artificial, sondagem, enemas '
         'e exploração obstétrica.')
    para(doc,
         'Cumpre delimitar o alcance da objeção: por força do artigo 32.º do Regime Geral das '
         'Contra-Ordenações operam as causas de exclusão da ilicitude do artigo 31.º do Código Penal, pelo '
         'que o acto praticado no exercício da atividade médico-veterinária estaria justificado. **Não se '
         'sustenta que um médico veterinário viesse a ser sancionado.** A objeção é de estrutura: a norma '
         'fica sobreinclusiva na sua face e a licitude passa a discutir-se por causa de justificação não '
         'escrita, quando o artigo 11.º da Lei n.º 92/95 atribui a fiscalização a nove entidades, incluindo '
         'autoridades policiais.')
    destaque(doc, [
        '**Correção que se propõe.** Introdução, na alínea h), de elemento que restrinja a conduta à '
        'finalidade sexual — ou, em alternativa, ressalva expressa dos actos médico-veterinários e '
        'zootécnicos legalmente praticados. Prefere-se a primeira: com elemento finalístico, o acto clínico '
        'não chega a preencher a norma, dispensando ressalva e a sua actualização.'])

    h1(doc, '4.', 'Observações de aperfeiçoamento')
    numlist(doc, [
        '**Taxatividade.** Sendo a lista fechada, ficam fora a masturbação do animal, o contacto '
        'oral-genital sem coito e a imposição de monta, incluindo quando a desproporção de porte seja '
        'susceptível de causar lesões — condutas que a exposição de motivos refere e o articulado não '
        'abrange.',
        '**Conteúdos audiovisuais.** A exposição de motivos anuncia a criminalização da produção e difusão '
        'de conteúdos, que o articulado não dispõe. A alínea e) do n.º 3 do artigo 1.º já cobre parte da '
        'produção; nada da difusão.',
        '**Dever de comunicação.** Deverá prever-se dever de comunicação a cargo do médico veterinário que '
        'detete indícios compatíveis com ofensa sexual, e como se articula com o sigilo do Código '
        'Deontológico Médico-Veterinário? Questão que se suscita, sem juízo prévio, sugerindo-se a audição '
        'da Ordem dos Médicos Veterinários.',
    ])

    h1(doc, '5.', 'Conclusão')
    destaque(doc, [
        'A insuficiência invocada verifica-se — a tutela vigente é toda de resultado e a violação do dever '
        'de cuidado que ponha em perigo o próprio animal não é contraordenável —, tendo a iniciativa '
        'utilidade normativa autónoma por deslocar a tutela do resultado para o acto. Sendo, porém, a '
        'redação proposta para a Lei n.º 92/95 sobreinclusiva quanto a actos médico-veterinários e '
        'zootécnicos, é premente a correção do ponto 3. **Nada mais se opõe, em termos técnicos, à '
        'aprovação da iniciativa.**'])
