extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis',
'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    número = int(input('Digite um número entre 0 e 20: '))
    if número >= 0 and número <= 20:
        print(f'Você digitou o número: {extenso[número]}')
        break
    else:
        continue
