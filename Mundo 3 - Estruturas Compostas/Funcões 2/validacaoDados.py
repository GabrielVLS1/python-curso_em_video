def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar {n}')



#############################################################################################################
print('\n')


'''

def leiaInt(msg):
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            return valor
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar {n}')




#############################################################################################################
print('\n')



def leiaInt(msg):
    num = str(input(msg))
    while num.isnumeric() == False:
         print('\033[31mERRO! Digite um número inteiro válido.\033[m')
         num = str(input(msg))
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar {n}')

'''