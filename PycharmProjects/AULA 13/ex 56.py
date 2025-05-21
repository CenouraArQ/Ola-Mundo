soma = 0
mais_velho = 0
nome_velho = ''
total_mulheres20 = 0
for pessoa in range (1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M] para masculino e [F] para feminino: ')).strip().upper()
    soma += idade
    if pessoa == 1:
        mais_velho = idade
        nome_velho = nome
    if sexo in 'mM' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
    if sexo in 'fF' and idade > 20:
        total_mulheres20 += 1
print(f'A média das idades é {soma / 4:.0f}')
print('O nome do homem mais velho é', nome_velho)
print(f'existe {total_mulheres20} mulheres com menos de 20 anos.')