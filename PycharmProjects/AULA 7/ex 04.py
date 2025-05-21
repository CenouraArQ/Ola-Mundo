v1 = float(input('Distãncia em metros: '))
centimetros = v1 * 100
milimetros = v1 * 1000
decimetro = v1 * 10
decametro = v1 * 0.1
quilometro = v1 * 0.001
hectometro = v1 * 0.01
print(f'{v1} metros convertido para centimentros é igual {centimetros} e para milimetros é igual a {milimetros}')
print(f'{v1} em decimetro {decimetro}')
print(f'{v1} em quilometro {quilometro}')
print(f'{v1} em hectometro {hectometro}')
print(f'{v1} em decametro {decametro:.1f}')