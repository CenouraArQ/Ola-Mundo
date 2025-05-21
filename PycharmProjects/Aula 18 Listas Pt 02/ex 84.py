lista = []
grupo = []
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(grupo) == 0:
        pmaior = pmenor = lista[1]
    else:
        if lista[1] > pmaior:
            pmaior = lista[1]
        if lista[1] < pmenor:
            pmenor = lista[1]
    grupo.append(lista[:])
    lista.clear()
    continuar = str(input('Deseja continuar? [Sim],[Não]')).strip().lower()
    if continuar in 'nãonao':
        break
print('-'*30)
print(f'Os dados foram {grupo}')
print(f'Foram cadastrados {len(grupo)} pessoas.')
print(f'O maior peso foi de {pmaior} Kg. Peso de ', end='')
for p in grupo:
    if p[1] == pmaior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {pmenor} Kg. Peso de ', end='')
for p in grupo:
    if p[1] == pmenor:
        print(f'[{p[0]}] ', end='')
print()
