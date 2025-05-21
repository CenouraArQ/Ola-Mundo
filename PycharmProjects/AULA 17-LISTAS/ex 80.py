lista = list()
for c in range(0,5):
    número = int(input('Digite um valor: '))
    if c == 0:
        lista.append(número)
        print('Adicionado na posição 0...')
    elif número > lista[len(lista)-1]:
        lista.append(número)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if número <= lista[pos]:
                lista.insert(pos, número)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')


