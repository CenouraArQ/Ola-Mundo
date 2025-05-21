idade =  contador = homens = mulher = 0
while True:
    idade = int(input('Qual idade deseja cadastrar? '))
    sexo = str(input('Qual o sexo deseja cadastrar? [Masculino/Feminino]: ')).strip().upper()[0]
    if idade >= 18:
        contador += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if sexo in 'MF':
        pergunta = str(input('Deseja continuar? [Sim/Não]: ')).strip().upper()[0]
        print(f'=-='*20)
        if pergunta in 'S':
            ...
        if pergunta in 'N':
            print('O PROGRAMA SERÁ ENCERRADO!!!')
            break
        if pergunta not in 'SN':
            print('O PROGRAMA SERÁ ENCERRADO!!!')
            break
    if sexo not in 'M' and sexo not in 'F':
        print('Sexo INESISTENTE!!!')
        break
print(f'Foi cadastrado {contador} pessoas com mais de 18 anos.')
print(f'Foi cadastrado {homens} pessoas do sexo Masculino.')
print(f'Foi cadastrado {mulher} mulheres com menos de 20 anos.')
