"""Fixture basica: o teste declara o que precisa no parametro e o pytest entrega.

`lista_exemplo` esta definida em `4.Fixtures/conftest.py`, nao aqui. Essa e a
forma padrao de compartilhar preparacao entre varios arquivos de teste.
"""


def test_soma_da_lista(lista_exemplo: list[int]) -> None:
    assert sum(lista_exemplo) == 15


def test_tamanho_da_lista(lista_exemplo: list[int]) -> None:
    assert len(lista_exemplo) == 5


def test_cada_teste_recebe_uma_lista_nova(lista_exemplo: list[int]) -> None:
    """Mexer na lista aqui nao afeta os outros testes: escopo function, o padrao."""
    lista_exemplo.append(6)
    assert len(lista_exemplo) == 6
