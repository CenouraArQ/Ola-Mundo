# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e
# tangente desse ângulo.

#import math
#ângulo = float(input('Digite um ângulo: '))
#seno = math.sin(math.radians(ângulo))
#print(f'O ângulo de {ângulo} tem o SENO de {seno:.2f}')
#cosseno = math.cos(math.radians(ângulo))
#print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')
#tangente = math.tan(math.radians(ângulo))
#print(f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}')

from math import radians, sin, cos, tan
ângulo = float(input('Digite um ângulo: '))
seno = sin(radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(ângulo))
print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(ângulo))
print(f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}')