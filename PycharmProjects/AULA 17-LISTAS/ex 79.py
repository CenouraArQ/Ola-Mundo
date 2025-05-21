lista = []  # lista vazia
while True:
    # string para perguntar o número
    num = int(input('Digite o valor: '))
    # Se o número não estiver na lista, o programa vai adiconar na lista
    if num not in lista:
        lista.append(num)
        print('Adicionado com sucesso!')
    # Senão, ou seja: se ele estiver na lista == print
    else:
        print('-' * 30)
        print('O número já existe na lista')
        print('-' * 30)

    pergunta = str(input('Deseja continuar? Sim/Não: ')).strip().lower()
    if pergunta not in 'simnãonao':
        while True:
            pergunta = str(input('Deseja continuar? Sim/Não: ')).strip().lower()
            if pergunta in 'sim':
                break
            if pergunta in 'nãonao':
                break
            else:
                continue
    if pergunta in 'sim':
        continue
    if pergunta in 'naonão':
        print('Fim do programa.')
        break

lista.sort()
print(f'Você digitou os valores {lista}')