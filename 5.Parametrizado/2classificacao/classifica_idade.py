"""Regra de faixa etaria testada em `test_classifica_idade.py`."""


def classifica_idade(idade: int) -> str:
    if idade < 12:
        return "Criança"
    if idade < 18:
        return "Adolescente"
    if idade < 60:
        return "Adulto"
    return "Idoso"
