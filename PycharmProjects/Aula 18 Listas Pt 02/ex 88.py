from random import randint
from time import sleep
lista = list()
jogos = []
print('-'*30)
print('     JOGA NA MEGA SENA    ')
print('-'*30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? ')) #quantidade de jogos
total = 1 #total de jogos
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-='*3, f'SORTEANDO {quantidade} JOGOS ', '-='*3)
for i, l in enumerate(jogos): #Para cada indice com a lista in enumerate(jogos)
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, 'Boa Sorte!', '-='*5)
