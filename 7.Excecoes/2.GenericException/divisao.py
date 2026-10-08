"""Divisao que recusa o zero com uma mensagem propria."""


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b
