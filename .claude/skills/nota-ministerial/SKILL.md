---
name: nota-ministerial
description: Produzir e manter as notas de apoio à atividade ministerial da DGAV, no modelo fixado pelo Gabinete do Senhor Ministro (MAGRIM) e desdobrado pela Diretora-Geral — fichas temáticas permanentes de 8 linhas, a nota temática por evento, a nota mensal de temas em destaque da primeira semana do mês e a atualização ao último dia útil. Usar sempre que o utilizador pedir uma nota, uma ficha temática ou uma nota de apoio para o Ministro ou para o Gabinete, falar de pontos sensíveis ou de linha defensiva, de preparação de audição regimental, debate parlamentar ou reunião do Ministro, pedir a nota mensal ou a atualização mensal, ou atualizar um tema acompanhado pela unidade orgânica, como o RGAC.
---

# Notas de apoio à atividade ministerial

As notas são documentos vivos. O conteúdo vive em `notas_ministeriais/dados_notas.py` e o Word é
gerado. **Nunca editar o `.docx` à mão** — é reescrito a cada geração.

| Ficheiro | Função |
|---|---|
| `notas_ministeriais/dados_notas.py` | Fichas temáticas permanentes, uma por tema. Designações proibidas, exceções e expressões a confirmar |
| `notas_ministeriais/gerar_nota.py` | Valida e gera os três documentos. **Recusa gerar** com erros; com avisos gera e diz |

```bash
python3 notas_ministeriais/gerar_nota.py --verificar            # valida tudo, não escreve nada
python3 notas_ministeriais/gerar_nota.py --verificar rgac       # valida uma ficha
python3 notas_ministeriais/gerar_nota.py rgac                   # nota temática
python3 notas_ministeriais/gerar_nota.py --mensal --mes 2026-09 # nota mensal do Gabinete
python3 notas_ministeriais/gerar_nota.py --atualizacao          # atualização à Diretora-Geral
```

**Começar sempre por `--verificar`.** É a forma de mexer na ficha e ver o estado sem produzir
ficheiros que ninguém pediu.

`--mes` fixa o mês a que o documento se refere, e sem ele usa-se o mês corrente — que raramente é o
certo: a nota da primeira semana de outubro reporta setembro. Passar `--mes` sempre.

## Os quatro produtos e quem os pede

| Produto | Quem pede | Quando | Conteúdo |
|---|---|---|---|
| **Ficha temática permanente** | Diretora-Geral | Mantida sempre atualizada; é a fonte de tudo | As 8 linhas |
| **Nota temática** | Gabinete, por evento | Com a antecedência que a agenda permitir | As 8 linhas, da ficha |
| **Nota mensal de temas em destaque** | Gabinete | Primeira semana de cada mês | Pontos 2 e 4, mais o subcapítulo obrigatório das medidas já tomadas |
| **Atualização da unidade orgânica** | Diretora-Geral | Até ao último dia útil do mês | Evoluções do mês, medidas adotadas, riscos e matérias com impacto |

A ficha é a fonte única e os três documentos são vistas dela. **Atualiza-se a ficha, não o Word.**

## As oito linhas

As quatro primeiras são o modelo fixado pelo Gabinete; as quatro últimas são o desdobramento pedido
pela Diretora-Geral. O gerador sombreia-as de forma diferente, como no modelo recebido.

| Campo em `dados_notas.py` | Linha | Origem |
|---|---|---|
| `enquadramento` | Enquadramento do tema | Gabinete |
| `pontos_sensiveis` | Pontos sensíveis / Linha defensiva | Gabinete |
| `mensagens_chave` | Mensagens-chave | Gabinete |
| `contexto` | Contexto e caracterização do setor | Gabinete |
| `acoes_medidas` | Ações em curso / Medidas adotadas | DGAV |
| `prioridades` | Prioridades futuras | DGAV |
| `impacto` | Matérias com impacto político, parlamentar e mediático | DGAV |
| `riscos` | Riscos / Constrangimentos | DGAV |

## Os campos de controlo

| Campo | Para que serve |
|---|---|
| `tema` | Cabeçalho do documento |
| `unidade` | Unidade orgânica que acompanha o tema. Vazio, a nota sai sem a identificar e o gerador avisa |
| `atualizado` | `AAAA-MM-DD` da última alteração. Passados 40 dias o gerador avisa que a ficha está por rever |
| `registo` | Pares (data, o que mudou) |
| `legislacao_verificada` | (data, âmbito varrido, resultado) do último varrimento de legislação nova |

O `registo` não é decorativo: o bloco **«Evoluções relevantes»** da atualização mensal é construído a
partir das linhas desse mês. Uma alteração à ficha sem linha de registo não chega à Diretora-Geral.
Por isso o gerador recusa gerar se o `registo` não tiver linha da data em `atualizado`.

## A linha que não pode ficar em branco

Na nota de 28.08.2026 a linha **«Pontos sensíveis / Linha defensiva» foi entregue vazia**. É a linha
que o Senhor Ministro mais precisa de levar para uma audição: é a única que lhe diz o que vão
perguntar e o que responder. O gerador **recusa gerar** com esse campo vazio, e a recusa diz porquê.

Escrevê-la bem: cada entrada é **um par** — a objeção previsível, e a resposta. Começar pela objeção,
em frase curta, e a seguir «Linha defensiva:». Não escrever a objeção sem resposta, nem resposta a
objeção que ninguém faria.

## O que o gerador recusa e o que só assinala

**Erros, não gera:** campo das oito linhas em falta ou vazio; designação errada da lista
`DESIGNACOES_PROIBIDAS`; parágrafo que acaba sem pontuação final (frase truncada); verbo de
publicação sem a data que lhe falta; `tema` em falta; `atualizado` em falta ou mal escrito; `registo`
vazio ou sem linha da data de `atualizado`.

**Avisos, gera e diz:** `unidade` vazia; ficha sem revisão há mais de 40 dias; parágrafo acima de 700
caracteres; varrimento legislativo em falta ou com mais de 45 dias; expressão da lista
`DESIGNACOES_A_CONFIRMAR`; e as duas confusões que esta casa não pode cometer — «em vigor» amarrado a
uma data de 2028 ou posterior, e dizer que o Regulamento (UE) 2026/1818 «já se aplica».

## Verificar legislação nova antes de atualizar a ficha

Uma nota que ignore um diploma saído na semana anterior é um risco para quem a assina. Antes de
atualizar uma ficha, varrer o período desde a data em `legislacao_verificada` e escrever lá o
resultado, mesmo quando é negativo — sobretudo quando é negativo, porque é isso que se pode afirmar.

O Diário da República não é pesquisável por ferramenta: o sítio é uma aplicação de página única e
devolve a aplicação, não os atos. Os fascículos da 1.ª série, esses, estão em PDF com texto, num
endereço previsível, e o número do fascículo é sequencial no ano:

```bash
# n é o número do fascículo, mm o mês em que saiu (o mês errado devolve 301)
curl -sS -o 1s_${n}.pdf "https://files.diariodarepublica.pt/gratuitos/1s/2026/${mm}/${n}00.pdf"
pdftotext -layout 1s_${n}.pdf 1s_${n}.txt
grep -i -E "animais de companhia|cães|gatos|bem-estar animal|centro de recolha oficial|SIAC" *.txt
```

A primeira linha de cada `.txt` traz o número e a data do fascículo, o que confirma que a série está
completa e sem saltos. O sumário está nas primeiras 60 linhas e identifica cada diploma. No lado
europeu, o EUR-Lex responde 202 sem corpo através do proxy desta sessão; usar pesquisa web e os
boletins mensais de legislação do setor para confirmar o Jornal Oficial.

## Regras de escrita

1. **PT-PT**, registo de administração pública, frases curtas. Sem negritos, itálicos ou cores no
   corpo — o modelo não os usa.
2. **Designações fixas.** `Regime Geral do Animal de Companhia (RGAC)`, nunca «Regulamento Geral» nem
   «Regime Geral dos Animais de Companhia». `Regulamento (UE) 2026/1818`, nunca «Regulamento
   2026/1818» nem «(EU)». `bem-estar` em minúscula e com hífen, salvo nos nomes próprios da lista
   `EXCECOES_DESIGNACAO` — é o caso de «Regime Geral do Bem-Estar dos Animais de Companhia», nome da
   proposta de 2024 e 2025.
3. **Nenhuma frase truncada.** A nota de agosto terminava um parágrafo em «que foi publicado dia».
4. **Datas completas** e verificadas. Nunca «publicado dia» sem o dia.
5. **Nada de inventado.** Números, datas e posições de entidades só entram se estiverem confirmados.
   Se não estiver confirmado, não entra — ou entra dito como por confirmar.
6. **Separar o que é facto do que é posição.** As linhas de enquadramento, contexto e medidas são
   descritivas. A linha defensiva e as mensagens-chave são posição, e é o utilizador que as valida.
7. **Nunca tratar o RGAC, o Código do Animal de Companhia ou o Regime Geral do Bem-Estar dos Animais
   de Companhia como direito em vigor.** São propostas. A nota que os confunda com legislação vigente
   põe o Ministro a afirmar o que não existe.

## Como trabalhar com o utilizador

- **Não gerar nem enviar sem ordem.** Propor em conversa o que se vai alterar na ficha, escrever no
  `dados_notas.py`, correr `--verificar`, e só gerar quando ele mandar.
- A linha dos **pontos sensíveis e a linha defensiva são do utilizador**, não minhas: redigir
  proposta, apresentá-la, e deixá-lo decidir o teor político antes de entrar na ficha.
- Ao fechar: gerar, conferir em PDF, acrescentar a linha ao `registo`, commit e envio.

## Ficha nova

1. Acrescentar a entrada a `FICHAS` em `dados_notas.py`, com `tema`, `unidade`, `atualizado`, os oito
   campos, `legislacao_verificada` e `registo`.
2. Correr `python3 notas_ministeriais/gerar_nota.py --verificar <slug>` e corrigir o que aparecer.
3. A ficha passa automaticamente a entrar na nota mensal e na atualização à Diretora-Geral.

## Fidelidade ao modelo

O formato foi medido no ficheiro do Gabinete de 28.08.2026 e é reproduzido: A4, margens de 3 cm e
4,25 cm em cima, Segoe UI, título a 14 pt negrito, tabela «Table Grid» com grelha fixa de 4,18 cm e
10,82 cm, rótulos em Aptos 12 pt negrito, sombreado D9D9D9 nas quatro linhas do Gabinete e D0CECE nas
quatro da DGAV, corpo a 11 pt justificado. Se o Gabinete mudar o modelo, medir o novo ficheiro antes
de alterar o gerador — o ficheiro do Gabinete não está no repositório e tem de ser pedido ao
utilizador.

## Onde isto fica guardado

O repositório `rancarvid/Legislacao` é **público**. Notas de apoio à atividade ministerial, e em
especial a linha defensiva, são documentos internos. Antes de acrescentar ou alterar conteúdo destas
notas, confirmar com o utilizador onde quer que ele viva. Nada de notas num repositório público sem
ele o ter decidido.
