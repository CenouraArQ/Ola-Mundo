print('Digite 999 se quiser encerrar o programa.')
contador = soma = 0
while True:
    número = int(input('Digite um valor: '))
    if número == 999:
        break
    else:
        contador += 1
        soma += número
print(f'Você digitou {contador} números, e a soma deles é = {soma}')
print('Fim do programa!!!')

#OUTRA MANEIRA

#n = cont = soma = 0
#n = int(input('Digite um valor, [999 para encerrar]: '))
#while n != 999:
#    soma += n
#    cont += 1
#    n = int(input('Digite um valor, [999 para encerrar]: '))
#print(f'Você digitou {cont} números e a soma deles é = {soma}')