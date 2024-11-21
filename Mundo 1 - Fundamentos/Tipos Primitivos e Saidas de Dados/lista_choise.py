import random
nome1 = str(input('Digite um nome: '))
nome2 = str(input('Digite um nome: '))
nome3 = str(input('Digite um nome: '))
nome4 = str(input('Digite um nome: '))

lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O nome escolhido é {}' .format(escolhido))

print('\n')

###########################################################



from random import choice

sla1 = str(input("Elemento 1: "))
sla2 = str(input("Elemento 2: "))
sla3 = str(input("Elemento 3: "))
sla4 = str(input("Elemento 4: "))

lista = [sla1, sla2, sla3, sla4]
escolha = choice(lista)

print(escolha)

###########################################################



import random
var1 = random.choice([1, 2, 3, 4])
print(var1)