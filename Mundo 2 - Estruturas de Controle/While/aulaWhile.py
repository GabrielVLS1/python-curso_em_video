c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

##########################################################
print()
##########################################################

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')


##########################################################
print()
##########################################################

resp = 'S'
while resp == 'S':
    n = int(input('Digite um valor: '))
    resp = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')


##########################################################
print()
##########################################################

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} ímpares')

