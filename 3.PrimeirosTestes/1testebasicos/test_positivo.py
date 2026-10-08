"""Varios asserts no mesmo teste.

Funciona, mas o pytest para no primeiro assert que falhar: se `eh_positivo(5)`
quebrar, voce nao fica sabendo o que aconteceu com `eh_positivo(-5)`. Nos
modulos seguintes (parametrizacao) cada caso vira um teste separado.
"""


def eh_positivo(numero: float) -> bool:
    return numero > 0


def test_eh_positivo() -> None:
    assert eh_positivo(5) is True
    assert eh_positivo(-5) is False
