num = int(input("Digite um número: "))
print(''' 
Escolha uma das bases numéricas para conversão
[1] para Binário 
[2] para Octal
[3] para Hexadecimal
''')
opcao = int(input("Digite a opção: "))
if opcao == 1:
    print(f"A conversão de {num} para binário é {bin(num)[2:]}")
elif opcao == 2:
    print(f"A conversão de {num} para binário é {oct(num)[2:]}")
elif opcao == 3:
    print(f"A conversão de {num} para binário é {hex(num)[2:]}")
else:
    print("Digita um número certo ai")