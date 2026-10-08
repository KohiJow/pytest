"""Parametrize empilhado: produto cartesiano dos parametros.

Tres decoradores com tres valores cada geram 3 x 3 x 3 = 27 testes. E a forma
mais barata de cobrir combinacoes, mas cuidado com o assert: repetir a formula
da funcao dentro do teste so prova que ela foi copiada certo. Aqui o teste do
produto cartesiano confere propriedades que valem para qualquer combinacao, e
os valores exatos ficam em `test_valores_conhecidos`, calculados a mao.
"""

import pytest

from calcula_total import calcula_total

TOLERANCIA = 0.005  # a funcao arredonda para centavos


@pytest.mark.parametrize("preco", [10.00, 50.00, 100.00])
@pytest.mark.parametrize("taxa_desconto", [0, 0.1, 0.25])
@pytest.mark.parametrize("taxa_imposto", [0, 0.05, 0.1])
def test_total_fica_entre_o_preco_descontado_e_o_preco_com_imposto(
    preco: float, taxa_desconto: float, taxa_imposto: float
) -> None:
    total = calcula_total(preco, taxa_desconto, taxa_imposto)
    piso = preco * (1 - taxa_desconto)  # imposto nunca diminui o total
    teto = preco * (1 + taxa_imposto)  # desconto nunca aumenta o total

    assert piso - TOLERANCIA <= total <= teto + TOLERANCIA
    assert total == round(total, 2)


@pytest.mark.parametrize(
    ("preco", "taxa_desconto", "taxa_imposto", "esperado"),
    [
        pytest.param(100.00, 0, 0, 100.00, id="sem_desconto_sem_imposto"),
        pytest.param(100.00, 0.25, 0, 75.00, id="so_desconto"),
        pytest.param(100.00, 0, 0.1, 110.00, id="so_imposto"),
        pytest.param(100.00, 0.1, 0.05, 94.50, id="desconto_e_imposto"),
        pytest.param(10.00, 0.25, 0.1, 8.25, id="arredonda_centavos"),
    ],
)
def test_valores_conhecidos(
    preco: float, taxa_desconto: float, taxa_imposto: float, esperado: float
) -> None:
    assert calcula_total(preco, taxa_desconto, taxa_imposto) == esperado
