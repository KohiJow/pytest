"""Comparando estruturas inteiras e mensagem no assert.

`assert a == b, "mensagem"` funciona com qualquer objeto. Para listas, dicts e
strings o pytest ainda mostra um diff indicando exatamente qual posicao difere.
"""


def test_listas_iguais() -> None:
    lista_esperada = [1, 2, 3, 4, 5]
    lista_resultado = [1, 2, 3, 4, 5]
    assert lista_resultado == lista_esperada, "As listas nao sao iguais."


def test_dicionarios_iguais() -> None:
    """Troque um valor de proposito e veja o diff chave a chave que o pytest gera."""
    esperado = {"nome": "Mouse", "quantidade": 10}
    resultado = {"nome": "Mouse", "quantidade": 10}
    assert resultado == esperado
