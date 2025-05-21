lista = list()
pares = list()
impares = list()
while True:
    número = int(input('Digite um número: '))
    cancelar = str(input('Deseja continuar? [Sim],[Não]: ')).strip().lower()
    lista.append(número)

    if número % 2 == 0:
        pares.append(número)

    else:
        impares.append(número)

    if cancelar in 'nãonao':
        print('Fim do programa.')
        break
print(f'A lista completa: {lista}')
print(f'Os números impares são {impares}')
print(f'Os números pares são {pares}')