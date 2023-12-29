def calcular_total_pedido(codigos_pedidos):
    total = 0.0
    cardapio = {
        100: 9.00,
        101: 11.00,
        102: 12.00,
        103: 12.00,
        104: 14.00,
        105: 17.00,
        200: 5.00,
        201: 4.00,
    }

    for codigo in codigos_pedidos:
        if codigo in cardapio:
            total += cardapio[codigo]
        else:
            raise ValueError(f"Código inválido: {codigo}")

    return total