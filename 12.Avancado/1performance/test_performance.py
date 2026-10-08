"""Teste de tempo de execucao sem depender do relogio de verdade.

A versao ingenua mede `time.time()` antes e depois e exige `duracao < 3`. Ela
passa na maquina de quem escreveu e falha num CI sobrecarregado: e um teste
fragil, e ainda gasta um segundo de sleep real a cada execucao.

Aqui o `monkeypatch` troca `time.sleep` e `time.perf_counter` por um relogio
falso que so avanca quando alguem chama `sleep`. A medicao continua a mesma
(inicio, chamada, fim), mas o resultado e deterministico e o teste leva
milissegundos. O `monkeypatch` desfaz a troca sozinho ao final de cada teste.
"""

import time

import pytest

from funcao_lenta import funcao_lenta

LIMITE_SEGUNDOS = 3


class RelogioFalso:
    """Relogio controlado pelo teste: `agora` so muda quando `sleep` e chamado."""

    def __init__(self) -> None:
        self.agora = 0.0

    def sleep(self, segundos: float) -> None:
        self.agora += segundos

    def perf_counter(self) -> float:
        return self.agora


@pytest.fixture
def relogio(monkeypatch: pytest.MonkeyPatch) -> RelogioFalso:
    relogio = RelogioFalso()
    monkeypatch.setattr(time, "sleep", relogio.sleep)
    monkeypatch.setattr(time, "perf_counter", relogio.perf_counter)
    return relogio


@pytest.mark.usefixtures("relogio")
def test_funcao_lenta_termina_dentro_do_limite() -> None:
    """`usefixtures` ativa a fixture quando o teste nao precisa do objeto dela."""
    inicio = time.perf_counter()
    resultado = funcao_lenta()
    duracao = time.perf_counter() - inicio

    assert resultado == "finished"
    assert duracao < LIMITE_SEGUNDOS, f"demorou {duracao}s, mais que o esperado"


def test_funcao_lenta_espera_exatamente_um_segundo(relogio: RelogioFalso) -> None:
    funcao_lenta()
    assert relogio.agora == pytest.approx(1.0)
