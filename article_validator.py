#!/usr/bin/env python3
"""
Validação de estrutura de dados para artigos do Regulamento 2023/0447

Define a estrutura esperada e fornece funções de validação para garantir
que todos os artigos estejam em conformidade.
"""

from typing import Dict, List, Any, Tuple

# Estrutura esperada (referência)
EXPECTED_ARTICLE_STRUCTURE = {
    "id": str,                          # ex: "ART-11"
    "tema": str,                        # ex: "Alimentação e Hidratação"
    "regulamento": dict,                # ref, titulo, texto, traducao
    "rgbeac": dict,                     # ref, texto
    "codigo": dict,                     # ref, texto
    "legislacao": dict,                 # ref, texto
    "divergencia": dict,                # legislacao, codigo, rgbeac, sumario
    "necessidade_alteracao": str,       # "Sim" ou "Não"
    "notas": str,                       # observações
}

EXPECTED_REGULAMENTO_KEYS = {"ref", "titulo", "texto", "traducao"}
EXPECTED_DIVERGENCIA_KEYS = {"legislacao", "codigo", "rgbeac", "sumario"}
EXPECTED_SUPPLEMENTARY_KEYS = {"ref", "texto"}  # rgbeac, codigo, legislacao


class ArticleValidationError(Exception):
    """Exceção levantada quando validação de artigo falha"""
    pass


def validate_article_structure(article: Dict[str, Any], strict: bool = False) -> Tuple[bool, List[str]]:
    """
    Valida se um artigo tem a estrutura esperada.

    Args:
        article: Dicionário do artigo a validar
        strict: Se True, levanta exceção em primeiro erro; se False, retorna lista de erros

    Returns:
        Tupla (is_valid: bool, errors: List[str])

    Raises:
        ArticleValidationError: Se strict=True e há erros
    """
    errors = []

    # Validação básica
    if not isinstance(article, dict):
        errors.append(f"Article must be dict, got {type(article)}")
        if strict:
            raise ArticleValidationError(errors[0])
        return False, errors

    # Verificar campos obrigatórios
    for field, expected_type in EXPECTED_ARTICLE_STRUCTURE.items():
        if field not in article:
            errors.append(f"Missing required field: '{field}'")
            if strict:
                raise ArticleValidationError(errors[-1])
            continue

        # Verificar tipo
        if not isinstance(article[field], expected_type):
            errors.append(
                f"Field '{field}' has wrong type: expected {expected_type.__name__}, "
                f"got {type(article[field]).__name__}"
            )
            if strict:
                raise ArticleValidationError(errors[-1])

    # Validar ID format
    if "id" in article:
        article_id = article["id"]
        if not isinstance(article_id, str) or not article_id.startswith("ART-"):
            errors.append(f"Invalid article ID format: '{article_id}' (expected ART-XX)")
            if strict:
                raise ArticleValidationError(errors[-1])

    # Validar regulamento tem todas as sub-keys
    if "regulamento" in article and isinstance(article["regulamento"], dict):
        reg_keys = set(article["regulamento"].keys())
        missing_keys = EXPECTED_REGULAMENTO_KEYS - reg_keys
        if missing_keys:
            errors.append(
                f"regulamento missing keys: {missing_keys}. "
                f"Expected: {EXPECTED_REGULAMENTO_KEYS}, got: {reg_keys}"
            )
            if strict:
                raise ArticleValidationError(errors[-1])

        # Verificar que texto e traducao são strings/tuples (não dicts)
        if "texto" in article["regulamento"]:
            if isinstance(article["regulamento"]["texto"], dict):
                errors.append(f"regulamento.texto must be string/tuple, not dict")
                if strict:
                    raise ArticleValidationError(errors[-1])
        if "traducao" in article["regulamento"]:
            if isinstance(article["regulamento"]["traducao"], dict):
                errors.append(f"regulamento.traducao must be string/tuple, not dict")
                if strict:
                    raise ArticleValidationError(errors[-1])

    # Validar divergencia tem todas as sub-keys
    if "divergencia" in article and isinstance(article["divergencia"], dict):
        div_keys = set(article["divergencia"].keys())
        missing_keys = EXPECTED_DIVERGENCIA_KEYS - div_keys
        if missing_keys:
            errors.append(
                f"divergencia missing keys: {missing_keys}. "
                f"Expected: {EXPECTED_DIVERGENCIA_KEYS}, got: {div_keys}"
            )
            if strict:
                raise ArticleValidationError(errors[-1])

    # Validar rgbeac, codigo, legislacao têm ref e texto
    for field in ["rgbeac", "codigo", "legislacao"]:
        if field in article and isinstance(article[field], dict):
            field_keys = set(article[field].keys())
            if field_keys and not EXPECTED_SUPPLEMENTARY_KEYS.issubset(field_keys):
                errors.append(
                    f"{field} should have keys {EXPECTED_SUPPLEMENTARY_KEYS}, got {field_keys}"
                )
                if strict:
                    raise ArticleValidationError(errors[-1])

    # Validar necessidade_alteracao começa com "Sim" ou "Não"
    if "necessidade_alteracao" in article:
        value = article["necessidade_alteracao"]
        if not (value.startswith("Sim") or value.startswith("Não")):
            errors.append(
                f"necessidade_alteracao must start with 'Sim' or 'Não', got '{value}'"
            )
            if strict:
                raise ArticleValidationError(errors[-1])

    is_valid = len(errors) == 0
    return is_valid, errors


def validate_articles_list(articles: List[Dict[str, Any]], strict: bool = False) -> Tuple[bool, Dict[str, List[str]]]:
    """
    Valida uma lista de artigos.

    Args:
        articles: Lista de dicionários de artigos
        strict: Se True, levanta exceção no primeiro erro

    Returns:
        Tupla (all_valid: bool, errors_by_article: Dict[article_id -> List[errors]])
    """
    all_errors = {}

    for article in articles:
        article_id = article.get("id", "UNKNOWN")
        is_valid, errors = validate_article_structure(article, strict=False)

        if not is_valid:
            all_errors[article_id] = errors
            if strict:
                raise ArticleValidationError(
                    f"Validation failed for {article_id}: {errors[0]}"
                )

    all_valid = len(all_errors) == 0
    return all_valid, all_errors


def validate_articles_sequence(articles: List[Dict[str, Any]], expected_sequence: List[str]) -> Tuple[bool, List[str]]:
    """
    Valida que todos os artigos da sequência esperada estão presentes.

    Args:
        articles: Lista de artigos carregados
        expected_sequence: Lista de IDs esperados (ex: ['ART-05', 'ART-06', ...])

    Returns:
        Tupla (sequence_complete: bool, missing_articles: List[str])
    """
    loaded_ids = {art.get("id") for art in articles}
    expected_ids = set(expected_sequence)
    missing = expected_ids - loaded_ids

    return len(missing) == 0, sorted(list(missing))


def print_validation_report(is_valid: bool, errors: Dict[str, List[str]]) -> None:
    """
    Imprime um relatório de validação formatado.

    Args:
        is_valid: Se a validação passou
        errors: Dicionário de erros por artigo
    """
    print("\n" + "=" * 80)
    print("VALIDATION REPORT")
    print("=" * 80)

    if is_valid:
        print("\n✓ ALL ARTICLES VALID")
        print("  All articles have correct structure and required fields")
    else:
        print(f"\n✗ VALIDATION FAILED")
        print(f"  {len(errors)} article(s) with errors:\n")

        for article_id, error_list in sorted(errors.items()):
            print(f"  {article_id}:")
            for error in error_list:
                print(f"    • {error}")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    # Teste básico
    from artigos_11_12_14_15_completos import ARTICLES_11_12_14_15_COMPLETE
    from artigos_15a_17a_20_completos import ARTICLES_15a_17a_20
    from artigos_20a_21_22_completos import ARTICLES_20A_21_22

    all_articles = ARTICLES_11_12_14_15_COMPLETE + ARTICLES_15a_17a_20 + ARTICLES_20A_21_22

    is_valid, errors = validate_articles_list(all_articles)
    print_validation_report(is_valid, errors)

    print(f"\nTotal articles validated: {len(all_articles)}")
