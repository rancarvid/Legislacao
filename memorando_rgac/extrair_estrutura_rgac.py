#!/usr/bin/env python3
"""
Extrai a estrutura do RGAC canónico (capítulos, artigos e epígrafes) para estrutura_rgac.json.

O ficheiro lido é FICHEIRO_RGAC de dados_memorando_rgac.py, que tem de ser o ficheiro ⭐ da tabela 2.1
do CLAUDE.md. Correr sempre que chegar uma versão nova do RGAC:

    python3 memorando_rgac/extrair_estrutura_rgac.py

Cada artigo recebe uma chave. Normalmente é o número («86»). Se o número se repetir no texto, a segunda
ocorrência fica «81-b», a terceira «81-c», e assim por diante. A repetição é ela própria um lapso
formal a registar em LAPSOS.

O texto lido é o texto com as alterações registadas aceites (convenção do projeto): conta o texto
inserido (w:ins) e não conta o texto apagado (w:del, w:moveFrom).

Um artigo sem número («Artigo º») fica com o número do artigo anterior e a chave seguinte desse número
(por exemplo «39-b»), com "sem_numero": true. É também um lapso formal a registar em LAPSOS.

Também lista no ecrã números repetidos, artigos sem número, números em falta e artigos fora de ordem.
"""

import collections
import importlib.util
import json
import os
import re

from docx import Document
from docx.oxml.ns import qn

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
spec = importlib.util.spec_from_file_location("dados", os.path.join(AQUI, "dados_memorando_rgac.py"))
D = importlib.util.module_from_spec(spec)
spec.loader.exec_module(D)

CAB = re.compile(r"^(CAPÍTULO|ANEXO)\s+([IVXLC]+)\b")
ART = re.compile(r"^Artigo\s+(\d+)\.º")
ART_SEM_NUMERO = re.compile(r"^Artigo\s+\.?º\s*$")

APAGADO = {qn("w:del"), qn("w:moveFrom")}
T, TAB, BR, CR = qn("w:t"), qn("w:tab"), qn("w:br"), qn("w:cr")


def texto_aceite(p):
    """Texto do parágrafo com as alterações registadas aceites."""
    partes = []
    for el in p._p.iter(T, TAB, BR, CR):
        if any(a.tag in APAGADO for a in el.iterancestors()):
            continue
        if el.tag == T:
            partes.append(el.text or "")
        else:
            partes.append("\t" if el.tag == TAB else "\n")
    return "".join(partes)


def main():
    doc = Document(os.path.join(RAIZ, D.FICHEIRO_RGAC))
    ps = [texto_aceite(p).strip() for p in doc.paragraphs]
    capitulo, epigrafe_cap = "", ""
    artigos = []
    vistos = collections.Counter()
    sem_numero = []
    for i, t in enumerate(ps):
        m = CAB.match(t)
        if m:
            capitulo = f"{m.group(1).capitalize()} {m.group(2)}"
            epigrafe_cap = ps[i + 1] if i + 1 < len(ps) else ""
            continue
        m = ART.match(t)
        sem = not m and ART_SEM_NUMERO.match(t) and artigos
        if m or sem:
            n = int(m.group(1)) if m else artigos[-1]["numero"]
            vistos[n] += 1
            chave = str(n) if vistos[n] == 1 else f"{n}-{'abcdefgh'[vistos[n] - 1]}"
            artigo = {
                "chave": chave,
                "numero": n,
                "epigrafe": ps[i + 1] if i + 1 < len(ps) else "",
                "capitulo": capitulo,
                "epigrafe_capitulo": epigrafe_cap,
            }
            if sem:
                artigo["sem_numero"] = True
                sem_numero.append(chave)
            artigos.append(artigo)
    with open(os.path.join(AQUI, "estrutura_rgac.json"), "w", encoding="utf-8") as f:
        json.dump({"ficheiro": D.FICHEIRO_RGAC, "artigos": artigos}, f, ensure_ascii=False, indent=1)

    nums = [a["numero"] for a in artigos]
    print(f"{len(artigos)} artigos extraídos de {D.FICHEIRO_RGAC}")
    numerados = collections.Counter(a["numero"] for a in artigos if not a.get("sem_numero"))
    rep = sorted(k for k, v in numerados.items() if v > 1)
    falta = [k for k in range(1, max(nums) + 1) if k not in vistos]
    fora = [(a, b) for a, b in zip(nums, nums[1:]) if b < a]
    print("Números repetidos:", rep or "nenhum")
    print("Artigos sem número:", sem_numero or "nenhum")
    print("Números em falta:", falta or "nenhum")
    print("Fora de ordem:", fora or "nenhum")


if __name__ == "__main__":
    main()
