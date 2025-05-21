total = produto = menor = contador = 0

while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço R$ '))
    pergunta = str(input('Deseja continuar com a compra? [Sim/Não]: ')).strip().upper()[0]
    print('=-'*30)
    contador += 1
    total += preço
    if contador == 1 or preço < menor:
        menor = preço
        barato = nome
    #else:
        #if preço < menor:
            #menor = preço
            #barato = nome
    if preço >= 1000:
        produto += 1
    if pergunta in 'S':
        ...
    if pergunta in 'N' or pergunta not in 'SN':
        print('O PROGRAMA SERÁ ENCERRADO!!!')
        break
print(f'O total gasto na compra foi de R${total:.2f} reais.')
print(f'Temos {produto} produtos custam mais de R$1000 reais.')
print(f'O produto mais barato foi {barato}.')