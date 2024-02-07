import random

# Gerando um número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

while True:
    # Pedindo ao usuário para fazer um palpite
    palpite = int(input("Digite seu palpite: "))

    # Verificando se o palpite está correto, muito alto ou muito baixo
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto:", numero_secreto)
        break
    elif palpite < numero_secreto:
        print("Seu palpite está muito baixo. Tente novamente!")
    else:
        print("Seu palpite está muito alto. Tente novamente!")
