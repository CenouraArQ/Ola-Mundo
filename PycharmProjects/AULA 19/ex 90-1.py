lista = {}
ficha = []
contador = 0
while True:
    lista['nome'] = str(input('Nome: '))
    lista['média'] = float(input(f'Média de {lista["nome"]}: '))
    if lista['média'] >= 7:
        lista['situação'] = 'Aprovado'
    elif 6 <= lista['média'] < 7:
        lista['situação'] = 'Recuperação.'
    else:
        lista['situação'] = 'Reprovado'
    ficha.append(lista.copy())
    pergunta = str(input('Deseja continuar? [Sim,Não]: ')).strip().lower()
    print('-=' * 20)
    if pergunta in 'naonão':
        print('Fim do programa.')
        break
for e in ficha:
    for k, v, in e.items():
        print(f'  - {k} é igual a {v}')
    print()
print(ficha)