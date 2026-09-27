# Propostas de organização do memorando de acompanhamento do RGAC

Documento de trabalho. Nenhuma destas opções está implementada. O memorando continua na versão 1.7
(temas T e C, mais temas por capítulo com letras, Anexo C de lapsos e Anexo D de cobertura).

## Problema a resolver

As letras por capítulo (A, P, H, E, M, R, Z, G, K, D, S, F) parecem aleatórias. Além disso, qualquer
código ligado ao número do capítulo ou do artigo fica errado quando o RGAC for renumerado.

Objetivo: seguir a disposição do RGAC sem ficar preso à numeração atual, ou atualizar-se sozinho quando
a numeração mudar.

## Opção A. Número permanente, localização calculada, temas como etiquetas

Guardada a 27.9.2026, a pedido do utilizador.

1. Identificação. Cada ficha tem um número permanente sem significado, pela ordem de criação:
   P-01, P-02, ... Nunca muda. Os lapsos mantêm L-01, L-02, ...
2. Localização. Cada ficha fica presa ao artigo principal pela epígrafe (por exemplo «Programas de
   captura, esterilização e devolução»), e não pelo número. O gerador lê `estrutura_rgac.json` e escreve
   o número e o capítulo atuais («art. 86.º, cap. X»).
3. Versão nova do RGAC. Corre-se `extrair_estrutura_rgac.py`; números e capítulos atualizam-se sozinhos
   em fichas, índice, Anexo C e Anexo D. Se uma epígrafe mudar ou um artigo desaparecer, o gerador pára
   e mostra uma lista «a reconciliar» (ficha, epígrafe antiga, candidatas na versão nova).
4. Referências no texto das fichas. Marca `[[epígrafe]]` convertida no número atual. O gerador avisa se
   um número escrito à mão não bater com a versão atual. Os n.ºs e alíneas dentro de um artigo continuam
   a rever-se à mão quando o artigo é reescrito.
5. Arrumação. As secções do memorando são os capítulos da versão atual (só os que têm fichas), com as
   fichas pela ordem dos artigos. Reordena-se sozinho quando o RGAC muda.
6. Temas como etiquetas. Titularidade, CED e errantes, registo, reprodução, etc. deixam de ser prefixo
   do código. Uma ficha pode ter várias etiquetas. Anexo novo «Índice por tema», automático.
7. Custo. As 35 fichas atuais (T-01 a T-18, C-01 a C-17) passam a P-01 a P-35, uma única vez, com
   tabela de correspondência no memorando. Variante: manter T-01 e C-01 e só as novas receberem P-.

Exemplo:

    P-27. Remissões e numeração erradas no artigo dos programas CED
    Onde: art. 86.º, n.º 1; art. 86.º, n.º 6, al. e) (cap. X)
    Temas: CED e errantes

Se o artigo passar a 90.º no cap. XI, a ficha continua P-27 e passa a dizer «art. 90.º (cap. XI)».

## Opção B. Um documento Word por tema em revisão

Em exploração. Ver secção seguinte quando for decidida.
