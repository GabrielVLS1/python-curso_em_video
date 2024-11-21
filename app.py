n = float(input('Digite um valor em metros: '))

km = n/1000
cm = n*100
mm = n*1000

print('O valor em km é {}, em cm é {} e em mm é {}' .format(km, cm, mm))



#########################################################

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