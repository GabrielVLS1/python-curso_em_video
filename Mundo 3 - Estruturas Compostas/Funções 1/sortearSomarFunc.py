from random import randint
from time import sleep


def sorteio(nums):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        nums.append(randint(1, 10))
        print(f'{nums[c]} ', end='')
        sleep(0.3)
    print('PRONTO!')


def soma_pares(nums):
    pares = 0
    for n in nums:
        if n % 2 == 0:
            pares += n
    print(f'Somando os valores pares de {nums}, temos {pares}')


numeros = []
sorteio(numeros)
soma_pares(numeros)



'''
while len(nums) < 5:
    valor = randint(0, 9)
    if valor not in nums:
        nums.append(valor)
print(nums)
'''

