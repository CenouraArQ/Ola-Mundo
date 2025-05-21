import random
from time import sleep
print('-=-'*15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*15)
sleep(1)
num = int(input('Em que número eu pensei? '))
pc = random.randint(0, 5)
print(pc)
if pc == num:
    print('Parabéns você acertou!')
else:
    print('Você errou!')
