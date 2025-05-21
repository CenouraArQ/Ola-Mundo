real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 6.00
euro = real / 6.28
iene = real / 0.83
libra = real / 7.60
#Ano 2024 dezembro
print(f'Você tem R${real:.2f} reais e pode commprar US${dolar:.2f} dólares\n'
      f'€${euro:.2f} Euros\n'
      f'¥${iene:.2f} Ienes\n'
      f'£${libra:.2f} Libras')