pessoas = {'nome': 'Antenor', 'sexo': 'M', 'idade': '176'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')



##########################################################
print()
##########################################################

del pessoas['sexo']
pessoas['nome'] = 'Petunia'
pessoas['peso'] = 56.5
print(pessoas)


##########################################################
print()
##########################################################

brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[1]['uf'])


##########################################################
print()
##########################################################



estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

'''
    for v in e.values():
        print(v, end=' ')
    print()
'''