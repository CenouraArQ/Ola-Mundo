num = int(input('Digite o factorial: '))
print(f'Factorial de {num}!',end=' = ')
resultado = 1
for contagem in range (1, num + 1):
    print(f'{contagem}', end='')
    if contagem < num: #se contagem for menor que o número
        print(' x ',end='')
    else:
        print(' = ',end='')
    resultado *= contagem
print(resultado)
