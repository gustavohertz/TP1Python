# Pedindo ao usuário para inserir o valor da compra
valor_compra = float(input("Digite o valor da compra: R$"))

# Aplicando descontos com base no valor da compra
if valor_compra > 200:
    desconto = 0.15
    valor_desconto = valor_compra * desconto
elif valor_compra > 100:
    desconto = 0.10
    valor_desconto = valor_compra * desconto
else:
    desconto = 0
    valor_desconto = 0

# Calculando o valor total com desconto
valor_total = valor_compra - valor_desconto

# Exibindo o valor total com desconto
print("Valor da compra: R${:.2f}".format(valor_compra))
print("Desconto aplicado: {:.0%}".format(desconto))
print("Valor do desconto: R${:.2f}".format(valor_desconto))
print("Valor total com desconto: R${:.2f}".format(valor_total))
