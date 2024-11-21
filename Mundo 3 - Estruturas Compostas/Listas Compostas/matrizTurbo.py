matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = tercol = maiseglin = 0
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))
        if matriz[lin][col] % 2 == 0:
            pares += matriz[lin][col]
        if col == 2:
            tercol += matriz[lin][col]
        if lin == 1 and matriz[lin][col] > maiseglin:
            maiseglin = matriz[lin][col]
print()
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()
print(f'\nA soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {tercol}')
print(f'O maior valor da segunda linha é {maiseglin}')



################################################################################################################




'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sPar = sTerCol = mSegLin = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print()
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            sPar += matriz[l][c]
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'\nA soma dos valores pares é {sPar}')

for l in range(0, 3):
    sTerCol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {sTerCol}')

for c in range(0, 3):
    if c == 0 or matriz[1][l] > mSegLin:
        mSegLin = matriz[1][l]
print(f'O maior valor da segunda linha é {mSegLin}')



'''














