from random import randint
from time import sleep

listaTemporaria = []
jogos = []
quant = int(input('Quantos jogos? '))

tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in listaTemporaria:
            listaTemporaria.append(num)
            cont += 1
            if cont >= 6:
                break
    listaTemporaria.sort()
    jogos.append(listaTemporaria[:])
    listaTemporaria.clear()
    tot += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('BOA SORTE')


