import random
n1 = str(input('Primeira pessoa: '))
n2 = str(input('Segunda pessoa: '))
n3 = str(input('Terceira pessoa: '))
n4 = str(input('Quarta pessoa: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem escolhida é {}' .format(lista))

print('\n')
##############################################################


from random import shuffle
n1 = str(input('Primeira pessoa: '))
n2 = str(input('Segunda pessoa: '))
n3 = str(input('Terceira pessoa: '))
n4 = str(input('Quarta pessoa: '))

lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem escolhida é: ')
print(lista)
##############################################################









