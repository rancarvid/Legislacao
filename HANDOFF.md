# HANDOFF — Análise Comparativa da Legislação sobre Animais
## Documento de briefing para nova instância Claude

> Este documento descreve o estado atual do projeto, as convenções estabelecidas, a arquitetura técnica dos scripts, o que já foi feito e o que ficou por fazer. Lê-lo na íntegra antes de qualquer intervenção.

---

## 1. O que é este projeto

Análise comparativa da legislação portuguesa e europeia sobre animais de companhia. O objetivo central é avaliar o **impacto do Regulamento Europeu 2023/0447** no quadro jurídico nacional, tendo em conta que já existem duas propostas de consolidação legislativa nacionais.

Os quatro diplomas principais em análise:

| Código interno | Diploma |
|---|---|
| `@legislacao` | Toda a legislação vigente (DL 276/2001, DL 82/2019, Lei 27/2016, Portarias) |
| `@codigo` | Código do Animal — DL n.º 214/2013 (proposta de consolidação 1) |
| `@rgbeac` | Regime Geral do Bem-Estar dos Animais de Companhia — jun. 2025 (proposta 2) |
| `@regulamento` | Regulamento Europeu 2023/0447 — cães e gatos (aplicação direta) |

O `@regulamento` é o **polo de referência** — toda a análise parte dele e avalia a conformidade/divergência dos restantes diplomas.

---

## 2. Ficheiros no repositório (branch de trabalho)

Branch atual: `claude/review-recent-tasks-YROKh`

### 2.1 Documentos legislativos

| Ficheiro | Código |
|---|---|
| `Código do Animal DL214.2013_OCR.docx.docx` | `@codigo` |
| `RGBEAC_junh_2025 Original com Índice.docx` | `@rgbeac` |
| `11.12.2025 Regulamento cães e gatos-ocr - sem rasuras.docx` | `@regulamento` (EN original) |
| `11.12.2025 Regulamento cães e gatos - votação com tradução-ocr.docx` | Tradução PT do `@regulamento` |
| `Regulamento - Primeira Versão portuguesa.docx` | Primeira versão PT do `@regulamento` (auxiliar) |
| `Parecer - European Economic and Social Committee - Opinion - PT-PT.docx` | Parecer EESC em PT |
| `Decreto-Lei n.º 276-2001, de 17 de outubro v2.docx` | `@legislacao` |
| `DL n. 82_2019, de 27 de Junho_ocred.docx` | `@legislacao` |
| `Lei n.º 27_2016, de 23 de agosto (...)` | `@legislacao` |
| `Portaria 146-2017_ocred.docx` | `@legislacao` |
| `Portaria 148_2016 (...)` | `@legislacao` |
| `Portaria n.º 264_2013 (...)` | `@legislacao` |
| `DECRET~1.DOC` | `@legislacao` |
| `oexcel.xlsx` | `@oexcel` — comparativo temático de referência |

Pasta `@opiniao/`: 52 opiniões externas de organizações (PDF) organizadas em 7 grupos temáticos. Ver análise integrada em `ad86f36`.

### 2.2 Scripts (não são documentos legislativos)

| Ficheiro | Função |
|---|---|
| `gerar_comparativo_reuniao.py` | Script principal — gera HTML SPA, Excel e Word em simultâneo |
| `gerar_word.py` | Gerador Word standalone (formatação completa) |

### 2.3 Outputs gerados (não editar à mão)

| Ficheiro | Tipo |
|---|---|
| `comparativo_reuniao_exemplo.html` | SPA interativo — ferramenta de reunião |
| `comparativo_reuniao_exemplo.xlsx` | Excel artigo a artigo |
| `comparativo_reuniao_exemplo.docx` | Word formatado por artigo |
| `cobertura_regulamento.csv` | Rastreamento da cobertura do @regulamento |
| `reproducao_comparativo.csv` | CSV temático — reprodução |
| `reproducao_infografia.html` | HTML infográfico — reprodução |

### 2.4 Documentos de trabalho produzidos

| Ficheiro | Descrição |
|---|---|
| `FICHA_RESPOSTA_AR_Regulamento_2023_0447.docx` | Ficha de resposta a inquirição parlamentar (Word, sem ícones) |
| `legislacao_vigente_animais_completa.xlsx` | 19 diplomas vigentes em estrutura Excel filtrávelg |
| `legislacao_vigente_animais_2026.csv` | Mesmos dados em CSV |
| `artigos_15a_17a_20_correspondencias.md` | Correspondências para ART-15a, 17a–20 |
| `artigos_17a_20_correspondencias.md` | Correspondências para ART-17a–20 |
| `artigos_20a_21_22_correspondencias.md` | Correspondências para ART-20a, 21, 22 |

---

## 3. Estado atual dos artigos — array ARTIGOS

O script `gerar_comparativo_reuniao.py` contém um array `ARTIGOS` com **21 entradas**, cobrindo os artigos 5.º a 22.º do Regulamento 2023/0447:

| ID | Tema |
|---|---|
| `ART-05` | Princípios Gerais de Bem-Estar |
| `ART-06` | Bem-Estar e Detenção |
| `ART-06a` | Estratégias de Criação — Conformação e Consanguinidade |
| `ART-07` | Reprodução e Criação |
| `ART-08` | Detenção Responsável |
| `ART-09` | Competências de Cuidadores |
| `ART-10` | Avaliação e Supervisão de Bem-Estar |
| `ART-11` | Alimentação e Hidratação |
| `ART-12` | Alojamento |
| `ART-13` | Saúde e Monitorização Sanitária |
| `ART-14` | Necessidades Comportamentais |
| `ART-15` | Práticas Dolorosas |
| `ART-15a` | Espetáculos e Competições Estéticas |
| `ART-17` | Identificação e Registo |
| `ART-17a` | Requisitos de Publicidade em Linha |
| `ART-18` | Treino de Cuidadores |
| `ART-19` | Base de Dados de Cães e Gatos |
| `ART-20` | Recolha de Dados sobre Bem-Estar |
| `ART-20a` | Proteção de Dados |
| `ART-21` | Entrada de Cães e Gatos na União |
| `ART-22` | Alteração dos Anexos |

Artigos ainda **não cobertos**: 1–4, 16, 23–28 (preâmbulo, disposições gerais, transitórias e finais).

---

## 4. Estrutura de cada entrada do array ARTIGOS

```python
{
    "id": "ART-13",
    "tema": "Saúde e Monitorização Sanitária",
    "regulamento": {
        "ref": "Art.º 13.º do Regulamento 2023/0447 (PE/Conselho)",
        "titulo": "Health",           # Título inglês — aparece no cabeçalho da card EN
        "texto": "...",               # Verbatim EN — NUNCA tem [dim], NUNCA é truncado
        "traducao": "...",            # PT-PT — baseada nos ficheiros de tradução do repositório
    },
    "rgbeac":    { "ref": "...", "texto": "..." },
    "codigo":    { "ref": "...", "texto": "..." },
    "legislacao":{ "ref": "...", "texto": "..." },  # pode ter [dim] — ver secção 5
    "divergencia": {
        "legislacao": "Divergência face ao @regulamento — legislação vigente",
        "codigo":     "Divergência face ao @regulamento — @codigo",
        "rgbeac":     "Divergência face ao @regulamento — @rgbeac",
        "sumario":    "Síntese e proposta de implementação",
    },
    "necessidade_alteracao": "Sim",   # ou "Não"
    "notas": "",                      # campo livre para notas de reunião
}
```

**Regras absolutas:**
- `regulamento.texto` — sempre verbatim EN, sem cortes, sem `[dim]`
- `regulamento.traducao` — sempre verbatim PT-PT, sem cortes, sem `[dim]`
- `[dim]` aplica-se **apenas** a `legislacao.texto`, `codigo.texto`, `rgbeac.texto`

---

## 5. Convenção [dim] — texto cinzento

Quando um n.º ou alínea de um artigo nacional não tem relação com o tema em análise, o bloco pode ser marcado com `[dim]`. O texto aparece a cinzento mas completamente legível — nunca é apagado.

```python
"texto": """1 — Os detentores devem assegurar que:

a) O animal dispõe de alimentação adequada.

b) O animal tem acesso a água potável.

[dim]2 — O presente decreto-lei não se aplica a animais de produção."""
```

- O `[dim]` é prefixo do bloco inteiro (n.º com todas as suas alíneas)
- Nunca se usa `[dim]` a meio de um bloco
- Nunca se usa `[dim]` no `@regulamento`
- A regra geral é citar o artigo todo — o `[dim]` é a exceção

---

## 6. Convenção de formatação do texto nas colunas

### 6.1 Blocos e linhas

```
Bloco A\n\nBloco B\n\nBloco C
```

Cada bloco é um parágrafo separado (n.º do artigo). Dentro de um bloco, `\n` separa linhas (alíneas, sub-alíneas).

### 6.2 Múltiplos artigos numa coluna

```python
"texto": """Artigo 13.º — Saúde

1 — Os animais devem receber cuidados veterinários.

a) Vacinação obrigatória.

Artigo 16.º — Identificação

1 — Todos os cães devem ser identificados.

a) Microchip obrigatório."""
```

### 6.3 Regra das alíneas

As alíneas **nunca aparecem sozinhas** — são sempre precedidas pelo n.º que as introduz.

### 6.4 Padrões reconhecidos (PT e EN)

| Padrão | Tipo |
|---|---|
| `1 —` ou `1.` | Parágrafo numerado (PT ou EN) |
| `a)` ou `(a)` | Alínea |
| `(i)` `(ii)` | Sub-alínea EN |
| `—` ou `–` no início da linha | Sub-alínea PT |
| `Artigo X.º` | Cabeçalho de artigo (separador visual) |

---

## 7. Ordem de apresentação no HTML e Word

### Na coluna `@regulamento`:
1. **Card EN** (primário, autoritativo) — com título inglês no cabeçalho
2. **Card PT-PT** (tradução, apoio de leitura) — a seguir

O inglês é sempre mostrado primeiro.

### Nas colunas `@rgbeac`, `@codigo`, `@legislacao`:
- Texto verbatim PT, sem ordem especial

---

## 8. Como extrair texto dos ficheiros DOCX

```python
import docx
from lxml import etree

doc = docx.Document("ficheiro.docx")
body = doc.element.body
text = etree.tostring(body, method='text', encoding='unicode')
```

Depois usa `re.finditer(r'Artigo (\d+)\.º', text)` para localizar artigos por posição.

---

## 9. Como correr os scripts

```bash
python3 gerar_comparativo_reuniao.py
# → gera comparativo_reuniao_exemplo.html + .xlsx + .docx

python3 gerar_word.py
# → gera apenas o Word
```

Dependências:
```bash
pip install python-docx openpyxl
```

---

## 10. Workflow Git

Branch de trabalho: `claude/review-recent-tasks-YROKh`

```bash
git status
git add <ficheiros específicos>
git commit -m "Descrição em PT-PT"
git push -u origin claude/review-recent-tasks-YROKh
```

**Nunca:**
- `git add -A` ou `git add .` sem verificar `git status` primeiro
- Push para `master` sem autorização explícita
- `--no-verify` ou `--force-push` para `master`

---

## 11. O que ficou por fazer

### 11.1 Artigos do Regulamento ainda não cobertos

- **Art. 1.º–4.º**: Âmbito, definições, autoridades competentes
- **Art. 16.º**: (em falta na sequência — verificar se existe no Regulamento)
- **Art. 23.º–28.º**: Disposições transitórias, finais, entrada em vigor

Para cada novo artigo:
1. Extrair texto EN verbatim do ficheiro `sem rasuras`
2. Extrair tradução PT do ficheiro `votação com tradução-ocr`
3. Localizar correspondências em `@legislacao`, `@codigo`, `@rgbeac`
4. Preencher campos `divergencia` (4 sub-campos)
5. Determinar `necessidade_alteracao`

### 11.2 Revisão de traduções

Os campos `regulamento.traducao` dos 21 artigos existentes **não foram revistos sistematicamente** com base nos três ficheiros de tradução disponíveis:

- `11.12.2025 Regulamento cães e gatos - votação com tradução-ocr.docx` ← fonte principal
- `Regulamento - Primeira Versão portuguesa.docx` ← fonte auxiliar
- `Parecer - European Economic and Social Committee - Opinion - PT-PT.docx` ← contexto

### 11.3 Recomendações legislativas por tema

Consolidar as divergências identificadas em recomendações concretas por eixo temático:
- Detenção responsável
- Reprodução
- Rastreabilidade
- Animais errantes

### 11.4 Infografias temáticas

Desenvolver infografias adicionais para além da existente (`reproducao_infografia.html`).

---

## 12. Regras analíticas críticas (nunca esquecer)

| Regra | Detalhe |
|---|---|
| Idioma | Produção analítica sempre em PT-PT |
| Citações nacionais | Sempre verbatim — nunca parafrasear |
| Citações europeias | EN verbatim primeiro + tradução PT-PT a seguir |
| Formato de referência | `al. X), do n.º Y, do art.º Z.º do [Diploma]` |
| Opiniões | Só na coluna "Observações" / campo `notas` |
| `[dim]` | Nunca no `@regulamento`; com parcimónia no resto |
| `@regulamento` | Sempre citado na íntegra — sem cortes |
| `@codigo` e `@rgbeac` | São PROPOSTAS — nunca citar como legislação vigente |

---

## 13. Como o HTML SPA funciona

O `comparativo_reuniao_exemplo.html` é um ficheiro HTML/JS autónomo (sem servidor):

- **Sidebar esquerda**: lista de artigos para navegação
- **Pesquisa**: campo de texto com highlight — pesquisa no texto, título e tema
- **Cards por artigo**: EN primeiro, PT depois, depois `@rgbeac`, `@codigo`, `@legislacao`
- **Divergência**: 4 secções (legislacao / codigo / rgbeac / sumario)
- **Campo de notas**: editável em reunião, exportável para CSV

O HTML é gerado pelo script — nunca editar o `.html` diretamente.

---

## 14. Onde está a lógica de renderização

### No HTML (dentro do script Python como f-string):

- `formatarTexto(str)` — converte string com `\n\n` em HTML com classes CSS
- `render(art)` — renderiza um artigo completo
- `artMatch(art, q)` — pesquisa por palavra-chave

Atenção: o HTML é gerado por uma f-string Python. Chaves JS devem ser escapadas como `{{` e `}}`.

### No Word (`gerar_word.py`):

- `_classify_line(line)` — devolve `"art-header"`, `"sub"`, `"alinea"`, ou `"normal"`
- `cell_body(cell, text, ...)` — preenche célula de tabela com texto formatado
- `add_article_section(doc, art)` — adiciona secção completa por artigo

---

## 15. Ficheiro CLAUDE.md

O `CLAUDE.md` é o documento metodológico oficial do projeto. Antes de qualquer trabalho analítico, ler o `CLAUDE.md` — define as convenções que este HANDOFF complementa com detalhe técnico.

Se detetares incoerências entre `CLAUDE.md` e `HANDOFF.md`, o `CLAUDE.md` prevalece — reportar ao utilizador para que ambos sejam alinhados.

---

*Atualizado em 2026-04-04. Estado do repositório: 21 artigos completos (ART-05 a ART-22), outputs gerados e commitados, ficha parlamentar produzida, investigação legislativa (19 diplomas) concluída.*
