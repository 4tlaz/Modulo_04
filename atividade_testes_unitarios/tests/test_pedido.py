import pytest
from modulos.pedido import calcular_total_pedido

def test_calculo_total_pedido():
    pedidos_validos = [100, 201, 105]
    resultado = calcular_total_pedido(pedidos_validos)
    assert resultado == 30.00

def test_aviso_pedido_invalido():
    pedidos_invalidos = [999, 105, 200]
    with pytest.raises(ValueError, match="Código inválido"):
      calcular_total_pedido(pedidos_invalidos)