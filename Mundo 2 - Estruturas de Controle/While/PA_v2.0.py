print(f'''{'='*43}
10 termos de uma Progressão Aritmética v2.0
{'='*43}''')

primeiro = int(input('1º termo: '))
razao = int(input('Razão: '))

#termo = primeiro
cont = 1
while cont <= 10:
    print(f'{primeiro} →', end=' ')
    primeiro += razao
    cont += 1

print('Fim')
