from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' *22)
print(' Vou escolher um número entre 0 e 5. Tente adivinhar qual ele é!')
print('-=-' *22)
jogador = int(input('Digite um número: '))
print('E o número escolhido é...')
sleep(3)

if jogador == computador:
    print('Você acertou!!!')
else: 
    print('Você errou!!! Era o número {}' .format(computador))