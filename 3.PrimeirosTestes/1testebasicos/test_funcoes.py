"""Teste importando o codigo de outro modulo.

`funcoes.py` esta na mesma pasta e nao existe `__init__.py`: o pytest insere a
pasta do teste no `sys.path` (modo de import `prepend`, o padrao), por isso o
`from funcoes import ...` funciona de qualquer diretorio em que o pytest rode.
"""

from funcoes import dividir, email_valido


def test_email_valido() -> None:
    assert email_valido("exemplo@dominio.com") is True
    assert email_valido("exemplo.com") is False


def test_dividir() -> None:
    assert dividir(4, 2) == 2
    assert dividir(4, 0) is None
