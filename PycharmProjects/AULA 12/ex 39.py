from datetime import date
atual = date.today().year
ano = int(input('Qual seu ano de nascimento? '))
idade = atual - ano
print(f'Você nasceu em {ano} e tem {idade} anos em {atual}')
if idade == 18:
    print(f'Você completou {idade} anos e já está na hora de se alistar!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você não tem 18 anos. Ainda faltam {18 - idade} anos para de alistar!')
    ano_alistamento = atual + saldo
    print(f'Seu alistamento sera em {ano_alistamento}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já completou 18 anos. Já passou {idade - 18} anos do prazo para se alistar!')
    ano_alistamento = atual - saldo
    print(f'Seu alistamento foi em {ano_alistamento}')