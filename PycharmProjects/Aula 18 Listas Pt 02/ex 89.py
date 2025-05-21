lista = []
while True:
    nome = str(input('Nome: '))
    nota = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    média = (nota + nota2) / 2
    lista.append([nome, [nota, nota2], média])
    pergunta = str(input('Quer continuar? [Sim],[Não]: ')).strip().lower()
    if pergunta in 'naonão':
        break
print('-=' * 30)
#print(lista)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*30)
for indice, aluno in enumerate(lista):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-='*30)
    opção = int(input('Mostrar as notas de qual aluno? (999 interromper): '))
    if opção == 999:
        print('Finalizando...')
        break
    if opção <= len(lista) - 1:
        print(f'Notas de {lista[opção][0]} são {lista[opção][1]}')
print('Obrigado pelos serviços.')
