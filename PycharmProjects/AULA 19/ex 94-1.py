galera = []
pessoa = {}
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: Masculino [M], Feminino [F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Error! Por favor, digite Masculino [M] ou Feminino [F].')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        pergunta = str(input('Continuar? [Sim], [Não]: ')).lower().strip()
        if pergunta in 'nãonaosim':
            break
        print('ERROR! Responda apenas [Sim] ou [Não].')
    if pergunta in 'nãonao':
        break
#print(pessoa)
print(galera)
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print('-='*30)
média = soma / len(galera)
print(f'A média de idade, é de {média:.0f} anos.')
print('-='*30)
print(f'As mulheres cadastradas foram: ')
for p in galera:
    if p['sexo'] in 'F':
        print(f'= {p["nome"]}')
print('-='*30)
print('Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('-='*30)
print('Programa Encerrado!')