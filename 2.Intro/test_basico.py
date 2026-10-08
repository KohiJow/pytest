"""Primeiro teste.

O pytest coleta todo arquivo `test_*.py` e, dentro dele, toda funcao `test_*`.
Nao precisa herdar de classe nem importar nada: um `assert` comum ja e um
teste. Rode `pytest 2.Intro -v` e veja o nome da funcao aparecer como PASSED.
"""


def test_soma_de_lista() -> None:
    assert sum([1, 2, 3]) == 6


def test_assert_mostra_os_valores_quando_falha() -> None:
    """Quando um assert falha, o pytest reescreve a expressao e mostra cada lado.

    Este passa de proposito. Troque o 6 por 7, rode de novo e repare que a
    mensagem de erro traz o valor real de `sum([1, 2, 3])`, sem print nenhum.
    """
    total = sum([1, 2, 3])
    assert total == 6
