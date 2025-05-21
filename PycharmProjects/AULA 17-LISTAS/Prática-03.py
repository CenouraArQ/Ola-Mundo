a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}'
      f'\nLista B: {b}')
print('-'*21)
#Dessa maneira o python entende que esta fazendo uma ligação entre as duas variaveis
# e no momento que altera um objeto em qual quer uma das duas, a outra também irá receber essa modificação

a = [2, 3, 4, 7]
b = a[:] #aqui o segredo [:]
b[2] = 8
print(f'Lista A: {a}'
      f'\nLista B: {b}')
#Dessa maneira eu faço b criar uma copía separada de a
# e assim posso modificar b sem alterar a, pois as duas variaveis não tera ligação nenhuma