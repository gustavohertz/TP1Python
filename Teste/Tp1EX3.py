def combine_names(username1, username2):
    # Pegando a primeira metade do primeiro nome de usuário
    metade_username1 = username1[:len(username1) // 2]

    # Pegando a segunda metade do segundo nome de usuário
    metade_username2 = username2[len(username2) // 2:]

    # Combinando as duas metades para formar o novo nome
    novo_nome = metade_username1 + metade_username2

    return novo_nome

# Recebendo os nomes de usuário
nome1 = input("Digite o primeiro nome de usuário: ")
nome2 = input("Digite o segundo nome de usuário: ")

# Combinando os nomes de usuário
novo_nome = combine_names(nome1, nome2)

print("O novo nome combinado é:", novo_nome)
