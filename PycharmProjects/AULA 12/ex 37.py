n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{n} convertido para BINÁRIO é igual a = {bin(n)[2:]}') # bin = BINÁRIO
elif opção == 2:
    print(f'{n} convertido para OCTAL é igual a = {oct(n)[2:]}') # oct = Octal
elif opção == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a = {hex(n)[2:]}') #hex = HEXADECIMAL
else:
    print('Opção inválida, tente novamente!!!')