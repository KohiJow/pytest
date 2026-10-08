"""Funcao que levanta excecao, testada em `test_verifica_idade.py`."""


def verifica_idade(idade: int) -> str:
    if idade < 18:
        raise ValueError("Acesso negado para menores de 18 anos")
    return "Acesso Permitido"
