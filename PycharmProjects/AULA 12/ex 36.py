casa = float(input('Qual o valor da casa? '))
salário = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos deseja pagar? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos ')
print(f'a prestação será de R${prestação:.2f}')
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')