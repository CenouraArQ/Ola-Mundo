valores = list()
for contador in range (0, 5):
    valores.append(int(input('Digite um valor: ')))
for posição, valor in enumerate(valores):
    print(f'Na posição {posição} encontrei o valor {valor}.')
print('Fim da lista!')