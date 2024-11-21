from datetime import date
atual = date.today().year

nasc = int(input("Digite o seu ano de nascimento: "))
idade = atual - nasc

print("Você é da categoria ", end='')
if idade < 10:
    print(f"MIRIM")
elif idade < 15:
    print("INFANTIL")
elif idade < 20:
    print("JUNIOR")
elif idade < 26:
    print("SÊNIOR")
else:
    print("MASTER")