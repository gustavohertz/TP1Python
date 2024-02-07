def historia():
    print("Bem-vindo à sua aventura!")

    escolha = input("Você está em uma encruzilhada. Você quer ir para a esquerda ou para a direita? (esquerda/direita): ")

    if escolha.lower() == "esquerda":
        escolha = input("Você encontrou um rio. Você quer atravessá-lo a nado ou procurar uma ponte? (nado/ponte): ")
        if escolha.lower() == "nado":
            print("Você atravessou o rio a nado e chegou ao outro lado com segurança!")
        elif escolha.lower() == "ponte":
            print("Você encontrou uma ponte e atravessou o rio com segurança!")
        else:
            print("Opção inválida.")
    elif escolha.lower() == "direita":
        escolha = input("Você encontrou uma caverna. Você quer entrar na caverna ou continuar pelo caminho? (caverna/caminho): ")
        if escolha.lower() == "caverna":
            print("Você entrou na caverna e encontrou um tesouro! Parabéns!")
        elif escolha.lower() == "caminho":
            print("Você decidiu continuar pelo caminho e encontrou uma cidade amigável.")
        else:
            print("Opção inválida.")
    else:
        print("Opção inválida.")

# Executando a história
historia()
