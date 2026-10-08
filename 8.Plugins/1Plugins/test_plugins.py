"""Plugins: o pytest-cov mede o que a suite executa.

Rode `pytest 8.Plugins --cov=8.Plugins --cov-report=term-missing`. A coluna
"Missing" lista as linhas de `validacoes.py` que nenhum teste tocou. Os dois
testes abaixo passam pelos dois ramos de cada funcao, por isso 100%. Comente o
`assert dividir(4, 0) is None`, rode de novo e veja a cobertura cair.
"""

from validacoes import dividir, email_valido


def test_email_valido() -> None:
    assert email_valido("exemplo@dominio.com") is True
    assert email_valido("exemplo.com") is False


def test_dividir() -> None:
    assert dividir(4, 2) == 2
    assert dividir(4, 0) is None
