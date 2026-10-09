"""Mais de um marcador no mesmo teste e expressoes de selecao.

`test_soma_mista` e `lento` e `rapido` ao mesmo tempo. O `-m` aceita expressao
booleana. Rodando so esta pasta:

- `-m "lento and rapido"` pega apenas `test_soma_mista`
- `-m "lento and not rapido"` pega apenas `test_soma_lenta`
- `-m "lento or rapido"` pega os tres
"""

import time

import pytest


@pytest.mark.rapido
def test_soma_rapida() -> None:
    assert 1 + 2 == 3


@pytest.mark.lento
def test_soma_lenta() -> None:
    time.sleep(2)
    assert 1 + 2 == 3


@pytest.mark.rapido
@pytest.mark.lento
def test_soma_mista() -> None:
    time.sleep(1)
    assert 1 + 2 == 3
