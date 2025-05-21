frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras) # joina() eliminar os espaços
#print(f'Você digitou a frase {frase}')
inverso = junto [::-1]
#print(junto, inverso)
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos uma frase palindrómo.')
else:
    print('A frase digitada não é um palindrómo.')