# Faça um programa que leia o comprimento
# do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre
# o comprimento da hipotenusa

#co = float(input('Digite o cateto oposto: ')) # co = cateto oposto
#ca = float(input('Digite o cateto adjacente: ')) # ca = cateto adjacente
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print(f'A hipotenusa vai medir {hi:.2f}')


import math
co = float(input('Digite o cateto oposto: ')) # co = cateto oposto
ca = float(input('Digite o cateto adjacente: ')) # ca = cateto adjacente
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')