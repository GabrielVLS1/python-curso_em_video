casa = int(input("Digite o valor da casa: R$"))
salario = float(input("Digite o valor do seu salário: R$"))
anos = int(input("Quantos anos de finaciamento? "))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f"Para pagar uma casa de R${casa} em {anos} anos ", end='')
print(f"a prestação será de {prestacao :.2f}")

if prestacao <= minimo:
    print("Empréstimo CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")