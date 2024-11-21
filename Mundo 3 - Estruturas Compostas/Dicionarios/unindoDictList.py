galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres castradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end=' | ')
print(f'\nD) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

##########################################################################################
print()


'''
pessoa = {}
listona = []
muie = []
cont = media = soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))

    soma += pessoa['idade']
    cont += 1
    media = soma / cont

    if pessoa['sexo'] == 'F':
        muie.append(pessoa['nome'])

    listona.append(pessoa.copy())
    pessoa.clear()

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {cont} pessoas cadastradas.')

print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres castradas foram: ', end='')
for c in range(0, len(muie)):
    print(f'{muie[c]}', end=' | ')
print(f'\nD) Lista das pessoas que estão acima da média: ')
for c in listona:
    if c['idade'] > media:
        print('    ', end='')
        for k, v in c.items():
            print(f'{k} = {v};', end=' ')
        print()
'''


