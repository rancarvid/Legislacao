---
name: memorando-rgac
description: Atualizar o Memorando de acompanhamento do RGAC (Word), que regista os problemas encontrados no projeto de Regime Geral do Animal de Companhia, os que já existem na legislação vigente e as críticas de entidades externas. Usar sempre que o utilizador identifique um problema novo no RGAC, peça para acrescentar ou fechar uma ficha, carregue uma versão nova do RGAC, ou peça o memorando de acompanhamento.
---

# Memorando de acompanhamento do RGAC

O memorando é um documento vivo. O conteúdo está todo num ficheiro de dados e o Word é gerado a partir dele.

| Ficheiro | Função |
|---|---|
| `memorando_rgac/dados_memorando_rgac.py` | Conteúdo: fichas, pontos resolvidos, entidades externas, fontes, registo de alterações |
| `memorando_rgac/gerar_memorando_rgac.py` | Gera o Word. Recusa gerar se houver travessões longos, códigos repetidos ou campos inválidos |
| `memorando_rgac/Memorando_Acompanhamento_RGAC.docx` | Resultado. Nunca editar à mão: é reescrito a cada geração |

Gerar: `python3 memorando_rgac/gerar_memorando_rgac.py` (requer `pip install python-docx`).

## Estrutura do memorando

1. Como ler este memorando
2. Tema T: titular, detentor, proprietário e operador (fichas T-01, T-02, ...)
3. Tema C: programas CED, colónias e animais errantes (fichas C-01, C-02, ...)
4. Pontos já resolvidos no RGAC
5. Anexo A: quadro-resumo (gerado automaticamente)
6. Anexo B: posições de entidades externas
7. Anexo C: fontes
8. Registo de alterações

Um tema novo cria uma letra nova (por exemplo R para reprodução, E para estabelecimentos). Acrescentar o dicionário do tema em `dados_memorando_rgac.py`, incluí-lo em `verificar_texto()`, `indice()`, no ciclo dos temas em `gerar()` e em `quadro_resumo()` no gerador. A ordem dos temas segue, mais ou menos, a ordem do RGAC.

## Ficha

Cada ficha é um dicionário com estes campos:

- `cod`: código fixo, por exemplo `T-18`. Nunca reutilizar um código. Nunca renumerar fichas existentes.
- `titulo`: frase curta que diga o problema.
- `onde`: lista de referências ao RGAC no formato `art. X.º, n.º Y, al. Z)`.
- `origem`: `RGAC` (criado pelo RGAC), `VIGENTE` (já existia e o RGAC não resolve) ou `PARCIAL` (já existia, o RGAC resolve em parte).
- `problema`: lista de parágrafos curtos.
- `proposta`: solução ou redação sugerida. Se ainda não houver, escrever «Por definir.».
- `levantado`: lista de quem apontou o problema (entidade e data, ou «Análise interna»).
- `estado`: `Aberto`, `Parcialmente resolvido` ou `Resolvido`.
- `rel`: lista de códigos de fichas relacionadas (o gerador verifica que existem).

Quando um problema fica resolvido numa versão nova do RGAC: mudar o `estado`, acrescentar ao `problema` uma frase a dizer em que versão e artigo foi resolvido, e acrescentar a entrada correspondente em `RESOLVIDOS`. Não apagar a ficha.

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
4. Fazer commit dos três ficheiros de `memorando_rgac/` e push para o ramo de trabalho.
