teste = list()
teste.append('Antenor')
teste.append(876)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)


##########################################################
print()
##########################################################


galera = [['João', 19], ['Ana', 33], ['Joaquim', 14], ['Maria', 45]]
print(galera[2][1])
for p in galera:
    print(p)

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

##########################################################
print()
##########################################################



galera = list()
dados = list()
totmai = totmen = 0

for c in range(0, 3):
    dados.append(str(input('\nDigite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galera.append(dados[:])
    dados.clear()

print(f'\n{galera}')

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maires e {totmen} menores de idade')