from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range (1, 8):
    nascimento = int(input(f'Em que ano a {pessoa}º pessoa nasceu? '))
    idade = atual - nascimento
    print(f'Você nasceu em {nascimento} e tem {idade} anos em {atual}')
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Tivemos {totalmaior} pessoas maiores que 18 anos.')
print(f'Tivemos {totalmenor} pessoas menores que 18 anos.')