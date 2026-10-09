"""Setup e teardown com `yield`.

O que vem antes do `yield` roda antes do teste (setup) e o que vem depois roda
ao final, mesmo que o teste falhe (teardown). Aqui o setup cria uma engine e
abre uma conexao com um SQLite em memoria; o teardown fecha a conexao e
descarta a engine. O `dispose()` importa: `close()` sozinho so devolve a
conexao crua ao pool do SQLAlchemy, e o banco em memoria continua vivo la
dentro. Como cada teste ganha uma engine nova e a anterior foi descartada,
cada um comeca com um banco vazio.
"""

from collections.abc import Iterator

import pytest
import sqlalchemy
from sqlalchemy import Connection, text


@pytest.fixture
def conexao() -> Iterator[Connection]:
    engine = sqlalchemy.create_engine("sqlite:///:memory:")
    conexao = engine.connect()
    yield conexao
    # teardown: roda depois do teste, mesmo se ele falhar
    conexao.close()
    engine.dispose()


def test_conexao_responde(conexao: Connection) -> None:
    resultado = conexao.execute(text("SELECT 1"))
    assert resultado.fetchone()[0] == 1


def test_criar_tabela_e_inserir(conexao: Connection) -> None:
    conexao.execute(text("CREATE TABLE produtos (nome TEXT, quantidade INTEGER)"))
    conexao.execute(text("INSERT INTO produtos VALUES ('Mouse', 10)"))
    linhas = conexao.execute(text("SELECT nome, quantidade FROM produtos")).all()
    assert linhas == [("Mouse", 10)]


def test_banco_comeca_vazio_em_cada_teste(conexao: Connection) -> None:
    """A tabela do teste anterior nao existe aqui: o teardown descartou o banco."""
    consulta = text("SELECT name FROM sqlite_master WHERE type = 'table'")
    assert conexao.execute(consulta).all() == []
