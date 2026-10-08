"""Codigo medido pelo plugin de cobertura (pytest-cov).

Esta separado do arquivo de teste de proposito: cobertura so faz sentido sobre
o codigo testado, nao sobre os testes. Com `--cov=8.Plugins` o relatorio mostra
quais linhas daqui foram executadas pela suite.
"""

from typing import Optional


def email_valido(email: str) -> bool:
    return "@" in email and "." in email


def dividir(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b
