import datetime

def calcular_idade_em_dias(ano_nascimento: int) -> int:
  """
  Calcula a idade de uma pessoa em dias, considerando a data atual.
  Esta função considera dias exatos e anos bissextos.
  """
  try:
    # Cria uma data de nascimento no dia 1 de janeiro do ano fornecido
    data_nascimento = datetime.date(ano_nascimento, 1, 1)
  except ValueError:
    # Lida com anos muito antigos ou inválidos
    raise ValueError("Ano de nascimento inválido.")
    
  data_atual = datetime.date.today()
  
  if data_nascimento > data_atual:
    return 0 # Pessoa ainda não nasceu

  # Calcula a diferença entre as datas
  diferenca = data_atual - data_nascimento
  
  return diferenca.days

def aplicacao_idade_em_dias():
  """Ponto de entrada da aplicação de cálculo de idade em dias."""
  print("--- 🗓️ Calculadora de Idade em Dias ---")
  try:
    ano_nascimento = int(input("Digite o seu ano de nascimento (ex: 1990): "))
    
    dias_vividos = calcular_idade_em_dias(ano_nascimento)

    print("\n--- Resultado ---")
    print(f"Seu ano de nascimento é: {ano_nascimento}")
    print(f"Você tem aproximadamente **{dias_vividos:,} dias** de vida!")

  except ValueError as e:
    print(f"Erro: Entrada inválida. {e}")

# Executa a aplicação
if __name__ == "__main__":
    aplicacao_idade_em_dias()