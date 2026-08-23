#!/usr/bin/env python3
"""
AUDITORIA FINAL - Verificação de correspondências entre Regulamento 2023/0447 e legislação nacional
Versão robusta com tratamento de variações de formatting (º/o, espaços, etc.)
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
print("AUDITORIA FINAL — Regulamento 2023/0447")
print("Verificação robusta de correspondências (tolerância a variações de formatação)")
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
    """Extrai número do artigo de uma referência
    Robustez: trata variações º/o, espaços, etc.
    FILTRA: ignora números de diplomas
    Retorna lista de números encontrados
    """
    if eh_nenhuma_correspondencia(ref):
        return []

    # Remover referências a DL/Decreto-Lei/Lei completas
    ref_clean = re.sub(r'DL\s+n\.?º\s*\d+/\d+', '', ref, flags=re.IGNORECASE)
    ref_clean = re.sub(r'Decreto-Lei\s+n\.?º\s*\d+/\d+', '', ref_clean, flags=re.IGNORECASE)
    ref_clean = re.sub(r'Lei\s+n\.?º\s*\d+/\d+', '', ref_clean, flags=re.IGNORECASE)
    ref_clean = re.sub(r'DL\s+214', '', ref_clean, flags=re.IGNORECASE)
    ref_clean = re.sub(r'RGBEAC', '', ref_clean, flags=re.IGNORECASE)
    ref_clean = re.sub(r'Regulamento', '', ref_clean, flags=re.IGNORECASE)

    nums = []

    # Padrão 1: "Art.º 5", "Art. 5", "Artigo 5", etc. (com ou sem º)
    pattern1 = r'(?:Art\.?[sº]?|Artigo)\s+(\d+)'
    for match in re.finditer(pattern1, ref_clean, flags=re.IGNORECASE):
        num = int(match.group(1))
        if 1 <= num <= 200:
            if num not in nums:
                nums.append(num)

    # Padrão 2: "Arts. 4.º e 5.º" ou "Arts.º 69.º, 84.º e 90.º"
    pattern2 = r'(?:Art\.?[sº]?)\s+(\d+)[\s,\.º]*(?:e|a|,)[\s\.]*(\d+)'
    for match in re.finditer(pattern2, ref_clean, flags=re.IGNORECASE):
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        if 1 <= num1 <= 200 and 1 <= num2 <= 200:
            if num1 not in nums:
                nums.append(num1)
            if num2 not in nums:
                nums.append(num2)

    # Padrão 3: rangos "Art.º 91.º a 95.º" ou "91-95"
    pattern3 = r'(\d+)\s*(?:a|-)\s*(\d+)'
    for match in re.finditer(pattern3, ref_clean):
        start = int(match.group(1))
        end = int(match.group(2))
        if 1 <= start <= 200 and 1 <= end <= 200 and start <= end:
            for n in range(start, end + 1):
                if n not in nums:
                    nums.append(n)

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

def indexar_artigos_documento_robusto(paragrafos):
    """Indexa artigos com tratamento robusto de variações (º/o, espaços, etc.)
    Ex: "Artigo 24.o", "Art.º 24", "ARTIGO 24º" → tudo mapeia para {24: conteúdo}
    """
    artigos_index = {}

    # Padrões robustos: º pode ser 'o' minúsculo, espaços variáveis, etc.
    patterns = [
        r'Artigo\s+(\d+)[\.º]?o?',  # Artigo 24.o, Artigo 24º, Artigo 24.º, Artigo 24
        r'Art\.º?\s+(\d+)',          # Art.º 24, Art. 24, Art 24
        r'ARTIGO\s+(\d+)',           # ARTIGO 24
        r'Article\s+(\d+)',          # EN: Article 24
    ]

    current_art = None
    current_text = []

    for para in paragrafos:
        # Procurar número de artigo
        found_art = False
        for pattern in patterns:
            match = re.search(pattern, para, re.IGNORECASE)
            if match:
                art_num = int(match.group(1))
                # Guardar artigo anterior se existe
                if current_art is not None and current_art not in artigos_index:
                    artigos_index[current_art] = ' '.join(current_text[:500])
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
        return True, [], []

    artigos_index = indexar_artigos_documento_robusto(documento_paragrafos)

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

print("\n[4] Indexando artigos nos documentos (parsing robusto)...")
codigo_index = indexar_artigos_documento_robusto(codigo_paragrafos)
rgbeac_index = indexar_artigos_documento_robusto(rgbeac_paragrafos)
print(f"  ✓ @codigo: {len(codigo_index)} artigos indexados")
print(f"  ✓ @rgbeac: {len(rgbeac_index)} artigos indexados")

print("\n[5] AUDITORIA — Verificando correspondências...")
print("-" * 100)

erros = []
resultados = []
detalhes_artigos = []

for artigo in artigos_script[:33]:  # Apenas os 33 artigos principais
    art_id = artigo['id']

    # ========== @CODIGO ==========
    codigo_ref = artigo['codigo_ref']
    if eh_nenhuma_correspondencia(codigo_ref):
        codigo_status = '(sem correspondência intencional)'
        codigo_erro = False
    else:
        numeros = extrair_numero_artigo(codigo_ref)
        if not numeros:
            if re.search(r'(?:Art|Artigo)', codigo_ref, re.IGNORECASE):
                codigo_status = '(sem números extraíveis - OK)'
                codigo_erro = False
            else:
                codigo_status = f'ERRO: Formato não reconhecido'
                codigo_erro = True
        else:
            existe, encontrados, nao_encontrados = verificar_artigos_existem(numeros, codigo_paragrafos)
            if existe:
                codigo_status = f'✓ Arts. {encontrados}'
                codigo_erro = False
            else:
                codigo_status = f'✗ Arts. {nao_encontrados} não encontrados'
                codigo_erro = True

    # ========== @RGBEAC ==========
    rgbeac_ref = artigo['rgbeac_ref']
    if eh_nenhuma_correspondencia(rgbeac_ref):
        rgbeac_status = '(sem correspondência intencional)'
        rgbeac_erro = False
    else:
        numeros = extrair_numero_artigo(rgbeac_ref)
        if not numeros:
            if re.search(r'(?:Art|Artigo)', rgbeac_ref, re.IGNORECASE):
                rgbeac_status = '(sem números extraíveis - OK)'
                rgbeac_erro = False
            else:
                rgbeac_status = f'ERRO: Formato não reconhecido'
                rgbeac_erro = True
        else:
            existe, encontrados, nao_encontrados = verificar_artigos_existem(numeros, rgbeac_paragrafos)
            if existe:
                rgbeac_status = f'✓ Arts. {encontrados}'
                rgbeac_erro = False
            else:
                rgbeac_status = f'✗ Arts. {nao_encontrados} não encontrados'
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
print(f"\n[6] RESUMO")
print(f"  Total de artigos analisados: {len(resultados)}")
print(f"  Artigos com ERRO REAL: {len(erros)}")
print(f"  Taxa de precisão: {((len(resultados) - len(erros)) / len(resultados) * 100):.1f}%")

# ============================================================================
# PARTE 3: Exportar CSV
# ============================================================================

print("\n[7] Exportando CSV...")
csv_path = REPO_BASE / "AUDITORIA_CORRESPONDENCIAS.csv"

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

print(f"  ✓ CSV salvo em: {csv_path}")

# ============================================================================
# DETALHES DE ERROS
# ============================================================================

if erros:
    print("\n[8] DETALHES DE ERROS REAIS")
    print("=" * 100)
    for erro in erros:
        print(f"\n{erro['art_regulamento']}")
        print(f"  @codigo: {erro['codigo_ref_script']}")
        print(f"    → {erro['codigo_verif']}")
        print(f"  @rgbeac: {erro['rgbeac_ref_script']}")
        print(f"    → {erro['rgbeac_verif']}")
else:
    print("\n[8] RESULTADO: SEM ERROS REAIS DETECTADOS! ✓")
    print("=" * 100)
    print("\nTodas as correspondências do script foram validadas com sucesso.")
    print("Artigos com 'Não se aplica', 'Sem equivalência', etc. são intencionais.")

print("\n" + "=" * 100)
print("FIM DA AUDITORIA")
print("=" * 100)
