# -*- coding: utf-8 -*-
"""Conteudo da nota juridica sobre a titularidade dos gatos em programas CED."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'criador informal'))
from _memo_engine import *  # noqa: F401,F403


def construir(doc):
    p = doc.add_paragraph(); spacing(p, 0, 2)
    font(p.add_run('NOTA JURÍDICA'), 8, SUB, bold=True)
    p = doc.add_paragraph(); spacing(p, 0, 2)
    font(p.add_run('Titularidade dos gatos em programas CED'), 15, HEAD, bold=True)
    p = doc.add_paragraph(); spacing(p, 0, 4)
    font(p.add_run('O titular é o município promotor do programa, não o cuidador da colónia   ·   '
                   'DGAV, outubro de 2026'), 9, MUTE)
    rule(doc, CIT_BAR, 6, 8)

    para(doc,
         '**Conclusão.** A titularidade é do **município promotor**. O cuidador é **detentor** — possuidor precário —, na '
        'aceção da al. a) do art.º 3.º do Decreto-Lei n.º 82/2019, de 27 de junho. Resulta da articulação '
        'deste com o art.º 4.º da Lei n.º 27/2016, de 23 de agosto, e o art.º 9.º da Portaria n.º 146/2017, '
         'de 26 de abril.')

    h2(doc, '1.', 'O CED é atividade pública, executada pelo município')
    para(doc,
         'O art.º 4.º da Lei n.º 27/2016 dispõe que «O Estado, por razões de saúde pública, assegura, por '
         'intermédio dos centros de recolha oficial de animais, […] a concretização de programas captura, '
         'esterilização, devolução (CED) para gatos». A colónia só existe por ato administrativo: as '
         'câmaras municipais, «sob parecer do médico veterinário municipal», autorizam «a manutenção, em '
         'locais especialmente designados para o efeito, de colónias de gatos» — n.º 1 do art.º 9.º da '
         'Portaria n.º 146/2017. O programa pode ser proposto por organização de proteção animal, mas é a '
         'câmara que lhe atribui a gestão (n.º 2): gestão delegada não é titularidade.')

    h2(doc, '2.', 'A lei designa o titular do registo nestes casos')
    para(doc,
         'O percurso do animal CED está desenhado na lei e desemboca na norma que fixa o titular. O '
         'capturado passa obrigatoriamente pelo centro de recolha oficial — «são entregues nos CRO para '
         'verificação da sua aptidão», al. d) do n.º 4 do art.º 9.º da Portaria — e, não sendo reclamado, '
         'opera a presunção legal de abandono do n.º 1 do art.º 3.º da Lei n.º 27/2016. E então:')
    citacao(doc, [
        'Os animais que sejam recolhidos num Centro de Recolha Oficial (CRO) e que não sejam reclamados '
        'pelos seus proprietários devem ser registados no SIAC em nome do titular desse CRO, após o período '
        'de 15 dias previsto no n.º 4 do artigo 8.º da Portaria n.º 146/2017, de 26 de abril.'],
        'n.º 5 do art.º 11.º do Decreto-Lei n.º 82/2019, de 27 de junho')
    para(doc,
         'A norma é imperativa, e o titular do CRO é a câmara municipal. Como a al. e) do '
         'n.º 4 do art.º 9.º da Portaria impõe que os capturados sejam «registados e identificados '
         'eletronicamente», o gato CED é necessariamente animal registado, e o registo efetua-se «em nome '
         'do respetivo titular» (n.º 1 do art.º 9.º do Decreto-Lei n.º 82/2019). Nenhuma norma vigente '
         'designa o cuidador como titular nem afasta a do n.º 5 do art.º 11.º')
    para(doc,
         'O município pode ser titular desde o art.º 425.º da Lei n.º 2/2020, de 31 de março, que no n.º 5 '
         'do art.º 9.º passou a admitir «as pessoas singulares ou coletivas». E o n.º 2 do art.º 17.º '
         'isenta de taxa «os animais de companhia recolhidos pelos CRO […] que sejam registados em seu '
         'nome»: não se isenta de taxa um registo que não se admite.')

    h2(doc, '3.', 'O cuidador é detentor, não titular')
    citacao(doc, [
        'a) «Detentor», a pessoa singular ou coletiva que se encontre na situação de possuidor precário, '
        'nos termos previstos no artigo 1253.º do Código Civil, de animal de companhia […];',
        'f) «Titular de animal de companhia», o proprietário ou o possuidor, quer se trate de pessoa '
        'singular ou coletiva, que seja responsável pelo animal de companhia, independentemente da '
        'finalidade com que o detém, e cuja posse faça presumir a propriedade e em cujo nome deve '
        'efetuar-se o registo da titularidade do animal de companhia no SIAC […]'],
        'als. a) e f) do art.º 3.º do Decreto-Lei n.º 82/2019, na redação da Lei n.º 2/2020')
    para(doc,
         'A remissão para o art.º 1253.º resolve a questão. São possuidores precários, nos '
         'termos da sua al. c), «os representantes ou mandatários do possuidor e, de um modo geral, todos '
         'os que possuem em nome de outrem». O cuidador exerce o poder de facto dentro de um programa '
         'autorizado pela câmara, consta do plano de gestão da colónia e está sujeito à supervisão do '
         'médico veterinário municipal — al. a) do n.º 4 e n.º 5 do art.º 9.º da Portaria. Possui em nome '
         'de outrem, e falta-lhe por isso o pressuposto da al. f): a posse que faça presumir a '
         'propriedade.')

    h2(doc, '4.', 'O poder de recolha confirma quem é o titular')
    para(doc,
         'O n.º 9 do art.º 9.º da Portaria n.º 146/2017 permite à câmara, verificado o incumprimento de '
         'qualquer dos requisitos do n.º 4, «proceder à recolha dos animais para o CRO».')
    para(doc,
         'A Administração não dispõe de poder de apreensão definitiva de coisa alheia sem título de '
         'ablação e sem indemnização. Se os gatos fossem do cuidador, o n.º 9 seria inválido; lido como a '
         'retoma, pela câmara, da detenção material de animais de que é titular, é lícito.')

    h2(doc, '5.', 'Objeções')
    numlist(doc, [
        '**«As despesas são da entidade promotora, logo os animais são dela.»** O custeio não é título de '
        'aquisição. A Portaria distingue a câmara que autoriza (n.º 1), a entidade responsável (n.º 4) e a '
        'promotora que custeia (n.º 8), e a nenhuma atribui titularidade — nem o poderia, por ser matéria '
        'de lei e não de regulamento.',
        '**«O gato errante é coisa sem dono e quem o toma adquire-o por ocupação.»** O gato CED é '
        'capturado ao abrigo de um programa público, entregue no CRO por imposição legal, sujeito a uma '
        'presunção de abandono que lhe fixa o destino por lei, e registado no SIAC. Não é coisa sem dono: '
        'o n.º 3 do art.º 389.º do Código Penal trata como animais de companhia os sujeitos a registo no '
        'SIAC mesmo em estado de abandono ou errância.',
        '**«Quem cuida responde, logo é titular.»** O n.º 1 do art.º 493.º do Código Civil faz responder '
        '«quem tiver assumido o encargo da vigilância de quaisquer animais», seja ou não proprietário: a '
        'responsabilidade nasce do controlo de facto, a titularidade do registo.',
    ])

    para(doc,
         'Decorre deste entendimento que o dever de identificação e registo recai sobre o município e que o '
         'cuidador, como detentor, fica vinculado apenas à comunicação prevista no n.º 2 do art.º 16.º do '
         'Decreto-Lei n.º 82/2019.')
    para(doc,
         '**Deduções.** O regime é assimétrico: o n.º 9 do art.º 9.º da Portaria '
         'dá à câmara o poder sobre os animais e o n.º 1 do art.º 493.º do Código Civil deixa o risco com '
         'quem os alimenta. É essa assimetria que alimenta a '
         'controvérsia. Não há jurisprudência localizada.')
