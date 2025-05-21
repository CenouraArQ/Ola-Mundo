#for c in range (1, 5):
#    n = int(input('Digite um valor: '))
#print('Fim')

#Na estrutura while sempre tem que colocar a variavel e seu valor antes de começar o projeto
#n = 1 #GAMBIARRA PARA FAZER O CODIGO FUNCIONAR
#while n != 0: # != "diferente" isso significa, condição de parada.
#    n = int(input('Digite um valor: '))
#print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [s/n]: ')).upper()[0]
print('Fim')

#Com a estrutura while, podemos criar situações onde façamos laços indeterminadamente.