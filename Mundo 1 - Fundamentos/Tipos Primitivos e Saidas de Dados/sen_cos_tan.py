import math
ângulo = float(input('Digite o ângulo: '))

seno = math.sin(math.radians(ângulo))
print('O ângulo {} tem o seno {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo {} tem o cosseno {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo {} tem a tangente {:.2f}'.format(ângulo, tangente))

print('\n\n')
########################################################################



from math import sin, cos, tan, radians
ângulo = float(input('Digite o ângulo: '))

seno = sin(radians(ângulo))
print('O ângulo {} tem o seno {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo {} tem o cosseno {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo {} tem a tangente {:.2f}'.format(ângulo, tangente))