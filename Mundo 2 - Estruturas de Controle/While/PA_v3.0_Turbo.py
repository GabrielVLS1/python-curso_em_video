print(f'''{'='*44}
🔥🔥🔥🔥 SUPER P.A. TURBO PLUS V3 🔥🔥🔥🔥
{'='*44}''')

primeiro = int(input('1º termo: '))
razao = int(input('Razão: '))

#termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{primeiro} → ', end='')
        primeiro += razao
        cont += 1
    print('PAUSA')
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))

print(f'Progressão Aritmética finalizada com {cont} termos.')
    
