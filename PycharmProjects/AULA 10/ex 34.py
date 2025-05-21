salario = float(input('Qual é o salário do funcionario? R$'))
if salario > 1250:
    recebe = salario * 10 / 100
if salario <= 1250:
    recebe = salario * 15 / 100
print(f'Quem recebe R${salario:.2f} reais, receberá um aumento de R${recebe:.2f} reais, total R${salario + recebe:.2f} reais')
