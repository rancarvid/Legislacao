#!/usr/bin/env python3
"""
Carregamento dinâmico de artigos do Regulamento 2023/0447

Fornece um interface único para carregar todos os artigos de diferentes fontes.
Elimina necessidade de hardcoding de artigos em gerar_comparativo_reuniao.py
"""

from typing import List, Dict, Any

def load_all_articles() -> List[Dict[str, Any]]:
    """
    Carrega TODOS os artigos de todas as fontes.

    A sequência é importante:
    1. Artigos base (05-17) - hardcoded em gerar_comparativo_reuniao.py (por agora)
    2. Artigos 11,12,14,15 - de artigos_11_12_14_15_completos.py
    3. Artigos 15a, 17a-20 - de artigos_15a_17a_20_completos.py
    4. Artigos 20a, 21, 22 - de artigos_20a_21_22_completos.py

    Returns:
        Lista de dicionários de artigos, sem ordenação garantida
    """
    articles = []

    # Importa artigos de diferentes módulos
    try:
        from artigos_11_12_14_15_completos import ARTICLES_11_12_14_15_COMPLETE
        articles.extend(ARTICLES_11_12_14_15_COMPLETE)
        print("✓ Carregados artigos 11, 12, 14, 15")
    except ImportError as e:
        print(f"✗ Erro ao carregar artigos 11-15: {e}")

    try:
        from artigos_15a_17a_20_completos import ARTICLES_15a_17a_20
        articles.extend(ARTICLES_15a_17a_20)
        print("✓ Carregados artigos 15a, 17a-20")
    except ImportError as e:
        print(f"✗ Erro ao carregar artigos 15a, 17a-20: {e}")

    try:
        from artigos_20a_21_22_completos import ARTICLES_20A_21_22
        articles.extend(ARTICLES_20A_21_22)
        print("✓ Carregados artigos 20a, 21, 22")
    except ImportError as e:
        print(f"✗ Erro ao carregar artigos 20a, 21, 22: {e}")

    return articles


def get_expected_article_sequence() -> List[str]:
    """
    Retorna a sequência esperada de IDs de artigos.

    Returns:
        Lista de IDs em ordem esperada (ex: ['ART-05', 'ART-06', ...])
    """
    return [
        'ART-05', 'ART-06', 'ART-06a', 'ART-07', 'ART-08', 'ART-09', 'ART-10',
        'ART-11', 'ART-12', 'ART-13', 'ART-14', 'ART-15', 'ART-15a',
        'ART-17', 'ART-17a', 'ART-18', 'ART-19', 'ART-20', 'ART-20a', 'ART-21', 'ART-22'
    ]


def reorder_articles(articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Reordena artigos de acordo com a sequência esperada.

    Args:
        articles: Lista de artigos (potencialmente desordenados)

    Returns:
        Lista de artigos reordenados de acordo com sequência esperada
    """
    expected_sequence = get_expected_article_sequence()

    # Cria mapa de artigos por ID
    articles_dict = {art['id']: art for art in articles}

    # Reconstrói em ordem
    reordered = []
    for art_id in expected_sequence:
        if art_id in articles_dict:
            reordered.append(articles_dict[art_id])

    return reordered


if __name__ == "__main__":
    # Teste
    print("Loading all articles...")
    all_articles = load_all_articles()
    print(f"\nTotal articles loaded: {len(all_articles)}")

    print("\nReordering...")
    reordered = reorder_articles(all_articles)
    print(f"Reordered articles: {len(reordered)}")
    for art in reordered:
        print(f"  - {art['id']}: {art['tema']}")
