temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    print()

print(f'Os dados foram: {princ}')
print(f'Ao todo foram cadastrados: {len(princ)} pessoas')
print(f'O maior peso cadastrado foi de: {maior}. Peso de: ', end='')
for p in princ:
    if p[1] == maior:
        print(f'| {p[0]} ', end='')


print(f'\nO menor peso cadastrado foi de: {menor}. Peso de: ', end='')
for p in princ:
    if p[1] == menor:
        print(f'| {p[0]} ', end='')