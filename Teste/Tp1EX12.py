# Pedindo ao usuário para inserir uma frase
frase = input("Digite uma frase: ")

# Dividindo a frase em palavras
palavras = frase.split()

# Classificando as palavras como curtas ou longas
palavras_curtas = []
palavras_longas = []

for palavra in palavras:
    if len(palavra) < 5:
        palavras_curtas.append(palavra)
    else:
        palavras_longas.append(palavra)

# Exibindo as palavras classificadas
print("Palavras curtas:", palavras_curtas)
print("Palavras longas:", palavras_longas)
