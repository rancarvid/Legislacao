# Análise Comparativa da Legislação sobre Animais de Companhia

Projeto de análise comparativa entre a legislação portuguesa vigente, duas propostas de consolidação nacional e o novo Regulamento Europeu 2023/0447 (cães e gatos).

---

## Ponto de Situação — 4 de abril de 2026

### O que foi feito

| Fase | Trabalho realizado | Estado |
|---|---|---|
| **Organização do repositório** | Catalogação de todos os ficheiros legislativos com códigos internos (`@legislacao`, `@codigo`, `@rgbeac`, `@regulamento`) | ✅ Completo |
| **Investigação legislativa** | Levantamento exaustivo de 19 diplomas portugueses vigentes (leis, DLs, portarias, DR) em 12 temáticas | ✅ Completo |
| **Análise comparativa — Art. 5.º a 22.º** | 21 artigos do Regulamento 2023/0447 mapeados artigo a artigo com correspondências em `@rgbeac`, `@codigo` e `@legislacao` | ✅ Completo |
| **Ferramenta de reunião** | HTML SPA interativo + Excel + Word gerados automaticamente pelo script `gerar_comparativo_reuniao.py` | ✅ Operacional |
| **Análise de opiniões** | 52 opiniões externas organizadas em 7 grupos; integradas na análise dos preâmbulos | ✅ Completo |
| **Tema cães de caça** | Documento de reflexão e integração de contexto específico nos artigos ART-05, ART-17, ART-18 | ✅ Completo |
| **Ficha parlamentar** | Ficha de resposta a inquirição parlamentar sobre o Regulamento 2023/0447 (formato Word) | ✅ Completo |

---

## Diplomas em Análise

| Código interno | Diploma | Tipo |
|---|---|---|
| `@legislacao` | Legislação vigente (DL 276/2001, DL 82/2019, Lei 27/2016, Portarias, etc.) | ✅ Vigente |
| `@codigo` | Código do Animal — DL n.º 214/2013 | Proposta de consolidação |
| `@rgbeac` | Regime Geral do Bem-Estar dos Animais de Companhia (jun. 2025) | Proposta de consolidação |
| `@regulamento` | Regulamento Europeu 2023/0447 — cães e gatos | ✅ Vigente (aplicação direta) |

---

## Artigos do Regulamento 2023/0447 Cobertos

21 artigos mapeados em sequência (Art. 5.º a 22.º):

| ID | Artigo | Tema |
|---|---|---|
| ART-05 | Art. 5.º | Princípios Gerais de Bem-Estar |
| ART-06 | Art. 6.º | Bem-Estar e Detenção |
| ART-06a | Art. 6.º-A | Estratégias de Criação — Conformação e Consanguinidade |
| ART-07 | Art. 7.º | Reprodução e Criação |
| ART-08 | Art. 8.º | Detenção Responsável |
| ART-09 | Art. 9.º | Competências de Cuidadores |
| ART-10 | Art. 10.º | Avaliação e Supervisão de Bem-Estar |
| ART-11 | Art. 11.º | Alimentação e Hidratação |
| ART-12 | Art. 12.º | Alojamento |
| ART-13 | Art. 13.º | Saúde e Monitorização Sanitária |
| ART-14 | Art. 14.º | Necessidades Comportamentais |
| ART-15 | Art. 15.º | Práticas Dolorosas |
| ART-15a | Art. 15.º-A | Espetáculos e Competições Estéticas |
| ART-17 | Art. 17.º | Identificação e Registo |
| ART-17a | Art. 17.º-A | Requisitos de Publicidade em Linha |
| ART-18 | Art. 18.º | Treino de Cuidadores |
| ART-19 | Art. 19.º | Base de Dados de Cães e Gatos |
| ART-20 | Art. 20.º | Recolha de Dados sobre Bem-Estar |
| ART-20a | Art. 20.º-A | Proteção de Dados |
| ART-21 | Art. 21.º | Entrada de Cães e Gatos na União |
| ART-22 | Art. 22.º | Alteração dos Anexos |

---

## Ficheiros Principais

### Documentos de saída (gerados automaticamente)

| Ficheiro | Tipo | Descrição |
|---|---|---|
| `comparativo_reuniao_exemplo.html` | HTML SPA | Ferramenta de reunião interativa — pesquisa, navegação artigo a artigo, notas exportáveis |
| `comparativo_reuniao_exemplo.xlsx` | Excel | Estrutura artigo a artigo com 4 sub-colunas de divergência |
| `comparativo_reuniao_exemplo.docx` | Word | Versão imprimível com tabelas e cores por diploma |
| `FICHA_RESPOSTA_AR_Regulamento_2023_0447.docx` | Word | Ficha de resposta a inquirição parlamentar |

### Scripts

| Script | Função |
|---|---|
| `gerar_comparativo_reuniao.py` | Gera HTML + Excel + Word em simultâneo a partir do array `ARTIGOS` |
| `gerar_word.py` | Gera documento Word standalone |

### Documentação interna

| Ficheiro | Descrição |
|---|---|
| `CLAUDE.md` | Documento metodológico — regras, convenções, protocolo de consulta legislativa |
| `HANDOFF.md` | Briefing técnico detalhado para colaboradores e assistentes de IA |
| `00_COMECE_AQUI.md` | Guia rápido de navegação da investigação legislativa |
| `RESUMO_PROGRESSO_2026-03-02.md` | Resumo de progresso (fase de expansão dos artigos) |

---

## Como Gerar os Outputs

```bash
# A partir da raiz do repositório:
python3 gerar_comparativo_reuniao.py
# → gera comparativo_reuniao_exemplo.html + .xlsx + .docx
```

Dependências:
```bash
pip install python-docx openpyxl
```

---

## Legislação Portuguesa Vigente Identificada

19 diplomas em 12 temáticas — ver `00_COMECE_AQUI.md` e `LEGISLACAO_VIGENTE_ANALISE_COMPLETA.md` para análise completa.

Destaques:
- **DL 82/2019** — Identificação eletrónica (SIAC/microchip)
- **Lei 27/2016** — Rede de centros de recolha; proibição do abate
- **DL 276/2001** — Proteção dos animais de companhia
- **Lei 8/2017** — Estatuto jurídico dos animais como seres sensíveis

---

## Próximos Passos Possíveis

- [ ] Expandir cobertura para artigos 1–4 e 23–28 do Regulamento
- [ ] Rever traduções PT dos artigos já mapeados (com base nos ficheiros de tradução disponíveis)
- [ ] Consolidar recomendações legislativas por tema (detenção, reprodução, rastreabilidade, errantes)
- [ ] Desenvolver infografias temáticas adicionais

---

*Repositório: rancarvid/legislacao — Branch de trabalho: `claude/review-recent-tasks-YROKh`*
