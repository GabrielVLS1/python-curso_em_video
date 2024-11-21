from random import randint

maior = menor = 0
nums = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: ', end='')
for n in nums:
    print(n, end=' ')

print(f'\nO maior valor sorteado foi: {max(nums)}')
print(f'O menor valor sorteado foi: {min(nums)}')
