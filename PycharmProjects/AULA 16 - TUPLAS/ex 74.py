from random import randint
números = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

for tupla in números:
    print(tupla, end=', ')

print(f'\nO maior valor foi: {max(números)}')
print(F'O menor valor foi: {min(números)}')



