valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))
opção = 0
while opção != 5:
    print('''Digite a função que deseja!
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    opção = int(input('Digite a opção: '))
    if opção == 1:
        print(f'{valor1} + {valor2} = {valor1 + valor2}')
    elif opção == 2:
        print(f'{valor1} x {valor2} = {valor1 * valor2}')
    elif opção == 3:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}')
        elif valor2 > valor1:
            print(f'O maior valor é {valor2}')
        elif valor1 == valor2:
            print(f'Os dois valores são iguais.')
    elif opção == 4:
        print('Digite novos números.')
        valor1 = int(input('Digite o 1º valor: '))
        valor2 = int(input('Digite o 2º valor: '))
    elif opção == 5:
        print('Programa encerrado!!!')
    else:
        print('Opção invalida, tente novamente.')
print('Volte sempre.')
