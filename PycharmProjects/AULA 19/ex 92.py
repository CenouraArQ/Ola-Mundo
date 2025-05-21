from datetime import datetime

dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
#idade = datetime.now().year - nascimento
dados['idade'] = datetime.now().year - nascimento
dados['stps'] = int(input('Digite sua carteira de trabalho. (0 "não tem"): '))

if dados['stps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
else:
    dados['stps'] = 'Não Existe.'
print('-=' * 30)

for k, v in dados.items():
    print(f'   = {k}: {v}')

print(dados)
