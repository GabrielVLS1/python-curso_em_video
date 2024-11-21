print(f'''{'='*38}
10 termos de uma Progressão Aritmética
{'='*38}''')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f"{c}", end='→ ')

print("Fim")




