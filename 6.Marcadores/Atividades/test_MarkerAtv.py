import pytest
from AtividadeMarkers import classifica_Idade

@pytest.mark.crianca
def test_classifica_crianca():
    assert classifica_Idade(12) == 'criança'

@pytest.mark.adolescente
def test_classifica_adolescente():
    assert classifica_Idade(17) == 'adolescente'

@pytest.mark.adulto
def test_classifica_adulto():
    assert classifica_Idade(34) == 'adulto'

@pytest.mark.idoso
def test_classifica_idoso():
    assert classifica_Idade(70) == 'idoso'
