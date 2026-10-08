"""Total de uma compra com desconto e imposto, testado em `test_calculo.py`."""


def calcula_total(preco: float, taxa_desconto: float, taxa_imposto: float) -> float:
    """Aplica o desconto sobre o preco e o imposto sobre o valor ja descontado."""
    desconto = preco * taxa_desconto
    imposto = (preco - desconto) * taxa_imposto
    return round(preco - desconto + imposto, 2)
