tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for palavra in tupla:
    print(f'\nNa palavra {palavra} temos as vogais: ', end='')
    for letra in palavra.lower(): #enquanto letra estiver em palavra(minuscula)
        if letra in 'aeiou': #se em letra tiver 'aeiou' ele vai prosseguir
            print(letra, end=' ')