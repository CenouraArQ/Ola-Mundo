
valor = int(input('Quanto desejar sacar do caixa eletrônico? R$ '))
cédula = 50
total_de_cédula = 0
while True:

    if valor >= cédula: #Se o valor for maior ou igual a 50 reais
        valor -= cédula #Vai retirar o maximo de cédulas de 50 reais
        total_de_cédula += 1 #Vai contar quantas cédulas sera necessario

    else: #Se valor não for maior ou igual a 50 reais.
        print(f'Total de {total_de_cédula} cédulas de R${cédula}')

        if cédula == 50: #Se cédula for igual a 50 reais.
            cédula = 20 #cédula irá receber o novo valor de 20 reais.

        elif cédula == 20: #Se não se cédula foi igual a 20
            cédula = 10 #Cédula irá receber o novo valor de 10

        elif cédula == 10: #Se não se cédula for igual a 10
            cédula = 1 #Cédula ira receber o novo valor de 1 real

        total_de_cédula = 0

        if valor == 0:
            break
