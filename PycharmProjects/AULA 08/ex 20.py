import random
#from random import shuffle
n1 = str(input('1º Aluno: '))
n2 = str(input('2º Aluno: '))
n3 = str(input('3º Aluno: '))
n4 = str(input('4º Aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista) #shuffler = embaralhar a lista
#shuffle(lista)
print(f'A ordem de apresentação sera: ')
print(lista)