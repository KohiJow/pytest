"""Escopo de fixture: de quanto em quanto tempo ela e recriada.

- `function` (padrao): recriada para cada teste.
- `module`: criada uma vez por arquivo e reaproveitada pelos testes dele.
- `session`: criada uma vez por execucao do pytest, para todos os arquivos.

Cada fixture abaixo devolve um `object()` novo, e o mesmo teste roda tres vezes
(parametrize) guardando o que recebeu. Assim da para provar que a de escopo
function muda a cada rodada e as outras duas nao, em qualquer ordem.
"""

import pytest

recebidos_function: list[object] = []
recebidos_module: list[object] = []
recebidos_session: list[object] = []


@pytest.fixture
def fixture_function() -> object:
    return object()


@pytest.fixture(scope="module")
def fixture_module() -> object:
    return object()


@pytest.fixture(scope="session")
def fixture_session() -> object:
    return object()


@pytest.mark.parametrize("rodada", [1, 2, 3])
def test_escopo_define_quando_a_fixture_e_recriada(
    rodada: int,
    fixture_function: object,
    fixture_module: object,
    fixture_session: object,
) -> None:
    # `object()` compara por identidade, entao `in` e `set` dizem se e o mesmo
    # objeto que outra rodada ja recebeu.
    assert fixture_function not in recebidos_function, f"rodada {rodada} repetiu"
    recebidos_function.append(fixture_function)

    recebidos_module.append(fixture_module)
    recebidos_session.append(fixture_session)
    assert len(set(recebidos_module)) == 1
    assert len(set(recebidos_session)) == 1
