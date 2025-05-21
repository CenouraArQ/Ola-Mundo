jogador = {}
partidas = []
jogador['nome'] = str(input('Nome: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for i in range(0, total):
    partidas.append(int(input(f'  Quantos gols na partida {i+1}?: ')))
jogador['gols'] = partidas[:]
jogador['somatotal'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v, in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Foi um totael de {jogador["somatotal"]} gols.')