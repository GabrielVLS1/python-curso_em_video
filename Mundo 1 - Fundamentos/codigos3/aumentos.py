salario = float(input('Digite o seu salário R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
if salario > 1250:
    novo = salario + (salario * 10 / 100)

print('O seu salario com aumento é R${:.2f}' .format(novo))