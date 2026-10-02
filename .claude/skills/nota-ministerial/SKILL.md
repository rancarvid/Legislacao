---
name: nota-ministerial
description: Produzir e manter as notas de apoio à atividade ministerial da DGAV, no modelo fixado pelo Gabinete do Senhor Ministro (MAGRIM) e desdobrado pela Diretora-Geral — fichas temáticas permanentes de 8 linhas, a nota mensal de temas em destaque da primeira semana do mês e a atualização ao último dia útil. Usar sempre que o utilizador pedir uma nota ou ficha para o Ministro ou para o Gabinete, falar de notas de apoio à atividade ministerial, de preparação de audição regimental, debate parlamentar ou reunião do Ministro, pedir a nota mensal ou a atualização mensal, ou atualizar um tema acompanhado pela unidade orgânica, como o RGAC.
---

# Notas de apoio à atividade ministerial

As notas são documentos vivos. O conteúdo vive em `notas_ministeriais/dados_notas.py` e o Word é
gerado. **Nunca editar o `.docx` à mão** — é reescrito a cada geração.

| Ficheiro | Função |
|---|---|
| `notas_ministeriais/dados_notas.py` | Fichas temáticas permanentes, uma por tema. Designações proibidas e respetivas exceções |
| `notas_ministeriais/gerar_nota.py` | Gera a nota temática e a nota mensal. **Recusa gerar** se a ficha tiver problemas |
| `notas_ministeriais/<data>_<TEMA>_Notas_apoio_atividade_ministerial.docx` | Nota temática |
| `notas_ministeriais/<data>_Nota_mensal_temas_destaque.docx` | Nota mensal |

```bash
python3 notas_ministeriais/gerar_nota.py rgac        # nota temática
python3 notas_ministeriais/gerar_nota.py --mensal    # nota mensal, todas as fichas
```

## Os três produtos e quem os pede

| Produto | Quem pede | Quando | Conteúdo |
|---|---|---|---|
| **Ficha temática permanente** | Diretora-Geral | Mantida sempre atualizada; serve de base a tudo | As 8 linhas |
| **Nota temática** | Gabinete, por evento | Com a antecedência que a agenda permitir | As 8 linhas, da ficha |
| **Nota mensal de temas em destaque** | Gabinete | Primeira semana de cada mês | Só pontos 2 e 4, mais o subcapítulo obrigatório das medidas já tomadas |
| **Atualização da unidade orgânica** | Diretora-Geral | Até ao último dia útil do mês | Evoluções, medidas adotadas, riscos e matérias com impacto. Serve de base à nota mensal |

A ficha é a fonte única. A nota temática e a mensal são vistas dela; a atualização mensal à
Diretora-Geral é o que alimenta a ficha. **Atualiza-se a ficha, não o Word.**

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

## A linha que não pode ficar em branco

Na nota de 28.08.2026 a linha **«Pontos sensíveis / Linha defensiva» foi entregue vazia**. É a linha
que o Senhor Ministro mais precisa de levar para uma audição: é a única que lhe diz o que vão
perguntar e o que responder. O gerador **recusa gerar** com esse campo vazio, e a recusa diz porquê.

Escrevê-la bem: cada entrada é **um par** — a objeção previsível, e a resposta. Começar pela objeção,
em frase curta, e a seguir «Linha defensiva:». Não escrever a objeção sem resposta, nem resposta a
objeção que ninguém faria.

## Regras de escrita

1. **PT-PT**, registo de administração pública, frases curtas. Sem negritos, itálicos ou cores no
   corpo — o modelo não os usa.
2. **Designações fixas.** `Regime Geral do Animal de Companhia (RGAC)`, nunca «Regulamento Geral» nem
   «Regime Geral dos Animais de Companhia». `Regulamento (UE) 2026/1818`, nunca «Regulamento
   2026/1818». `bem-estar` em minúscula e com hífen, salvo nos nomes próprios da lista
   `EXCECOES_DESIGNACAO` — é o caso de «Regime Geral do Bem-Estar dos Animais de Companhia», nome da
   proposta de 2024 e 2025. O gerador verifica isto e recusa.
3. **Nenhuma frase truncada.** A nota de agosto terminava um parágrafo em «que foi publicado dia». O
   gerador deteta parágrafos sem pontuação final e datas em falta.
4. **Datas completas** e verificadas. Nunca «publicado dia» sem o dia.
5. **Nada de inventado.** Números, datas e posições de entidades só entram se estiverem confirmados.
   Se não estiver confirmado, não entra — ou entra dito como por confirmar.
6. **Separar o que é facto do que é posição.** As linhas de enquadramento, contexto e medidas são
   descritivas. A linha defensiva e as mensagens-chave são posição, e é o utilizador que as valida.

## Como trabalhar com o utilizador

- **Não gerar nem enviar sem ordem.** Propor em conversa o que se vai alterar na ficha e só depois
  escrever no `dados_notas.py`.
- A linha dos **pontos sensíveis e a linha defensiva são do utilizador**, não minhas: redigir
  proposta, apresentá-la, e deixá-lo decidir o teor político antes de entrar na ficha.
- Ao fechar: gerar, conferir em PDF, acrescentar a linha ao `registo` da ficha, commit e envio.

## Ficha nova

1. Acrescentar a entrada a `FICHAS` em `dados_notas.py`, com `tema`, `atualizado`, os oito campos e
   `registo`.
2. Gerar com `python3 notas_ministeriais/gerar_nota.py <slug>` e corrigir o que o validador apontar.
3. A ficha passa automaticamente a entrar na nota mensal.

## Fidelidade ao modelo

O formato foi medido no ficheiro do Gabinete de 28.08.2026 e é reproduzido: A4, margens de 3 cm e
4,25 cm em cima, Segoe UI, título a 14 pt negrito, tabela «Table Grid» com grelha fixa de 4,18 cm e
10,82 cm, rótulos em Aptos 12 pt negrito, sombreado D9D9D9 nas quatro linhas do Gabinete e D0CECE nas
quatro da DGAV, corpo a 11 pt justificado. Se o Gabinete mudar o modelo, medir o novo ficheiro antes
de alterar o gerador.
