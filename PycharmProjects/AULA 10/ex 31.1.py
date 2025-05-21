viajem = float(input('Qual a distância da sua viajem? '))
if viajem <= 200:
    preço = viajem * 0.50
else:
    preço = viajem * 0.45
print(f'Sua viajem foi de {viajem}Km e custou R${preço:.2f} reais')