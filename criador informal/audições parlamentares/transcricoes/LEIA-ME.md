# Transcrições das audições parlamentares sobre o caso de Santo Tirso

**Não são transcrição oficial da Assembleia da República**, que para estas audições não existe: o
registo oficial disponibiliza o requerimento que as motivou e uma gravação, sem ata.

Foram produzidas localmente por reconhecimento automático de fala (`faster-whisper`, língua `pt`,
`compute_type=int8`, 4 threads), a partir das gravações que estão na pasta acima.

As gravações são de três audições distintas, duas de 30.7.2020 e uma posterior.

| Ficheiro | Modelo | Cobertura |
|---|---|---|
| `32-CAM-XIV_varrimento-completo_small.txt` | `small` | Audição integral, 109,6 min, 1135 segmentos |
| `32-CAM-XIV_janelas-A-a-D_medium.txt` | `medium` | 00:34–00:37, 00:43–00:45, 00:49–00:51, 01:01–01:09 |
| `32-CAM-XIV_janela-E-nucleo-juridico_medium.txt` | `medium` | 01:28–01:46:30 |
| `33-CAM-XIV_varrimento-completo_small.txt` | `small` | Audição integral, 160,5 min, 1884 segmentos |
| `33-CAM-XIV_janelas-A-a-H_medium.txt` | `medium` | Oito janelas, 10,4 min — ver `_janelas_33.py` |
| `SE-AI_relatorio-IGAI_varrimento-completo_small.txt` | `small` | Audição integral, 72,3 min, 890 segmentos |

## As três audições

| Designação | Audição | Data |
|---|---|---|
| `32-CAM-XIV` | Presidente da Câmara Municipal de Santo Tirso | 30.7.2020 |
| `33-CAM-XIV` | Ministro da Administração Interna e Ministra da Agricultura | 30.7.2020 |
| `SE-AI` | Secretária de Estado da Administração Interna, sobre o relatório de inquérito da IGAI | **a estabelecer** — posterior a 2020 |

Sobre a terceira: fica **infirmada** a hipótese, registada numa versão anterior deste ficheiro, de que
fosse recorte da audição dos ministros. É audição autónoma, requerida pelo PAN, realizada como segunda
parte de uma reunião da comissão — «A segunda parte da nossa reunião é a audição da Senhora Secretária de
Estado da Administração Interna» (00:00:05) — e tem por objecto o relatório de inquérito da Inspeção-Geral
da Administração Interna sobre o incêndio, que foi arquivado sem indícios de infração disciplinar dos
operacionais da ANEPC ou da GNR.

**A data não está estabelecida.** Uma deputada refere-se às audições de 30.7.2020 como tendo sido «em
finais de julho do ano passado» (00:32:48), pelo que a audição é de 2021 ou posterior. Enquanto a data não
for conferida, o ficheiro não leva número de sequência, para não sugerir que pertence à sessão de 2020, e
nada dele se cita com data.

## Para que servem

O ficheiro `small` serve para **localizar** passagens: varrer as duas horas e saber onde está o que
interessa. Não serve para citar — troca nomes próprios com frequência («São Justiça» e «Santista» por
Santo Tirso, «de gaiva» e «de Grave» por DGAV, «enferramento» por encerramento).

Os ficheiros `medium` cobrem as janelas cujas passagens foram citadas no estudo. Foram reprocessadas
precisamente por isso: nenhuma citação do estudo provém do varrimento `small`.

## Regras de citação (as mesmas do Anexo C.6 do estudo)

1. Toda a citação vai acompanhada da **marca temporal**, para poder ser conferida na gravação.
2. As correcções evidentes de nomes e termos técnicos vão entre parênteses rectos: «[Santo Tirso]».
3. Nenhuma conclusão jurídica assenta apenas numa destas citações — todas têm fundamento normativo
   independente, conferido no jornal oficial.
4. Onde a substância de uma passagem dependa de um nome ou número mal reconhecido, a passagem não se usa:
   reprocessa-se a janela primeiro.

## Reproduzir

```bash
pip install faster-whisper
python3 _transcrever.py "<ficheiro de áudio>" saida.txt small      # varrimento
python3 _janelas.py                                                 # janelas (editar a lista JANELAS)
```

Ritmos medidos neste contentor (4 CPU, int8): `small` ≈ 4,4× tempo real; `medium` ≈ 1× tempo real.
O `medium` descarrega ~1,5 GB na primeira utilização.

**Cuidado ao encadear processos**: um `pgrep -f "x.py"` lançado dentro de `bash -c` apanha o próprio
comando de espera e nunca termina. Encadear por PID (`while [ -d /proc/<pid> ]`) ou por nome exacto.

## Estado

As três gravações estão varridas com `small`. As janelas com `medium` estão feitas para a `32-CAM-XIV` e a
`33-CAM-XIV`.

Por fazer:

- Estabelecer a data da audição `SE-AI` e, feito isso, renomear o ficheiro com o número de sequência.
- Janelas com `medium` na `SE-AI`, se dela se vier a citar. A passagem de interesse para o estudo é
  00:32–00:35, sobre o não cumprimento e o não acompanhamento da ordem de encerramento da DGAV e sobre a
  ausência e a dupla posição do médico veterinário municipal.
- Obter o próprio relatório da IGAI, que foi remetido à Assembleia da República e lido pelos deputados. O
  que consta destas transcrições é a caracterização que os deputados dele fazem, não o relatório.
