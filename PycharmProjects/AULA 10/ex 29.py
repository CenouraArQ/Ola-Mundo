velocidade = int(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de 80km/h!')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f} reais')
print('Bom dia, dirija com segurança!')
