lPrinc = []
temp = []
cont = n1 = n2 = media = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    lPrinc.append(temp[:])
    cont += 1
    temp.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print()
    if resp == 'N':
        break

print('=-'*14+'=')
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA"}')
print('-'*29)
for pos in range(0, len(lPrinc)):
    media = (lPrinc[pos][1] + lPrinc[pos][2]) / 2
    print(f'{pos:<3} {lPrinc[pos][0]:<15} {media}')

while True:
    print('-'*50)
    notas = int(input('Mostrar aluno de qual aluno? (999 interrompe): '))
    if notas == 999:
        break
    if notas <= len(lPrinc) - 1:
        print(f'Notas de "{lPrinc[notas][0]}" são: [{lPrinc[notas][1]}, {lPrinc[notas][2]}]')
print('FINALIZANDO...')


##########################################################################################################


'''
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print()
    if resp == 'N':
        break

print('=-'*14+'=')
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>9}')
print('-'*29)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 50)
    opcao = int(input('Mostrar aluno de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    if opcao <= (len(ficha)) -1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('FINALIZANDO...')

'''