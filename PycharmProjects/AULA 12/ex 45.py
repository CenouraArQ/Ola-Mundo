import random
pc = random.randint(1, 3)
print('Vamos jogar JOKENPÔ!')
print('''Digite sua escolha:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
opção = int(input('Sua opção: '))
print(pc)
if pc == 1 and opção == 2:
    print('você perdeu!')
elif pc == 1 and opção == 3:
    print('Você perdeu!')
elif pc == 1 and opção == 1:
    print('Você Ganhou!')
elif pc == 2 and opção == 3:
    print('Você perdeu!')
elif pc == 2 and opção == 1:
    print('Você perdeu!')
elif pc == 3 and opção == 2 and opção != 1 and opção != 3:
    print('Você perdeu!')
