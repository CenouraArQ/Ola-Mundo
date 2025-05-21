primeiro = int(input('Primeiro termo: '))
razão = int(input('Digite a razão: '))
termos = int(input('Quantos termos deseja mostrar?: '))
contagem = 1
total = 0
mais_termos = termos
while mais_termos != 0:
    total += mais_termos
    while contagem <= total: #enquanto contagem for menor ou igual a número ele executa.
        print(f'{primeiro} > ',end='')
        primeiro += razão
        contagem += 1
    print('FIM.')
    mais_termos = int(input('Quantos termos você quer mostrar a mais? '))
print('O programa será encerrado.')

