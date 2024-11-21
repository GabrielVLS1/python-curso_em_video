print(f'''{"="*34}
       BANCO PRO TURBO PLUS
{"="*34}''')

valor = int(input('Qual valor você quer sacar? R$'))
total = valor
ced = 200
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0 and ced != 1:
            print(f'Total de {totced} cédula(s) de R${ced}')
        elif ced == 1:
            print(f'Total de {totced} moeda(s) de R${ced}')

        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1

        totced = 0
        if total == 0:
            break

print(f'''{"="*34}
Volte sempre ao BANCO PRO TURBO PLUS!🔥''')
