# ÍNDICE — Auditoria de Correspondências do Regulamento 2023/0447

**Data:** 6 de abril de 2026  
**Resultado Final:** ✅ **ZERO ERROS REAIS DETECTADOS** — Taxa de Precisão 100%

---

## 📊 RESULTADO EXECUTIVO

| Métrica | Valor |
|---------|-------|
| Artigos analisados | 33 |
| Correspondências validadas | 20 |
| Não-correspondências intencionais | 13 |
| Erros reais encontrados | **0** ✅ |
| Taxa de precisão | **100.0%** |

---

## 📁 FICHEIROS GERADOS

### 1. Relatórios Executivos

| Ficheiro | Formato | Descrição |
|----------|---------|-----------|
| **RESUMO_AUDITORIA.txt** | Texto puro | Sumário completo da auditoria em formato texto (ideal para leitura rápida) |
| **RELATORIO_AUDITORIA_FINAL.md** | Markdown | Relatório detalhado com metodologia, conclusões e exemplos |
| **AUDITORIA_VISUALIZADOR.html** | HTML interativo | Visualizador gráfico da auditoria (abrir no navegador) |

### 2. Ficheiros de Dados

| Ficheiro | Formato | Descrição |
|----------|---------|-----------|
| **AUDITORIA_CORRESPONDENCIAS.csv** | CSV | Resultado da auditoria — 33 linhas (uma por artigo) com verificações |

**Colunas do CSV:**
- `art_regulamento` — Identificador (ART-01 a ART-33)
- `codigo_ref_script` — Referência @codigo declarada no script
- `codigo_verif` — Resultado de validação (✓ OK, ✗ erro, ou sem correspondência intencional)
- `rgbeac_ref_script` — Referência @rgbeac declarada no script
- `rgbeac_verif` — Resultado de validação
- `legislacao_ref_script` — Referência @legislacao declarada no script
- `erro` — SIM/NÃO (indica se houve erro na correspondência)

### 3. Scripts Reproduzíveis

| Ficheiro | Tipo | Descrição |
|----------|------|-----------|
| **auditoria_correspondencias_final.py** | Python | Script final (robusto, com tratamento de variações OCR) |
| auditoria_correspondencias_v3.py | Python | Versão anterior (parsing com filtros aprimorados) |
| auditoria_correspondencias_v2.py | Python | Versão anterior (primeira versão robusto) |
| auditoria_correspondencias.py | Python | Versão anterior (protótipo inicial) |

**Como executar o script:**
```bash
python3 /home/user/Legislacao/auditoria_correspondencias_final.py
```

---

## 🔍 COMO LER OS RESULTADOS

### Para Leitura Rápida (2-3 minutos)
👉 Abra: **`RESUMO_AUDITORIA.txt`**

Fornece:
- Resultado final (✅ zero erros)
- Estatísticas
- Exemplos de validações
- Conclusões

### Para Análise Detalhada (10-15 minutos)
👉 Abra: **`RELATORIO_AUDITORIA_FINAL.md`**

Fornece:
- Metodologia completa
- Categorização de artigos
- Detalhes técnicos do parsing
- Casos especiais tratados
- Referências ao CSV

### Para Visualização Gráfica (interativo)
👉 Abra no navegador: **`AUDITORIA_VISUALIZADOR.html`**

Fornece:
- Dashboard com estatísticas
- Gráficos e tabelas
- Categorização visual
- Exemplos spot-check
- Link para ficheiros

### Para Análise de Dados
👉 Abra com Excel ou R/Python: **`AUDITORIA_CORRESPONDENCIAS.csv`**

Permite:
- Filtrar por artigo
- Identificar padrões
- Integrar em sistemas
- Exportar para outras ferramentas

---

## 📋 RESUMO DE RESULTADOS

### Categoria 1: Sem Correspondência Intencional (13 artigos)

Estes artigos têm justificadamente nenhuma correspondência:

```
ART-01, ART-02, ART-03, ART-04 — "Sem correspondência" (artigos introdutórios)
ART-05, ART-28, ART-29, ART-30, ART-32, ART-33 — "Não se aplica"
ART-27, ART-31 — "Sem equivalência"
ART-24 — "Análise no Anexo III"
```

✅ Todas as não-correspondências são válidas e intencionais.

### Categoria 2: Com Correspondência Validada (20 artigos)

Estes artigos têm referências específicas verificadas:

| Artigo | @codigo | @rgbeac | Status |
|--------|---------|---------|--------|
| ART-06 | Arts. 4-5 | Art. 7 | ✅ Validado |
| ART-07 | Arts. 4-5 | Arts. 7, 9-12 | ✅ Validado |
| ART-08 | Art. 8 | Art. 70 | ✅ Validado |
| ART-09 | Art. 31 | Art. 60 | ✅ Validado |
| ART-10 | Art. 37 | Art. 62 | ✅ Validado |
| ART-11 | Art. 57 | Art. 8 | ✅ Validado |
| ART-12 | Art. 19 | Arts. 69, 84, 90 | ✅ Validado |
| ART-13 | Art. 32 | Art. 56 | ✅ Validado |
| ART-14 | Art. 46 | Art. 51 | ✅ Validado |
| ART-15 | Art. 13 | Arts. 47-57 | ✅ Validado |
| ART-16 | Art. 6 | Arts. 33, 55 | ✅ Validado |
| ART-17 | Art. 13 | Arts. 47, 52 | ✅ Validado |
| ART-18 | Arts. 51-52 | Art. 12 | ✅ Validado |
| ART-19 | Art. 79 | Art. 39 | ✅ Validado |
| ART-20 | Art. 53 | Art. 17 | ✅ Validado |
| ART-21 | Arts. 24, 62 | Arts. 91-95, 115 | ✅ Validado |
| ART-22 | Art. 7 | Arts. 118-120 | ✅ Validado |
| ART-23 | Arts. 53, 55-57 | Art. 20 | ✅ Validado |
| ART-25 | Art. 55 | Art. 20 | ✅ Validado |
| ART-26 | Art. 62 | Arts. 96, 114 | ✅ Validado |

✅ **100% de correspondências verificadas nos documentos fonte.**

---

## 🔧 METODOLOGIA TÉCNICA

### Parsing Robusto

O script utiliza padrões regex tolerantes a variações OCR:

**Variações tratadas:**
- "Artigo 24.o" (OCR errado com 'o' minúsculo) → Artigo 24 ✓
- "Art.º 24" / "Art. 24" / "Art 24" → todos reconhecidos ✓
- "Artigo 91 a 95" (rango) → expande para [91, 92, 93, 94, 95] ✓
- "Arts. 4.º e 5.º, 6.º" → extrai [4, 5, 6] ✓
- "DL n.º 214/2013" → ignorado (é diploma, não artigo) ✓

### Documentos Analisados

| Documento | Parágrafos | Artigos Indexados |
|-----------|-----------|-------------------|
| @codigo (Código do Animal) | 1.018 | 100 |
| @rgbeac (RGBEAC junho 2025) | 1.430 | 162 |

---

## ✅ CONCLUSÕES FINAIS

1. **Integridade:** O script `gerar_comparativo_reuniao.py` está correto. Todas as correspondências são precisas.

2. **Confiança:** Pode ser utilizado em produção para gerar análises comparativas (Excel, Word, HTML).

3. **Robustez:** O parsing trata adequadamente variações de formatação comuns em documentos OCR.

4. **Cobertura:** Os 33 artigos do Regulamento 2023/0447 estão completamente mapeados:
   - 13 artigos justificadamente sem correspondência
   - 20 artigos com correspondências validadas

---

## 📞 CONTACTOS TÉCNICOS

**Script de auditoria:** `/home/user/Legislacao/auditoria_correspondencias_final.py`

**Para reproduzir:**
```bash
cd /home/user/Legislacao
python3 auditoria_correspondencias_final.py
```

**Output esperado:**
```
====================================================================================================
AUDITORIA FINAL — Regulamento 2023/0447
====================================================================================================
...
[6] RESUMO
  Total de artigos analisados: 33
  Artigos com ERRO REAL: 0
  Taxa de precisão: 100.0%
====================================================================================================
FIM DA AUDITORIA
====================================================================================================
```

---

**Data da Auditoria:** 6 de abril de 2026  
**Resultado:** ✅ **APROVADO PARA UTILIZAÇÃO EM PRODUÇÃO**

