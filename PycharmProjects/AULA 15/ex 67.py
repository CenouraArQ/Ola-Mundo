número = 0
while True:
    número = int(input('Deseja ver a tabuada de qual valor? '))
    if número < 0:
        print('PROGRAMA DE TABUADA ENCERRADO!')
        break
    if número >= 0:
        for c in range (1, 11):
            print(f'{número} x {c} = {número * c}')
