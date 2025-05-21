#Dicionario tem os Indices literais
dados = dict()
dados = {'nome':'Pedro','idade':25}
print(dados['nome']) #Pedro
print(dados['idade']) # 25
dados['sexo'] = 'M'
dados.del['idade']
filme = {
    'Titulo':'Star Wars',
    'ano':1977,
    'diretor':'GerogeLucas'
}
print(filme.valoues()) # para selecionar os textos
print(filme.keys()) #para selecionar a parte dos indices
print(filme.items()) #para selecionar os dois
for k, v in filme.items():
    print(f'O {k} é {v}')
    O titulo é star wars
    O ano é 1977
    O diretor é GerogeLucas