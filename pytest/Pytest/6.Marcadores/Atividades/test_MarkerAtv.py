import pytest
from AtividadeMarkers import classifica_Idade
    
@pytest.mark.criança
def test_classifica_Idade():
    assert classifica_Idade == 12
    
@pytest.mark.adolescente
def test_classifica_Idade():
    assert classifica_Idade(17) == 'adolescente'
    
@pytest.mark.adulto
def test_classifica_Idade():
    assert classifica_Idade(34) == 'adulto'
    
@pytest.mark.idoso
def test_classifica_Idade():
    assert classifica_Idade(70) == 'idoso'
    
    