print("{:=^40}".format(" Lojas Nengue "))
preco = float(input("Preço das compras: R$"))

print('''
Formas de pagamento 
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')

opcao = int(input("Qual é a opção? "))
if opcao == 1:
    novoPreco = preco - preco * 10 / 100
    print("Valor com desconto de 10% - ", end='')
elif opcao == 2:
    novoPreco = preco - preco * 5 / 100
    print("Valor com desconto de 5% - ", end='')
elif opcao == 3:
    novoPreco = preco
    totalParc = preco / 2
    print(f"Valor parcelado em 2x de \033[7mR${totalParc :.2f}\033[m - ", end='')
elif opcao == 4:
    novoPreco = preco + preco * 20 / 100
    parcelas = int(input("Quantidade de parcelas: "))
    if parcelas > 36 < 3:
        print("Valor inválido de parcelas")
    else:
        totalParc = novoPreco / parcelas
        print(f"Valor parcelado em {parcelas}x de \033[7mR${totalParc :.2f}\033[m - ", end='')
else:
    print("Opção inválida, tente novamente.")

print(f"Compra de R${preco} vai sair por um total de \033[7mR${novoPreco :.2f}\033[m")