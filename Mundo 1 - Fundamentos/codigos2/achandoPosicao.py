frase = str(input("Digite uma frase: "))
achar = str(input("Digite o que você quer achar na frase: "))

achou = frase.find(achar)

if achou != -1:
    print(f"\n=> '{achar}' começa na posiçao {achou}, pelo índice.")

else:
    print(f"\nNão foi possível encontar '{achar}' na frase digitada.")
    print(f"Frase: {frase}")
