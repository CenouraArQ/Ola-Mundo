primeiro = int(input('Primeiro termo: '))
razão = int(input('Digite a razão: '))
número= int(input('Quantos termos exibir: ')) #número de termos
ultimo = primeiro + (número-1) * razão
ultimo = ultimo + 1
for c in range (primeiro, ultimo, razão):
    print(c, end=' > ')
print('Acabou!')

