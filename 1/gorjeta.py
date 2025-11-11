def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
  """Calcula o valor da gorjeta a ser deixada."""
  if valor_conta < 0 or porcentagem_gorjeta < 0:
    raise ValueError("O valor da conta e a porcentagem da gorjeta devem ser positivos.")
    
  fator_gorjeta = porcentagem_gorjeta / 100
  valor_gorjeta = valor_conta * fator_gorjeta
  return valor_gorjeta

def aplicacao_gorjeta():
  """Ponto de entrada da aplicação de cálculo de gorjeta."""
  print("--- 💰 Calculadora de Gorjeta ---")
  try:
    valor_conta = float(input("Digite o valor total da conta (ex: 150.00): R$ "))
    porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta desejada (ex: 15): "))

    valor_da_gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
    valor_total = valor_conta + valor_da_gorjeta

    print("\n--- Resultado ---")
    print(f"Valor da Gorjeta: R$ {valor_da_gorjeta:.2f}")
    print(f"Total a pagar (Conta + Gorjeta): R$ {valor_total:.2f}")

  except ValueError as e:
    print(f"Erro: Entrada inválida. {e}")

# Executa a aplicação
if __name__ == "__main__":
    aplicacao_gorjeta()