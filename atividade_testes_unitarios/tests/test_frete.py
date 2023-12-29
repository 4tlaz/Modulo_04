# No arquivo test_frete.py

import pytest
from modulos.frete import ler_dimensoes_objeto

@pytest.fixture
def input_values(monkeypatch):
    inputs = [
        '10',   # Altura
        '20',   # Comprimento
        '5',    # Largura
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    return inputs

def test_ler_dimensoes_objeto(input_values):
    resultado = ler_dimensoes_objeto()

    assert resultado == 20.0 

