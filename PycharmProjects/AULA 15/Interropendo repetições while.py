n = s = 0
while True:
    n = int(input('Informe um valor: '))
    if n == 999:
        break
    s += n
print(f'A soma dos valores é = {s}')