"""Codigo testado por `test_funcoes.py`.

Fica num arquivo separado para mostrar o caso comum: o teste importa a funcao
de outro modulo em vez de defini-la no proprio arquivo de teste.
"""

from typing import Optional


def email_valido(email: str) -> bool:
    """Checagem de email bem ingenua, suficiente para o exercicio."""
    return "@" in email and "." in email


def dividir(a: float, b: float) -> Optional[float]:
    """Divide `a` por `b`, devolvendo None em vez de estourar quando `b` e zero."""
    if b == 0:
        return None
    return a / b
