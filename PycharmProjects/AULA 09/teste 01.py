#fatiamento
frase = 'Curso em Video Python' #21 caracteres contando com os espaços
print(frase[3]) #mostrar o 3º caractere
print(frase[3:13]) #do 3º caractere até o 12º caractere
print(frase[:13]) #do inicio até o 12º caractere
print(frase[13:]) #do 13º caractere ate o final
print(frase[1:15])
print(frase[1:15:2]) #do 1º até o 14º caractere de 2 em 2
print(frase[::2]) #não sei o inicio nem o final mas ira contar de 2 em 2 caractere
print('=-=' * 20)
print('''Texto é uma forma de nos expressarmos, 
ou seja, de transmitir uma mensagem a alguém. 
Os textos podem ser verbais, quando utilizam palavras, 
e podem ser não-verbais, quando utilizam cores, texturas, 
gestos e sons em vez de palavras.''') # ''' três aspas
print('=-=' * 20)
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print(frase[0]) # ira mostrar a 1º letra que é C
#frase = frase.replace('Python', 'Android')
#print(frase)
print('Curso' in frase)
print(frase.find('Curso')) # find = irá mostrar a posição da palavra referente a 1º caractere
print(frase.find('em'))
print(frase.find('Video'))
print(frase.find('Python'))
print(frase.split())
dividido = frase.split()
print(dividido[0]) # [0] primeira casa de numero irá mostrar a a palavra referente dentro da frase
print(dividido[2][3]) # [2][3] irá mostrar a palavra referente dentro da frase e irá mostrar o caractere dentro da palavra