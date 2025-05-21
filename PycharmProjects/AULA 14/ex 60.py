num = int(input('Digite um número para calcular seu Factorial: '))
contagem = num
resultado = 1
print(f'Calculando {num}! = ',end='')
while contagem > 0: #enquanto a contagem for maior que 0 o programa vai executar
    print(f'{contagem}', end='')
    if contagem > 1:
        print(f' x ', end='')
    else:
        print(' = ',end='')
    resultado *= contagem
    contagem -= 1
print(f'{resultado}')



