#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extração FINAL de disposições novas do Regulamento 2023/0447
Parseia gerar_comparativo_reuniao.py e gera CSVs estruturados
"""

import re
import csv
from collections import defaultdict

def extract_field(text, field_name):
    """Extrai um campo entre aspas duplas ou simples."""
    pattern = f'"{field_name}":\s*[\'"]([^\'"]*)[\'"]'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    return ""

def extract_multiline_field(text, field_name):
    """Extrai um campo que pode ter múltiplas linhas (text, traducao)."""
    # Procura por "field_name": '...' ou "field_name": "..."
    # que pode se estender por várias linhas
    pattern = f'"{field_name}":\s*[\'"]'
    match = re.search(pattern, text)
    if not match:
        return ""

    start = match.end()
    # Procura o fechamento correspondente
    quote_char = text[match.end() - 1]  # Tipo de aspas usado
    i = start
    escaped = False
    result = ""

    while i < len(text):
        char = text[i]
        if escaped:
            result += char
            escaped = False
        elif char == '\\':
            result += char
            escaped = True
        elif char == quote_char:
            # Fim do campo
            return result
        else:
            result += char
        i += 1

    return result

def parse_artigos_from_python():
    """
    Parseia o ficheiro gerar_comparativo_reuniao.py
    Extrai cada artigo do array ARTIGOS
    """

    with open('/home/user/Legislacao/gerar_comparativo_reuniao.py', 'r', encoding='utf-8') as f:
        content = f.read()

    artigos = []

    # Encontra o início de ARTIGOS = [
    artigos_start = content.find('ARTIGOS = [')
    if artigos_start == -1:
        print("ERRO: ARTIGOS não encontrado")
        return []

    # Extrai cada bloco {... } individualmente
    # Procura por padrão: {<conteúdo>,<próximo ID>
    current_pos = artigos_start + len('ARTIGOS = ')
    depth = 0
    in_dict = False
    dict_start = -1

    for i in range(current_pos, len(content)):
        char = content[i]

        if char == '{' and not in_dict:
            in_dict = True
            dict_start = i
            depth = 1
        elif in_dict:
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1

                if depth == 0:
                    # Fim de um artigo
                    dict_block = content[dict_start:i + 1]

                    artigo = parse_single_artigo(dict_block)
                    if artigo:
                        artigos.append(artigo)

                    in_dict = False

        # Parada se encontrar fim do array
        if char == ']' and in_dict == False and depth == 0:
            break

    return artigos

def parse_single_artigo(dict_text):
    """Parseia um único bloco {... } de artigo."""

    try:
        art = {
            'id': extract_field(dict_text, 'id'),
            'tema': extract_field(dict_text, 'tema'),
            'reg_titulo': extract_field(dict_text.split('"regulamento"')[1], 'titulo'),
            'reg_ref': extract_field(dict_text.split('"regulamento"')[1], 'ref'),
            'rgbeac_ref': extract_field(dict_text.split('"rgbeac"')[1], 'ref') if '"rgbeac"' in dict_text else 'Sem correspondência',
            'codigo_ref': extract_field(dict_text.split('"codigo"')[1], 'ref') if '"codigo"' in dict_text else 'Sem correspondência',
            'legislacao_ref': extract_field(dict_text.split('"legislacao"')[1], 'ref') if '"legislacao"' in dict_text else 'Sem correspondência',
            'sumario': '',
        }

        # Extrai sumário se existir
        if '"divergencia"' in dict_text:
            div_section = dict_text.split('"divergencia"')[1]
            art['sumario'] = extract_field(div_section, 'sumario')

        # Determina se é novo
        tem_rgbeac = 'Sem correspondência' not in art['rgbeac_ref'] and art['rgbeac_ref'].strip()
        tem_codigo = 'Sem correspondência' not in art['codigo_ref'] and art['codigo_ref'].strip()
        tem_legislacao = 'Sem correspondência' not in art['legislacao_ref'] and art['legislacao_ref'].strip()

        art['eh_novo'] = not (tem_rgbeac or tem_codigo or tem_legislacao)
        art['tem_rgbeac'] = tem_rgbeac
        art['tem_codigo'] = tem_codigo
        art['tem_legislacao'] = tem_legislacao

        return art
    except Exception as e:
        print(f"Erro ao parsear artigo: {e}")
        return None

def main():
    print("\n" + "=" * 100)
    print("EXTRAÇÃO FINAL - DISPOSIÇÕES NOVAS REGULAMENTO 2023/0447")
    print("=" * 100)

    print("\n[1] Parseando gerar_comparativo_reuniao.py...")
    artigos = parse_artigos_from_python()
    print(f"    ✓ Extraídos {len(artigos)} artigos")

    if not artigos:
        print("    ERRO: Nenhum artigo extraído")
        return

    # Filtra artigos novos
    artigos_novos = [a for a in artigos if a['eh_novo']]
    artigos_com_corresp = [a for a in artigos if not a['eh_novo']]

    print(f"\n[2] Classificando artigos...")
    print(f"    - Artigos NOVOS (sem correspondência): {len(artigos_novos)}")
    print(f"    - Artigos COM correspondência: {len(artigos_com_corresp)}")

    # CSV 1: Resumido (todos os artigos)
    print("\n[3] Gravando CSVs...")
    csv_path = '/home/user/Legislacao/disposicoes_regulamento_resumido.csv'
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        fieldnames = ['id', 'numero', 'tema', 'titulo', 'sumario',
                      'tem_rgbeac', 'tem_codigo', 'tem_legislacao', 'classificacao']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for art in artigos:
            match = re.search(r'(\d+)', art['id']) if art['id'] else None
            numero = match.group(1) if match else ''
            writer.writerow({
                'id': art['id'],
                'numero': numero,
                'tema': art['tema'],
                'titulo': art['reg_titulo'],
                'sumario': art['sumario'][:180] if art['sumario'] else '',
                'tem_rgbeac': 'Sim' if art['tem_rgbeac'] else 'Não',
                'tem_codigo': 'Sim' if art['tem_codigo'] else 'Não',
                'tem_legislacao': 'Sim' if art['tem_legislacao'] else 'Não',
                'classificacao': 'NOVO' if art['eh_novo'] else 'COM CORRESPONDÊNCIA',
            })

    print(f"    ✓ {csv_path}")

    # CSV 2: Apenas novos (artigos sem correspondência)
    if artigos_novos:
        csv_novos = '/home/user/Legislacao/disposicoes_totalmente_novas.csv'
        with open(csv_novos, 'w', newline='', encoding='utf-8-sig') as f:
            fieldnames = ['id', 'numero', 'tema', 'titulo', 'sumario', 'justificacao']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for art in artigos_novos:
                match = re.search(r'(\d+)', art['id']) if art['id'] else None
                numero = match.group(1) if match else ''
                writer.writerow({
                    'id': art['id'],
                    'numero': numero,
                    'tema': art['tema'],
                    'titulo': art['reg_titulo'],
                    'sumario': art['sumario'],
                    'justificacao': 'Nenhuma correspondência em @codigo, @rgbeac ou legislação portuguesa vigente (DL 276/2001, DL 82/2019, Lei 27/2016)',
                })

        print(f"    ✓ {csv_novos}")

    # CSV 3: Artigos com correspondência (para análise de alinhamento)
    if artigos_com_corresp:
        csv_corresp = '/home/user/Legislacao/disposicoes_com_correspondencia_pt.csv'
        with open(csv_corresp, 'w', newline='', encoding='utf-8-sig') as f:
            fieldnames = ['id', 'numero', 'tema', 'titulo', 'sumario',
                          'correspondencia_rgbeac', 'correspondencia_codigo', 'correspondencia_legislacao']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for art in artigos_com_corresp:
                match = re.search(r'(\d+)', art['id']) if art['id'] else None
                numero = match.group(1) if match else ''
                writer.writerow({
                    'id': art['id'],
                    'numero': numero,
                    'tema': art['tema'],
                    'titulo': art['reg_titulo'],
                    'sumario': art['sumario'][:180],
                    'correspondencia_rgbeac': 'Sim' if art['tem_rgbeac'] else 'Não',
                    'correspondencia_codigo': 'Sim' if art['tem_codigo'] else 'Não',
                    'correspondencia_legislacao': 'Sim' if art['tem_legislacao'] else 'Não',
                })

        print(f"    ✓ {csv_corresp}")

    # Sumário
    print("\n" + "=" * 100)
    print("SUMÁRIO - ARTIGOS TOTALMENTE NOVOS (SEM CORRESPONDÊNCIA)")
    print("=" * 100)

    for art in artigos_novos:
        match = re.search(r'(\d+)', art['id']) if art['id'] else None
        numero = match.group(1) if match else ''
        print(f"\n  Art. {numero}: {art['reg_titulo']}")
        print(f"  Tema: {art['tema']}")
        if art['sumario']:
            print(f"  Descrição: {art['sumario']}")
        print(f"  Motivo: Não existe correspondência em nenhuma legislação portuguesa (verificado em @codigo, @rgbeac, DL 276/2001, DL 82/2019, Lei 27/2016)")

    print("\n" + "=" * 100)

if __name__ == "__main__":
    main()
