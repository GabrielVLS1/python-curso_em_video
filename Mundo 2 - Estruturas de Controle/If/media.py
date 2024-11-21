nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
if media < 5:
    print(f"A casa caiu. Sua média foi {media :.1f}")
elif media >= 5 and media < 7:
    print(f"Ta de recuperação. Sua média foi {media :.1f}")
else:
    print(f"Passou. Sua média foi {media :.1f}")
