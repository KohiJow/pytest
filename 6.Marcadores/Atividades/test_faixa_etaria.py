"""Atividade: um marcador por faixa etaria.

Os marcadores `crianca`, `adolescente`, `adulto` e `idoso` estao registrados
no pyproject.toml. `pytest -m adulto` roda so o teste daquela faixa.
"""

import pytest

from faixa_etaria import classifica_idade


@pytest.mark.crianca
def test_classifica_crianca() -> None:
    assert classifica_idade(12) == "criança"


@pytest.mark.adolescente
def test_classifica_adolescente() -> None:
    assert classifica_idade(17) == "adolescente"


@pytest.mark.adulto
def test_classifica_adulto() -> None:
    assert classifica_idade(34) == "adulto"


@pytest.mark.idoso
def test_classifica_idoso() -> None:
    assert classifica_idade(70) == "idoso"
