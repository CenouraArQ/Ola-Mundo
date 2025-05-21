nome = str(input('Qual é seu nome? ')).upper()
if nome == 'Gustavo':
    print('Que nome bonito!'.upper())
elif nome == 'Pedro'.upper() or nome == 'Maria'.upper() or nome == 'Paulo'.upper():
    print(f'Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claúdia Jessica Juliana'.upper():
    print(f'Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}!')