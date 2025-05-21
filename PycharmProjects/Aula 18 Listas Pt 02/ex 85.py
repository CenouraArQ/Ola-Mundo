lista = [[], []]
valor = 0
for index in range(1, 8):
    valor = int(input(f'Digite um valor qualquer {index}º: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append((valor))
lista[0].sort()
lista[1].sort()
print(f'Todos os valores pares são {lista[0]}'
      f'\nE os valores impares são {lista[1]}')

