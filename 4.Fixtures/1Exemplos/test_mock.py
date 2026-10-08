"""Fixture que devolve um mock no lugar de uma resposta HTTP de verdade.

`MagicMock(spec=requests.Response)` cria um objeto que so aceita os atributos
que `requests.Response` tem: um erro de digitacao como `resposta.jsn()` levanta
AttributeError em vez de passar em silencio. Nenhuma requisicao sai da maquina.
"""

from unittest.mock import MagicMock

import pytest
import requests


@pytest.fixture
def resposta_mock() -> MagicMock:
    mock = MagicMock(spec=requests.Response)
    mock.status_code = 200
    mock.json.return_value = {"message": "Success"}
    return mock


def test_status_e_corpo_da_resposta(resposta_mock: MagicMock) -> None:
    assert resposta_mock.status_code == 200
    assert resposta_mock.json() == {"message": "Success"}


def test_mock_registra_as_chamadas(resposta_mock: MagicMock) -> None:
    """Alem de responder, o mock lembra como foi usado.

    O contador comeca em zero porque cada teste recebe um mock novo (escopo function).
    """
    resposta_mock.json()
    resposta_mock.json()
    assert resposta_mock.json.call_count == 2


def test_spec_bloqueia_atributo_que_nao_existe(resposta_mock: MagicMock) -> None:
    with pytest.raises(AttributeError):
        resposta_mock.jsn()
