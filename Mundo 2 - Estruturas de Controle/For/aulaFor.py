for c in range(0, 10):
    print('OI')
print('FIM')

##########################################################
print('\n')
##########################################################


for c in range(1, 11):
    print(c)

##########################################################
print('\n')
##########################################################


for c in range(10, 1, -1):
    print(c)

##########################################################
print()
##########################################################

for c in range(0, 21, 2):
    print(c)

##########################################################
print()
##########################################################

i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')

##########################################################
print()
##########################################################


soma = 0
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    soma += num

print(f"A soma dos valores é {soma}")