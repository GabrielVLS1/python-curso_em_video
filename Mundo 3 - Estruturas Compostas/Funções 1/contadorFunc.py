from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passor: '))
contador(inicio, fim, passo)

######################################################################################
print()

'''

def contador(i, f, p):
    from time import sleep
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    sleep(1)
    for c in range(i, f, p):
        print(f'{c} ', end='')
        sleep(0.5)
    #print(f'{f} ', end='')
    print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, -2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

'''