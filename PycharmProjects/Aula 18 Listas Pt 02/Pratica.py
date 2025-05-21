teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
print(galera)

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

for pessoa in galera:
    print(pessoa[0])
    print(pessoa[1])
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade. ')