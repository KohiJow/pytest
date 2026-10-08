"""Fixtures compartilhadas por toda a pasta 4.Fixtures.

O pytest carrega todo `conftest.py` que encontra no caminho ate o teste. Uma
fixture declarada aqui fica disponivel para qualquer teste desta pasta e das
subpastas, sem import: basta pedir pelo nome no parametro da funcao de teste.
Para ver a lista completa, rode `pytest 4.Fixtures --fixtures`.
"""

import pytest


@pytest.fixture
def lista_exemplo() -> list[int]:
    """Lista usada em `1Exemplos`. Cada teste recebe uma lista nova."""
    return [1, 2, 3, 4, 5]
