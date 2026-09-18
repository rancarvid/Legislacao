# Ponto de Situação — Projeto Análise Comparativa Regulamento (UE) 2026/1818

**Data**: 10 de abril de 2026  
**Ramo Git**: `claude/review-recent-tasks-YROKh`  
**Estado**: ⚠️ Em Progresso — Aguardando Confirmação para Proceder

---

## ⚖️ Texto final do `@regulamento` publicado no Jornal Oficial

**Regulamento (UE) 2026/1818 do Parlamento Europeu e do Conselho, de 17 de junho de 2026, relativo ao bem-estar dos cães e dos gatos e à respetiva rastreabilidade**

| | |
|---|---|
| Publicação | JO da União Europeia, série L, 2026/1818, de **10.8.2026** |
| ELI | <http://data.europa.eu/eli/reg/2026/1818/oj> |
| Assinatura | Estrasburgo, 17 de junho de 2026 |
| Base jurídica | art.º 43.º, n.º 2, e art.º 114.º do TFUE |
| Estrutura | 7 capítulos, 33 artigos, 3 anexos |
| Entrada em vigor | 20.º dia seguinte ao da publicação no JO (art.º 33.º) |
| Início de aplicação | **31 de agosto de 2028**, com datas diferidas no art.º 33.º (art.º 16.º: 2029; art.º 21.º, n.º 3 e art.º 23.º, n.º 1: 2030; art.º 8.º, n.º 2: 1.7.2030; art.º 15.º e outros: 2031; art.º 12.º, n.os 2 e 3: 2033; art.º 10.º: 2034; art.º 8.º, n.º 1: 1.7.2036; art.º 26.º, n.º 4: 2036) |

**Ficheiros canónicos no repositório**

| Ficheiro | Versão linguística |
|---|---|
| `Regulamento 2026_01818_PT.pdf` | PT — texto publicado no JO |
| `Regulamento Versao final en-en.pdf` | EN — texto publicado no JO |

O número **2023/0447** identifica o **procedimento legislativo (COD)**, não o ato publicado. Os ficheiros `.docx` anteriores (`pe00002.*`, `11.12.2025 Regulamento…`) são **arquivo** e não devem ser usados como fonte primária.


---

## 1. CONTEXTO GERAL DO PROJETO

**Objetivo Principal**: Análise comparativa da Legislação sobre Animais de Companhia (cães e gatos) em Portugal e UE, com foco na implementação do Regulamento (UE) 2026/1818 (Dogs and Cats Welfare Regulation).

**Documentos Principais**:
- `@regulamento`: Regulamento (UE) 2026/1818 — texto publicado no JO (ficheiros: `Regulamento 2026_01818_PT.pdf` (PT) + `Regulamento Versao final en-en.pdf` (EN)). Os ficheiros `pe00002.*.docx` passaram a arquivo (versões pré-publicação).
- `@legislacao`: Legislação portuguesa vigente (DL 276-2001, DL 82/2019, etc.)
- `@codigo`: Código do Animal (DL 214/2013) — proposta de consolidação
- `@rgbeac`: Regime Geral Bem-Estar Animais de Companhia (proposta jun. 2025)

---

## 2. OUTPUTS GERADOS

### 2.1 Três Ficheiros Principais
| Ficheiro | Tipo | Descrição | Status |
|----------|------|-----------|--------|
| `comparativo_reuniao_exemplo.html` | SPA Interativo | Visualizador artigo-a-artigo + pesquisa | ⚠️ Desatualizado (Anexo I) |
| `comparativo_reuniao_exemplo.docx` | Word | Tabelas por artigo, cores por diploma | ⚠️ Desatualizado (Anexo I) |
| `comparativo_reuniao_exemplo.xlsx` | Excel | Estrutura artigo-a-artigo + preamble | ⚠️ Desatualizado (Anexo I) |

### 2.2 Ficheiros Auxiliares
| Ficheiro | Descrição | Status |
|----------|-----------|--------|
| `gerar_comparativo_reuniao.py` | Script gerador dos 3 outputs | ⚠️ Dados Anexo I errados |
| `gerar_word.py` | Script Word com formatação | ✅ OK |
| `comparativo_reuniao_exemplo_old_09042026.html` | Backup HTML anterior | ✅ Arquivo |
| Tabelas temáticas (13) | Excel por temas (art. 1-21) | ⚠️ Parcialmente atualizadas |
| `Art.5 - Isenções das obrigações.xlsx` | Matriz isenções por categoria | ❌ Verificação abandonada |

---

## 3. PROGRESSO ANTERIOR À PRESENTE SESSÃO

### ✅ Tarefas Completadas (Commits anteriores)

1. **Renomeação de HTML** (commit `6485f15`)
   - `comparativo_reuniao_exemplo.html` → `comparativo_reuniao_exemplo_old_09042026.html` (backup)
   - `comparativo_reuniao_exemplo_preamb_teste_v2.html` → `comparativo_reuniao_exemplo.html` (novo principal)
   - Inclui Preâmbulo (91 CONSIDERANDOS em 35 temas)

2. **Atualização de Tabelas Temáticas** (commit `04e42b7`)
   - `tabela_art6_art7_comparativo.docx`: 3 atualizações em Article 7
   - `tabela_art21_comparativo.docx`: 1 atualização (row 7)
   - Método: Comparação SequenceMatcher com textos regulamento vs. propostas

3. **Adição de Preâmbulo ao DOCX**
   - Tabela com 91 CONSIDERANDOS + 35 temas
   - Merge de row de sumário em 3 colunas (`gridSpan=3`)
   - Formatação com cabeçalhos, alternância de cores

4. **Adição de Preâmbulo ao XLSX**
   - Folha "Preâmbulo" como primeira (com pré-paginação)
   - 91 CONSIDERANDOS: número, tema, texto EN/PT
   - Formatação: header escuro, linhas alternadas, borders, freeze B2

5. **Correções de Erros Menores**
   - Revert de "Art.5" que foi atualizado incorretamente (commit `a4035b5`)
   - Git rm de ficheiro HTML deletado após rename (commit `6485f15`)

### ⚠️ Tarefas Interrompidas

- **Verificação de "Art.5 - Isenções das obrigações.xlsx"**: Tentativa de validar matriz de isenções vs. regulamento → Abandonada após feedback "vem tudo errado"

---

## 4. PROBLEMA IDENTIFICADO — ANNEXO I DESATUALIZADO

### 4.1 Constatação

Os 3 outputs (HTML, DOCX, XLSX) contêm **dados desatualizados do Anexo I** (Requisitos Técnicos para Estabelecimentos):

- **ANNEX-I-NUMERO-1**: Alimentação/Feeding
- **ANNEX-I-NUMERO-2**: Alojamento/Housing
- **ANNEX-I-NUMERO-3**: Saúde/Health
- **ANNEX-I-NUMERO-4**: Necessidades Comportamentais/Behavioural needs

**Causa-raiz**: Dados hardcoded em `gerar_comparativo_reuniao.py` (linhas ~1016-1134) não foram atualizados com a versão final do regulamento.

### 4.2 Fontes Confirmadas

| Documento | Conteúdo | Localização |
|-----------|----------|-------------|
| `pe00002.en26.GB.RC.AFTERMEETING - alterações aceites.docx` *(arquivo)* | Annexo I EN (correto) | Parágrafos 520-567 |
| `Regulamento Versao final en-en.pdf` **(fonte atual)** | Anexo I EN — texto publicado no JO | Pág. 45-47 |
| `pe00002.pt26.PB.aftermeeting 2.docx` *(arquivo)* | Anexo I PT (correto) | Parágrafos 514-560 |
| `Regulamento 2026_01818_PT.pdf` **(fonte atual)** | Anexo I PT — texto publicado no JO | Pág. 45-47 |
| `/tmp/texts_pt_clean.json` | Artigos 1-33 (SEM anexos) | Gerado anteriormente |
| `/tmp/texts_en_clean.json` | Articles 1-33 (SEM annexes) | Gerado anteriormente |

### 4.3 Diferenças Encontradas (Resumo Executivo)

#### **ANNEX-I-NUMERO-1 (Alimentação)**
- **EN**: Título falta "pursuant to Articles 14 to 17"; numeração errada (2.2→1.2, 3.3→1.3, 4.4→1.4)
- **PT**: Título falta completamente; numeração errada; múltiplas variações textuais (progenitora→mãe, sucedâneo→substituto, etc.)

#### **ANNEX-I-NUMERO-2 (Alojamento)**
- **EN**: Iluminação deve ser 3 subitens (2.2.1, 2.2.2, 2.2.3); numeração 2.3.3 não existe
- **PT**: Mesmo; mudanças terminológicas (espectro amplo→largo espetro, Hz→hertz); valores tabela espaços errados
- **Tabela Espaços**: Valores incorretos — <30:4m², 30-39:4m², 40-59:5m², 60-70:8m², >70:10m²

#### **ANNEX-I-NUMERO-3 (Saúde)**
- **EN & PT**: Numeração completamente errada (1.1→3.1, 2.2→3.2, ..., 6.6→3.6); falta 3.7
- **EN**: "Queens" → "Female cats"; "delivered" → "produced"; múltiplas mudanças de redação
- **PT**: "cães de proteção de gado" → "cães de guarda de gado"; "estro" → "cio"; "nascimortos" → "nados-mortos"

#### **ANNEX-I-NUMERO-4 (Necessidades Comportamentais)**
- **EN & PT**: Numeração errada (3. → 4.); subitens restruturados (1.1→4.1.1, 2.2→4.2.1, etc.)
- **EN**: "their conspecifics" → "other animals of the same species"; "permit" → "allow"
- **PT**: "Bem-Estar Comportamental" → "4. Necessidades comportamentais"; "postes de arranhadura" → "arranhadores"

**📄 Documento Completo**: Ver `/tmp/DIFEREN CAP_ANEXO_I_COMPLETA.md` (gerado nesta sessão)

---

## 5. ESTADO ATUAL — O QUE FALTA FAZER

### ✅ Pronto para Proceder

1. **Corrigir `gerar_comparativo_reuniao.py`** (linhas 1016-1134)
   - Atualizar ANNEX-I-NUMERO-1 (EN + PT)
   - Atualizar ANNEX-I-NUMERO-2 (EN + PT + tabela)
   - Atualizar ANNEX-I-NUMERO-3 (EN + PT + numeração)
   - Atualizar ANNEX-I-NUMERO-4 (EN + PT + numeração)

2. **Regenerar 3 Outputs**
   ```bash
   python3 gerar_comparativo_reuniao.py
   ```
   - `comparativo_reuniao_exemplo.html` ← HTML SPA atualizado
   - `comparativo_reuniao_exemplo.docx` ← Word atualizado
   - `comparativo_reuniao_exemplo.xlsx` ← Excel atualizado

3. **Commit + Push**
   ```bash
   git add gerar_comparativo_reuniao.py comparativo_reuniao_exemplo.*
   git commit -m "Atualizar Anexo I com dados corretos do Regulamento (UE) 2026/1818"
   git push -u origin claude/review-recent-tasks-YROKh
   ```

### ⏳ Aguardando Confirmação do Utilizador

**Questão**: Proceder com as correções de Anexo I acima descritas?

---

## 6. REGRAS APLICADAS DURANTE O TRABALHO

Conforme definido em CLAUDE.md e feedback anterior:

| Regra | Status |
|-------|--------|
| ✅ Ignorar `▌` (marcas de edição Word) | Aplicada |
| ✅ Não alterar PT versões/correspondências/sequências | Aplicada |
| ✅ Apenas atualizar verbatim onde há diferenças reais | Aplicada |
| ✅ Pedir confirmação antes de alterações | Aplicada |
| ✅ Usar ramo `claude/review-recent-tasks-YROKh` | Aplicada |
| ✅ Commits com mensagens PT/EN descritivas | Aplicada |
| ✅ Não fazer push para master sem autorização | Aplicada |

---

## 7. ESTRUTURA DO REPOSITÓRIO (Ficheiros-Chave)

```
/home/user/Legislacao/
├── gerar_comparativo_reuniao.py          ← GERADOR principal (a corrigir)
├── gerar_word.py                         ← Gerador Word (OK)
├── comparativo_reuniao_exemplo.html      ← OUTPUT HTML (desatualizado)
├── comparativo_reuniao_exemplo.docx      ← OUTPUT Word (desatualizado)
├── comparativo_reuniao_exemplo.xlsx      ← OUTPUT Excel (desatualizado)
├── comparativo_reuniao_exemplo_old_09042026.html  ← Backup anterior
├── Regulamento Versao final en-en.pdf           ← Fonte EN (JO, atual)
├── Regulamento 2026_01818_PT.pdf                ← Fonte PT (JO, atual)
├── pe00002.en26.GB.RC.AFTERMEETING - alterações aceites.docx  ← arquivo (pré-publicação EN)
├── pe00002.pt26.PB.aftermeeting 2.docx          ← arquivo (pré-publicação PT)
├── Tabelas temáticas/                   ← 13 ficheiros Excel por tema
│   ├── tabela_art6_art7_comparativo.docx
│   ├── tabela_art21_comparativo.docx
│   └── ...
├── Art.5 - Isenções das obrigações.xlsx ← Verificação abandonada
├── CLAUDE.md                             ← Instruções metodológicas
└── .git/                                 ← Ramo: claude/review-recent-tasks-YROKh
```

---

## 8. PRÓXIMAS SESSÕES (Roadmap)

Após correção Anexo I:

1. **Verificação Preamble**: Confirmar se 91 CONSIDERANDOS estão corretos vs. nova versão regulamento
2. **Verificação Artigos 1-33**: Spot-check de alguns artigos para confirmar no/relação com Anexo I
3. **Tabelas Temáticas**: Completar atualização das 13 tabelas (atualmente apenas 2 foram revisadas)
4. **Revisão Final**: Leitura em diagonal dos 3 outputs para identificar lacunas óbvias
5. **PR/Merge**: Criar pull request para `master` (após aprovação do utilizador)

---

## 9. PONTOS DE CONTACTO COM UTILIZADOR

- **Questão Principal Pendente**: Confirmar proceder com correção Anexo I?
- **Feedback esperado**: Validação das diferenças identificadas
- **Próximos passos**: Após proceder, regenerar outputs e comunicar resultado

---

**Última Atualização**: 10 de abril de 2026, 14:00 UTC  
**Próxima Ação**: Aguardar confirmação para proceder com correções de Anexo I
