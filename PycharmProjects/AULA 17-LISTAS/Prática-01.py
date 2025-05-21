# Podemos criar uma lista vazia de 2 maneiras
valores = []
valores = list()
#deixando assim irá aparecer com os couchetes
valores.append('melancia')
valores.append('uva')
valores.append('laranja')
print(valores)


  #objetos in indices = 3 objetos
for valor in valores:
    print(f'{valor}', end=' ')

#enumerate() para enumerar em ordem a variavel
for posição, valor in enumerate(valores):
# Para cada indice e valor in valores:
    print(f'\nNa posição {posição} encontrei o valor {valor}', end=' ')


