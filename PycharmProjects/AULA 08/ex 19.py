#Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro.
# Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
#from random import chocie
n1 = str(input('1º Aluno: '))
n2 = str(input('2º Aluno: '))
n3 = str(input('3º Aluno: '))
n4 = str(input('4º Aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista) #choice = uma escolha
#escolhido = choice(lista)
print(f'O aluno escolhido foi: {escolhido}')