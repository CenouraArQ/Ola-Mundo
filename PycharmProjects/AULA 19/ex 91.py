from random import randint
from operator import itemgetter
dicionario = {'jogador': randint(0,6),
              'jogador2': randint(0,6),
              'jogador3': randint(0, 6),
              'jogador4': randint(0, 6)}
#print(dicionario)
for k, v in dicionario.items():
    print(f'{k} tirou {v} no dado.')
print('-='*20)
print('   == RANKING DOS JOGADORES =='  )
ranking = []
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1}° lugar: {v[0]} com {v[1]}.')


