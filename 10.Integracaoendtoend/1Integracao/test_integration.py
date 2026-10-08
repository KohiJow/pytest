"""Teste de integracao: varias unidades trabalhando juntas.

Diferente do teste unitario, aqui ninguem e substituido por mock: `Produto` e
`Estoque` sao os objetos reais, e o que se confere e o fluxo completo
(cadastrar, somar, consultar). A fixture `estoque` entrega um estoque vazio
para cada teste, entao a ordem de execucao nao importa.
"""

import pytest

from app import Estoque, Produto


@pytest.fixture
def estoque() -> Estoque:
    return Estoque()


def test_adicionar_e_verificar_quantidade(estoque: Estoque) -> None:
    estoque.adicionar_produto(Produto("Mouse", 10))
    estoque.adicionar_produto(Produto("Teclado", 5))

    assert estoque.verifica_quantidade("Mouse") == 10
    assert estoque.verifica_quantidade("Teclado") == 5


def test_adicionar_produto_existente_soma_a_quantidade(estoque: Estoque) -> None:
    estoque.adicionar_produto(Produto("Mouse", 10))
    estoque.adicionar_produto(Produto("Mouse", 5))

    assert estoque.verifica_quantidade("Mouse") == 15


def test_produto_nao_cadastrado_tem_quantidade_zero(estoque: Estoque) -> None:
    assert estoque.verifica_quantidade("Monitor") == 0
