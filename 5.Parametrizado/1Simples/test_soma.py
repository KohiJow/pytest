"""Parametrizacao simples: um teste, varios conjuntos de dados.

`@pytest.mark.parametrize` recebe os nomes dos parametros e uma lista de
tuplas. O pytest gera um teste por tupla, cada um com nome proprio no relatorio
(`test_soma[1-2-3]`), e um caso quebrado nao impede os outros de rodar.
"""

import pytest

from soma import soma


@pytest.mark.parametrize(
    ("a", "b", "esperado"),
    [
        (1, 2, 3),
        (4, 5, 9),
        (10, 20, 30),
        (-1, 1, 0),
    ],
)
def test_soma(a: float, b: float, esperado: float) -> None:
    assert soma(a, b) == esperado


def test_soma_de_floats_usa_approx() -> None:
    """0.1 + 0.2 nao da exatamente 0.3 em ponto flutuante; `approx` tolera isso."""
    assert soma(0.1, 0.2) == pytest.approx(0.3)
