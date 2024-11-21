maior = menor = 0
valores = []

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    #num = valores[cont]
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print('=-'*30 + '=')
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, n in enumerate(valores):
    if n == maior:
        print(f'{i}... ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, n in enumerate(valores):
    if n == menor:
        print(f'{i}... ', end='')


'''    
O mesmo que:

for i in range(0, len(valores)):
    if valores[i] == maior:
        print(f'{i}... ', end='')
'''