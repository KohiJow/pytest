"""Funcao propositalmente demorada, testada em `test_performance.py`."""

import time


def funcao_lenta() -> str:
    time.sleep(1)
    return "finished"
