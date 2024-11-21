n = int(input('Digite um número: '))
print(f'Calculando {n}! = ', end='')

#c = n
f = 1
while n > 1:
    print(f'{n} x ', end='')
    f *= n
    n -= 1

print(f'{n} = {f}')

#print('x' if c > 1 else '=', end='')