matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):
    for col in range(0, 3):
        matrix[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))
print()
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matrix[lin][col]:^5}]', end='')
    print()
