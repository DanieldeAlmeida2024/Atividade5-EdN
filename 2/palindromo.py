import re

def verificar_palindromo(texto: str) -> str:
  """
  Verifica se uma palavra ou frase é um palíndromo. 
  Retorna "Sim" ou "Não".
  """
  # 1. Formata: minúsculas e remove caracteres não alfanuméricos
  texto_formatado = texto.lower()
  texto_limpo = re.sub(r'[^a-z0-9]', '', texto_formatado)

  # 2. Verifica se a string limpa é igual à sua versão invertida
  e_palindromo = texto_limpo == texto_limpo[::-1]

  return "Sim" if e_palindromo else "Não"

def aplicacao_palindromo():
  """Ponto de entrada da aplicação de verificação de palíndromo."""
  print("--- 🔄 Verificador de Palíndromo ---")
  texto_usuario = input("Digite uma palavra ou frase: ")

  resultado = verificar_palindromo(texto_usuario)

  print(f"\nResultado: '{texto_usuario}'")
  print(f"É um palíndromo? **{resultado}**")

# Executa a aplicação
if __name__ == "__main__":
    aplicacao_palindromo()