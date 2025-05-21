num = [2, 5, 9, 1]

num[2] = 3 # vai substituir o número 9 por 3
print(num)

num.append(7) #adicionando o valor 7 na variavel
num = [2, 5, 9, 1, 7]
print(num)

num.sort() #para ordenar a variavel

print(num)

num.sort(reverse=True) #ordenar a variavel ao contrario
print(num)

num.insert(2, 2) #na posição 2 vai inserir(acrescentar) o valor 2
num = [2, 5, 2, 9, 1, 7]
print(num)

num.pop(2)  #eliminar o 1º número 2 da lista
print(num)

num.remove(2) #elimina o 1º número 2 da lista
print(num)

print(f'Esta lista tem {len(num)} elementos.') #contagem da quantidade de emelentos