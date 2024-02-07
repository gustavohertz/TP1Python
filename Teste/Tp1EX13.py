def eh_palindromo(texto):
    # Remover espaços em branco e converter para minúsculas
    texto = texto.replace(" ", "").lower()
    # Verificar se o texto é igual ao seu inverso
    return texto == texto[::-1]

# Pedindo ao usuário para inserir uma palavra ou frase
palavra_frase = input("Digite uma palavra ou frase: ")

# Verificando se é um palíndromo
if eh_palindromo(palavra_frase):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
