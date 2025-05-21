#Faça um programa que leia a largura e a altura
#de uma parede em metros, calcule a sua área e a
#quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
área = largura * altura
tinta = área / 2
print(f'Para pintar uma área de {área}m² é necessario {tinta} litros de tinta.')
