import random

# Listas de personagens, ações e locais
personagens = ["um cavaleiro", "um mago", "um ladrão", "um dragão"]
acoes = ["derrotou", "encontrou", "roubou", "fez amizade com"]
locais = ["um castelo abandonado", "uma floresta encantada", "uma caverna sombria", "um reino distante"]

# Escolha aleatória de elementos das listas
personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)

# Exibindo a história gerada
print("Era uma vez,", personagem, "que", acao, "em", local + ".")
