from random import randint
from time import sleep
from operator import itemgetter

jogo = {}
for c in range(1, 5):
    jogo[f'Jogador({c})'] = randint(1, 6)

'''Mesmo que:
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
'''

print('Valores sorteados:')
for k, v in jogo.items():
    sleep(1)
    print(f'{k} tirou {v} no dado', end='')
    sleep(0.7)
    print('.', end='')
    sleep(0.7)
    print('.', end='')
    sleep(0.7)
    print('.')

ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(1.5)
print('-='*15+'-')
print('  == RANKING DOS JOGADORES ==')
sleep(1)
for i, v in enumerate(ranking):
    print(f' - {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.4)