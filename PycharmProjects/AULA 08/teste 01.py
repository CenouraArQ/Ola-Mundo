#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print(f'A raiz de {num} é igual a {math.floor(raiz)}')

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz)}')
