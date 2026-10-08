"""Parametrizacao com ids legiveis e casos de fronteira.

Sem `ids`, o pytest nomeia cada caso pelos valores (`[10-Criança]`). Com
`pytest.param(..., id="...")` o relatorio fica legivel e da para rodar um caso
so: `pytest -k fronteira_adulto`. Os limites (11/12, 17/18, 59/60) sao onde
esse tipo de regra costuma quebrar, por isso cada um vira um caso.
"""

import pytest

from classifica_idade import classifica_idade


@pytest.mark.parametrize(
    ("idade", "categoria_esperada"),
    [
        pytest.param(10, "Criança", id="crianca"),
        pytest.param(15, "Adolescente", id="adolescente"),
        pytest.param(30, "Adulto", id="adulto"),
        pytest.param(70, "Idoso", id="idoso"),
        pytest.param(11, "Criança", id="ultima_crianca"),
        pytest.param(12, "Adolescente", id="fronteira_adolescente"),
        pytest.param(17, "Adolescente", id="ultimo_adolescente"),
        pytest.param(18, "Adulto", id="fronteira_adulto"),
        pytest.param(59, "Adulto", id="ultimo_adulto"),
        pytest.param(60, "Idoso", id="fronteira_idoso"),
    ],
)
def test_classifica_idade(idade: int, categoria_esperada: str) -> None:
    assert classifica_idade(idade) == categoria_esperada
