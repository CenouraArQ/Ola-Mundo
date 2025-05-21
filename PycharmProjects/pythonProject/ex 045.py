from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint (0,2)
print('''Suas opçês:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('-=' * 11)
print(computador )