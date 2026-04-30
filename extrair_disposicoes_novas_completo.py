#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrai disposições novas do Regulamento 2023/0447 a partir do array ARTIGOS
do ficheiro gerar_comparativo_reuniao.py
"""

import csv
import sys
import os

# Importar os dados do script existente
sys.path.insert(0, '/home/user/Legislacao')

# Para evitar executar código, vamos parsear manualmente o ficheiro
import re

def extract_artigos_from_python():
    """Extrai o array ARTIGOS do ficheiro Python."""
    with open('/home/user/Legislacao/gerar_comparativo_reuniao.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Encontra a secção ARTIGOS
    start = content.find('ARTIGOS = [')
    if start == -1:
        print("Erro: ARTIGOS não encontrado")
        return []

    # Para simplificar, vamos usar um padrão estruturado
    # Procura cada artigo pelo padrão "id": "ART-
    artigos = []
    pattern = r'"id":\s*[\'"]([^"\']+)[\'"]'

    for match in re.finditer(pattern, content):
        artigo_id = match.group(1)
        # Encontra a posição deste artigo
        art_start = match.start()
        # Procura o próximo artigo
        next_match = re.search(pattern, content[art_start + 10:])
        if next_match:
            art_end = art_start + 10 + next_match.start()
        else:
            art_end = len(content)

        art_block = content[art_start:art_end]

        # Extrai campos
        artigos.append({
            "id": artigo_id,
            "bloco": art_block[:500]  # Primeiros 500 chars
        })

    return artigos

# Melhor abordagem: compilar o ficheiro Python e aceder aos dados
import ast
import json

def extract_artigos_ast():
    """Usa AST para extrair dados do Python."""
    try:
        # Lê o arquivo e procura o dict ARTIGOS
        with open('/home/user/Legislacao/gerar_comparativo_reuniao.py', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Encontra onde ARTIGOS começa
        artigos_start_idx = None
        for i, line in enumerate(lines):
            if 'ARTIGOS = [' in line:
                artigos_start_idx = i
                break

        if artigos_start_idx is None:
            print("Erro: ARTIGOS não encontrado")
            return []

        # Coleta as linhas até o fechamento de ]
        artigos_lines = []
        bracket_count = 0
        for i in range(artigos_start_idx, len(lines)):
            line = lines[i]
            artigos_lines.append(line)

            # Conta colchetes
            bracket_count += line.count('[')
            bracket_count -= line.count(']')

            if bracket_count == 0 and i > artigos_start_idx:
                break

        artigos_str = ''.join(artigos_lines)
        # Remove "ARTIGOS = " para deixar só a lista
        artigos_str = artigos_str.replace('ARTIGOS = ', '', 1)

        # Tenta avaliar
        artigos = eval(artigos_str)
        return artigos

    except Exception as e:
        print(f"Erro ao extrair com AST: {e}")
        return []

def main():
    print("\n" + "=" * 100)
    print("EXTRAÇÃO DE DISPOSIÇÕES NOVAS - Regulamento 2023/0447")
    print("Fonte: gerar_comparativo_reuniao.py")
    print("=" * 100)

    print("\n[1] Extractando dados da estrutura ARTIGOS...")
    artigos = extract_artigos_ast()

    if not artigos:
        print("Erro: Nenhum artigo extraído")
        sys.exit(1)

    print(f"    ✓ Extraídos {len(artigos)} artigos")

    # 2. Processa artigos
    print("\n[2] Processando artigos...")

    csv_rows = []
    artigos_novos = []
    artigos_com_correspondencia = []

    for i, artigo in enumerate(artigos, 1):
        if not isinstance(artigo, dict):
            continue

        art_id = artigo.get('id', f'ART-{i:02d}')
        tema = artigo.get('tema', '')
        regulamento = artigo.get('regulamento', {})
        rgbeac = artigo.get('rgbeac', {})
        codigo = artigo.get('codigo', {})
        legislacao = artigo.get('legislacao', {})
        divergencia = artigo.get('divergencia', {})

        # Extrai texto
        reg_titulo = regulamento.get('titulo', '')
        reg_texto = regulamento.get('texto', '')
        reg_traducao = regulamento.get('traducao', '')
        reg_ref = regulamento.get('ref', '')

        # Determina se é novo
        tem_rgbeac = rgbeac.get('texto', '').strip() and rgbeac.get('ref', '') != 'Sem correspondência'
        tem_codigo = codigo.get('texto', '').strip() and codigo.get('ref', '') != 'Sem correspondência'
        tem_legislacao = legislacao.get('texto', '').strip() and legislacao.get('ref', '') != 'Sem correspondência'

        eh_novo = not (tem_rgbeac or tem_codigo or tem_legislacao)

        sumario = divergencia.get('sumario', '')
        necessidade = artigo.get('necessidade_alteracao', '')

        # Cria linha CSV
        row = {
            'artigo_id': art_id,
            'numero': re.search(r'\d+', art_id).group() if re.search(r'\d+', art_id) else '',
            'tema': tema,
            'titulo_en': reg_titulo,
            'ref_regulamento': reg_ref,
            'tem_correspondencia_rgbeac': 'Sim' if tem_rgbeac else 'Não',
            'tem_correspondencia_codigo': 'Sim' if tem_codigo else 'Não',
            'tem_correspondencia_legislacao': 'Sim' if tem_legislacao else 'Não',
            'classificacao': 'NOVO' if eh_novo else 'COM CORRESPONDÊNCIA',
            'resumo_sumario': sumario[:200] if sumario else '',
            'necessidade_alteracao': necessidade,
            'tamanho_texto_en': len(reg_texto),
        }

        csv_rows.append(row)

        if eh_novo:
            artigos_novos.append({
                'artigo_id': art_id,
                'numero': re.search(r'\d+', art_id).group() if re.search(r'\d+', art_id) else '',
                'tema': tema,
                'titulo_en': reg_titulo,
                'titulo_pt': '',  # Não disponível no script
                'texto_en': reg_texto[:1000],  # Primeiros 1000 chars
                'traducao_pt': reg_traducao[:1000],
                'ref_regulamento': reg_ref,
                'sumario': sumario,
                'motivo_novo': 'Sem correspondência em @codigo, @rgbeac ou legislação portuguesa vigente',
            })
        else:
            artigos_com_correspondencia.append({
                'artigo_id': art_id,
                'tema': tema,
                'titulo': reg_titulo,
                'correspondencia_rgbeac': 'Sim' if tem_rgbeac else 'Não',
                'correspondencia_codigo': 'Sim' if tem_codigo else 'Não',
                'correspondencia_legislacao': 'Sim' if tem_legislacao else 'Não',
            })

    # 3. Grava CSVs
    print("\n[3] Gravando CSVs...")

    # CSV resumido (artigo a artigo)
    csv_resumido = '/home/user/Legislacao/disposicoes_novas_resumido.csv'
    with open(csv_resumido, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=csv_rows[0].keys() if csv_rows else [])
        writer.writeheader()
        writer.writerows(csv_rows)
    print(f"    ✓ {csv_resumido}")

    # CSV completo (artigos novos)
    if artigos_novos:
        csv_novos_completo = '/home/user/Legislacao/disposicoes_novas_completo.csv'
        with open(csv_novos_completo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=artigos_novos[0].keys() if artigos_novos else [])
            writer.writeheader()
            writer.writerows(artigos_novos)
        print(f"    ✓ {csv_novos_completo}")

    # CSV artigos com correspondência
    if artigos_com_correspondencia:
        csv_correspondencia = '/home/user/Legislacao/disposicoes_com_correspondencia.csv'
        with open(csv_correspondencia, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=artigos_com_correspondencia[0].keys())
            writer.writeheader()
            writer.writerows(artigos_com_correspondencia)
        print(f"    ✓ {csv_correspondencia}")

    # Sumário
    print("\n" + "=" * 100)
    print("SUMÁRIO")
    print("=" * 100)
    print(f"Total de artigos analisados:        {len(artigos)}")
    print(f"Artigos NOVOS (sem correspondência): {len(artigos_novos)}")
    print(f"Artigos COM correspondência:        {len(artigos_com_correspondencia)}")

    print("\n--- ARTIGOS TOTALMENTE NOVOS ---")
    for art in artigos_novos[:10]:  # Primeiros 10
        print(f"\n  {art['artigo_id']}: {art['titulo_en']}")
        if art['sumario']:
            print(f"     {art['sumario'][:100]}...")

    if len(artigos_novos) > 10:
        print(f"\n  ... e mais {len(artigos_novos) - 10} artigos novos")

if __name__ == "__main__":
    main()
