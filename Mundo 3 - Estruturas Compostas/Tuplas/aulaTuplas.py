lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutáveis
print(lanche)
print(lanche[2])
print(lanche[-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])

##########################################################
print()
##########################################################



lanche = ('Hambúrguer', 'Pizza', 'Pudim', 'Batata Frita')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi bastante!')

##########################################################
print()
##########################################################



lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')                        # lanche na posição cont
print('Comi bastante!')

##########################################################
print()
##########################################################



lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

##########################################################
print()
##########################################################



lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))

##########################################################
print('\n')
##########################################################



a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5)) # Conta quantos cincos tem
print(c.index(8)) # Posição
print(c.index(2, 1)) # Deslocamento

##########################################################
print('\n')
##########################################################

pessoa = ('Antenor', 354, 'M', 210.55)
del(pessoa)
print(pessoa)