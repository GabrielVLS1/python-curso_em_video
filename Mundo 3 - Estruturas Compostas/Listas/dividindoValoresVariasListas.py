valores = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    valores.append(num)

    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('=-'*30+'=')
print(f'A lista completa é: {valores}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')


##################################################################################################






num = []
pares = []
impares = []

while True:
    num.append(int(input('Digite um número: ')))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Digite um valor: ')).strip().upper()[0]
    if resp == 'N':
        break

for pos, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('=-'*30+'=')
print(f'A lista completa é: {num}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')