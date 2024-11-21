media = 0
maiorIdade = 0
nomeVelho = ''
mulher20 = 0

for c in range(1, 5):
    print(f"----- {c}ª PESSOA -----")
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    media += idade / 4
    if sexo in 'Mm' and c == 1:
        maiorIdade = idade
        nomeVelho = nome

    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome

    if sexo in 'Ff' and idade < 20:
        mulher20 += 1


print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maiorIdade} anos e se chama {nomeVelho}.')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos.')