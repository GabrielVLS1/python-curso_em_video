from datetime import datetime
# from datetime import date
trabalhador = {}

trabalhador['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
trabalhador['idade'] = datetime.now().year - nasc
# date.today().year
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))

    if trabalhador['idade'] >= 65:
        trabalhador['aposentadoria'] = '"Já deveria estar aposentado então kkk"'
    else:
        trabalhador['aposentadoria'] = 65 - trabalhador['idade']

print('-='*22+'-')

for k, v in trabalhador.items():
    print(f' - {k} tem o valor {v}')

