jogador = {}
partidas = []
jogador['nome'] = str(input('Nome: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, total):
    partidas.append(int(input(f'Quantos gols na {i+1} partida? ')))
jogador['gols'] = partidas[:]
print(jogador)
print(partidas)