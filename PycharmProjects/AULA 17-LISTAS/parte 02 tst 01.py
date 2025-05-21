#Criação de dados de uma lista para atendimento.
dados = list()
turma = list()

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    turma.append(dados[:])
    dados.clear()
    continuar = str(input('Continuar? [Sim], [Não]: ')).lower()
    if continuar in 'naonão':
        break
print(turma[0][0])
print(turma[1][0])
print(turma[2][1])
