matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_pares = maior = soma_da_coluna = 0
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-='*20)
for l in range (0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()
print('-='*20)
print(f'a) A soma dos valores pares é {soma_pares}')
for l in range (0, 3):
    soma_da_coluna += matriz[l][2]
print(f'b) A soma dos valores da 3º coluna é {soma_da_coluna}')
for c in range (0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')

