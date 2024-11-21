co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é igual a: {:.2f} \n' .format(hi))

#########################################################


import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa é igual a: {}' .format(hi))

#########################################################


import math
co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
hi = math.hypot(co, ca)
print(f"A hipotenusa é igual a {hi :.2f}")

