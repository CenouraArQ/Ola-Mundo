valores = (int(input('Digite um valor: ')),
        int(input('Digite outro valor: ')),
        int(input('Digite mais um valor: ')),
        int(input('Digite o último valor: ')))
print(f'Você digitou os valores: {valores}')
print(f'O número 9 aparece {valores.count(9)} vez(es)')
if 3 in valores:
    print(f'O número 3 aparece na {valores.index(3)+1}º posição.')
else:
    print(f'O número 3 não foi encontrado em nenhuma posição!')
print('Os valores pares são:', end=' ')
for pares in valores:
    if pares % 2 == 0:
        print(f'{pares}', end=' ')
