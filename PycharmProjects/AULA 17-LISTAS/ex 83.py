expre = str(input('Digite uma expressão: '))
pilha = list()
for simbolo in expre: #para cada simbolo que estiver em expressão
    if simbolo == '(': #se simbolo for igual a (
        pilha.append('(') #adicionar ( na lista pilha
    elif simbolo == ')': #se não se simbolo for igual a )
        if len(pilha) > 0: #se a quantidade de indice for maior que 0
            pilha.pop() #eliminar o ultimo indice
        else: #se não
            pilha.append(')')  #adicionar ) na listapilha
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')