listanum = list()
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite o valor na posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

# Parte 3: Prints
print(f'Você digitou os valores: {listanum}')
print(f'O maior valor foi: {maior} nas posiçôes', end=' ')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor foi: {menor} nas posições', end=' ')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
