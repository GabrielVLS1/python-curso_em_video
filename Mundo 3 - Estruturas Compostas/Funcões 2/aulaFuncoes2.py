help(print)
print(input.__doc__)

########################################################################
print('\n')


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)


########################################################################
print('\n')


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}', end='')


somar(3, 5)


########################################################################
print('\n')


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 5)
r2 = somar(8, 7, 1)
r3 = somar(2)
print(f'Os resultados foram {r1}, {r2} e {r3}')


########################################################################
print('\n')
''' ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Fatorial ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ '''


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

''' OU ↓
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
'''


########################################################################
print('\n')
''' ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Par ou Ímpar ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ '''


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
#print(par(num))
if par(num):
    print('É par!')
else:
    print('Não é par!')

