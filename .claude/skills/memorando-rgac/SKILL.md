---
name: memorando-rgac
description: Atualizar o Memorando de acompanhamento do RGAC (Word), que regista os problemas encontrados no projeto de Regime Geral do Animal de Companhia (fichas por tema ou capítulo, lapsos formais, cobertura da revisão artigo a artigo, posições de entidades externas e bibliografia verificada). Usar sempre que o utilizador identifique um problema, lapso ou melhoria no RGAC, peça para rever um artigo ou capítulo, acrescentar ou fechar uma ficha, carregue uma versão nova do RGAC, ou peça o memorando de acompanhamento.
---

# Memorando de acompanhamento do RGAC

O memorando é um documento vivo. O conteúdo está todo num ficheiro de dados e o Word é gerado a partir dele.

| Ficheiro | Função |
|---|---|
| `memorando_rgac/dados_memorando_rgac.py` | Conteúdo: fichas, pontos resolvidos, entidades externas, fontes, registo de alterações |
| `memorando_rgac/gerar_memorando_rgac.py` | Gera o Word. Recusa gerar se houver travessões longos, códigos repetidos ou campos inválidos |
| `memorando_rgac/Memorando_Acompanhamento_RGAC.docx` | Resultado. Nunca editar à mão: é reescrito a cada geração |
| `memorando_rgac/extrair_estrutura_rgac.py` | Lê o RGAC canónico e escreve `estrutura_rgac.json` (capítulos, artigos, epígrafes). Correr sempre que chegar versão nova |
| `memorando_rgac/estrutura_rgac.json` | Estrutura do RGAC usada no Anexo D e na validação das chaves de artigo. Não editar à mão |
| `memorando_rgac/verificar_ligacoes.py` | Verifica todas as ligações da bibliografia (curl, browser real e Europe PMC) e escreve `verificacao_ligacoes.md` |
| `memorando_rgac/pistas_imprensa_uso_interno.md` | Notícias de imprensa, só para uso interno. Não entram no memorando |

Gerar: `python3 memorando_rgac/gerar_memorando_rgac.py` (requer `pip install python-docx`).

## Estrutura do memorando

1. Como ler este memorando (inclui a lista de letras dos códigos)
2. Temas com fichas, pela ordem de `TEMAS`: primeiro os transversais T e C, depois os capítulos do RGAC. Só aparecem os temas com fichas; a numeração é automática.
3. Pontos já resolvidos no RGAC
4. Anexo A: quadro-resumo das fichas (automático)
5. Anexo B: posições de entidades externas
6. Anexo C: lapsos formais (tabela `LAPSOS`)
7. Anexo D: cobertura da revisão, artigo a artigo (automático, a partir de `estrutura_rgac.json`, das fichas, dos lapsos e de `REVISAO`)
8. Registo de alterações
9. Bibliografia (a partir de `BIBLIOGRAFIA`, com ligações clicáveis)

### Temas e letras

| Letra | Tema |
|---|---|
| T | Titular, detentor, proprietário e operador (transversal) |
| C | Programas CED, colónias e animais errantes (transversal) |
| A | Cap. I, disposições gerais e definições |
| P | Cap. II, princípios gerais |
| H | Cap. III, detenção |
| E | Cap. IV, detenção em estabelecimentos |
| M | Caps. V a VII, alimentação, maneio, transporte, contenção e intervenções cirúrgicas |
| R | Cap. VIII, registo, identificação e sistemas de informação |
| Z | Cap. IX, zoonoses |
| G | Cap. X, gestão das populações animais |
| K | Caps. XI a XIII, cadáveres, exposições, comércio e livros genealógicos |
| D | Cap. XIV, animais perigosos e potencialmente perigosos |
| S | Cap. XV, medidas administrativas, fiscalização e contraordenações |
| F | Cap. XVI e anexos, disposições finais e transitórias |
| L | Reservada aos lapsos formais |

As letras estão em `CAPITULOS` no ficheiro de dados. Uma ficha nova entra na lista `fichas` do capítulo onde está o problema. Se o problema atravessa vários capítulos e é de titularidade ou de CED, vai para T ou C. Um tema transversal novo cria-se como T e C (dicionário com `letra`, `titulo`, `intro`, `fichas`) e acrescenta-se a `TEMAS`; o gerador não precisa de alterações.

Se uma versão nova do RGAC mudar a divisão em capítulos, ajustar `capitulos` e `titulo` em `CAPITULOS`, sem mudar as letras nem os códigos já atribuídos.

## Ficha

Cada ficha é um dicionário com estes campos:

- `cod`: código fixo, com a letra do tema, por exemplo `T-18` ou `R-01`. Nunca reutilizar um código. Nunca renumerar fichas existentes. O gerador recusa códigos que não comecem pela letra do tema.
- `titulo`: frase curta que diga o problema.
- `onde`: lista de referências ao RGAC no formato `art. X.º, n.º Y, al. Z)`. O Anexo D liga a ficha aos artigos citados aqui; referências a outros diplomas levam o nome do diploma (DL, Lei, Portaria, Código, Regulamento) e são ignoradas.
- `origem`: `RGAC` (criado pelo RGAC), `VIGENTE` (já existia e o RGAC não resolve) ou `PARCIAL` (já existia, o RGAC resolve em parte).
- `problema`: lista de parágrafos curtos.
- `proposta`: solução ou redação sugerida. Se ainda não houver, escrever «Por definir.».
- `levantado`: lista de quem apontou o problema (entidade e data, ou «Análise interna»).
- `estado`: `Aberto`, `Parcialmente resolvido` ou `Resolvido`.
- `rel`: lista de códigos de fichas relacionadas (o gerador verifica que existem).

Quando um problema fica resolvido numa versão nova do RGAC: mudar o `estado`, acrescentar ao `problema` uma frase a dizer em que versão e artigo foi resolvido, e acrescentar a entrada correspondente em `RESOLVIDOS`. Não apagar a ficha.

## Lapso ou ficha?

- Lapso formal (Anexo C, código `L-`): remissão errada, número de artigo ou de n.º repetido, secção mal numerada, gralha, marca de trabalho («??», «XX», «ALTERAR», comentários esquecidos), epígrafe que não corresponde ao conteúdo. Corrige-se sem decisão de fundo.
- Ficha: tudo o que exige escolha do grupo (conteúdo da norma, conflito com legislação vigente ou com o Regulamento (UE) 2026/1818, lacuna, melhoria de redação que muda o sentido).
- Quando um lapso esconde uma questão de fundo, cria-se a ficha e o lapso aponta para ela no campo `ficha`.

Cada lapso é um dicionário: `cod`, `onde` (lista de chaves de artigo de `estrutura_rgac.json`, por exemplo `"86"` ou `"81-b"`), `lapso`, `correcao`, `estado` (um de `ESTADOS`), `ficha` (código ou vazio).

## Rever um artigo ou um capítulo

1. Confirmar o RGAC canónico (tabela 2.1 do `CLAUDE.md`) e que `estrutura_rgac.json` foi extraída desse ficheiro (o gerador recusa se não foi).
2. Ler o artigo inteiro no ficheiro canónico. Verificar: remissões internas (o artigo remetido existe e diz o que se pretende), termos definidos no art. 3.º usados com o mesmo sentido (titular, detentor, operador, abandono, errante), numeração de n.ºs e alíneas, coerência com o art. 140.º (contraordenações) e com o art. 149.º (norma revogatória).
3. Confrontar com a legislação vigente que o artigo substitui (validação tripla: online, pasta `Legislação vigente/`, repositório) e registar o que se perde ou muda.
4. Confrontar com o Regulamento (UE) 2026/1818: há correspondência? O RGAC repete, contraria ou vai além? Ter em conta as datas de aplicação do art. 33.º do Regulamento.
5. Registar: lapsos em `LAPSOS`, problemas de fundo em fichas do capítulo, e o resultado em `REVISAO`:
   `"86": {"estado": "Revisto", "data": "27.9.2026", "regulamento": "Sem correspondência", "nota": "Regulamento não trata errantes (SWD(2024) 88)"}`.
   Estados de revisão: `Por rever`, `Em revisão`, `Revisto`. Relação com o Regulamento: `A verificar`, `Sem correspondência`, `Conforme`, `Divergente`, `Integra o Regulamento`.
6. Os artigos sem entrada em `REVISAO` aparecem no Anexo D como «Por rever», ou «Parcial» se já tiverem fichas ou lapsos.

## Versão nova do RGAC

1. Atualizar a linha ⭐ do `CLAUDE.md` (tabela 2.1), `FICHEIRO_RGAC` e `VERSAO_RGAC` no ficheiro de dados.
2. Correr `python3 memorando_rgac/extrair_estrutura_rgac.py`. Ver no ecrã os números repetidos, em falta e fora de ordem: são lapsos a registar ou a fechar.
3. Rever todas as fichas e lapsos: numeração dos artigos em `onde`, estado (resolvido ou não), e fechar os que a versão nova corrige (estado `Resolvido` e frase a dizer em que versão). Não apagar.
4. Rever `REVISAO`: um artigo alterado volta a «Em revisão».

## Regras de escrita (obrigatórias)

- Português de Portugal. Frases curtas. Uma ideia por frase.
- Linguagem simples, de quem trabalha no texto. Nada de «importa salientar», «cumpre referir», «no que concerne», «de facto», «crucial», «robusto», «abordagem», «em suma».
- Sem travessões longos (— ou –). Usar vírgula, ponto ou dois pontos. O gerador falha se os encontrar.
- Sem itálico, sem cores, sem negrito no meio do texto. O gerador trata da formatação.
- Sem listas de três adjetivos, sem frases de efeito, sem conclusões genéricas.
- Referências sempre localizáveis: `art. 86.º, n.º 6, al. d)`. Para outros diplomas, nomear o diploma: `DL 82/2019, art. 16.º, n.º 2`.
- Citações do RGAC curtas e entre «», só quando a palavra exata importa. Nunca parafrasear dentro de aspas.
- Opinião e proposta vão no campo `proposta`. O campo `problema` descreve.

## Antes de acrescentar ou alterar uma ficha

1. Confirmar qual é a versão canónica do RGAC na tabela 2.1 do `CLAUDE.md` (linha ⭐). Se o utilizador carregou uma versão nova, atualizar `VERSAO_RGAC` e rever a numeração de todas as referências `onde` (os artigos mudam de número entre versões).
2. Confirmar o texto do artigo no ficheiro canónico. Os artigos têm números explícitos na revisão formal; se o ficheiro usar numeração automática do Word, reconstruir pelo índice e indicar a epígrafe.
3. Para legislação vigente, fazer a validação tripla definida no projeto: online (DRE ou PGDL), pasta `Legislação vigente/` e ficheiros do repositório.
4. Para posições de entidades externas, guardar a fonte (URL ou ficheiro) e só usar aspas quando o texto foi transcrito da fonte.

## Depois de alterar

1. Subir `VERSAO_MEMORANDO`, atualizar `DATA_MEMORANDO` e acrescentar uma linha a `REGISTO_ALTERACOES` a dizer o que mudou (fichas novas, fichas fechadas, versão do RGAC).
2. Gerar o Word e confirmar que o gerador não deu erros. Validar o ficheiro contra o esquema (por exemplo, com o validador da skill docx: `scripts/office/validate.py`). O Word ignora propriedades de tabela fora da ordem do esquema; o gerador reordena-as em `ordenar_tblpr()`, que não deve ser removida.
3. Rever o texto gerado (por exemplo, com python-docx a listar títulos e tabelas).
4. Fazer commit dos ficheiros alterados de `memorando_rgac/` (dados, gerador, docx, estrutura, verificação) e push para o ramo de trabalho.

## Fontes

1. O memorando usa só documentos: diplomas e projetos, pareceres, relatórios, estratégias, recomendações do Provedor de Justiça, acórdãos, doutrina publicada e artigos científicos. Só se cita entre «» texto transcrito do próprio documento.
2. Notícias de imprensa (notícias, entrevistas, resumos de audições) nunca entram no memorando, nem no Anexo B nem nas fichas. O gerador recusa gerar se uma fonte do Anexo B for de um domínio de `DOMINIOS_IMPRENSA` ou se um campo `levantado` mencionar imprensa. Acrescentar domínios novos a essa lista.
3. As notícias guardam-se em `memorando_rgac/pistas_imprensa_uso_interno.md`. Servem para formular hipóteses, preparar propostas e procurar o documento de origem. Quando esse documento for encontrado e lido, a posição pode entrar no memorando com a fonte documental.

## Bibliografia e ligações

1. Toda a fonte usada no memorando entra em `BIBLIOGRAFIA` como (grupo, referência, ligação, palavra de controlo). A ligação é um URL ou `repositório: <ficheiro>`.
2. A fonte de cada entrada do Anexo B tem de ser exatamente uma ligação da bibliografia. O gerador recusa gerar se não for, ou se um ficheiro do repositório não existir.
3. A palavra de controlo é uma expressão que tem de aparecer no documento. Serve para confirmar que a ligação abre o documento certo, e não só uma página qualquer.
4. Depois de acrescentar ou mudar fontes, correr `python3 memorando_rgac/verificar_ligacoes.py`. Só se faz commit com 0 falhas. Atualizar `DATA_LIGACOES` com a data da verificação.
5. Preferir ligações estáveis: PDF do Diário da República, PGDL, DGSI ou jurisprudencia.pt, EUR-Lex por ELI, DOI ou PubMed Central para artigos científicos.
