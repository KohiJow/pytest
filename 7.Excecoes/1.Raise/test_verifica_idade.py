"""Testar que a excecao certa acontece: `pytest.raises`.

O bloco `with pytest.raises(ValueError)` passa se o codigo dentro dele levanta
ValueError e falha se nao levanta nada ou levanta outro tipo. O `match` e uma
expressao regular conferida contra a mensagem: sem ele, qualquer ValueError
serviria, inclusive um vindo de um bug sem relacao com a regra testada.
"""

import pytest

from verifica_idade import verifica_idade


def test_menor_de_idade_levanta_value_error() -> None:
    with pytest.raises(ValueError, match="menores de 18"):
        verifica_idade(17)


def test_maior_de_idade_nao_levanta() -> None:
    assert verifica_idade(20) == "Acesso Permitido"


def test_dezoito_e_o_primeiro_permitido() -> None:
    """A fronteira da regra (`< 18`) merece um caso proprio."""
    assert verifica_idade(18) == "Acesso Permitido"
