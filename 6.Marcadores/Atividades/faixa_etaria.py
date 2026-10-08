"""Regra de faixa etaria da atividade de marcadores.

Os limites (13 e 20) sao diferentes dos de `5.Parametrizado/2classificacao`
de proposito: cada exercicio tem a propria regra.
"""


def classifica_idade(idade: int) -> str:
    if idade < 13:
        return "criança"
    if idade < 20:
        return "adolescente"
    if idade < 60:
        return "adulto"
    return "idoso"
