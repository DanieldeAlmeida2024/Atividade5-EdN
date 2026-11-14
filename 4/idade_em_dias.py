import datetime

def calcular_idade_em_dias(ano_nascimento: int, referencia: datetime.date | None = None) -> int:
  """
  Calcula dias desde 1 de janeiro do ano informado (aproximação).
  Sem dia e mês de nascimento, a idade real em dias não pode ser conhecida.
  """
  data_atual = referencia if referencia is not None else datetime.date.today()
  if not isinstance(data_atual, datetime.date):
    raise ValueError('A data de referência deve ser uma data válida.')
  if type(ano_nascimento) is not int or ano_nascimento < 1 or ano_nascimento > data_atual.year:
    raise ValueError('Ano de nascimento inválido ou futuro.')
  try:
    # Cria uma data de nascimento no dia 1 de janeiro do ano fornecido
    data_nascimento = datetime.date(ano_nascimento, 1, 1)
  except ValueError:
    # Lida com anos muito antigos ou inválidos
    raise ValueError("Ano de nascimento inválido.")
    

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