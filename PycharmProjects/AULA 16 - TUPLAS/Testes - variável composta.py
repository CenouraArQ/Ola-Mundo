lanche = 'hamburguer', 'suco', 'pizza', 'pudim', 'Batata frita'
#              0          1       2        3            4
print('FATIAMENTO')
print('Durante o fatiamento, o último elemento vai ser ignorado, eliminando-o')
print(lanche) #vai mostar todos os elementos
print(lanche[2]) #[2] vai mostrar a pizza, porque está no índice 2
print(lanche[0:2]) #[0:2] vai mostrar do hamburguer até o suco, porque o programa exclui o ultimo elemento, no caso o 2, por causa da estrutura de fatiamento que exclui o ultimo elemento
print(lanche[1:]) #[1:] vai mostrar apartir do suco, ate o final que é a Batata frita
print(lanche[-1]) # vaimostrar a Batata frita
print(len(lanche)) #len() Irá mostrar o total de elementos ná variável
print(sorted(lanche)) # sorted() vai deixar a string(atribuição) em ordem. seja alfabética para texto e númerica para valores

for comida in lanche: #para cada comida in(em) lanche:
    print(comida)

#CONCEITO IMPORTANTE
#"As Tuplas são imutáveis!!!"
a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)
c = a + b
print(c)
print(c.count(5)) # count() quantas vezes está aparecendo o número 5
print(lanche.index('suco')) # index() para mostar a posição da variavel
del(lanche) #del() em tupla só funciona para apagar a tupla inteira
#Tuplas pode receber texto e números, tudo junto se quiser

