resp = 's'
n = total = cont = media = maior = menor = 0

while resp in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    total += n
    media = total / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    '''if resp not in 'Ss' and resp not in "Nn":
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    elif resp in 'Nn':
        print('Fim')'''


print(f'Você digitou {cont} números e a média foi {media :.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')