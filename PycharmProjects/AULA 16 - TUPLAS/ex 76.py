listagem = ('Lápis', 1.75, #index 0, 1
            'Borracha', 2.00, #index 2, 3
            'Caderno', 15.90, #index 4, 5
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
# O nome dos produtos está em posição par e o preço em posições impares

print('-'*40)

print(f'{'LISTAGEM DE PREÇOS':^40}')

print('-'*40)

for posição in range(0, len(listagem)): #in range vai mostrar d index (0, até o 18) pq a função len(listagem) vai contar todos os index da tupla
    if posição % 2 == 0: #par
        print(f'{listagem[posição]:.<30}', end='')
    else: # == 1, impar
        print(f'R${listagem[posição]:>7.2f}')

print('-'*40)
