from datetime import date
atual = date.today().year

maiores = 0
menores = 0
for pessoas in range(0, 7):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = atual - nasc
    maiores += idade >= 21
    menores += idade < 21

print(f'Temos {maiores} pessoas de maioridade civil e {menores} de menoridade')


    # OU
    #if idade >= 21:
    #    maiores += 1
    #else:
    #    menores += 1








