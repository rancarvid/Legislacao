#!/usr/bin/env python3
"""
Verifica que as três versões do memorando têm o mesmo conteúdo:

  - versão principal (1.x): dados_memorando_rgac.py      códigos T-/C- e letras de capítulo, números escritos à mão
  - ensaio 2.0 (opção A):   v2/dados_memorando_rgac_v2.py códigos P-NN, artigos pela epígrafe
  - ensaio 3.0 (opção B):   v3/dados_memorando_rgac_v3.py códigos SIGLA-NN, artigos pela epígrafe

Compara, ficha a ficha (pela tabela CORRESPONDENCIA do ensaio 3.0), o título, onde, origem, problema,
proposta, quem levantou, estado e fichas relacionadas, depois de trocar as epígrafes pelo número atual
do artigo e os códigos pelos da versão 1.x. Compara também lapsos, pontos resolvidos e textos de
enquadramento. A bibliografia e as posições externas são partilhadas (os ensaios importam-nas da 1.x).

Uso: python3 memorando_rgac/verificar_versoes.py   (termina com código 1 se houver diferenças)
"""
import importlib.util
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))


def carregar(nome, caminho):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


V1 = carregar("v1", os.path.join(AQUI, "dados_memorando_rgac.py"))
G2 = carregar("g2", os.path.join(AQUI, "v2", "gerar_memorando_rgac_v2.py"))
G3 = carregar("g3", os.path.join(AQUI, "v3", "gerar_memorando_rgac_v3.py"))
V2, V3 = G2.D, G3.D

erros = []
fichas1 = {f["cod"]: f for t in V1.TEMAS for f in t["fichas"]}
fichas2 = {f["cod"]: f for f in V2.FICHAS}
fichas3 = {f["cod"]: f for f in V3.FICHAS}

# ---------------------------------------------------------------- correspondência
trios = V3.CORRESPONDENCIA
para1 = {}
for c1, c2, c3 in trios:
    para1[c2] = c1
    para1[c3] = c1
    if c1 not in fichas1:
        erros.append(f"{c1}: está na correspondência mas não existe na versão 1.x")
    if c2 not in fichas2:
        erros.append(f"{c2}: está na correspondência mas não existe no ensaio 2.0")
    if c3 not in fichas3:
        erros.append(f"{c3}: está na correspondência mas não existe no ensaio 3.0")
    if V2.CORRESPONDENCIA.get(c1) != c2:
        erros.append(f"{c1}: a correspondência do ensaio 2.0 diz {V2.CORRESPONDENCIA.get(c1)}, a do 3.0 diz {c2}")
    if c3 in fichas3 and fichas3[c3].get("cod_ensaio_2") != c2:
        erros.append(f"{c3}: cod_ensaio_2 devia ser {c2}")
    if c2 in fichas2 and fichas2[c2].get("cod_antigo") != c1:
        erros.append(f"{c2}: cod_antigo devia ser {c1}")
for conj, nome, pos in ((fichas1, "1.x", 0), (fichas2, "2.0", 1), (fichas3, "3.0", 2)):
    falta = set(conj) - {t[pos] for t in trios}
    for c in sorted(falta):
        erros.append(f"{c} (versão {nome}) não está na tabela CORRESPONDENCIA do ensaio 3.0")


def em_v1(txt, gerador):
    txt = gerador.r(txt, "verificar_versoes")
    return re.sub(r"\b(P-\d\d|[A-Z]{3}-\d\d)\b", lambda m: para1.get(m.group(0), m.group(0)), txt)


def comparar(rotulo, a, b):
    if a != b:
        erros.append(f"{rotulo}\n      1.x: {str(a)[:160]}\n      ensaio: {str(b)[:160]}")


# ---------------------------------------------------------------- fichas
for c1, c2, c3 in trios:
    if c1 not in fichas1 or c2 not in fichas2 or c3 not in fichas3:
        continue
    f1 = fichas1[c1]
    for fx, g, nome in ((fichas2[c2], G2, c2), (fichas3[c3], G3, c3)):
        for k in ("titulo", "proposta", "origem", "estado"):
            comparar(f"{c1}/{nome}: campo {k}", f1[k], em_v1(fx[k], g))
        for k in ("problema", "levantado", "rel"):
            comparar(f"{c1}/{nome}: campo {k}", list(f1[k]), [em_v1(x, g) for x in fx[k]])
        onde = [em_v1(x, g) for x in fx["onde"]]
        if onde and onde[0].startswith("artigo mais próximo"):
            onde = [x.replace("sem norma própria", "sem norma no RGAC") for x in onde[1:]]
        comparar(f"{c1}/{nome}: campo onde", list(f1["onde"]), onde)
    tema_v3 = fichas3[c3]["etiquetas"][0]
    if c1[0] in "TC" and len(c1) == 4 and {"T": "TIT", "C": "CED"}[c1[0]] != tema_v3:
        erros.append(f"{c1}/{c3}: tema principal diferente")

# ---------------------------------------------------------------- lapsos
estr = {a["chave"]: a for a in G2.ARTS}
l2 = {l["cod"]: l for l in V2.LAPSOS}
l3 = {l["cod"]: l for l in V3.LAPSOS}
for l in V1.LAPSOS:
    for lx, g, nome in ((l2.get(l["cod"]), G2, "2.0"), (l3.get(l["cod"]), G3, "3.0")):
        if lx is None:
            erros.append(f"{l['cod']}: falta no ensaio {nome}")
            continue
        comparar(f"{l['cod']}/{nome}: onde", [estr[k]["ancora"] for k in l["onde"]],
                 [g.D.RENOMEACOES.get(k, k) for k in lx["onde"]])
        comparar(f"{l['cod']}/{nome}: estado", l["estado"], lx["estado"])
        comparar(f"{l['cod']}/{nome}: ficha", l["ficha"], para1.get(lx["ficha"], lx["ficha"]))
        comparar(f"{l['cod']}/{nome}: correção", l["correcao"], em_v1(lx["correcao"], g))
        comparar(f"{l['cod']}/{nome}: lapso", l["lapso"], em_v1(lx["lapso"], g))
for nome, lx in (("2.0", l2), ("3.0", l3)):
    for c in set(lx) - {l["cod"] for l in V1.LAPSOS}:
        erros.append(f"{c}: existe no ensaio {nome} mas não na versão 1.x")

# ---------------------------------------------------------------- resolvidos e enquadramento
for g, nome in ((G2, "2.0"), (G3, "3.0")):
    comparar(f"RESOLVIDOS/{nome}", [(a, b) for a, b in V1.RESOLVIDOS], [(a, em_v1(b, g)) for a, b in g.D.RESOLVIDOS])
    intro = {t["etiqueta"]: t["intro"] for t in g.D.TRANSVERSAIS}
    comparar(f"Enquadramento TIT/{nome}", list(V1.TEMA_T["intro"]), [em_v1(x, g) for x in intro["TIT"]])
    comparar(f"Enquadramento CED/{nome}", list(V1.TEMA_C["intro"]), [em_v1(x, g) for x in intro["CED"]])
    comparar(f"REVISAO/{nome}", {estr[k]["ancora"]: v for k, v in V1.REVISAO.items()},
             {g.D.RENOMEACOES.get(k, k): v for k, v in g.D.REVISAO.items()})

if erros:
    print(f"As três versões NÃO estão alinhadas ({len(erros)} diferenças):")
    for e in erros:
        print("  -", e)
    sys.exit(1)
print(f"As três versões estão alinhadas: {len(trios)} fichas, {len(V1.LAPSOS)} lapsos, "
      f"{len(V1.RESOLVIDOS)} pontos resolvidos.")
