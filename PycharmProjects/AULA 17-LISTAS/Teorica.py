lanche = ['laranja', 'abacaxi', 'uva']
#             0           1        2
lanche = ['laranja', 'abacaxi', 'uva'
lanche[2] = 'melancia'
lanche = ['laranja', 'abacaxi', 'melância'] # a atribuição melancia vai entrar no lugar do indíce 2(eliminando a uva e tornando a melância o novo objeto no lugar
#             0          1           2

lanche.append('banana') # append() usa-se para adicionar um novo elemento na variavel
lanche = ['laranja', 'abacaxi', 'melância', 'banana']

lanche.insert(0,'pêra') # insert() Usa-se para adicionar um elemento em qual quer posição
lanche = ['pêra', 'laranja', 'abacaxi', 'melância', 'banana']

#del lanche[2] #pode eliminar qual quer índice(elemento)

lanche.pop() # pop() sem nada entre os parenteses, eliminará o ultimo índice
lanche.pop(2) # pode eliminar qual quer índice

lanche.remove('pêra')
# remove() irá eliminar pelo conteúdo
if 'laranja' in lanche:          # Se 'laranja' estiver em lanche
    lanche.remove('laranja')     # 'laranja' será removida da variavel lanche

valores1 = list(range(4, 11))
# vai criar uma lista e começar do número 4 até o 10, pq o ultimo elemento é eliminado!
# ex: valores = [4, 5, 6, 7, 8, 9, 10]
#                0  1  2  3  4  5  6   >>>>>     indices

valores = [8, 2, 5, 4, 9, 3, 0]
#          0  1  2  3  4  5  6
print(valores)
valores.sort()  # vai ordem todos os valroes
valores.sort(reverse=True)  # os valores vão ficar na ordem reversa
print(len(valores))  # quantos elementos tem na variaveel de valores (começa a contagem com 1)
