valores = list()
for posição in range (0, 5):
    valores.append(int(input(f'Digite um valor para a posição {posição}: ')))
print(f'Você digitou os valores: {valores}')
print(f'O maior valor é: {max(valores)}'
      f'\nO menor valor é: {min(valores)}')

