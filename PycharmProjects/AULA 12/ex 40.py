n1 = float(input('Digite sua 1º nota: '))
n2 = float((input('Digite sua 2º nota: ')))
n3 = float(input('Digite sua 3º nota: '))
soma = (n1 + n2 + n3) / 3
print(f'a média é {soma}')
if soma < 5:
    print(f'Você tirou a média {soma} e está REPROVADO!!!')
elif soma >= 5 and soma <7:
    print(f'Você tirou a média {soma} e está de RECUPERAÇÃO!!!')
elif soma >= 7:
    print(f'Você tirou a média {soma} e está APROVADO!!!')