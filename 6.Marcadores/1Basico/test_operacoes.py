"""Marcadores: etiquetas para selecionar testes na linha de comando.

`@pytest.mark.lento` nao muda o teste, so o marca. A selecao vem depois:
`pytest -m lento` roda so os marcados e `pytest -m "not lento"` pula todos.
Como o pyproject.toml liga `--strict-markers`, um marcador que nao esta
registrado la e erro de coleta, nao aviso.
"""

import time

import pytest


def soma(a: float, b: float) -> float:
    return a + b


def multiplica(a: float, b: float) -> float:
    return a * b


@pytest.mark.lento
def test_soma_lenta() -> None:
    time.sleep(2)  # simula uma dependencia demorada, como banco ou rede
    assert soma(2, 2) == 4


def test_soma_rapida() -> None:
    assert soma(2, 3) == 5


@pytest.mark.lento
def test_multiplicacao_lenta() -> None:
    time.sleep(2)
    assert multiplica(3, 3) == 9


@pytest.mark.rapido
def test_multiplicacao_rapida() -> None:
    assert multiplica(3, 3) == 9
