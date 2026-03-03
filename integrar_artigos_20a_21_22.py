#!/usr/bin/env python3
"""
Script de integração: Adiciona artigos 20a, 21, 22 aos outputs (HTML, Excel, Word)
Segue protocolo Opção 1: Regeneração dinâmica sem alteração permanente do gerar_comparativo_reuniao.py
Data: 2026-03-02
"""

import sys
sys.path.insert(0, '/home/user/Claude---Legislacao')

from artigos_20a_21_22_completos import ARTICLES_20A_21_22
import gerar_comparativo_reuniao as gen
import gerar_word
from article_validator import validate_articles_list, print_validation_report

def main():
    print("\n" + "="*80)
    print("INTEGRAÇÃO: Artigos 20a, 21, 22")
    print("="*80)

    # Adiciona os novos artigos à lista em memória
    print("\n✓ Carregando artigos 20a, 21, 22...")
    gen.ARTIGOS.extend(ARTICLES_20A_21_22)

    # Remove duplicatas (em caso de artigos já presentes em gerar_comparativo_reuniao.py)
    print("✓ Removendo duplicatas...")
    seen_ids = set()
    unique_articles = []
    duplicates_removed = 0
    for art in gen.ARTIGOS:
        art_id = art.get('id')
        if art_id not in seen_ids:
            unique_articles.append(art)
            seen_ids.add(art_id)
        else:
            duplicates_removed += 1
    gen.ARTIGOS = unique_articles
    if duplicates_removed > 0:
        print(f"  ⚠️  {duplicates_removed} artigo(s) duplicado(s) removido(s)")

    # Valida estrutura de todos os artigos
    print("✓ Validando estrutura de dados...")
    is_valid, errors = validate_articles_list(gen.ARTIGOS)
    if not is_valid:
        print("\n✗ ERRO: Validação de estrutura falhou!")
        print_validation_report(is_valid, errors)
        print("\nINTEGRAÇÃO ABORTADA")
        return
    print("✓ Validação bem-sucedida")

    # Reordena os artigos em sequência numérica
    print("✓ Reordenando artigos em sequência...")
    ordem_sequencial = [
        'ART-05', 'ART-06', 'ART-06a', 'ART-07', 'ART-08', 'ART-09', 'ART-10',
        'ART-11', 'ART-12', 'ART-13', 'ART-14', 'ART-15', 'ART-15a',
        'ART-17', 'ART-17a', 'ART-18', 'ART-19', 'ART-20', 'ART-20a', 'ART-21', 'ART-22'
    ]

    # Cria mapa de artigos por ID
    artigos_dict = {art['id']: art for art in gen.ARTIGOS}

    # Reconstrói a lista em ordem sequencial
    artigos_reordenados = []
    for art_id in ordem_sequencial:
        if art_id in artigos_dict:
            artigos_reordenados.append(artigos_dict[art_id])
        else:
            print(f"⚠️  Aviso: Artigo {art_id} não encontrado no sistema")

    gen.ARTIGOS = artigos_reordenados

    print(f"✓ Total de artigos em sequência: {len(gen.ARTIGOS)}")

    # Regenera outputs
    print("\n" + "-"*80)
    print("REGENERAR OUTPUTS")
    print("-"*80)

    print("\n1. Regenerando Excel...")
    try:
        gen.criar_excel('/home/user/Claude---Legislacao/comparativo_reuniao_exemplo.xlsx')
        print("   ✓ Excel regenerado com sucesso")
    except Exception as e:
        print(f"   ✗ Erro ao gerar Excel: {e}")

    print("\n2. Regenerando HTML...")
    try:
        gen.criar_html('/home/user/Claude---Legislacao/comparativo_reuniao_exemplo.html', gen.ARTIGOS)
        print("   ✓ HTML regenerado com sucesso")
    except Exception as e:
        print(f"   ✗ Erro ao gerar HTML: {e}")

    print("\n3. Regenerando Word...")
    try:
        gerar_word.ARTIGOS = gen.ARTIGOS
        gerar_word.criar_word('/home/user/Claude---Legislacao/comparativo_reuniao_exemplo.docx')
        print("   ✓ Word regenerado com sucesso")
    except Exception as e:
        print(f"   ✗ Erro ao gerar Word: {e}")

    # Relatório final
    print("\n" + "="*80)
    print("RESUMO DA INTEGRAÇÃO")
    print("="*80)

    print(f"\nArtigos adicionados: {', '.join([art['id'] for art in ARTICLES_20A_21_22])}")
    print(f"\nSequência final ({len(gen.ARTIGOS)} artigos):")
    for i, art in enumerate(gen.ARTIGOS, 1):
        print(f"  {i:2d}. {art['id']:8s} - {art.get('tema', '?')}")

    print("\n" + "="*80)
    print("✓ INTEGRAÇÃO CONCLUÍDA")
    print("="*80)
    print("\nNOTA (Protocolo Opção 1):")
    print("  - Os outputs (HTML, Excel, Word) foram regenerados com sucesso")
    print("  - Artigos adicionados em memória (sem alterar gerar_comparativo_reuniao.py)")
    print("  - Para manter as mudanças, execute este script sempre que necessário")
    print(f"  - Data da integração: 2026-03-02")
    print("\n" + "="*80 + "\n")

if __name__ == '__main__':
    main()
