# Ponto de Situação — 5 de Abril de 2026

**Status**: Investigação concluída | Plano criado | **Execução adiada (por confirmar mais tarde)**

---

## Contexto

Trabalho em curso: **Integração de Glossário Flutuante com Hiperlinks Internos no Word**

### Situação Anterior (Final de Março)

O **glossário interativo** (com termos do Artigo 4 — Definições do Regulamento 2023/0447) foi implementado com sucesso no **HTML** com:
- ✅ Tooltips flutuantes ao passar o rato
- ✅ Normalização de hífens especiais (U+2011, U+2010 → U+002D)
- ✅ Matching de termos (longest-first, evitar overlaps)
- ✅ Suporte a plurais (singular + plural)

**Problema resolvido no ramo `claude/review-recent-tasks-YROKh`**:
- Commits resolveram encoding de hífens que impedia regex matching
- Último commit: `e8e2f39` — Fix hyphen encoding in marcarGlossario

### Situação Atual (5 Abril)

**Objetivo não executado**: Trazer funcionalidade similar para o documento Word (.docx)

**Desafio**: Word não suporta JavaScript/tooltips como HTML. Solução proposta:
- Marcar termos com **sublinhado intermitente (dashed)**
- Criar **hiperlinks internos** que apontam para definições exatas em Art. 4
- Implementar via **bookmarks XML** (padrão python-docx)

---

## Plano Detalhado Criado

📄 **Ficheiro**: `/root/.claude/plans/glistening-wishing-stallman.md`

### Resumo Executivo

| Fase | Tarefas | Ficheiros | Estimativa |
|------|---------|-----------|-----------|
| 1. Preparação | Importar glossários extraídos | `gerar_word.py` | Mínima |
| 2. Bookmarks Art. 4 | Criar bookmark para cada definição | `gerar_word.py` | Média |
| 3. Marcação de Termos | Detectar + marcar com sublinhado | `gerar_word.py` (cell_body) | Alta |
| 4. Hiperlinks | Envolver termos em `<w:hyperlink>` | `gerar_word.py` + XML | Alta |
| 5. Output | Gerar `comparativo_reuniao_exemplo_glossario.docx` | `gerar_word.py` | Mínima |
| 6. Testes | Verificar links, cobertura, edge cases | Manual | Média |

### Output de Teste Proposto

- **Ficheiro**: `comparativo_reuniao_exemplo_glossario.docx` (NOVO)
- **Original preservado**: `comparativo_reuniao_exemplo.docx` (sem alterações até validação)
- **Propósito**: Validar implementação antes de mesclar na versão oficial

### Funcionalidades Específicas

#### Bookmarks (em Art. 4)
```
Cada definição tem bookmark: art04_def_{numero}_{termo_normalizado}
Ex: art04_def_1_cao, art04_def_5_bem_estar
```

#### Estilos de Marcação
- **Visual**: Sublinhado intermitente (`w:u w:val="dash"`)
- **Cor**: Padrão (texto preto + underline apenas)
- **Interação**: Click → navega para definição exata em Art. 4

#### Técnica XML
```python
# Bookmark start
<w:bookmarkStart w:id="0" w:name="art04_def_1_cao"/>
# Conteúdo
<w:bookmarkEnd w:id="0"/>

# Hiperlink (envolvendo um run)
<w:hyperlink w:anchor="art04_def_1_cao">
  <w:r>
    <w:rPr><w:u w:val="dash"/></w:rPr>
    <w:t>termo</w:t>
  </w:r>
</w:hyperlink>
```

---

## Ficheiros Envolvidos

### Modificação Necessária

**`gerar_word.py`** (principal)
- Adicionar imports: `extrair_glossario_pt`, `extrair_glossario_en` de `gerar_comparativo_reuniao.py`
- Novas funções:
  - `criar_bookmarks_art04()` — bookmarks em definições Art. 4
  - `marcar_glossario_word()` — detecção de termos + hiperlinks
  - `add_hyperlink_to_run()` — implementação de hiperlink XML
- Modificar:
  - `add_article_section()` — integrar bookmarks (ART-04) + marcação (outros)
  - `cell_body()` — chamar `marcar_glossario_word()`
  - `criar_word()` — extrair glossários, gerar output novo

**`gerar_comparativo_reuniao.py`** (mínima)
- Garantir exportabilidade de `extrair_glossario_pt()` e `extrair_glossario_en()`
- Possivelmente: função helper `mapear_glossario_para_bookmarks()`

---

## Decisões Tomadas

| Decisão | Opção | Justificação |
|---------|-------|-------------|
| **Marcação Visual** | Sublinhado intermitente (dashed) | Visualmente distinto, compatível com Word |
| **Navegação** | Hiperlink → definição exata em Art. 4 | Mais útil que apenas topo do artigo |
| **Output** | Novo ficheiro `..._glossario.docx` | Preservar original durante testes |
| **Scope** | Apenas Word (não Excel) | HTML já tem tooltips; Excel é complexo |
| **Fonte de Dados** | Glossários já extraídos em Python | Reutilizar lógica existente |

---

## Status: Por Confirmar

### Próximas Ações (quando retomar)

1. ✅ Iniciar implementação em branch `claude/review-recent-tasks-YROKh`
2. ✅ Implementar `criar_bookmarks_art04()` + `add_hyperlink_to_run()`
3. ✅ Integrar em `cell_body()` e `add_article_section()`
4. ✅ Gerar output de teste: `comparativo_reuniao_exemplo_glossario.docx`
5. ✅ Testes manuais:
   - Abrir Word, verificar sublinhados
   - Clicar em 5-10 termos diferentes
   - Confirmar navegação para definição exata
   - Verificar cobertura (termos encontrados vs. esperados)
6. ✅ Otimizações (se necessário):
   - Tratamento de edge cases (hífens, plurais, tabelas)
   - Performance (se houver muitos termos)

### Pontos de Atenção

- **Encoding de hífens**: Já resolvido no HTML; reutilizar padrão
- **Overlaps de spans**: Usar longest-match-first (já em código)
- **Bookmarks únicos**: ID numérico + nome string devem ser únicos globalmente
- **Compatibilidade**: Testar em Word 2019, 2021, Office 365

---

## Referências

### Ficheiros de Código

- **Scripts**: `gerar_comparativo_reuniao.py`, `gerar_word.py`
- **Branch**: `claude/review-recent-tasks-YROKh`
- **Ramo anterior**: `claude/review-last-task-bjZbi`

### Documentação do Glossário

- **Extração PT**: `gerar_comparativo_reuniao.py:1385-1503` (`extrair_glossario_pt()`)
- **Extração EN**: `gerar_comparativo_reuniao.py:1506-1609` (`extrair_glossario_en()`)
- **Marcação HTML**: `gerar_comparativo_reuniao.py:1629-1704` (`marcarGlossario()`)

### Artigo 4 (Definições)

- **Posição em ARTIGOS**: Índice 3 (id='ART-04', tema='Definições')
- **Estrutura**: 39 definições numeradas (PT) + tradução EN
- **Termos coletados**: ~15-20 termos que aparecem em outros artigos

---

## Notas de Implementação

1. **Bookmarks em Word precisam de**:
   - ID numérico único (0, 1, 2, ...)
   - Nome string único (ex: "art04_def_1_cao")

2. **Sublinhado intermitente**: `w:u w:val="dash"` (não "dashed")

3. **Hiperlinks internos**: Usar atributo `w:anchor` (não `r:id`)

4. **Normalização obrigatória**: Hífens especiais (U+2011, U+2010) → regular (U+002D)

5. **Evitar aninhamentos**: Um termo dentro de outro não deve ter hiperlink duplo

6. **Reutilizar**:
   - Lógica de matching do HTML (`marcarGlossario()`)
   - Extração de glossários (`extrair_glossario_pt/en()`)
   - Padrão XML de `OxmlElement` (cores, bordas)

---

## Conclusão

**Investigação**: ✅ Completa  
**Plano**: ✅ Detalhado  
**Execução**: ⏳ Adiada (por retomar quando decidido)

**Próxima sessão**: Confirmar se proceder com implementação ou explorar abordagem alternativa (ex: notas de rodapé).
