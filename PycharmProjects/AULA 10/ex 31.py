viajem = float(input('Qual a distância da sua viajem? '))
p1 = 0.50
p2 = 0.45
if viajem <= 200:
    print(f'Sua viajem irá custar R${viajem * p1:.2f} reais')
else:
    print(f'Sua viajem ultrapassou os 200km e ira custar R${viajem * p2:.2f} reais')