def decorator_imprimir(func):
  def wrapper(capital, taxa, tempo):
    print(f"Parâmetros: Capital = {capital}, Taxa = {taxa}, Tempo = {tempo}")

    resultado = func(capital, taxa, tempo)

    print(f"Resultado: {resultado}")

    return resultado
  
  return wrapper


@decorator_imprimir
def juros_simples(capital, taxa, tempo):
  juros = capital * taxa * tempo
  return juros

# Exemplo de uso: #
capital = 1000
taxa = 0.05
tempo = 2
# Chamada 
resultado_juros = juros_simples(capital, taxa, tempo)