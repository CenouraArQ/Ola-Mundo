soma = contador = maior = menor = 0
opção = 'S'
while opção in 'S':
    número = int(input('Digite um valor: '))
    opção = str(input('Deseja continuar? [Sim/Não]: ')).strip().upper()[0]
    contador += 1
    soma += número
    média = soma / contador
    if contador == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
    if opção in 'N':
        print(f'Foram digitados {contador} números e a soma deles é {soma} sua média foi {média:.2f}')
        print(f'O maior valor foi {maior} e o menor é {menor}.')
        break
    elif opção not in 'S' and 'N':
        print('Error 404!')

