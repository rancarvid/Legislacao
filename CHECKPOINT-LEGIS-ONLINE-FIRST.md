# CHECKPOINT: LEGIS-ONLINE-FIRST

**Data**: 2026-03-04
**Ramo**: `claude/retrieve-last-order-mKVch`
**Código de referência**: `LEGIS-ONLINE-FIRST`

---

## Problema Identificado
Confusão metodológica entre:
- `@legislacao` (legislação vigente)
- `@codigo` (proposta de consolidação)
- `@rgbeac` (proposta, jun. 2025)

**Symptoma**: ANNEX-II-NUMERO-1 citava DL 276/2001 ou @codigo como se fossem legislação vigente, quando deveria remeter para DL 82/2019 consolidado (legislação vigente atual).

---

## Solução Implementada

### 1. Protocolo de Consulta de Legislação (CLAUDE.md § 2.4)

**Ordem de Prioridade Obrigatória:**

1. **PASSO 1 — Legislação vigente consolidada ONLINE (PRIORIDADE MÁXIMA)**
   - Consultar [dre.pt](https://dre.pt) (Portugal) ou [EUR-Lex](https://eur-lex.europa.eu) (Europa)
   - Usar **WebFetch** ou **WebSearch** para versão consolidada + atualizações
   - Exemplo: DL 82/2019 consolidado para identificação/registo de cães e gatos

2. **PASSO 2 — Validação com ficheiros @legislacao repositório**
   - Comparar resultado online com ficheiros repositório
   - Usar repositório como **validação secundária**, não fonte primária

3. **PASSO 3 — Análise de propostas (@codigo, @rgbeac)**
   - **APENAS APÓS** análise de legislação vigente
   - Indicar claramente: "Proposta @rgbeac" ≠ "Legislação vigente"

### 2. Regra de Distinção Absoluta

| Categoria | Status | Como Tratar |
|-----------|--------|------------|
| `@legislacao` | ✅ VIGENTE | Consultar online consolidado; citar como "legislação vigente" |
| `@codigo` | ❌ PROPOSTA | Citar como "proposta de consolidação"; **NUNCA** como vigente |
| `@rgbeac` | ❌ PROPOSTA | Citar como "proposta (jun. 2025)"; **NUNCA** como vigente |
| `@regulamento` | ✅ VIGENTE | Legislação europeia; aplicação direta; verbatim EN + tradução PT |

### 3. Erros a Evitar

- ❌ Tratar `@codigo` (proposta) como legislação que "revoga" DL 276/2001
- ❌ Omitir legislação vigente (ex: DL 82/2019) não presente no repositório
- ❌ Usar ficheiros repositório como **única fonte** de legislação
- ❌ Não distinguir claramente entre "vigente" e "proposta" na análise

---

## Commits Realizados

### Commit 1: Correção ANNEX-II-NUMERO-1
```
Corrigir ANNEX-II-NUMERO-1: remeter para DL 82/2019 (legislação vigente)

- @legislacao: DL 82/2019 é a legislação vigente relevante
- REMETE para análise online consolidada em dre.pt
- Reconhecimento: Erro metodológico de confundir @codigo (proposta) com @legislacao (vigente)
```

### Commit 2: Protocolo ao CLAUDE.md
```
Adicionar PROTOCOLO DE CONSULTA DE LEGISLAÇÃO ao CLAUDE.md (CRÍTICO)

- Nova secção 2.4: PROTOCOLO OBRIGATÓRIO de consulta de legislação
- ORDEM DE PRIORIDADE: Online → Repositório → Propostas
- REGRA CRÍTICA: Distinção absoluta @legislacao ≠ @codigo/@rgbeac
- Secção 10.1 reescrita para aplicar protocolo ANTES de qualquer análise
```

---

## Próximas Fases

Ao retomar trabalho, aplicar **SEMPRE** o protocolo 2.4 do CLAUDE.md:
1. Consultar legislação consolidada online PRIMEIRO
2. Usar WebFetch/WebSearch para legislação vigente
3. Validar com ficheiros repositório
4. Indicar claramente quando se cita "propostas" vs "legislação vigente"

---

**Código de referência para futuras conversas**: `LEGIS-ONLINE-FIRST`

Use este checkpoint para retomar análise com metodologia corrigida.
