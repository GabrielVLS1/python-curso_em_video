sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Informe seu sexo: [M/F] ')).strip().upper()[0]

if sexo == 'M':
    sexo = 'masculino'
else:
    sexo = 'feminino'

print(f'Sexo {sexo} cadastrado com sucesso')
