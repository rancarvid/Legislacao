#!/usr/bin/env python3
"""
Extrai a estrutura do RGAC canónico (capítulos, artigos e epígrafes) para estrutura_rgac.json.

O ficheiro lido é FICHEIRO_RGAC de dados_memorando_rgac.py, que tem de ser o ficheiro ⭐ da tabela 2.1
do CLAUDE.md. Correr sempre que chegar uma versão nova do RGAC:

    python3 memorando_rgac/extrair_estrutura_rgac.py

O texto lido é o texto com as alterações registadas aceites: conta o texto inserido (w:ins) e não conta
o apagado (w:del). Um parágrafo cuja marca de fim foi apagada junta-se ao seguinte, como no Word. O
resultado pode ser conferido com:

    pandoc --track-changes=accept -t plain "<ficheiro do RGAC>"

Cada artigo recebe uma chave. Normalmente é o número («86»). Se o número se repetir no texto, a segunda
ocorrência fica «81-b», a terceira «81-c», e assim por diante. Um artigo sem número («Artigo º») recebe
o número do artigo anterior e a letra seguinte («39-b»), e fica marcado com "sem_numero". A repetição e
a falta de número são lapsos formais a registar em LAPSOS.

Também lista no ecrã números repetidos, números em falta, artigos sem número e artigos fora de ordem.
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
ART = re.compile(r"^Artigo\s+(?:(\d+)\.)?º")

W_P, W_R, W_TBL = qn("w:p"), qn("w:r"), qn("w:tbl")
APAGADO = (qn("w:del"), qn("w:moveFrom"))
MARCA_APAGADA = f"{qn('w:pPr')}/{qn('w:rPr')}/{qn('w:del')}"


def texto_aceite(p):
    """Texto do parágrafo com as alterações aceites.

    O p.text do python-docx só lê os runs que são filhos diretos de w:p e perde o texto inserido. Aqui
    contam todos os runs do parágrafo, menos os apagados e os de caixas de texto (outro w:p lá dentro).
    """
    partes = []
    for r in p.iter(W_R):
        a = r.getparent()
        while a is not p and a.tag not in APAGADO and a.tag != W_P:
            a = a.getparent()
        if a is p:
            partes.append(r.text)
    return "".join(partes)


def paragrafos_aceites(doc):
    """Parágrafos do corpo do documento (sem tabelas nem índice), com as alterações aceites."""
    ps, resto = [], ""
    for el in doc.element.body.iterchildren():
        if el.tag == W_TBL and resto:
            ps.append(resto.strip())
            resto = ""
        if el.tag != W_P:
            continue
        t = resto + texto_aceite(el)
        resto = ""
        if el.find(MARCA_APAGADA) is not None:
            resto = t
        else:
            ps.append(t.strip())
    if resto:
        ps.append(resto.strip())
    return ps


def main():
    doc = Document(os.path.join(RAIZ, D.FICHEIRO_RGAC))
    ps = paragrafos_aceites(doc)
    capitulo, epigrafe_cap = "", ""
    artigos = []
    chaves = collections.Counter()
    vistos = collections.Counter()
    for i, t in enumerate(ps):
        m = CAB.match(t)
        if m:
            capitulo = f"{m.group(1).capitalize()} {m.group(2)}"
            epigrafe_cap = ps[i + 1] if i + 1 < len(ps) else ""
            continue
        m = ART.match(t)
        if m:
            sem_numero = m.group(1) is None
            n = (artigos[-1]["numero"] if artigos else 0) if sem_numero else int(m.group(1))
            if not sem_numero:
                vistos[n] += 1
            chaves[n] += 1
            chave = str(n) if chaves[n] == 1 else f"{n}-{'abcdefgh'[chaves[n] - 1]}"
            # A epígrafe é o parágrafo seguinte, ou o que vem depois de uma quebra de linha no mesmo parágrafo.
            epigrafe = t.partition("\n")[2].strip() or (ps[i + 1] if i + 1 < len(ps) else "")
            artigos.append({
                "chave": chave,
                "numero": n,
                "epigrafe": epigrafe,
                "capitulo": capitulo,
                "epigrafe_capitulo": epigrafe_cap,
            })
            if sem_numero:
                artigos[-1]["sem_numero"] = True
    with open(os.path.join(AQUI, "estrutura_rgac.json"), "w", encoding="utf-8") as f:
        json.dump({"ficheiro": D.FICHEIRO_RGAC, "artigos": artigos}, f, ensure_ascii=False, indent=1)

    nums = [a["numero"] for a in artigos]
    print(f"{len(artigos)} artigos extraídos de {D.FICHEIRO_RGAC} (texto com as alterações aceites)")
    rep = sorted(k for k, v in vistos.items() if v > 1)
    falta = [k for k in range(1, max(nums) + 1) if k not in vistos]
    sem = [a["chave"] for a in artigos if a.get("sem_numero")]
    fora = [(a, b) for a, b in zip(nums, nums[1:]) if b < a]
    print("Números repetidos:", rep or "nenhum")
    print("Números em falta:", falta or "nenhum")
    print("Artigos sem número:", sem or "nenhum")
    print("Fora de ordem:", fora or "nenhum")


if __name__ == "__main__":
    main()
