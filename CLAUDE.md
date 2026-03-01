# CLAUDE.md — Análise Comparativa da Legislação sobre Animais

Documento metodológico estruturante do projeto. Referência para produção analítica consistente por assistentes de IA e colaboradores humanos.

---

## 1. Contexto e Objetivo

Este repositório suporta uma **análise comparativa da legislação portuguesa e europeia sobre animais**, com foco em animais de companhia. A análise abrange:

- Legislação portuguesa e europeia vigente
- Duas propostas de nova legislação que compilam e alteram a vigente
- Um novo Regulamento Europeu de aplicação direta (2023/0447)

**Objetivo central**: avaliar o impacto da aplicação do Regulamento europeu na legislação nacional, considerando que já existem duas propostas de consolidação e revisão do regime jurídico.

---

## 2. Mapeamento de Ficheiros do Repositório

### 2.1 Documentos e Códigos Internos

Cada ficheiro tem um **código interno** para referência rápida em prompts e análises:

| Código Interno | Ficheiro | Descrição |
|---|---|---|
| `@codigo` | `Código do Animal DL214.2013_OCR.docx.docx` | Código do Animal — DL n.º 214/2013 |
| `@rgbeac` | `RGBEAC_junh_2025 Original com Índice.docx` | Regime Geral do Bem-Estar dos Animais de Companhia (proposta, jun. 2025) |
| `@regulamento` | `11.12.2025 Regulamento cães e gatos-ocr - sem rasuras.docx` | Regulamento Europeu 2023/0447 (cães e gatos) |
| `@oexcel` | `oexcel.xlsx` | Ficheiro Excel comparativo por temas |
| `@legislacao` | `Decreto-Lei n.º 276-2001, de 17 de outubro v2.docx` | DL 276/2001 — Proteção dos animais de companhia |
| `@legislacao` | `DL n. 82_2019, de 27 de Junho_ocred.docx` | DL n.º 82/2019 — Bem-estar de animais de companhia |
| `@legislacao` | `Lei n.º 27_2016, de 23 de agosto - (...).docx` | Lei 27/2016 — Rede de centros de recolha; proibição do abate |
| `@legislacao` | `Portaria 146-2017_ocred.docx` | Portaria n.º 146/2017 |
| `@legislacao` | `Portaria 148_2016 - (...).docx` | Portaria n.º 148/2016 — Matilhas de caça maior |
| `@legislacao` | `Portaria n.º 264_2013 - (...).docx` | Portaria n.º 264/2013 — PNLVERAZ (raiva e zoonoses) |
| `@legislacao` | `DECRET~1.DOC` | Decreto-Lei n. 74_2007, de 27 de Março - Direito de acesso das pessoas com deficiência acompanhadas de cães de assistência.docx |

> **Regra de classificação**: Tudo o que não for `@codigo`, `@rgbeac` ou `@regulamento` integra o grupo `@legislacao`.

### 2.2 Legislação Ainda Não No Repositório

A legislação relevante que não conste do repositório deve ser consultada online na sua versão mais atual (e.g., via [dre.pt](https://dre.pt) ou [EUR-Lex](https://eur-lex.europa.eu)).

---

## 3. Estrutura das Categorias Documentais

### a) Legislação portuguesa e europeia atual — `@legislacao`
Toda a legislação vigente relevante que não seja `@codigo`, `@rgbeac` ou `@regulamento`.

### b) Propostas compiladoras da legislação nacional

- **`@codigo`** — Código do Animal (DL 214/2013): proposta de consolidação do regime jurídico nacional.
- **`@rgbeac`** — Regime Geral do Bem-Estar dos Animais de Companhia: segunda proposta de consolidação, versão de junho de 2025.

### c) Novo Regulamento Europeu — `@regulamento`
Regulamento 2023/0447, de aplicação direta nos Estados-Membros. Ponto de referência central para a análise de impacto.

### d) Ficheiro Excel comparativo — `@oexcel`
Contém colunas comparativas por temas entre: DL 276/2001, `@codigo`, `@rgbeac` e `@regulamento`. O modelo será replicado para os restantes diplomas vigentes.

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
  al. X), do n.º Y, art.º Zº do [Diploma]
  ```

### 5.3 Citações de Legislação do Parlamento Europeu

1. Citação verbatim em **inglês**.
2. Tradução imediatamente a seguir, respeitando a terminologia histórica consolidada.
3. Resultado final: **duas citações** (original + tradução).

### 5.4 Observações

- Qualquer **dedução, inferência ou opinião** deve constar exclusivamente na coluna "Observações".
- A análise principal deve ser descritiva e comparativa — nunca valorativa.

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
| Tipo de norma | obrigação / proibição / definição / sanção / competência / etc. |
| Divergência face ao Regulamento | Descrição objetiva da diferença normativa |
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

### 10.1 Antes de qualquer análise

1. Verificar quais ficheiros estão presentes no repositório.
2. Identificar o código interno correto (`@codigo`, `@rgbeac`, `@regulamento`, `@legislacao`, `@oexcel`).
3. Para legislação em falta, consultar online na versão mais atual.

### 10.2 Ao produzir análises

- **Nunca parafrasear** dispositivos legais — citar sempre verbatim.
- **Nunca misturar** descrição analítica com opiniões — opiniões vão em "Observações".
- **Sempre referenciar** no formato `al. X), do n.º Y, art.º Zº`.
- **Sempre produzir em PT-PT**, exceto citações europeias (com tradução imediata).

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
