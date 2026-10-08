"""Funcao e teste no mesmo arquivo.

Bom para exercicio rapido; em projeto de verdade o codigo testado fica fora do
arquivo de teste (ver `test_funcoes.py` ao lado).
"""


def somar(a: float, b: float) -> float:
    return a + b


def comprimento(lista: list[int]) -> int:
    return len(lista)


def test_somar_e_comprimento() -> None:
    assert somar(3, 2) == 5
    assert comprimento([1, 2, 3, 4, 5]) == 5
