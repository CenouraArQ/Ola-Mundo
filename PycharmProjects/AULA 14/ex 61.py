primeiro = int(input('Primeiro um termo: '))
razão = int(input('Digite a razão: '))
número = int(input('Digite a quantidade de termos: '))
contagem = 1
while contagem <= número: #enquanto contagem for menor ou igual a número ele executa.
    print(f'{primeiro} > ',end='')
    primeiro += razão
    contagem += 1
print('FIM.')
