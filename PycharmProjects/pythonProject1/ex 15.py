dias = int(input('Quantos dias alugado? '))
km = int(input('Quantos Km rodados? '))
pago = (60 * dias) + (km * 0.15)
print(f'Você alugou o carro por {dias} dias e rodou {km} quilometros e total a pagar é de R${pago:.2f} ')