"""O teste que o primeiro workflow rodava.

Esta pasta (`main.py`, este teste e um `requirements.txt` so com pytest) e o
projeto minimo que serviu para entender o GitHub Actions antes de aplicar o
workflow de `.github/workflows/tests.yml` ao repositorio inteiro.
"""

from main import soma


def test_soma() -> None:
    assert soma(2, 3) == 5
