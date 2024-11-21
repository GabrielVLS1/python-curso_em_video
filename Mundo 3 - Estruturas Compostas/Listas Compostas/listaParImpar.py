listona = [[], []]

for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        listona[0].append(num)
    else:
        listona[1].append(num)

listona[0].sort()
listona[1].sort()
print()
print(f'Pares: {listona[0]}')
print(f'Ímpares: {listona[1]}')



