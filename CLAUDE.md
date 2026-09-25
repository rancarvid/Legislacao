# CLAUDE.md — Análise Comparativa da Legislação sobre Animais

Documento metodológico estruturante do projeto. Referência para produção analítica consistente por assistentes de IA e colaboradores humanos.

---

## 1. Contexto e Objetivo

Este repositório suporta uma **análise comparativa da legislação portuguesa e europeia sobre animais**, com foco em animais de companhia. A análise abrange:

- Legislação portuguesa e europeia vigente
- Duas propostas de nova legislação que compilam e alteram a vigente (`@codigo`, `@rgbeac`)
- O novo Regulamento Europeu de aplicação direta — **Regulamento (UE) 2026/1818** (ex-procedimento 2023/0447) — `@regulamento`
- Um diploma final consolidado que integra os três anteriores — **`@rgac`**

**Objetivo central**: avaliar o impacto da aplicação do Regulamento europeu na legislação nacional e acompanhar a evolução do diploma final `@rgac`, que integra `@codigo`, `@regulamento` e `@rgbeac` numa proposta consolidada única.

---

## 2. Mapeamento de Ficheiros do Repositório

### 2.1 Documentos e Códigos Internos

Cada ficheiro tem um **código interno** para referência rápida em prompts e análises:

| Código Interno | Ficheiro | Descrição |
|---|---|---|
| `@rgac` ⭐ | `RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO - Revisto 30-06-2026 18h00 Grupo.docx` | **Diploma final** — integra `@codigo` + `@regulamento` + `@rgbeac`. Revisão formal DAJA V1 revista pelo grupo, **30.6.2026, 18h00**. Ficheiro canónico mais recente do projeto. Identifica-se pela frase «Privação do direito de titularidade e detenção» (art. 141.º). |
| `@rgac` (arquivo) | `RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO.docx` | Revisão formal DAJA V1, 30.6.2026, antes da revisão do grupo. **Arquivo.** Tem «Mantêm-se transitoriamente em vigor» (n.º 2 do art. 149.º), mas não tem a frase da linha anterior. |
| `@rgac` (arquivo) | `RGAC_Rev. DAJA _V1_06_2026 - Cópia.docx` | Versão DAJA V1 de 29.6.2026, anterior à revisão formal. **Arquivo.** Identifica-se pela nota «ACRESCENTAR os RESTANTES» na norma revogatória. |
| `@codigo` | `Código do Animal DL214.2013_OCR.docx.docx` | Código do Animal — DL n.º 214/2013 (proposta de consolidação original; incorporada em `@rgac`) |
| `@rgbeac` | `RGBEAC_junh_2025 Original com Índice.docx` | Regime Geral do Bem-Estar dos Animais de Companhia (proposta, jun. 2025; incorporada em `@rgac`) |
| `@regulamento` (PT) ⭐ | `Regulamento 2026_01818_PT.pdf` | **Regulamento (UE) 2026/1818 — texto final publicado no JO (PT).** Referência canónica em PT. Idêntico a `Regulamento Versao final pt-pt.pdf`. |
| `@regulamento` (EN) ⭐ | `Regulamento Versao final en-en.pdf` | **Regulation (EU) 2026/1818 — texto final publicado no JO (EN).** Referência canónica em EN e texto autoritativo para citação verbatim. |
| `@regulamento` (arquivo) | `pe00002.en26.GB.RC.AFTERMEETING - alterações aceites.docx` | Versão EN pré-publicação (após reunião, alterações aceites). **Arquivo — não usar como referência primária.** |
| `@regulamento` (arquivo) | `PT Revisão Jurídico-Linguística Sem Track changes até 15 de abril pe00002.pt26.PB.aftermeeting (003)1.docx` | Versão PT pré-publicação (revisão jurídico-linguística, sem track changes, até 15 abril). **Arquivo.** |
| `@regulamento` (arquivo) | `11.12.2025 Regulamento cães e gatos-ocr - sem rasuras.docx` | Versão de trabalho anterior (OCR, dez. 2025). **Arquivo.** |
| `@oexcel` | `oexcel.xlsx` | Ficheiro Excel comparativo por temas |
| `@legislacao` | `Decreto-Lei n.º 276-2001, de 17 de outubro v2.docx` | DL 276/2001 — Proteção dos animais de companhia |
| `@legislacao` | `DL n. 82_2019, de 27 de Junho_ocred.docx` | DL n.º 82/2019 — Bem-estar de animais de companhia |
| `@legislacao` | `Lei n.º 27_2016, de 23 de agosto - Aprova medidas para a criação de uma rede de centros de recolha oficial de animais e estabelece a proibição do abate de animais errantes como forma de controlo da população_ocred.docx` | Lei 27/2016 — Rede de centros de recolha; proibição do abate |
| `@legislacao` | `Portaria 146-2017_ocred.docx` | Portaria n.º 146/2017 |
| `@legislacao` | `Portaria 148_2016 - Estabelece a obrigatoriedade de registo dos cães que integrem matilhas de caça maior, bem como dos respetivos proprietários e matilheiros, prevendo as respetivas regras_ocred.docx` | Portaria n.º 148/2016 — Matilhas de caça maior |
| `@legislacao` | `Portaria n.º 264_2013 - Aprova as normas técnicas de execução regulamentar do Programa Nacional de Luta e Vigilância Epidemiológica da Raiva Animal e Outras Zoonoses_ocred.docx` | Portaria n.º 264/2013 — PNLVERAZ (raiva e zoonoses) |
| `@legislacao` | `DECRET~1.DOC` | Decreto-Lei (legislação vigente adicional) |
| `@legislacao` | `Portaria 148_2016 - (...).docx` | Portaria n.º 148/2016 — Matilhas de caça maior |
| `@legislacao` | `Portaria n.º 264_2013 - (...).docx` | Portaria n.º 264/2013 — PNLVERAZ (raiva e zoonoses) |
| `@legislacao` | `DECRET~1.DOC` | Decreto-Lei n. 74_2007, de 27 de Março - Direito de acesso das pessoas com deficiência acompanhadas de cães de assistência.docx |

> **Regra de classificação**: Tudo o que não for `@rgac`, `@codigo`, `@rgbeac` ou `@regulamento` integra o grupo `@legislacao`.

> **Identidade do `@regulamento` (publicado)**: **Regulamento (UE) 2026/1818 do Parlamento Europeu e do Conselho, de 17 de junho de 2026, relativo ao bem-estar dos cães e dos gatos e à respetiva rastreabilidade** (texto relevante para efeitos do EEE).
> - Publicação: Jornal Oficial da União Europeia, série L, 2026/1818, de **10.8.2026**
> - ELI: <http://data.europa.eu/eli/reg/2026/1818/oj>
> - Feito em Estrasburgo, em 17 de junho de 2026
> - **Entrada em vigor**: vigésimo dia seguinte ao da publicação no JO (art.º 33.º)
> - **Aplicação**: a partir de **31 de agosto de 2028**, com as datas diferidas do art.º 33.º (ver secção 3, alínea c)
> - Estrutura: **7 capítulos, 33 artigos e 3 anexos** (Anexo I — requisitos aplicáveis a todos os estabelecimentos; Anexo II — identificação e registo; Anexo III — dados sobre o bem-estar dos animais)
> - O número **2023/0447** é o número do **procedimento legislativo (COD)**, não do ato publicado. Em produção analítica nova, citar sempre **Regulamento (UE) 2026/1818**; `2023/0447` só é admissível como referência histórica ao processo.

> **Nota de versão — `@rgac`**: O documento `@rgac` é atualizado periodicamente. A versão canónica é sempre o ficheiro cujo nome contém o sufixo **"MAIS ATUAL"**. Versões anteriores são arquivadas com sufixo numérico entre parênteses — e.g., `(1)`, `(2)` — e não devem ser usadas como referência primária. Sempre que o utilizador fizer upload de uma versão nova, o ficheiro "MAIS ATUAL" deve ser considerado a referência vigente de `@rgac`, independentemente da data de revisão inscrita no nome.

### 2.2 Ficheiros de Trabalho Gerados

Scripts e outputs produzidos no âmbito do projeto. Não são documentos legislativos; não têm código interno.

| Ficheiro | Tipo | Descrição |
|---|---|---|
| `gerar_comparativo_reuniao.py` | Script Python | Gera HTML (SPA interativo), Excel e Word artigo a artigo |
| `gerar_word.py` | Script Python | Gera documento Word formatado por artigo |
| `comparativo_reuniao_exemplo.html` | Output gerado | Visualizador SPA interativo (ferramenta de reunião) |
| `comparativo_reuniao_exemplo.xlsx` | Output gerado | Excel de reunião — estrutura artigo a artigo com divergência em 4 sub-colunas |
| `comparativo_reuniao_exemplo.docx` | Output gerado | Word formatado por artigo |
| `cobertura_regulamento.csv` | Output gerado | CSV de rastreamento da cobertura do @regulamento por artigo |
| `reproducao_comparativo.csv` | Output gerado | CSV temático — tema reprodução |
| `reproducao_infografia.html` | Output gerado | HTML infográfico — tema reprodução |

### 2.3 Legislação Ainda Não No Repositório

A legislação relevante que não conste do repositório deve ser consultada online na sua versão mais atual (e.g., via [dre.pt](https://dre.pt) ou [EUR-Lex](https://eur-lex.europa.eu)).

### 2.4 PROTOCOLO DE CONSULTA DE LEGISLAÇÃO (CRÍTICO)

**ORDEM DE PRIORIDADE OBRIGATÓRIA** para análise de legislação:

#### PASSO 1: LEGISLAÇÃO VIGENTE CONSOLIDADA (ONLINE) — PRIORIDADE MÁXIMA
1. **Sempre consultar PRIMEIRO a legislação vigente consolidada** via [dre.pt](https://dre.pt) (Portugal) ou [EUR-Lex](https://eur-lex.europa.eu) (Europa)
2. Usar **WebFetch** ou **WebSearch** para obter versão consolidada + atualizações recentes
3. **Exemplo crítico**: Ao analisar identificação de cães/gatos, procurar PRIMEIRO DL 82/2019 consolidado (não DL 276/2001)
4. **Regra**: Se legislação não está no repositório, procurar online ANTES de usar ficheiros locais

#### PASSO 2: VALIDAÇÃO COM FICHEIROS @LEGISLACAO DO REPOSITÓRIO
1. Comparar resultado online com ficheiros `@legislacao` do repositório (confirmar concordância)
2. Usar ficheiros repositório como **segunda validação**, não como fonte primária
3. **NUNCA confundir**: DL 276/2001 (vigente) com @codigo (proposta)

#### PASSO 3: ANÁLISE DE PROPOSTAS E DIPLOMA FINAL (@CODIGO, @RGBEAC, @RGAC)
1. **APENAS DEPOIS** de analisar legislação vigente, comparar com propostas e diploma final
2. **REGRA CRÍTICA**: `@codigo`, `@rgbeac` e `@rgac` são PROPOSTAS / TRABALHO EM CURSO, NÃO LEGISLAÇÃO VIGENTE
3. Na análise, indicar claramente: "Diploma final @rgac" ≠ "Legislação vigente"
4. **`@rgac` tem precedência analítica** sobre `@codigo` e `@rgbeac` quando se pretende compreender o estado consolidado atual do projeto legislativo

#### REGRA DE DISTINÇÃO ABSOLUTA
| Categoria | Status | Como Tratar |
|-----------|--------|------------|
| **@legislacao** | ✅ VIGENTE | Consultar online consolidado; citar como "legislação vigente" |
| **@codigo** | ❌ PROPOSTA (incorporada em @rgac) | Citar como "proposta de consolidação original"; usar @rgac para texto atual |
| **@rgbeac** | ❌ PROPOSTA (incorporada em @rgac) | Citar como "proposta (jun. 2025)"; usar @rgac para texto atual |
| **@regulamento** | ✅ PUBLICADO / EM VIGOR (aplicação diferida) | Regulamento (UE) 2026/1818, de 17.6.2026 (JO L de 10.8.2026). Aplicação direta, sem transposição. Citar verbatim a partir do texto publicado no JO: EN (`Regulamento Versao final en-en.pdf`) + PT (`Regulamento 2026_01818_PT.pdf`) — a versão PT é autêntica, não é tradução. Atenção: **em vigor ≠ aplicável** — regra geral de aplicação a partir de 31.8.2028, com datas diferidas no art.º 33.º |
| **@rgac** | ⚠️ DIPLOMA FINAL (trabalho em curso) | Citar como "diploma final @rgac"; versão "MAIS ATUAL" é a referência canónica; NUNCA como legislação vigente |

#### ERROS A EVITAR
- ❌ Tratar @codigo (proposta) como legislação que "revoga" DL 276/2001
- ❌ Tratar @rgac como legislação vigente — é o diploma final em desenvolvimento
- ❌ Usar versões arquivadas de @rgac (com numeração em parênteses) em vez do ficheiro "MAIS ATUAL"
- ❌ Omitir legislação vigente (ex: DL 82/2019) que não está no repositório
- ❌ Usar ficheiros repositório como única fonte de legislação
- ❌ Não distinguir claramente entre "vigente" e "proposta/diploma final" na análise
- ❌ Citar o `@regulamento` pelo número de procedimento `2023/0447` em produção analítica nova — o ato publicado é o **Regulamento (UE) 2026/1818**
- ❌ Usar as versões `.docx` pré-publicação do `@regulamento` (pe00002…, 11.12.2025…) como fonte primária — são arquivo; a fonte é o PDF do JO
- ❌ Confundir **entrada em vigor** (20.º dia após a publicação) com **início de aplicação** (31.8.2028, salvo as datas diferidas do art.º 33.º)

---

## 3. Estrutura das Categorias Documentais

### a) Legislação portuguesa e europeia atual — `@legislacao`
Toda a legislação vigente relevante que não seja `@codigo`, `@rgbeac` ou `@regulamento`.

### b) Propostas compiladoras da legislação nacional

- **`@codigo`** — Código do Animal (DL 214/2013): proposta de consolidação do regime jurídico nacional. Incorporada no diploma final `@rgac`.
- **`@rgbeac`** — Regime Geral do Bem-Estar dos Animais de Companhia: segunda proposta de consolidação, versão de junho de 2025. Incorporada no diploma final `@rgac`.

### c) Novo Regulamento Europeu — `@regulamento`

**Regulamento (UE) 2026/1818 do Parlamento Europeu e do Conselho, de 17 de junho de 2026, relativo ao bem-estar dos cães e dos gatos e à respetiva rastreabilidade** (JO L, série L, 2026/1818, de 10.8.2026; ELI: <http://data.europa.eu/eli/reg/2026/1818/oj>). Ato de **aplicação direta** nos Estados-Membros, sem necessidade de transposição. Ponto de referência central para a análise de impacto. Incorporado no diploma final `@rgac`.

Corresponde ao procedimento legislativo **2023/0447 (COD)** — designação que deve ser tratada apenas como referência histórica ao processo, e não como identificação do ato.

**Base jurídica**: artigo 43.º, n.º 2, e artigo 114.º do TFUE.

**Estrutura** — 7 capítulos, 33 artigos, 3 anexos:

| Capítulo | Artigos | Epígrafe |
|---|---|---|
| I | 1.º a 4.º | Objeto, âmbito de aplicação e definições |
| II | 5.º a 19.º | Obrigações dos operadores de estabelecimentos |
| III | 20.º e 21.º | Identificação e registo de cães e gatos e requisitos relativos à publicidade em linha e à colocação no mercado |
| IV | 22.º a 25.º | Autoridades competentes |
| V | 26.º | Entrada de cães e gatos na União |
| VI | 27.º a 29.º | Disposições processuais |
| VII | 30.º a 33.º | Regras nacionais mais restritivas e disposições finais |

| Anexo | Epígrafe |
|---|---|
| I | Requisitos aplicáveis a todos os estabelecimentos nos termos dos artigos 14.º a 17.º |
| II | Identificação e registo de cães e gatos |
| III | Dados sobre o bem-estar dos animais |

**Entrada em vigor e aplicação (art.º 33.º)** — verbatim PT:

> O presente regulamento entra em vigor no vigésimo dia seguinte ao da sua publicação no *Jornal Oficial da União Europeia*.
>
> O presente regulamento é aplicável a partir de 31 de agosto de 2028. No entanto:
>
> a) O artigo 16.º é aplicável a partir de 31 de agosto de 2029;
> b) O artigo 21.º, n.º 3, e o artigo 23.º, n.º 1, são aplicáveis a partir de 31 de agosto de 2030;
> c) O artigo 8.º, n.º 1, é aplicável a partir de 1 de julho de 2036 e o artigo 8.º, n.º 2, é aplicável a partir de 1 de julho de 2030;
> d) O artigo 15.º, o artigo 21.º, n.º 3, segundo parágrafo, o artigo 21.º, n.os 4 e 5, o artigo 22.º, n.º 1, alíneas a), b) e c), o artigo 23.º, n.os 3 e 4, e o artigo 26.º, n.os 1, 2 e 3, são aplicáveis a partir de 31 de agosto de 2031;
> e) O artigo 12.º, n.os 2 e 3, é aplicável a partir de 31 de agosto de 2033;
> f) O artigo 10.º é aplicável a partir de 31 de agosto de 2034; e
> g) O artigo 26.º, n.º 4, é aplicável a partir de 31 de agosto de 2036.

Esta calendarização é determinante para a análise de impacto: o `@rgac` deve ser lido contra as datas em que cada obrigação do Regulamento se torna efetivamente aplicável, e não contra a data de entrada em vigor.

### e) Diploma final consolidado — `@rgac`

**`@rgac`** — `RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO - Revisto 30-06-2026 18h00 Grupo.docx` (revisão formal DAJA V1 revista pelo grupo, 30.6.2026, 18h00)

Diploma final que integra `@codigo` + `@regulamento` + `@rgbeac` numa proposta consolidada única. É o documento de trabalho mais avançado do projeto e o ponto de chegada da análise comparativa. Ficam como arquivo as versões anteriores: `RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO.docx` (30.6.2026, antes da revisão do grupo), `RGAC_Rev. DAJA _V1_06_2026 - Cópia.docx` (29.6.2026) e `Código do Animal DL214.2013_OCR com índice automático - rev 16mar26 MAIS ATUAL.docx` (março 2026, apesar do sufixo).

**Convenção de versão**: O ficheiro canónico é sempre o que contém o sufixo **"MAIS ATUAL"** no nome. Versões anteriores são arquivadas com sufixo numérico — e.g., `(1)`, `(2)`. O utilizador pode fazer upload de versões mais recentes; o ficheiro "MAIS ATUAL" será sempre substituído pelo mais recente. Nunca usar versões arquivadas como referência primária.

### d) Ficheiros Excel comparativos — `@oexcel` e ferramenta de reunião

**`@oexcel` — `oexcel.xlsx`**: comparação temática por assunto entre DL 276/2001, `@codigo`, `@rgbeac` e `@regulamento`. Organizado por temas e sub-temas, com uma coluna por diploma. É o instrumento de referência para análise temática transversal.

**`comparativo_reuniao_exemplo.xlsx`** (ver secção 12): ferramenta distinta, organizada artigo a artigo do `@regulamento`, com estrutura de colunas diferente — inclui texto verbatim por diploma e divergência estruturada em 4 sub-colunas. Gerada automaticamente pelos scripts. Não usa o código `@oexcel`.

---

## 4. Objetivos da Análise

A análise deve:

- Salientar diferenças entre regimes jurídicos
- Identificar incompatibilidades ou lacunas normativas
- Procurar harmonização entre o direito nacional e o Regulamento europeu

### 4.1 Eixos Materiais de Harmonização

| Eixo | Descrição |
|---|---|
| Detenção responsável | Reforço dos deveres e responsabilidades dos detentores |
| Reprodução | Limitação da reprodução não planeada |
| Rastreabilidade | Promoção da identificação e registo de animais |
| Animais errantes | Inversão do panorama descontrolado de animais errantes |

---

## 5. Regras Metodológicas

### 5.1 Idioma

- Toda a produção analítica deve ser em **PT-PT**.
- Exceção: citações de legislação europeia (manter em inglês, com tradução incluída).

### 5.2 Citações de Legislação Nacional

- Sempre **verbatim** — proibido alterar palavras, estrutura ou ideia.
- Referenciação obrigatória no formato:

  ```
  al. X), do n.º Y, do art.º Z.º do [Diploma]
  ```

### 5.3 Citações do `@regulamento` (Regulamento (UE) 2026/1818)

Com a publicação do ato no *Jornal Oficial*, **a versão portuguesa deixou de ser uma tradução de trabalho**: é a versão linguística portuguesa autêntica, com o mesmo valor jurídico da versão inglesa. Ambas são texto oficial.

1. Citação verbatim em **inglês**, extraída de `Regulamento Versao final en-en.pdf` (texto publicado no JO).
2. Citação verbatim em **português**, extraída de `Regulamento 2026_01818_PT.pdf` (texto publicado no JO) — **já não se traduz o Regulamento**; transcreve-se a versão PT oficial.
3. **Ordem de apresentação**: EN primeiro, PT-PT segundo.
4. Resultado final: **duas citações** (EN oficial + PT oficial), ambas verbatim e sem supressões.
5. Referenciação: `art.º Z.º, n.º Y, al. X) do Regulamento (UE) 2026/1818`.

### 5.3a Ficheiros de Referência para Tradução (Parecer, Votação, Tradução) — regime transitório

**Estado atual**: esta regra ficou **obsoleta para o articulado do `@regulamento`**. A versão PT autêntica está publicada, pelo que não há tradução a produzir — transcreve-se o texto do JO.

Os ficheiros `@traducao` (parecer, votação, tradução, primeira versão portuguesa) passam a ter três usos, e apenas estes:

1. **Rastreio histórico** — perceber como uma formulação evoluiu entre as versões de trabalho e o texto final publicado.
2. **Apoio terminológico** para textos do projeto que **não** sejam o Regulamento (e.g., redação do `@rgac`), quando um conceito não tenha correspondência direta na legislação nacional.
3. **Verificação de divergências** entre versões de trabalho anteriores e o texto publicado.

**Nunca**: usar `@traducao` como fonte do texto do Regulamento, nem referenciar esses ficheiros como fonte na documentação final.

**Resultado esperado**: todo o texto do Regulamento citado no projeto provém do JO (PT ou EN), com terminologia estável e verificável.

### 5.4 Observações

- Qualquer **dedução, inferência ou opinião** deve constar exclusivamente na coluna "Observações".
- A análise principal deve ser descritiva e comparativa — nunca valorativa.

### 5.5 Formatação das Citações Legais

Regras de formatação que se aplicam tanto à produção analítica como aos scripts geradores:

**Integridade da citação**
- Cada artigo é citado na íntegra. Não se omitem n.ºs ou alíneas por conveniência de espaço.
- Quando um n.º ou alínea está citado por integridade mas não tem correspondência direta com o tema em análise, é marcado com `[dim]` — texto exibido a cinza mas perfeitamente legível.
- O marcador `[dim]` aplica-se **exclusivamente à legislação nacional** (`@legislacao`, `@codigo`, `@rgbeac`, `@rgac`). **Nunca ao `@regulamento`**, que é sempre citado sem supressões, a partir do texto publicado no JO.

**Cabeçalho de artigo**
- Quando uma coluna cita múltiplos artigos do mesmo diploma, cada artigo é precedido de um cabeçalho `Artigo X.º — Título` que funciona como separador visual.

**Numeração antes das alíneas**
- As alíneas nunca aparecem isoladas: são sempre precedidas pelo n.º do parágrafo que as introduz.
- Exemplo correto: `1 — Os operadores devem assegurar que:` seguido de `a)`, `b)`, `c)`.

**Padrões de formatação reconhecidos pelos scripts**

| Padrão | Tipo | Formato |
|---|---|---|
| `1 —` / `1.` | Parágrafo numerado | PT / EN |
| `a)` / `(a)` / `(-a)` | Alínea | PT / EN |
| `(i)` / `(ii)` | Sub-alínea | EN |
| `—` / `–` (início de linha) | Sub-alínea | PT |

---

## 6. Estrutura das Tabelas (Excel / CSV)

Cada linha deve conter os seguintes campos:

| Campo | Descrição |
|---|---|
| Tema | Eixo temático (ex.: detenção, reprodução, rastreabilidade) |
| Subtema | Subdivisão específica do tema |
| Diploma | Diploma de origem (ex.: DL 276/2001, `@regulamento`) |
| Artigo | Referência articulada no formato normalizado |
| Texto citado | Transcrição verbatim do dispositivo legal |
| Div. vs `@legislacao` | Divergência face ao Regulamento — legislação vigente |
| Div. vs `@codigo` | Divergência face ao Regulamento — `@codigo` |
| Div. vs `@rgbeac` | Divergência face ao Regulamento — `@rgbeac` |
| Div. vs `@rgac` | Divergência face ao Regulamento — diploma final `@rgac` |
| Sumário / Proposta | Síntese da divergência e proposta de implementação |
| Necessidade de alteração | Sim / Não |
| Observações | Deduções, inferências ou recomendações |

### Requisitos dos Ficheiros

- Compatíveis com tratamento posterior em **Python** e **HTML**.
- Permitir filtragem por tema, diploma e tipo de norma.
- Manter estrutura uniforme entre diplomas.

---

## 7. Requisitos Analíticos

É essencial:

- Análise aprofundada de todos os documentos do repositório.
- Pesquisa de legislação conexa quando necessário (consulta online).
- Identificação de remissões e referências normativas internas e cruzadas.
- Comparação artigo a artigo, organizada por tema.

---

## 8. Estratégia de Apresentação Gráfica

Além da análise tabular, devem ser previstas formas de apresentação sintética:

- **Poster temático** por eixo (detenção, reprodução, rastreabilidade, errantes)
- **Infografia comparativa** por diploma
- **Matriz artigo-a-artigo**
- **Diagrama de impacto** do Regulamento
- **Sistema de cores** por tipo de alteração

Organização obrigatoriamente **temática** para garantir legibilidade.

---

## 9. Workflow de Desenvolvimento (Git)

### Ramo de trabalho

O desenvolvimento decorre no ramo:

```
claude/claude-md-mm6om6hd0ro2q4cd-HlaxD
```

Nunca fazer push para `master` sem autorização explícita.

### Fluxo de commits

```bash
git checkout claude/claude-md-mm6om6hd0ro2q4cd-HlaxD
# ... editar ficheiros ...
git add <ficheiros específicos>
git commit -m "Descrição clara da alteração"
git push -u origin claude/claude-md-mm6om6hd0ro2q4cd-HlaxD
```

### Convenções de commit

- Mensagens em **PT-PT** ou inglês técnico, descritivas e concisas.
- Nunca usar `git add -A` ou `git add .` sem verificar o estado com `git status` primeiro.
- Não usar `--no-verify` nem `--force-push` para `master`.

---

## 10. Instruções para Assistentes de IA

### 10.1 Antes de qualquer análise — PROTOCOLO OBRIGATÓRIO

1. **PRIMEIRO**: Aplicar **PROTOCOLO DE CONSULTA DE LEGISLAÇÃO** (secção 2.4)
   - Consultar ONLINE legislação vigente consolidada ([dre.pt](https://dre.pt), [EUR-Lex](https://eur-lex.europa.eu))
   - Usar WebFetch/WebSearch para legislação consolidada
   - **NUNCA usar @codigo ou @rgbeac como fonte primária de legislação vigente**

2. **SEGUNDO**: Verificar ficheiros do repositório
   - Verificar quais ficheiros estão presentes
   - Usar como VALIDAÇÃO (não como fonte primária)
   - Identificar o código interno correto (`@rgac`, `@codigo`, `@rgbeac`, `@regulamento`, `@legislacao`, `@oexcel`)
   - Para `@rgac`: usar **sempre** o ficheiro com sufixo "MAIS ATUAL"; ignorar versões arquivadas com número em parênteses
   - Para `@regulamento`: usar **sempre** o texto publicado no JO — `Regulamento 2026_01818_PT.pdf` (PT) e `Regulamento Versao final en-en.pdf` (EN); ignorar as versões `.docx` pré-publicação (arquivo)

3. **TERCEIRO**: Para propostas e diploma final (@codigo, @rgbeac, @rgac)
   - Comparar com legislação vigente
   - Indicar claramente se são "propostas/diploma final" ou "legislação vigente"
   - **`@rgac`** é o diploma final mais avançado — tem precedência sobre `@codigo` e `@rgbeac` quando se pretende o estado atual consolidado
   - **NUNCA confundir** DL 276/2001 (vigente) com @codigo (proposta) nem com @rgac (diploma final)

### 10.2 Ao produzir análises

- **Nunca parafrasear** dispositivos legais — citar sempre verbatim.
- **Nunca misturar** descrição analítica com opiniões — opiniões vão em "Observações".
- **Sempre referenciar** no formato `al. X), do n.º Y, do art.º Z.º`.
- **Sempre produzir em PT-PT**, exceto citações europeias (com tradução imediata).
- Ao citar `@rgac`, indicar sempre: "diploma final @rgac (versão: [data/rev indicada no nome do ficheiro])".
- `@rgac` é documento vivo — ao trabalhar com ele, confirmar que o ficheiro usado é o "MAIS ATUAL" disponível no repositório.
- Ao citar `@regulamento`, identificar o ato pela designação publicada: **Regulamento (UE) 2026/1818**. Nunca `2023/0447`, salvo quando o que se refere é o próprio procedimento legislativo.
- Ao afirmar que uma obrigação do `@regulamento` "já se aplica", confirmar a data no **art.º 33.º** — a regra geral é 31.8.2028 e há obrigações diferidas até 2036.

### 10.3 Ao trabalhar com o Excel (`@oexcel`)

- Manter a estrutura de colunas definida na secção 6.
- Garantir que cada linha corresponde a um único dispositivo legal.
- Não fundir células; manter compatibilidade com pandas/Python.

### 10.4 Pesquisa online

Quando a legislação não estiver no repositório:
- Usar [dre.pt](https://dre.pt) para legislação portuguesa.
- Usar [EUR-Lex](https://eur-lex.europa.eu) para legislação europeia.
- Citar sempre a versão consolidada mais recente.

---

## 11. Finalidade deste Documento

Este ficheiro constitui:

- Documento metodológico estruturante do projeto.
- Referência para produção analítica consistente por humanos e assistentes de IA.
- Base para integração futura em interfaces gráficos e sistemas automatizados.
- Guia para manutenção e expansão do repositório.

---

## 12. Ferramentas de Análise e Scripts

### 12.1 Scripts geradores

| Script | Função |
|---|---|
| `gerar_comparativo_reuniao.py` | Gera três outputs em simultâneo: HTML SPA de reunião, Excel artigo a artigo, Word formatado |
| `gerar_word.py` | Gera documento Word com formatação completa (cabeçalhos, tabelas, cores por diploma) |

Para executar (a partir da raiz do repositório):

```bash
python3 gerar_comparativo_reuniao.py
python3 gerar_word.py
```

### 12.2 Estrutura dos dados (array ARTIGOS)

Cada artigo do `@regulamento` é definido em `gerar_comparativo_reuniao.py` como uma entrada do array `ARTIGOS`, com os seguintes campos:

```
id                        — identificador (ex.: "ART-13")
tema                      — tema de harmonização
regulamento
  ref                     — referência normalizada do artigo (Regulamento (UE) 2026/1818)
  titulo                  — título oficial do artigo em inglês
  texto                   — verbatim EN (texto publicado no JO — Regulamento Versao final en-en.pdf)
  traducao                — verbatim PT (texto publicado no JO — Regulamento 2026_01818_PT.pdf);
                            o nome do campo é histórico, já não contém tradução de trabalho
rgac
  ref                     — referência no diploma final @rgac
  texto                   — verbatim PT (versão "MAIS ATUAL")
rgbeac
  ref                     — referência no diploma
  texto                   — verbatim PT
codigo
  ref                     — referência no diploma
  texto                   — verbatim PT
legislacao
  ref                     — referência no(s) diploma(s)
  texto                   — verbatim PT (pode conter vários artigos com [dim])
divergencia
  legislacao              — divergência face ao @regulamento — legislação vigente
  codigo                  — divergência face ao @regulamento — @codigo
  rgbeac                  — divergência face ao @regulamento — @rgbeac
  rgac                    — divergência face ao @regulamento — diploma final @rgac
  sumario                 — síntese e proposta de implementação
necessidade_alteracao     — "Sim" / "Não"
notas                     — notas de reunião (campo livre)
```

### 12.3 Ferramentas de visualização

| Ferramenta | Descrição |
|---|---|
| `comparativo_reuniao_exemplo.html` | SPA interativo com sidebar de navegação por artigo, pesquisa por palavra-chave com highlight, exportação de notas em CSV |
| `comparativo_reuniao_exemplo.docx` | Documento Word imprimível com tabelas por artigo, cores por diploma, divergência em 4 secções |
| `comparativo_reuniao_exemplo.xlsx` | Excel de reunião — artigo a artigo, 4 sub-colunas de divergência, folha de legenda |
| `reproducao_infografia.html` | HTML infográfico temático — reprodução |

### 12.4 Outputs auxiliares (CSV)

| Ficheiro | Conteúdo |
|---|---|
| `cobertura_regulamento.csv` | Rastreamento da cobertura do `@regulamento` por artigo |
| `reproducao_comparativo.csv` | Análise comparativa — tema reprodução |
