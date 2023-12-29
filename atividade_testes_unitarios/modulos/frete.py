def ler_dimensoes_objeto():
    altura, comprimento, largura = ler_dimensoes()
    volume = calcular_volume(altura, comprimento, largura)
    preco_volume = calcular_preco_volume(volume)
    return preco_volume

def ler_dimensoes():
    altura = ler_medida('Altura do objeto (em cm): ')
    comprimento = ler_medida('Comprimento do objeto (em cm): ')
    largura = ler_medida('Largura do objeto (em cm): ')
    return altura, comprimento, largura

def ler_medida(mensagem):
    medida = -1
    while medida == -1:
        medida_lida = input(mensagem)
        medida = validar_medida(medida_lida)
    return medida

def validar_medida(medida):
    try:
        medida_validada = int(medida)
    except ValueError:
        print('Você digitou alguma dimensão do objeto com valor não numérico')
        print('Entre com as dimensões desejadas novamente')
        return -1
    return medida_validada

def calcular_volume(altura, comprimento, largura):
    volume = altura * comprimento * largura
    if volume > 100000.0 or volume <= 0:
        raise ValueError('Não aceitamos objetos com dimensões grandes e/ou zeradas')
    return volume

def calcular_preco_volume(volume):
    valor_volume = 0.0
    if volume < 1000:
        valor_volume = 10.0
    elif 1000 <= volume < 10000:
        valor_volume = 20.0
    elif 10000 <= volume < 30000:
        valor_volume = 30.0
    elif 30000 <= volume < 100000:
        valor_volume = 20.0
    return valor_volume
