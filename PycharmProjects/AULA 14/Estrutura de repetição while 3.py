número = 1
par = 0
impar = 0
while número != 0:
    número = int(input('Digite um valor: '))
    if número != 0:
        if número % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'{par} são pares.')
print(f'{impar} são impares.')
print('Acabou')