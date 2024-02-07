# Opções de voto
opcoes = ["Opção A", "Opção B", "Opção C"]

# Inicializando o dicionário de contagem de votos
votos = {opcao: 0 for opcao in opcoes}

# Solicitando votos ao usuário
print("Por favor, vote nas opções disponíveis:")
for i, opcao in enumerate(opcoes, start=1):
    print(f"{i}. {opcao}")

while True:
    voto = input("Digite o número correspondente à sua opção de voto (ou 'fim' para encerrar): ")
    
    if voto.lower() == 'fim':
        break
    
    try:
        indice_opcao = int(voto) - 1
        if 0 <= indice_opcao < len(opcoes):
            votos[opcoes[indice_opcao]] += 1
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas o número correspondente à sua opção de voto.")

# Exibindo os resultados dos votos
print("\nResultados dos votos:")
for opcao, num_votos in votos.items():
    print(f"{opcao}: {num_votos} votos")
