lanche = 'hamburguer', 'suco', 'pizza', 'pudim'

for comida in lanche:
    print(f'Eu vou comer {comida}')   # Maneira 1
print('-='*20)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') # Maneira 3
print('-='*20)

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}') # Maneira 2

