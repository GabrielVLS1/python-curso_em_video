aluno = {}
aluno['Nome'] = str(input('Nome: '))

x = aluno['Nome'][0].upper()
y = aluno['Nome'].replace(aluno['Nome'][0], x)
aluno['Nome'] = y

aluno['Média'] = float(input(f'Média de {y}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('=-'*30+'=')

for k, v in aluno.items():
    print(f' - {k} é igual a {v}')


