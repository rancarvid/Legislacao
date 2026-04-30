#!/usr/bin/env python3
"""
AUDITORIA COMPLETA - Verificação de correspondências entre Regulamento 2023/0447 e legislação nacional
Verifica se as referências do script gerar_comparativo_reuniao.py realmente existem nos ficheiros
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

# Lista de ficheiros legislação (para análise @legislacao)
LEGISLACAO_FICHEIROS = [
    REPO_BASE / "Decreto-Lei n.º 276-2001, de 17 de outubro v2.docx",
    REPO_BASE / "DL n. 82_2019, de 27 de Junho_ocred.docx",
    REPO_BASE / "Lei n.º 27_2016, de 23 de agosto - Aprova medidas para a criação de uma rede de centros de recolha oficial de animais e estabelece a proibição do abate de animais errantes como forma de controlo da população_ocred.docx",
]

print("=" * 100)
print("AUDITORIA DE CORRESPONDÊNCIAS — Regulamento 2023/0447")
print("=" * 100)
print(f"\n[1] Verificando ficheiros...")
print(f"  @codigo: {CODIGO_FICHEIRO.name} — {CODIGO_FICHEIRO.exists()}")
print(f"  @rgbeac: {RGBEAC_FICHEIRO.name} — {RGBEAC_FICHEIRO.exists()}")
print(f"  @legislacao: {len([f for f in LEGISLACAO_FICHEIROS if f.exists()])} ficheiros encontrados")

# ============================================================================
# PARTE 1: Extrair correspondências do script
# ============================================================================

def extrair_artigos_do_script():
    """Extrai array ARTIGOS do gerar_comparativo_reuniao.py"""
    with open(SCRIPT_COMPARATIVO, 'r', encoding='utf-8') as f:
        content = f.read()

    # Localizar o início do array ARTIGOS
    start = content.find('ARTIGOS = [')
    if start == -1:
        print("ERRO: Não consegue encontrar ARTIGOS = [")
        return []

    # Procurar todos os blocos de dicionário com "id" como chave
    artigos_script = []

    # Usar regex para extrair cada artigo
    pattern = r'\{\s*"id":\s*[\'"]([^\'"]+)[\'"].*?"regulamento":\s*\{[^}]*?"ref":\s*[\'"]([^\'"]+)[\'"].*?"rgbeac":\s*\{[^}]*?"ref":\s*[\'"]([^\'"]+)[\'"].*?"codigo":\s*\{[^}]*?"ref":\s*[\'"]([^\'"]+)[\'"].*?"legislacao":\s*\{[^}]*?"ref":\s*[\'"]([^\'"]+)[\'"]'

    # Mais simples: fazer parsing JSON
    print("\n[2] Extraindo correspondências do script...")
    import ast

    # Encontrar ARTIGOS = [ ... ]
    start_idx = content.find('ARTIGOS = [')
    if start_idx == -1:
        print("ERRO: Não consegue encontrar ARTIGOS")
        return []

    # Procurar o final (última ] antes de uma nova variável global ou if/def)
    # Vamos procurar "ARTIGOS = [" e depois o próximo "]\n" que finaliza a lista
    # Estratégia: encontrar todas as linhas com "id": e depois associar

    lines = content.split('\n')
    artigos = []
    current_article = None
    brace_count = 0
    in_artigos = False

    for i, line in enumerate(lines[lines.index(next(l for l in lines if 'ARTIGOS = [' in l)):]):
        if 'ARTIGOS = [' in line:
            in_artigos = True
            continue

        if not in_artigos:
            continue

        if '],  # fim ARTIGOS' in line or (line.strip() == ']' and brace_count == 0):
            if current_article:
                artigos.append(current_article)
            break

        # Procurar "id" para iniciar novo artigo
        if '"id":' in line and '{' in line:
            if current_article:
                artigos.append(current_article)
            # Extract id
            id_match = re.search(r'"id":\s*[\'"]([^\'"]+)[\'"]', line)
            if id_match:
                current_article = {
                    'id': id_match.group(1),
                    'codigo_ref': None,
                    'rgbeac_ref': None,
                    'legislacao_ref': None,
                }

        # Procurar referências
        if current_article and '"codigo":' in line and '"ref":' in line:
            ref_match = re.search(r'"ref":\s*[\'"]([^\'"]+)[\'"]', line)
            if ref_match:
                current_article['codigo_ref'] = ref_match.group(1)

        if current_article and '"rgbeac":' in line and '"ref":' in line:
            ref_match = re.search(r'"ref":\s*[\'"]([^\'"]+)[\'"]', line)
            if ref_match:
                current_article['rgbeac_ref'] = ref_match.group(1)

        if current_article and '"legislacao":' in line and '"ref":' in line:
            ref_match = re.search(r'"ref":\s*[\'"]([^\'"]+)[\'"]', line)
            if ref_match:
                current_article['legislacao_ref'] = ref_match.group(1)

    # Melhor abordagem: procurar manualmente por padrões
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

# ============================================================================
# PARTE 2: Ler documentos e indexar artigos
# ============================================================================

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

def indexar_artigos_documento(paragrafos, nome_documento):
    """Indexa artigos num documento (ex: "Artigo 5.º", "Artigo 10.º", etc.)"""
    artigos_index = {}

    # Padrões para encontrar artigos: "Artigo X.º", "Art.º X", etc.
    patterns = [
        r'Artigo\s+(\d+)\.º',
        r'Art\.º\s+(\d+)',
        r'ARTIGO\s+(\d+)',
        r'^(\d+)\s*[-–]',  # Apenas número no início da linha
    ]

    current_art = None
    current_text = []

    for para in paragrafos:
        # Procurar número de artigo
        found_art = False
        for pattern in patterns:
            match = re.search(pattern, para, re.IGNORECASE)
            if match:
                art_num = match.group(1)
                # Guardar artigo anterior se existe
                if current_art is not None:
                    artigos_index[current_art] = ' '.join(current_text)
                current_art = int(art_num)
                current_text = [para]
                found_art = True
                break

        if not found_art and current_art is not None:
            current_text.append(para)

    # Guardar último artigo
    if current_art is not None:
        artigos_index[current_art] = ' '.join(current_text)

    return artigos_index

def verificar_correspondencia(art_ref, documento_paragrafos):
    """Verifica se uma referência "Art.º X.º" existe realmente no documento
    Retorna: (existe, conteudo, palavras-chave relevantes)
    """
    if not art_ref or art_ref == 'Sem correspondência':
        return False, '', []

    # Extrair número do artigo
    match = re.search(r'Art\.º\s*(\d+)', art_ref)
    if not match:
        # Tentar outros padrões
        match = re.search(r'Artigo\s+(\d+)', art_ref)
    if not match:
        match = re.search(r'^(\d+)', art_ref)

    if not match:
        return False, 'Formato de referência não reconhecido', []

    art_num = int(match.group(1))

    # Procurar no documento
    artigos_index = indexar_artigos_documento(documento_paragrafos, '')

    if art_num in artigos_index:
        content = artigos_index[art_num]
        # Extrair palavras-chave (primeiras 100 caracteres)
        preview = content[:150].replace('\n', ' ')
        return True, content, preview

    return False, '', []

# ============================================================================
# PARTE 3: Executar auditoria
# ============================================================================

print("\n[3] Lendo documentos...")
codigo_paragrafos = ler_documento_docx(CODIGO_FICHEIRO)
rgbeac_paragrafos = ler_documento_docx(RGBEAC_FICHEIRO)
print(f"  ✓ @codigo: {len(codigo_paragrafos)} parágrafos")
print(f"  ✓ @rgbeac: {len(rgbeac_paragrafos)} parágrafos")

print("\n[4] Extraindo artigos do script...")
artigos_script = extrair_artigos_do_script()

print("\n[5] AUDITORIA — Verificando correspondências...")
print("-" * 100)

erros = []
resultados = []

for artigo in artigos_script[:33]:  # Apenas os 33 artigos principais
    art_id = artigo['id']

    # Verificar @codigo
    codigo_existe, codigo_content, codigo_preview = verificar_correspondencia(
        artigo['codigo_ref'], codigo_paragrafos
    )
    codigo_erro = not codigo_existe if artigo['codigo_ref'] != 'Sem correspondência' else False

    # Verificar @rgbeac
    rgbeac_existe, rgbeac_content, rgbeac_preview = verificar_correspondencia(
        artigo['rgbeac_ref'], rgbeac_paragrafos
    )
    rgbeac_erro = not rgbeac_existe if artigo['rgbeac_ref'] != 'Sem correspondência' else False

    resultado = {
        'art_regulamento': art_id,
        'codigo_ref_script': artigo['codigo_ref'],
        'codigo_verif': 'OK' if (codigo_existe or artigo['codigo_ref'] == 'Sem correspondência') else 'NÃO ENCONTRADO',
        'rgbeac_ref_script': artigo['rgbeac_ref'],
        'rgbeac_verif': 'OK' if (rgbeac_existe or artigo['rgbeac_ref'] == 'Sem correspondência') else 'NÃO ENCONTRADO',
        'legislacao_ref_script': artigo['legislacao_ref'],
        'erro': 'SIM' if (codigo_erro or rgbeac_erro) else 'NÃO',
        'descricao_erro': []
    }

    if codigo_erro:
        resultado['descricao_erro'].append(f"@codigo: Ref '{artigo['codigo_ref']}' não encontrada no documento")

    if rgbeac_erro:
        resultado['descricao_erro'].append(f"@rgbeac: Ref '{artigo['rgbeac_ref']}' não encontrada no documento")

    resultado['descricao_erro'] = ' | '.join(resultado['descricao_erro']) if resultado['descricao_erro'] else '-'

    resultados.append(resultado)

    if codigo_erro or rgbeac_erro:
        erros.append(resultado)
        print(f"⚠️  {art_id}")
        if codigo_erro:
            print(f"   ERRO @codigo: '{artigo['codigo_ref']}'")
        if rgbeac_erro:
            print(f"   ERRO @rgbeac: '{artigo['rgbeac_ref']}'")

print("-" * 100)
print(f"\n[6] RESUMO DE ERROS")
print(f"  Total de artigos analisados: {len(resultados)}")
print(f"  Artigos com ERRO: {len(erros)}")
print(f"  Artigos OK: {len(resultados) - len(erros)}")

# ============================================================================
# PARTE 4: Exportar CSV
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
        'descricao_erro'
    ])
    writer.writeheader()
    writer.writerows(resultados)

print(f"  ✓ CSV salvo: {csv_path}")

# ============================================================================
# DETALHES DE ERROS
# ============================================================================

if erros:
    print("\n[8] DETALHES DE ERROS")
    print("=" * 100)
    for erro in erros:
        print(f"\n{erro['art_regulamento']}")
        print(f"  @codigo ref script: {erro['codigo_ref_script']}")
        print(f"  @codigo verificação: {erro['codigo_verif']}")
        print(f"  @rgbeac ref script: {erro['rgbeac_ref_script']}")
        print(f"  @rgbeac verificação: {erro['rgbeac_verif']}")
        print(f"  Erro: {erro['descricao_erro']}")

print("\n" + "=" * 100)
print("FIM DA AUDITORIA")
print("=" * 100)
