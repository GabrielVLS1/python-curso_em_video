from random import randint
c = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(1, 10)
    total = jogador + computador

    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU')
            c += 1
        else:
            print('VOCÊ PERDEU')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU')
            c += 1
        else:
            print('VOCÊ PERDEU')
            break

print(f'''{"=-"*16}=
FIM DE JOGO. Você ganhou {c} vezes''')

################################################################################################################

