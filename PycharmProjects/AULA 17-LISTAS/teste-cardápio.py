print('-'*30)
print(f'{'Cardápio':^30}')
print('-'*30)
cardapio = ['laranja', 'abacaxi', 'uva']
for comida in cardapio:
    print(f'{comida:.<30}')
while True:
    pergunta = str(input('Escolha um item: ')).strip().lower()
    if pergunta in cardapio:
        cardapio.remove(pergunta)
    elif pergunta not in cardapio:
        print('-'*30)
        print('Este item não está no cardapio!'
              '\nEscolha outro item!')
        print('-'*30)
    if len(cardapio) == 0:
        print('A suas escolham acabaram!'
                  '\nVolte sempre!!!')
        break