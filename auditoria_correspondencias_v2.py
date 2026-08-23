#!/usr/bin/env python3
"""
AUDITORIA COMPLETA v2 - Verificação de correspondências entre Regulamento 2023/0447 e legislação nacional
Detecta apenas ERROS REAIS (referências que deveriam existir mas não existem)
Distingue entre não-referências intencionais e referências quebradas
"""

import sys
import json
import re
import csv
from pathlib import Path
from docx import Document
from collections import defaultdict

# Caminho dos ficheiros
REPO_BASE = Path("/home/user/Legislacao")
SCRIPT_COMPARATIVO = REPO_BASE / "gerar_comparativo_reuniao.py"
CODIGO_FICHEIRO = REPO_BASE / "Código do Animal DL214.2013_OCR.docx.docx"
RGBEAC_FICHEIRO = REPO_BASE / "RGBEAC_junh_2025 Original com Índice.docx"

# Padrões de não-referência (intencionais)
NENHUMA_CORRESPONDENCIA = [
    'não se aplica',
    'sem correspondência',
    'sem equivalência',
    'análise no anexo',
    'ver tabela anexo',
]

print("=" * 100)
print("AUDITORIA DE CORRESPONDÊNCIAS v2 — Regulamento 2023/0447")
print("=" * 100)
print(f"\n[1] Verificando ficheiros...")
print(f"  @codigo: {CODIGO_FICHEIRO.name} — {CODIGO_FICHEIRO.exists()}")
print(f"  @rgbeac: {RGBEAC_FICHEIRO.name} — {RGBEAC_FICHEIRO.exists()}")

# ============================================================================
# PARTE 1: Extrair correspondências do script
# ============================================================================

def extrair_artigos_do_script():
    """Extrai array ARTIGOS do gerar_comparativo_reuniao.py"""
    with open(SCRIPT_COMPARATIVO, 'r', encoding='utf-8') as f:
        content = f.read()

    artigos = []

    # Procurar todos os blocos "ART-XX"
    art_pattern = r'"id":\s*\'(ART-\d+)\''
    for match in re.finditer(art_pattern, content):
        art_id = match.group(1)
        # Procurar o bloco completo deste artigo
        start_pos = match.start()
        # Encontrar a próxima "id" ou fim do array
        next_id_pos = content.find('"id":', start_pos + 5)
        if next_id_pos == -1:
            block = content[start_pos:start_pos+10000]
        else:
            block = content[start_pos:next_id_pos]

        # Extrair refs do bloco
        codigo_ref = re.search(r'"codigo":\s*\{\s*"ref":\s*\'([^\']*)\''    , block)
        rgbeac_ref = re.search(r'"rgbeac":\s*\{\s*"ref":\s*\'([^\']*)\''    , block)
        legislacao_ref = re.search(r'"legislacao":\s*\{\s*"ref":\s*\'([^\']*)\''    , block)

        artigos.append({
            'id': art_id,
            'codigo_ref': codigo_ref.group(1) if codigo_ref else 'Sem correspondência',
            'rgbeac_ref': rgbeac_ref.group(1) if rgbeac_ref else 'Sem correspondência',
            'legislacao_ref': legislacao_ref.group(1) if legislacao_ref else 'Sem correspondência',
        })

    print(f"  ✓ Extraídos {len(artigos)} artigos do script")
    return artigos

def eh_nenhuma_correspondencia(ref):
    """Verifica se ref é uma não-referência intencional"""
    ref_lower = ref.lower().strip()
    for pattern in NENHUMA_CORRESPONDENCIA:
        if pattern in ref_lower:
            return True
    return False

def extrair_numero_artigo(ref):
    """Extrai número do artigo de uma referência como 'Art.º 5.º' ou 'Arts. 4.º e 5.º'
    Retorna lista de números encontrados
    """
    if eh_nenhuma_correspondencia(ref):
        return []

    # Padrões: "Art.º X", "Arts. X", "Art. X", "Artigo X"
    # Também casos como "Arts. 4.º e 5.º" → [4, 5]
    # E "arts.º 69.º, 84.º e 90.º" → [69, 84, 90]

    nums = []

    # Remover "do/da/de" preposições
    ref_clean = re.sub(r'\bdo\b|\bda\b|\bde\b|\bdos\b|\bdas\b', '', ref, flags=re.IGNORECASE)

    # Procurar todos os números seguidos de º ou de . ou de nada
    pattern = r'(\d+)\s*[º\.]?'
    for match in re.finditer(pattern, ref_clean):
        num = int(match.group(1))
        if 1 <= num <= 500:  # filtro básico
            if num not in nums:
                nums.append(num)

    return sorted(list(set(nums)))

def ler_documento_docx(caminho):
    """Lê documento .docx e retorna lista de parágrafos"""
    try:
        doc = Document(caminho)
        paragrafos = []
        for para in doc.paragraphs:
            if para.text.strip():
                paragrafos.append(para.text.strip())
        return paragrafos
    except Exception as e:
        print(f"  ERRO ao ler {caminho.name}: {e}")
        return []

def indexar_artigos_documento(paragrafos):
    """Indexa artigos num documento (ex: "Artigo 5.º" → {5: "conteúdo..."})"""
    artigos_index = {}

    # Padrões para encontrar artigos
    patterns = [
        (r'Artigo\s+(\d+)\.º', 'PT'),
        (r'Art\.º\s+(\d+)', 'PT'),
        (r'Article\s+(\d+)', 'EN'),
        (r'Art\.\s+(\d+)', 'EN'),
    ]

    current_art = None
    current_text = []

    for para in paragrafos:
        # Procurar número de artigo
        found_art = False
        for pattern, lang in patterns:
            match = re.search(pattern, para, re.IGNORECASE)
            if match:
                art_num = int(match.group(1))
                # Guardar artigo anterior se existe
                if current_art is not None and current_art not in artigos_index:
                    artigos_index[current_art] = ' '.join(current_text[:500])  # Primeiros 500 chars
                current_art = art_num
                current_text = [para]
                found_art = True
                break

        if not found_art and current_art is not None:
            current_text.append(para)

    # Guardar último artigo
    if current_art is not None and current_art not in artigos_index:
        artigos_index[current_art] = ' '.join(current_text[:500])

    return artigos_index

def verificar_artigos_existem(numeros_artigos, documento_paragrafos):
    """Verifica se múltiplos artigos (números) existem no documento
    Retorna: (todos_existem, encontrados, nao_encontrados)
    """
    if not numeros_artigos:
        return True, [], []  # Sem números para procurar = OK

    artigos_index = indexar_artigos_documento(documento_paragrafos)

    encontrados = []
    nao_encontrados = []

    for num in numeros_artigos:
        if num in artigos_index:
            encontrados.append(num)
        else:
            nao_encontrados.append(num)

    return len(nao_encontrados) == 0, encontrados, nao_encontrados

# ============================================================================
# PARTE 2: Executar auditoria
# ============================================================================

print("\n[2] Lendo documentos...")
codigo_paragrafos = ler_documento_docx(CODIGO_FICHEIRO)
rgbeac_paragrafos = ler_documento_docx(RGBEAC_FICHEIRO)
print(f"  ✓ @codigo: {len(codigo_paragrafos)} parágrafos")
print(f"  ✓ @rgbeac: {len(rgbeac_paragrafos)} parágrafos")

print("\n[3] Extraindo artigos do script...")
artigos_script = extrair_artigos_do_script()

print("\n[4] AUDITORIA — Verificando correspondências...")
print("-" * 100)

erros = []
resultados = []

for artigo in artigos_script[:33]:  # Apenas os 33 artigos principais
    art_id = artigo['id']

    # ========== @CODIGO ==========
    codigo_ref = artigo['codigo_ref']
    if eh_nenhuma_correspondencia(codigo_ref):
        # Sem correspondência intencional
        codigo_status = '(sem correspondência intencional)'
        codigo_erro = False
    else:
        # Verificar se os artigos existem
        numeros = extrair_numero_artigo(codigo_ref)
        if not numeros:
            # Não consegue extrair número — erro de formato
            codigo_status = f'ERRO: Não consegue extrair número de: {codigo_ref}'
            codigo_erro = True
        else:
            existe, encontrados, nao_encontrados = verificar_artigos_existem(numeros, codigo_paragrafos)
            if existe:
                codigo_status = f'OK: Arts. {encontrados} encontrados'
                codigo_erro = False
            else:
                codigo_status = f'ERRO: Arts. {nao_encontrados} NÃO encontrados (procurados: {numeros})'
                codigo_erro = True

    # ========== @RGBEAC ==========
    rgbeac_ref = artigo['rgbeac_ref']
    if eh_nenhuma_correspondencia(rgbeac_ref):
        # Sem correspondência intencional
        rgbeac_status = '(sem correspondência intencional)'
        rgbeac_erro = False
    else:
        # Verificar se os artigos existem
        numeros = extrair_numero_artigo(rgbeac_ref)
        if not numeros:
            # Não consegue extrair número — erro de formato
            rgbeac_status = f'ERRO: Não consegue extrair número de: {rgbeac_ref}'
            rgbeac_erro = True
        else:
            existe, encontrados, nao_encontrados = verificar_artigos_existem(numeros, rgbeac_paragrafos)
            if existe:
                rgbeac_status = f'OK: Arts. {encontrados} encontrados'
                rgbeac_erro = False
            else:
                rgbeac_status = f'ERRO: Arts. {nao_encontrados} NÃO encontrados (procurados: {numeros})'
                rgbeac_erro = True

    # ========== RESULTADO ==========
    resultado = {
        'art_regulamento': art_id,
        'codigo_ref_script': codigo_ref,
        'codigo_verif': codigo_status,
        'rgbeac_ref_script': rgbeac_ref,
        'rgbeac_verif': rgbeac_status,
        'legislacao_ref_script': artigo['legislacao_ref'],
        'erro': 'SIM' if (codigo_erro or rgbeac_erro) else 'NÃO',
    }

    resultados.append(resultado)

    if codigo_erro or rgbeac_erro:
        erros.append(resultado)
        print(f"⚠️  {art_id}")
        if codigo_erro:
            print(f"   @codigo: {codigo_status}")
        if rgbeac_erro:
            print(f"   @rgbeac: {rgbeac_status}")

print("-" * 100)
print(f"\n[5] RESUMO")
print(f"  Total de artigos analisados: {len(resultados)}")
print(f"  Artigos com ERRO: {len(erros)}")
print(f"  Artigos OK: {len(resultados) - len(erros)}")

# ============================================================================
# PARTE 3: Exportar CSV
# ============================================================================

print("\n[6] Exportando CSV...")
csv_path = REPO_BASE / "AUDITORIA_CORRESPONDENCIAS_v2.csv"

with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'art_regulamento',
        'codigo_ref_script',
        'codigo_verif',
        'rgbeac_ref_script',
        'rgbeac_verif',
        'legislacao_ref_script',
        'erro',
    ])
    writer.writeheader()
    writer.writerows(resultados)

print(f"  ✓ CSV salvo: {csv_path}")

# ============================================================================
# DETALHES DE ERROS
# ============================================================================

if erros:
    print("\n[7] DETALHES DE ERROS (apenas erros reais)")
    print("=" * 100)
    for erro in erros:
        print(f"\n{erro['art_regulamento']}")
        print(f"  @codigo: {erro['codigo_ref_script']}")
        print(f"    Verificação: {erro['codigo_verif']}")
        print(f"  @rgbeac: {erro['rgbeac_ref_script']}")
        print(f"    Verificação: {erro['rgbeac_verif']}")

print("\n" + "=" * 100)
print("FIM DA AUDITORIA")
print("=" * 100)

# ============================================================================
# RESUMO EXECUTIVO
# ============================================================================

print("\n[8] RESUMO EXECUTIVO")
print("-" * 100)

tipo_erros = defaultdict(int)
for erro in erros:
    if 'ERRO' in erro['codigo_verif']:
        tipo_erros['@codigo - artigos não encontrados'] += 1
    if 'ERRO' in erro['rgbeac_verif']:
        tipo_erros['@rgbeac - artigos não encontrados'] += 1

if tipo_erros:
    for tipo, count in tipo_erros.items():
        print(f"  {count}x {tipo}")
else:
    print("  Nenhum erro real encontrado!")

print("\nObservação: Referências com 'Não se aplica', 'Sem equivalência', etc.")
print("            são VÁLIDAS (não-correspondências intencionais).")
print("-" * 100)
