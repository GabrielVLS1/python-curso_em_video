def mostraLinha():
    print('-' * 30)


# Programa Principal
mostraLinha()
print('Sistema de Aluno')
mostraLinha()
print('Cadastro de Funcionário')
mostraLinha()
print('ERRO! [...]')


###############################################################################
print('\n')


def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


título('SISTEMA CADASTRO')
título('Python é muito bom!')
título('AAAAAAAAAA')


###############################################################################
print('\n')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print()


soma(4, 5)
soma(8, 9)
soma(2, 1)


###############################################################################
print('\n')


def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')
    '''
    for valor in núm:
            print(f'{valor} ', end='')
        print('=> FIM!')
    '''


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


###############################################################################
print('\n')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 8, 4, 11, 42, 0, 2]
dobra(valores)
print(valores)


###############################################################################
print('\n')


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
    tipo = type(valores)
    print(tipo)


soma(5, 2)
soma(2, 9, 4)
