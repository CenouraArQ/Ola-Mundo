#Dicionario tem os Indices literais
dados = dict()
dados = {'nome':'Pedro','idade':25}
print(dados['nome']) #Pedro
print(dados['idade']) # 25
dados['sexo'] = 'M'
del.dados['idade']
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
filme = {
    'Titulo':'Star Wars',
    'ano':1977,
    'diretor':'GerogeLucas'
}
print(filme.values()) # para selecionar os textos
print(filme.keys()) #para selecionar a parte dos indices
print(filme.items()) #para selecionar os dois
for keys, values in filme.items():
    print(f'O {keys} é {values}')
    O titulo é star wars
    O ano é 1977
    O diretor é GerogeLucas

locadora = list()
locadora.append(filme[:])
print(locadora[0]['ano'])  # 'ano':1977,'
print(locadora[2]['titulo']) #Matrix
