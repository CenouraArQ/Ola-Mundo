número = soma = contador = 0
while True:
    número = int(input('Digite um valor: '))
    if número == 999:
        break
    contador += 1
    soma += número
print(f'Você digitou {contador} números e a soma deles é = {soma}.')
