# CHECKPOINT — Análise Cross-References: Regulamento vs. @codigo/@rgbeac/@legislacao

**Data:** 2026-03-18
**Branch:** `claude/update-regulations-document-lKSWW`
**Sessão:** Revisão sistemática de cross-references e textos verbatim

---

## Estado actual do trabalho

### Problema identificado pelo utilizador
O Excel e o HTML não citavam os artigos de @codigo, @rgbeac e @legislacao de forma sistemática — havia referências como "correspondência parcial" sem identificar os artigos concretos, campos de texto vazio, e análises que não iam buscar todos os artigos relevantes dos documentos.

**Exemplo dado pelo utilizador:** Art.º 46.º do @codigo (Alimentação e abeberamento) tem 7 números muito detalhados sobre nutrição, que correspondem directamente ao Art.º 14.º do Regulamento — mas não estava citado correctamente.

---

## O que foi feito nesta sessão

### 1. Extracção sistemática dos documentos
- `@codigo` (Código do Animal DL 214/2013): 99 artigos extraídos → `/tmp/codigo_articles.json`
- `@rgbeac` (RGBEAC jun. 2025): 160 artigos extraídos → `/tmp/rgbeac_articles.json`
- `@legislacao` DL 276/2001: 73 artigos extraídos → `/tmp/dl276_articles.json`

Scripts de extracção em Python estão documentados mas NÃO guardados (usar python-docx).

### 2. Mapeamento sistemático por tópico
Para cada artigo do Regulamento (ART-05 a ART-33), foi feita pesquisa por palavras-chave em todos os documentos para identificar artigos potencialmente relevantes.

### 3. Correcções feitas em `gerar_comparativo_reuniao.py`

| Artigo | Problema | Correcção |
|--------|----------|-----------|
| **ART-06** | Campos `rgbeac`, `codigo`, `legislacao` vazios ("Análise no Art.º 7") | Preenchidos com texto verbatim: @rgbeac Art.º 7, @codigo Arts. 4+5, DL276 Art.º 7 |
| **ART-08** | `divergencia.rgbeac` vazio | Análise do @rgbeac Art.º 70 vs. Regulamento |
| **ART-10** | `divergencia.rgbeac` e `divergencia.codigo` vazios | Análise de Arts. 62 (@rgbeac) e 37 (@codigo) |
| **ART-14** | `divergencia.legislacao` vazio | Análise DL276 Art.º 12 vs. Regulamento |
| **ART-15** | `divergencia.codigo` e `divergencia.legislacao` vazios | Análise @codigo Art.º 13 e DL276 Art.º 8 vs. Regulamento |
| **ART-17** | `@rgbeac.texto` e `@codigo.texto` eram sumários/análises, não verbatim | Substituídos por verbatim: @rgbeac Arts. 47+52n7, @codigo Art.º 13, DL276 Art.º 8 |
| **ART-21** | `divergencia.legislacao` vazio | Análise DL276 Arts. 53+57 e DL82/2019 |
| **ART-23** | `divergencia.legislacao` vazio | Análise DL82/2019 (SIAC) |
| **ART-24** | `divergencia.legislacao` vazio | Análise de ausência de mecanismo de reporte trienal |
| **ART-25** | `divergencia.legislacao` vazio | Análise conformidade SIAC com RGPD |
| **ART-27** | `divergencia.sumario` vazio | Análise de implicações da habilitação delegada |
| **ART-29** | `divergencia.sumario` vazio | Análise procedimento de comité |
| **ART-30** | `divergencia.sumario` vazio | Análise medidas nacionais mais restritivas (proibição venda online) |
| **ART-32** | `divergencia.sumario` vazio | Análise regime sancionatório nacional |

---

## Trabalho ainda por fazer (continuação)

### Prioridade ALTA — Cross-references verbatim em falta

Para os seguintes artigos, os campos de texto têm apenas o artigo "principal" mas há outros artigos relevantes nos diplomas que não foram adicionados:

| ART | Diplomas | Artigos em falta (a verificar) |
|-----|----------|-------------------------------|
| ART-07 | @codigo | Arts. 6.º (cuidados MV), 47.º (maneio), 50.º (coleira/trela) |
| ART-07 | @rgbeac | Arts. 9.º, 10.º, 11.º, 12.º já estão mas verificar completude |
| ART-09 | @codigo, @rgbeac | Verificar artigos de notificação/registo de alojamentos |
| ART-11 | @codigo, @rgbeac | Verificar artigos sobre informação ao detentor/comprador |
| ART-12 | @codigo | Verificar Art.º 47.º n.1 (maneio por pessoal competente) — texto completo |
| ART-13 | Todos | Verificar completude das visitas veterinárias obrigatórias |
| ART-16 | @rgbeac | Verificar Arts. 55.º (cuidados saúde), 56.º (isolamento), 57.º (registos) |
| ART-22 | @rgbeac | Verificar Art.º 118.º (formação MV) completude |
| ART-26 | @rgbeac | Verificar Art.º 114.º completude |

### Prioridade MÉDIA — Divergencia analyses incompletas

- **ART-07**: divergencia.rgbeac menciona famílias de acolhimento mas não analisa os n.ºs 6, 7 e 8 (monitorização baseada em animais)
- **ART-09**: verificar se análise de notificação vs. aprovação está correcta
- **ART-11**: verificar análise de informação ao comprador/detentor
- **ART-16**: verificar análise de saúde e cuidados veterinários

### Prioridade BAIXA — Artigos processuais/institucionais

- ART-28, ART-31, ART-33: já têm análise básica, podem ser melhorados mas não são críticos

---

## Metodologia para continuar

### Ferramentas disponíveis
```python
# Textos dos documentos disponíveis para pesquisa rápida:
with open('/tmp/codigo_articles.json') as f:
    codigo = json.load(f)  # {num: texto_verbatim}
with open('/tmp/rgbeac_articles.json') as f:
    rgbeac = json.load(f)
with open('/tmp/dl276_articles.json') as f:
    dl276 = json.load(f)
```

**Nota:** Estes ficheiros são temporários (`/tmp/`). Em nova sessão, re-extrair com:
```bash
python3 -c "
import zipfile, re, json
# Extrai texto do .docx via XML interno
fname = 'Código do Animal DL214.2013_OCR.docx.docx'
with zipfile.ZipFile(fname, 'r') as z:
    content = z.read('word/document.xml').decode('utf-8')
text = re.sub(r'<[^>]+>', ' ', content)
# ... indexar por artigo ...
"
```

### Abordagem correcta para cada artigo
1. **Ler o artigo do Regulamento** (já está no script)
2. **Pesquisar por palavras-chave** nos JSONs dos diplomas
3. **Identificar 2-5 artigos mais directamente relevantes** (não todos)
4. **Copiar texto verbatim** (sem parafrasear)
5. **Usar [dim]...[/dim]** para parágrafos do mesmo artigo não directamente relevantes
6. **Analisar divergências** comparando ponto a ponto

---

## Ficheiros modificados nesta sessão
- `gerar_comparativo_reuniao.py` — script principal (ARTIGOS array)
- `comparativo_reuniao_exemplo.xlsx` — output regenerado
- `comparativo_reuniao_exemplo.html` — output regenerado
- `comparativo_reuniao_exemplo.docx` — output regenerado

---

## Validação rápida ao iniciar nova sessão
```bash
python3 -c "
import re
with open('gerar_comparativo_reuniao.py') as f:
    script = f.read()
ids = re.findall('\"id\": \"(ART-\d+)\"', script)
# Verificar artigos com campos vazios:
for art_id in ids:
    m = re.search(f'\"id\": \"{art_id}\"(.+?)(?:\"id\": \"ART-|\])', script, re.DOTALL)
    if m:
        text = m.group(1)
        if '\"texto\": \"\"' in text:
            print(f'{art_id}: tem campos texto vazios')
        if '\"sumario\": \"\"' in text:
            print(f'{art_id}: tem sumario vazio')
"
```
