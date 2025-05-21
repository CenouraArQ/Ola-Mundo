
número = int(input('Digite um número: '))
total = 0
for c in range(1, número + 1):
    if número % c == 0: # % usá-se para encontrar o resto da divisão
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[32m',end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO número {número} foi divisível {total} vezes.')
if total == 2: # somente 2 número foi divisel que resultou = á zero 0
    print('E por isso ele É PRIMO.')
else:
    print('E por isso ele NÃO É PRIMO.')
