from random import randint
print('Vamos jogar PAR ou IMPAR!!!')
contador = 0
while True:
    computador = randint(0, 10)
    número = int(input('Escolha um número entre 0 e 10: '))
    soma = (número + computador) % 2
    opção = str(input('Par ou Impar? ')).strip().upper()[0]
    if opção in 'P' and soma == 0:
        print('VOCÊ GANHOU!!!')
        print(f'Eu joguei {computador} e você {número}')
        print(f'A soma deles é = {computador + número} e o resultado é Par!')
        contador += 1
    if opção in 'I' and soma == 1:
        print('VOCÊ GANHOU!!!')
        print(f'Eu joguei {computador} e você {número}')
        print(f'A soma deles é = {computador + número} e o resultado é Impar!')
        contador += 1
    if opção in 'P' and soma == 1:
        print('VOCÊ PERDEU!!!')
        print(f'Eu joguei {computador} e você {número}')
        print(f'A soma deles é = {computador + número} e o resultado é Impar')
        break
    elif opção in 'I' and soma == 0:
        print('VOCÊ PERDEU!!!')
        print(f'Eu joguei {computador} e você {número}')
        print(f'A soma deles é = {computador + número} e o resultado é Par')
        break
print(f'GAME OVER!!! Você venceu {contador} vezes.')