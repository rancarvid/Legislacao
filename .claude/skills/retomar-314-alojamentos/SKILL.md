---
name: retomar-314-alojamentos
description: Retomar o estudo jurídico «314 vs alojamentos» — se os limites de detenção por fogo do art.º 3.º do DL n.º 314/2003 (três cães ou quatro gatos, máximo de quatro, seis com parecer vinculativo) fixam a lotação de um alojamento de animais registado ao abrigo do DL n.º 276/2001. Produz e mantém o Word `criador informal/Estudo_Limites_por_Fogo.docx`, gerado a partir de `criador informal/_estudo_fogo.py`. Usar sempre que o utilizador disser «314 vs alojamentos», pedir para retomar essa tarefa ou esse estudo, falar de limites de animais por fogo, da lotação de alojamentos registados, do poder municipal de remoção de animais, do caso de Santo Tirso ou do caso de Amarante, ou carregar transcrições ou gravações de audições parlamentares sobre esses casos.
---

# 314 vs alojamentos

`314 vs alojamentos` é a designação convencionada deste tema, fixada em 25.9.2026 e válida entre sessões.
Sempre que o utilizador usar a expressão, refere-se a esta questão.

**Antes de qualquer coisa, ler `CHECKPOINT-FOGO-vs-ALOJAMENTO-REGISTADO.md` na raiz do repositório.**
É o registo completo: a resposta, os textos verbatim, os argumentos das duas séries, a jurisprudência, a
doutrina, o método e os pontos em aberto. Este ficheiro é apenas o mapa.

## A questão e a resposta

Os limites do n.º 2 do art.º 3.º do DL n.º 314/2003 **não fixam a lotação de um alojamento registado**. A
razão decisiva não é a palavra «alojamento» — é a **unidade de contagem**: o n.º 2 conta por **fogo**, e um
alojamento não é um fogo. Quem quiser atacar a tese deve atacar aí, e não na palavra.

Ressalvas que fazem parte da resposta, e não devem ser omitidas:
- O **n.º 1** (salubridade) aplica-se sempre, incluindo ao alojamento registado. Registar não isenta.
- **Caso residual**: quem tem alojamento registado mas mantém os animais integrados na casa, como animais
  do agregado, continua sujeito ao n.º 2.

## Ficheiros

| Ficheiro | Função |
|---|---|
| `CHECKPOINT-FOGO-vs-ALOJAMENTO-REGISTADO.md` | Registo completo do estado. Ler primeiro. Atualizar ao fechar cada avanço |
| `criador informal/_estudo_fogo.py` | **Conteúdo do estudo.** É aqui que se escreve; o Word é gerado |
| `criador informal/_memo_engine.py` | Helpers de formatação: `capa, h1, h2, h3, para, bullets, numlist, citacao, destaque, nota, enquadramento, tabela, pagebreak` |
| `criador informal/gerar_memorando.py` | Gera o Word. Correr sempre depois de editar |
| `criador informal/Estudo_Limites_por_Fogo.docx` | Resultado. **Nunca editar à mão** — é reescrito a cada geração |
| `criador informal/audições parlamentares/` | Gravações das audições de 30.7.2020 e transcrições |

Gerar e conferir:

```bash
cd "criador informal" && python3 gerar_memorando.py
soffice --headless --convert-to pdf Estudo_Limites_por_Fogo.docx --outdir <scratchpad>
pdftotext -layout <scratchpad>/Estudo_Limites_por_Fogo.pdf - | less
```

`gerar_memorando.py` gera cinco documentos. **Só `Estudo_Limites_por_Fogo.docx` pertence a esta tarefa**;
os outros quatro são de outra e mudam só o carimbo temporal — descartá-los antes do commit:

```bash
git checkout -- "criador informal/Anexo_Delimitacao_DL314_2003.docx" \
  "criador informal/Anexo_Jurisprudencia_Doutrina_DL314.docx" \
  "criador informal/Memorando_Criacao_Pequena_Escala_refs-completas.docx" \
  "criador informal/Memorando_Criacao_Pequena_Escala_refs-leves.docx"
```

## Estrutura do estudo

18 capítulos e três anexos. Os que importa conhecer de cor:

| Onde | Matéria |
|---|---|
| **2** | Conclusões em pontos de um parágrafo — **a primeira página tem de dar o veredicto em 1-2 páginas** |
| **5** | O conceito de «fogo» (questão 4). **Toda a conclusão repousa aqui** |
| **9.2** | O que a resposta entrega e o que não entrega |
| **9.3** | Alcance da norma sancionatória — al. c) do n.º 3 do art.º 14.º |
| **9.5** | Poder de remoção; art.º 3.º-G; caso de Santo Tirso; audição parlamentar; DL n.º 116/98 |
| **11.4** | Doutrina — Bruno Branco, RJLB 2019 |
| **13.4** | Trajetória do título de acesso: câmara (2001-03) → director-geral (2003-12) → MCP (desde 2012) |
| **14.5** | Três actos coordenados no DR n.º 290 de 17.12.2003 — o argumento mais forte |
| **15.7** | Inibição da fiscalização; a alavanca efectiva foi o urbanismo |
| **17** | Questões em aberto e limites |
| **18.2** | Como consultar o DR de forma verificável |
| **Anexo C** | Bibliografia e fontes, com o regime de citação das transcrições (C.6) |

## Regras de escrita (obrigatórias)

1. **PT-PT.** Citações de legislação europeia em EN com a versão PT oficial ao lado.
2. **Citação verbatim, sempre.** Nunca parafrasear um dispositivo legal.
3. **Referência no formato** `al. X), do n.º Y, do art.º Z.º do [Diploma]`.
4. **A citação faz-se contra o PDF do jornal oficial**, nunca contra compilador — e nem contra a
   consolidação oficial, que já se apanhou a errar uma proveniência. Indicar sempre o DR, a data e a página.
5. **Dedução, inferência e opinião vão em «Observação»**, dentro de `nota(...)`. O corpo é descritivo.
6. **Citações de transcrição automática** levam sempre a marca temporal e a identificação como tal. Nunca
   se apresentam como transcrição oficial da Assembleia — que para estas audições não existe.
7. **Nunca tratar `@codigo`, `@rgbeac` ou `@rgac` como legislação vigente.** Este estudo é de direito
   interno vigente e **não** mobiliza o Regulamento (UE) 2026/1818 nem o projeto RGAC.

## Como trabalhar com o utilizador

- **Não escrever no Word sem ordem.** O utilizador pediu expressamente que se pergunte antes de cada
  aditamento. Propor em chat o que se vai acrescentar e onde; escrever depois da aprovação.
- Quando o aditamento é extenso, **mostrar primeiro o texto proposto**, na redação e no registo do
  documento, para ele julgar antes de se mexer no ficheiro.
- Ao fechar um avanço: gerar, conferir em PDF, atualizar o checkpoint, commit e push no ramo de trabalho.

## Estado e pendentes (28.9.2026, revisto às 20h)

Estudo em **63 páginas**. A resposta à questão central está estabelecida; o que continua aberto é de
política legislativa, não de interpretação.

**As três audições estão transcritas.** Os resultados e a triagem de relevância estão na **PARTE 0-B do
checkpoint**. Nada disso foi levado ao Word: o utilizador decidiu que só entra o relevante e a decisão está
por tomar. A terceira gravação não era recorte da segunda — é audição autónoma sobre o relatório de inquérito
da IGAI, de data ainda não estabelecida.

Por ordem de utilidade — o detalhe está na PARTE X-A do checkpoint:

1. **Decidir o que da PARTE 0-B entra no estudo.** Proposta de triagem: entram o facto de o Governo ter
   declarado que os alojamentos nunca tiveram título (B.2) e o de ter citado em 2020 a redação já cessada do
   DL n.º 116/98 (B.3); o resto é corroboração ou contexto.
2. **Caso de Amarante** — mais de 300 cães num alojamento de criadora **registada**. É o teste empírico da
   questão central. **Adiado por decisão do utilizador; não retomar sem ele o pedir.**
3. Acórdão de 9.9.2026 (não obtido; recurso anunciado pelo PAN).
4. Prática decisória da DGAV ao abrigo do art.º 3.º-G.

Duas coisas que o utilizador já decidiu, e que não se devem repropor: **não apresentar requerimentos de
acesso a documentos administrativos**, e **não tratar de Amarante** até indicação em contrário.
