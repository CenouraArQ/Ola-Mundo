estado = {}
brasil = []
for contador in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    #print(e)
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()