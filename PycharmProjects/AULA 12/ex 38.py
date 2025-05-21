n1 = int(input('Digite número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'O 1º valor é valor!')
elif n2 > n1:
    print(f'O 2º valor é maior!')
elif n2 == n1:
    print(f'Não existe valor maior, os dois são iguais!')
