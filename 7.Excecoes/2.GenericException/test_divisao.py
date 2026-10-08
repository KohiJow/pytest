"""Inspecionando a excecao capturada.

`pytest.raises(...) as exc_info` guarda a excecao em `exc_info.value` depois
que o bloco termina. Da para conferir a mensagem, os argumentos, a causa, o que
for preciso. Repare que o assert fica fora do `with`: dentro dele, nada apos a
linha que levanta a excecao e executado.
"""

import pytest

from divisao import dividir


def test_dividir_por_zero_levanta_zero_division_error() -> None:
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)


def test_mensagem_da_excecao() -> None:
    with pytest.raises(ZeroDivisionError) as exc_info:
        dividir(10, 0)
    assert str(exc_info.value) == "Não é possível dividir por zero."


def test_divisao_normal_nao_levanta() -> None:
    assert dividir(10, 4) == 2.5
