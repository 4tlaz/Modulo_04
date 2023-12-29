import pytest
from modulos.calculo import calcular_valor_com_desconto

@pytest.fixture
def exemplo_de_produto():
    return 10.0, 50  
    
def test_calculo_desconto(exemplo_de_produto):
    valor_unitario, quantidade = exemplo_de_produto
    valor_sem_desconto, valor_com_desconto = calcular_valor_com_desconto(valor_unitario, quantidade)
    assert valor_sem_desconto == 500.0
    assert valor_com_desconto == 475.0