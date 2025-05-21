produto = float(input('Qual o valor do produto? R$ '))
desconto = produto * 5  / 100
pagar = produto - desconto
print(f'O produto custou R${produto} e com 5% de desconto o preço final é de R${pagar} reias.')