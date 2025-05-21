dados = list()
dados.append('Pedro')
dados.append(25)
print(dados)  #['Pedro', 25]
print(dados[0]) #Pedro
print(dados[1]) #25
#Adionando lista dentro de lista
pessoas = list()
pessoas.append(dados[:]) #adicionar dados na listapessoas
print(pessoas)
#     ............    ............
#     .Pedro, 25 .    .Maria, 19 .
#     .  0     1 .    .  0     1 .
#     ............    ............
#           0               1