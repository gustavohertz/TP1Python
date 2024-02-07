def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"

# Pedindo ao usuário para inserir seu peso e altura
peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

# Calculando o IMC
imc = calcular_imc(peso, altura)

# Classificando o IMC e fornecendo feedback
classificacao = classificar_imc(imc)
print("Seu IMC é:", imc)
print("Você está classificado como:", classificacao)
