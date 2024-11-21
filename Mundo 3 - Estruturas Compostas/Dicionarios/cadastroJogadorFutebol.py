jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')



################################################################################################################
print()




'''
jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
totparts = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = gols = []
soma = 0
for c in range(0, totparts):
    gols.append(int(input(f'    Quantos gols na partida {c}? ')))
    soma += gols[c]
jogador['total'] = soma
print('-='*40+'-')
print(jogador)
print('-='*40+'-')
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*40+'-')
jogador['partida'] = totparts
print(f'O jogador {jogador["nome"]} jogou {jogador["partida"]} partidas.')

for c in range(0, jogador['partida']):
    print(f'    => Na partida {c}, fez {gols[c]} gols.')
print(f'Total de {jogador["total"]} gols.')
'''

















