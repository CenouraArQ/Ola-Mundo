from random import randint
pc = randint(0, 10)
palpites = 0
print('Adivinhe em qual número eu pensei de 0 a 10 !!!')
jogador = int(input('Em que número eu pensei? '))
#print(pc)
while jogador != pc:
    if jogador != pc:
        print('='*30)
        print('Você errou, tente novamente!')
        palpites += 1
    pc = randint(0, 10)
    print('='*30)
    jogador = int(input('Em que número eu pensei? '))
    #print(pc)
    if jogador == pc:
        print(f'Você acertou, eu pensei no número {pc}.')
print(f'Você deu {palpites} palpites até conseguir acertar!!!')

