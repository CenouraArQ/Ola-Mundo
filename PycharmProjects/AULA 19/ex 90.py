lista = {}
lista['nome'] = str(input('Nome: '))
lista['média'] = float(input(f'Média de {lista["nome"]}: '))
print('-=' * 20)

if lista['média'] >= 7:
    lista['situação'] = 'Aprovado'
elif 6 <= lista['média'] < 7:
    lista['situação'] = 'Recuperação.'
else:
    lista['situação'] = 'Reprovado'

for k, v in lista.items():
    print(f'  - {k} é igual a {v}')
print('-=' * 20)
print(lista)

