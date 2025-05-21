lista = list()
while True:
    número = int(input('Digite um número: '))
    lista.append(número)
    pergunta = str(input('Deseja continuar? [Sim],[Nâo]: ')).strip().lower()[:]
    if pergunta in 'sim':
        continue
    elif pergunta in 'nãonao':
        print('Fim do programa!')
        break
    else:
        print('Tente novamente.')
print(f'Você digitou {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente...{lista}')
if 5 in lista:
    print('O valor 5 foi digitado e esta na lista.')
else:
    print('O valor 5 não foi digitado e por isso não está na lista.')
