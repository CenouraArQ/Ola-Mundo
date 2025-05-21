maior_peso = 0
menor_peso = 0
for pessoa in range (1, 6):
    peso = float(input(f'Qual o peso da {pessoa}º pessoa? '))
    if pessoa == 1: # Se pessoa for igual  1ºpessoa
        maior_peso = peso #O maior_peso recebe o peso
        menor_peso = peso #O menor_peso recebe o peso
    else: # se não for a primeira pessoa
        if peso > maior_peso: # Se o peso é maior que o maior_peso
            maior_peso = peso # maior_peso recebe peso
        if peso < menor_peso: #Se o peso for menor que o menor_peso
            menor_peso = peso #menor_peso recebe o peso
print(f'O maior peso lido foi de {maior_peso}Kg')
print(f'O menor peso lido foi de {menor_peso}Kg')