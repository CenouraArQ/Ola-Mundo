print('Sequencia de fibonacci')
termos = int(input('Quantos termos deseja mostrar?: '))
num1 = 0
num2 = 1
print(f'{num1}, {num2}', end=', ')
contador = 3
while contador <= termos:
    num3 = num1 + num2
    print(f'{num3}', end=', ')
    num1 = num2
    num2 = num3
    contador += 1
print('FIM')
