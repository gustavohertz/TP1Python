def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    else:
        return x / y

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Digite a opção (1/2/3/4): ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print("Resultado da adição:", adicao(numero1, numero2))
elif opcao == '2':
    print("Resultado da subtração:", subtracao(numero1, numero2))
elif opcao == '3':
    print("Resultado da multiplicação:", multiplicacao(numero1, numero2))
elif opcao == '4':
    print("Resultado da divisão:", divisao(numero1, numero2))
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
