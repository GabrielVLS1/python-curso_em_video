n = soma = cont = 0
n = int(input('Digite um número (999 para parar): '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número (999 para parar): '))
print(f'A soma dos {cont} valores é de {soma}')
