valores = []

while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        valores.sort()
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não pode 😠😤🤚')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('=-'*30+'=')
print(f'Você digitou os valores {valores}')

