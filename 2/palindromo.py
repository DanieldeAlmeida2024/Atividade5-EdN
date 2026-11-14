import unicodedata

def verificar_palindromo(texto: str) -> str:
  """
  Verifica se uma palavra ou frase é um palíndromo. 
  Retorna "Sim" ou "Não".
  """
  if not isinstance(texto, str):
    raise TypeError('O texto deve ser uma string.')
  normalizado = unicodedata.normalize('NFKD', texto.casefold())
  texto_limpo = ''.join(
    caractere for caractere in normalizado
    if not unicodedata.combining(caractere) and caractere.isalnum()
  )

  # 2. Verifica se a string limpa é igual à sua versão invertida
  e_palindromo = bool(texto_limpo) and texto_limpo == texto_limpo[::-1]

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