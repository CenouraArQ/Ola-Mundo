pessoas = {'nome':'Gustavo','sexo':'M','idade': 22}
print(pessoas)
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print('-='*10)
for k in pessoas.keys():
    print(k)
print('-='*10)

for k in pessoas.values():
    print(k)
print('-='*10)

for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-='*10)

del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-='*10)

pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['peso'] = 98.5
for k, v, in pessoas.items():
    print(f'{k} = {v}')