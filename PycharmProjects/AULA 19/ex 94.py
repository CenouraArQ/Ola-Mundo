lista = []
mulheres = []
soma = cont = 0
dados = {}
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: Masculino [M], Feminino [F]: ')).upper().strip()[0]
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    cont += 1
    soma = (soma + dados['idade'])
    lista.append(dados.copy())
    pergunta = str(input('Continuar?: [Sim], [Não]: ')).strip().lower()
    if pergunta in 'naonão':
        break

print(lista)

print('-='*30)
print(f'A) Foram cadastradas {len(lista)} pessoas.')

print('-=' * 30)
print('== Lista Feminina ==')
for e in mulheres:
    print(f'  Nome = {e}')
média = soma / cont
#print(soma)
print('-='*30)
print(f'B) Á média das idades é igual á {média:.1f} anos')

print('-=' * 30)
print('D)Lista das pessoas que estão acima da média:')
if dados['idade'] > média:
    for k, v in lista.items(média):
        print(f'{k}, {v}', end=' ')