print('-='*16 + '-')
print('Analisar triângulo')
print('-='*16 + '-')

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas PODEM FORMAR um triângulo')
else:
    print('Essas retas NÃO PODEM FORMAR um triângulo')
