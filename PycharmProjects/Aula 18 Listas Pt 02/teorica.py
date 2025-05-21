dados = list()
dados.append('Pedro')
dados.append(25)
print(dados)  #['Pedro', 25]
print(dados[0]) #Pedro
print(dados[1]) #25
#Adionando lista dentro de lista
pessoas = [['Pedro', 25], ['Maria',19], ['Joao', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[1])
print(pessoas[2][0])
#     ............    ............
#     .Pedro, 25 .    .Maria, 19 .
#     .  0     1 .    .  0     1 .
#     ............    ............
#           0               1