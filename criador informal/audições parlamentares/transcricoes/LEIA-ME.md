# Transcrições das audições parlamentares de 30.7.2020

**Não são transcrição oficial da Assembleia da República**, que para estas audições não existe: o
registo oficial disponibiliza o requerimento que as motivou e uma gravação, sem ata.

Foram produzidas localmente por reconhecimento automático de fala (`faster-whisper`, língua `pt`,
`compute_type=int8`, 4 threads), a partir das gravações que estão na pasta acima.

| Ficheiro | Modelo | Cobertura |
|---|---|---|
| `32-CAM-XIV_varrimento-completo_small.txt` | `small` | Audição integral, 109,6 min, 1135 segmentos |
| `32-CAM-XIV_janelas-A-a-D_medium.txt` | `medium` | 00:34–00:37, 00:43–00:45, 00:49–00:51, 01:01–01:09 |
| `32-CAM-XIV_janela-E-nucleo-juridico_medium.txt` | `medium` | 01:28–01:46:30 |

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

## Ainda por transcrever

- Audição n.º 33-CAM-XIV (Ministro da Administração Interna e Ministra da Agricultura), 160,8 min.
- Excerto da Secretária de Estado da Administração Interna, 73,2 min — possivelmente recorte da anterior.
