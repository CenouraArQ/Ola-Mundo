print('Analisando um triângulo...')
r1 = float(input('1º segmento: '))
r2 = float(input('2º segmento: '))
r3 = float(input('3º segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos acima PODEM formar um triângulo!')
else:
    print(f'Os segmentos acima NÂO podem formar um triângulo!')
