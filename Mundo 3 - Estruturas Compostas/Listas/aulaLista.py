num = [2, 5, 9, 1, 4, 1]
num[2] = 3
num.append(7)
num.insert(0, 8)
num.sort()
num.sort(reverse=True)
num.pop(4)
del num[2]
num.remove(1)
if 5 in num:
    num.remove(5)
else:
    print('Não encontrei 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')

##########################################################
print()
##########################################################



valores = list()    # OU '[]', mas aí o python reclama
valores.append(5)
valores.append(9)
valores.append(6)

for n in valores:
    print(f'{n}... ', end='')

print('\n')

for i, n in enumerate(valores):
    print(f'O número {n} se encontra na posição {i}')


##########################################################
print()
##########################################################



valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um número bem bonitinho: ')))
print(valores)

for i in range(0, len(valores)):
    print(f'O número {valores[i]} se encontra na posição {i}')

##########################################################
print()
##########################################################



a = [2, 3, 4, 7]
#b = a
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')