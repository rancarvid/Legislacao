#!/usr/bin/env python3
"""
Extrai a estrutura do RGAC canónico (capítulos, artigos e epígrafes) para estrutura_rgac.json.

O ficheiro lido é FICHEIRO_RGAC de dados_memorando_rgac.py, que tem de ser o ficheiro ⭐ da tabela 2.1
do CLAUDE.md. Correr sempre que chegar uma versão nova do RGAC:

    python3 memorando_rgac/extrair_estrutura_rgac.py

Cada artigo recebe uma chave. Normalmente é o número («86»). Se o número se repetir no texto, a segunda
ocorrência fica «81-b», a terceira «81-c», e assim por diante. A repetição é ela própria um lapso
formal a registar em LAPSOS.

Também lista no ecrã números repetidos, números em falta e artigos fora de ordem.
"""

import collections
import importlib.util
import json
import os
import re

from docx import Document

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
spec = importlib.util.spec_from_file_location("dados", os.path.join(AQUI, "dados_memorando_rgac.py"))
D = importlib.util.module_from_spec(spec)
spec.loader.exec_module(D)

CAB = re.compile(r"^(CAPÍTULO|ANEXO)\s+([IVXLC]+)\b")
ART = re.compile(r"^Artigo\s+(\d+)\.º")


def main():
    doc = Document(os.path.join(RAIZ, D.FICHEIRO_RGAC))
    ps = [p.text.strip() for p in doc.paragraphs]
    capitulo, epigrafe_cap = "", ""
    artigos = []
    vistos = collections.Counter()
    for i, t in enumerate(ps):
        m = CAB.match(t)
        if m:
            capitulo = f"{m.group(1).capitalize()} {m.group(2)}"
            epigrafe_cap = ps[i + 1] if i + 1 < len(ps) else ""
            continue
        m = ART.match(t)
        if m:
            n = int(m.group(1))
            vistos[n] += 1
            chave = str(n) if vistos[n] == 1 else f"{n}-{'abcdefgh'[vistos[n] - 1]}"
            artigos.append({
                "chave": chave,
                "numero": n,
                "epigrafe": ps[i + 1] if i + 1 < len(ps) else "",
                "capitulo": capitulo,
                "epigrafe_capitulo": epigrafe_cap,
            })
    with open(os.path.join(AQUI, "estrutura_rgac.json"), "w", encoding="utf-8") as f:
        json.dump({"ficheiro": D.FICHEIRO_RGAC, "artigos": artigos}, f, ensure_ascii=False, indent=1)

    nums = [a["numero"] for a in artigos]
    print(f"{len(artigos)} artigos extraídos de {D.FICHEIRO_RGAC}")
    rep = sorted(k for k, v in vistos.items() if v > 1)
    falta = [k for k in range(1, max(nums) + 1) if k not in vistos]
    fora = [(a, b) for a, b in zip(nums, nums[1:]) if b < a]
    print("Números repetidos:", rep or "nenhum")
    print("Números em falta:", falta or "nenhum")
    print("Fora de ordem:", fora or "nenhum")


if __name__ == "__main__":
    main()
