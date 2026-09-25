# Análise Comparativa da Legislação sobre Animais de Companhia

Projeto de análise comparativa entre a legislação portuguesa vigente, duas propostas de consolidação nacional e o novo Regulamento (UE) 2026/1818 (cães e gatos).

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

## Ponto de Situação — 4 de abril de 2026

### O que foi feito

| Fase | Trabalho realizado | Estado |
|---|---|---|
| **Organização do repositório** | Catalogação de todos os ficheiros legislativos com códigos internos (`@legislacao`, `@codigo`, `@rgbeac`, `@regulamento`, `@rgac`) | ✅ Completo |
| **Investigação legislativa** | Levantamento exaustivo de 19 diplomas portugueses vigentes (leis, DLs, portarias, DR) em 12 temáticas | ✅ Completo |
| **Análise comparativa — Art. 5.º a 22.º** | 21 artigos do Regulamento (UE) 2026/1818 mapeados artigo a artigo com correspondências em `@rgbeac`, `@codigo` e `@legislacao` | ✅ Completo |
| **Ferramenta de reunião** | HTML SPA interativo + Excel + Word gerados automaticamente pelo script `gerar_comparativo_reuniao.py` | ✅ Operacional |
| **Análise de opiniões** | 52 opiniões externas organizadas em 7 grupos; integradas na análise dos preâmbulos | ✅ Completo |
| **Tema cães de caça** | Documento de reflexão e integração de contexto específico nos artigos ART-05, ART-17, ART-18 | ✅ Completo |
| **Ficha parlamentar** | Ficha de resposta a inquirição parlamentar sobre o Regulamento (UE) 2026/1818 (formato Word) | ✅ Completo |

---

## Diplomas em Análise

| Código interno | Diploma | Tipo |
|---|---|---|
| `@legislacao` | Legislação vigente (DL 276/2001, DL 82/2019, Lei 27/2016, Portarias, etc.) | ✅ Vigente |
| `@codigo` | Código do Animal — DL n.º 214/2013 | Proposta de consolidação (incorporada em `@rgac`) |
| `@rgbeac` | Regime Geral do Bem-Estar dos Animais de Companhia (jun. 2025) | Proposta de consolidação (incorporada em `@rgac`) |
| `@regulamento` | Regulamento (UE) 2026/1818 — cães e gatos | ✅ Publicado no JO (aplicação direta; aplicável a partir de 31.8.2028; incorporado em `@rgac`) |
| `@rgac` ⭐ | Diploma final — texto de trabalho do projeto: recolhe contributos do `@codigo` e do `@rgbeac` e integra diretamente o `@regulamento` | Diploma final (trabalho em curso; ficheiro `RGAC_DAJA_REV. FORMAL_V1_Versão TRABALHO - Revisto 30-06-2026 18h00 Grupo.docx`) |

---

## Artigos do Regulamento (UE) 2026/1818 Cobertos

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
| `FICHA_RESPOSTA_AR_Regulamento_2023_0447.docx` | Word | Ficha de resposta a inquirição parlamentar (nome do ficheiro mantém o n.º de procedimento) |
| `Regulamento 2026_01818_PT.pdf` | PDF | `@regulamento` — texto PT publicado no JO **(fonte canónica)** |
| `Regulamento Versao final en-en.pdf` | PDF | `@regulamento` — texto EN publicado no JO **(fonte canónica)** |

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

- [ ] Integrar `@rgac` na ferramenta de reunião (coluna adicional nos scripts geradores)
- [ ] Expandir cobertura para artigos 1–4 e 23–28 do Regulamento
- [ ] Rever traduções PT dos artigos já mapeados com base no texto consolidado de `@rgac`
- [ ] Consolidar recomendações legislativas por tema (detenção, reprodução, rastreabilidade, errantes)
- [ ] Desenvolver infografias temáticas adicionais

---

*Repositório: rancarvid/legislacao — Branch de trabalho: `claude/review-recent-tasks-YROKh`*
