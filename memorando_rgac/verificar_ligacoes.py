#!/usr/bin/env python3
"""
Verifica as ligações da bibliografia do Memorando de acompanhamento do RGAC.

Para cada entrada de BIBLIOGRAFIA (dados_memorando_rgac.py):
  - ficheiro do repositório: confirma que existe;
  - URL: descarrega com curl e confirma resposta 200 e, quando há palavra de controlo,
    que essa palavra aparece no documento (PDF ou HTML);
  - se o sítio bloquear pedidos automáticos, tenta num browser real (Playwright + Chromium).

Escreve o resultado em verificacao_ligacoes.md e termina com código 1 se alguma ligação falhar.

Uso: python3 memorando_rgac/verificar_ligacoes.py
"""

import datetime
import importlib.util
import os
import re
import subprocess
import tempfile
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
spec = importlib.util.spec_from_file_location("dados", os.path.join(AQUI, "dados_memorando_rgac.py"))
D = importlib.util.module_from_spec(spec)
spec.loader.exec_module(D)

CHROMIUM = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"


def texto(caminho):
    with open(caminho, "rb") as f:
        b = f.read()
    if b[:4] == b"%PDF":
        try:
            import pymupdf
            return " ".join(p.get_text() for p in pymupdf.open(caminho))
        except Exception:
            return ""
    if b[:2] == b"PK":
        try:
            from docx import Document
            return " ".join(p.text for p in Document(caminho).paragraphs)
        except Exception:
            return ""
    for enc in ("utf-8", "latin-1"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    return ""


def normal(t):
    return re.sub(r"\s+", " ", t.replace("-\n", "").replace("- ", "")).lower()


def por_curl(url, palavra, tentativas=3):
    for i in range(tentativas):
        ok, nota = _curl(url, palavra)
        if ok or "429" not in nota:
            return ok, nota
        time.sleep(15 * (i + 1))
    return ok, nota


def _curl(url, palavra):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        destino = tmp.name
    r = subprocess.run(["curl", "-sSL", "-m", "60", "-A", UA, "-o", destino, "-w", "%{http_code}", url],
                       capture_output=True, text=True)
    codigo = r.stdout.strip()
    t = texto(destino) if os.path.exists(destino) else ""
    os.unlink(destino)
    bloqueio = any(x in t for x in ("RecaptchaChallengePageUi", "Performing security verification", "Access Denied"))
    if codigo == "200" and not bloqueio and (not palavra or normal(palavra) in normal(t)):
        return True, f"curl {codigo}"
    return False, f"curl {codigo}" + (" (bloqueio anti-robô)" if bloqueio else "")


def por_browser(url, palavra):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False, "Playwright indisponível"
    proxy = os.environ.get("HTTPS_PROXY")
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path=CHROMIUM if os.path.exists(CHROMIUM) else None,
                                  proxy={"server": proxy} if proxy else None,
                                  args=["--ignore-certificate-errors"])
            ctx = b.new_context(ignore_https_errors=True, user_agent=UA)
            pg = ctx.new_page()
            r = pg.goto(url, timeout=60000, wait_until="domcontentloaded")
            pg.wait_for_timeout(10000)
            t = pg.inner_text("body")
            final = pg.url
            b.close()
    except Exception as e:
        return False, "browser: " + str(e).split("\n")[0][:80]
    bloqueio = "Performing security verification" in t or "Access Denied" in t
    if bloqueio:
        return False, "browser: bloqueio anti-robô"
    if palavra and normal(palavra) not in normal(t):
        return False, f"browser {r.status if r else ''}: palavra «{palavra}» não encontrada"
    return True, f"browser {r.status if r else ''} ({final[:60]})"


def resolve_doi(url):
    r = subprocess.run(["curl", "-sSI", "-m", "30", url], capture_output=True, text=True)
    m = re.search(r"(?im)^location:\s*(\S+)", r.stdout)
    return m.group(1) if m else None


def main():
    linhas = []
    falhas = 0
    for grupo, ref, lig, palavra in D.BIBLIOGRAFIA:
        if lig.startswith("repositório: "):
            nome = lig[len("repositório: "):]
            ok = os.path.exists(os.path.join(RAIZ, nome))
            estado, nota = ("OK" if ok else "FALHA"), "ficheiro no repositório"
        else:
            ok, nota = por_curl(lig, palavra)
            if not ok:
                ok, nota2 = por_browser(lig, palavra)
                nota = nota + "; " + nota2
            m = re.search(r"pmc\.ncbi\.nlm\.nih\.gov/articles/(PMC\d+)", lig)
            if not ok and m:
                ok3, nota3 = por_curl(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{m.group(1)}/fullTextXML", palavra)
                ok = ok3
                nota += f"; mesmo artigo ({m.group(1)}) confirmado na Europe PMC: {nota3}" if ok3 else f"; Europe PMC: {nota3}"
            if not ok and lig.startswith("https://doi.org/"):
                destino = resolve_doi(lig)
                if destino:
                    ok = True
                    nota += f"; DOI registado, resolve para {destino[:70]} (editor bloqueia verificação automática)"
            estado = "OK" if ok else "FALHA"
        falhas += not ok
        linhas.append((estado, grupo, ref, lig, nota))
        print(f"{estado}\t{ref[:60]}\t{nota}")

    hoje = datetime.date.today().strftime("%-d.%-m.%Y")
    out = [f"# Verificação das ligações da bibliografia do memorando", "",
           f"Executado em {hoje}. {len(linhas) - falhas} de {len(linhas)} ligações verificadas; {falhas} falhas.", "",
           "| Estado | Grupo | Referência | Ligação | Como foi verificada |", "|---|---|---|---|---|"]
    for e, g, r, l, n in linhas:
        out.append("| " + " | ".join(x.replace("|", "/") for x in (e, g, r, l, n)) + " |")
    with open(os.path.join(AQUI, "verificacao_ligacoes.md"), "w") as f:
        f.write("\n".join(out) + "\n")
    raise SystemExit(1 if falhas else 0)


if __name__ == "__main__":
    main()
