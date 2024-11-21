altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / altura**2

print(f"Seu IMC é de {imc :.2f} e você está: ", end='')
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("com Peso normal")
elif imc < 30:
    print("Acima do peso")
elif imc < 40:
    print("com Obesidade")
else:
    print("com Obesidade mórbida")