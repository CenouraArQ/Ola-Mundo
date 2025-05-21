# + (Adição)
# - (Subtração)
# * (Multiplicação)
# / (Divisão)
# ** (Potência)
# // (Divisão inteira)
# % (Resto da divisão)
#Console python
a = 5 + 3 * 2
b = 5 ** 2
c = 5 ** 3
d = 19 // 2
e = 19 / 2
f = 18 % 2
g = pow (4 , 3)
h = 81 ** (1/2) # 81 elevado a meio
i = 127 ** (1/3) #raiz cubica, 127 elevado a um terso
j = 'oi' + 'olá'
k = 'oi' * 5
l = '=' * 20
nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer {nome:20}!') #alinhamento em  20 espaços
print(f'Prazer em te conhecer {nome:>20}!') # alinhamento a direita em 20 espaços
print(F'prazer em te conhecer {nome:<20}!') # alinhamento a esquerda em 20 espaços
print(F'prazer em te conhecer {nome:^20}!') #alinhamento em 20 espaços centralizado
