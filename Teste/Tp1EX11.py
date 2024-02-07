import random

def lancar_dado():
    return random.randint(1, 6)  # Simula o lançamento de um dado de seis faces

# Pedindo ao usuário para inserir a quantidade de dados a serem jogados
quantidade_dados = int(input("Quantos dados você deseja jogar? "))

# Lançando os dados e exibindo os resultados
print("Resultados dos lançamentos:")
for i in range(quantidade_dados):
    resultado = lancar_dado()
    print("Dado", i+1, ":", resultado)
