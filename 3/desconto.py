def calcular_preco_com_desconto(preco_original: float, percentual_desconto: float) -> tuple[float, float]:
  """Calcula o valor do desconto e o preço final."""
  if preco_original < 0 or not (0 <= percentual_desconto <= 100):
    raise ValueError("Preço deve ser positivo e desconto entre 0 e 100%.")

  valor_desconto = preco_original * (percentual_desconto / 100)
  preco_final = preco_original - valor_desconto
  return valor_desconto, preco_final

def aplicacao_desconto():
  """Ponto de entrada da aplicação de cálculo de desconto."""
  print("--- 🏷️ Calculadora de Desconto ---")
  try:
    preco_original = float(input("Digite o preço original do produto (ex: 250.75): R$ "))
    percentual_desconto = float(input("Digite o percentual de desconto (ex: 10): "))
    
    valor_desconto, preco_final = calcular_preco_com_desconto(preco_original, percentual_desconto)
    
    print("\n--- Resultado ---")
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Percentual de Desconto: {percentual_desconto}%")
    print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
    print(f"**Preço Final: R$ {preco_final:.2f}**")

  except ValueError as e:
    print(f"Erro: Entrada inválida. {e}")

# Executa a aplicação
if __name__ == "__main__":
    aplicacao_desconto()