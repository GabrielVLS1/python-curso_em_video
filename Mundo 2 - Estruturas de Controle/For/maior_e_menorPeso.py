maior = menor = 0

for c in range(1, 6):
    peso = float(input(f'Peso da {c}º pessoa: '))
    if c == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'''
O maior peso foi {maior}Kg
O menor peso foi {menor}Kg
''')

