from datetime import date
atual = date.today().year

nasc = int(input("Digite sua data de nascimento: "))
idade = atual - nasc

if idade < 18:
    print(f"Você ainda vai se alistar, daqui {18 - idade} ano(s)")
elif idade == 18:
    print(f"Tá na hora de se alistar!")
else:
    print("Já passou o prazo, ta lascadokk")

###################################################################################


from datetime import date
atual = date.today().year

nasc = int(input("Digite sua data de nascimento: "))
idade = atual - nasc

if idade < 18:
    saldo = 18 - idade
    print(f"Você ainda vai se alistar, daqui {saldo} ano(s)")
    ano = atual + saldo
    print(f"O ano vai ser {ano}")
elif idade == 18:
    print(f"Tá na hora de se alistar!")
else:
    saldo = idade - 18
    print(f"Já passou o prazo, que foi há {saldo} ano(s), ta lascadokk")
    ano = atual - saldo
    print(f"O ano foi {ano}")