tot18 = totH = totM20 = 0

while True:
    print(f'''{"-"*27}
    CADASTRE UMA PESSOA   
{"-"*27}''')

    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

print(f'''\nTotal de pessoas com mais de 18 anos: {tot18}
Ao todo temos {totH} homens cadastrados
E temos {totM20} mulheres com menos de 20 anos''')
