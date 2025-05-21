medida = float(input('Uma distância em metros: '))
km = medida * 0.001 #quilometros
hm = medida * 0.01 #hectômetro
dam = medida * 0.1 #decânmetro
m = medida * 1 #metro
dm = medida * 10 #decímetro
cm = medida * 100 #centimetros
mm = medida * 1000 #melimetros
print(f'A medida de {medida}m corresponde a \n{mm}mm  \n{cm}cm \n{dm}dm \n{dam:.1f}dam \n{hm}hm \n{km}km')
