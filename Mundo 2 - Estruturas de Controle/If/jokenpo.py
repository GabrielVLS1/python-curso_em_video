from random import randint
from time import sleep

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('''
[0] = PEDRA
[1] = PAPEL
[2] = TESOURA
''')

jogador = int(input("Digite uma opção: "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print(f"O computador jogou {opcoes[computador]}")
print(f"O jogador jogou {opcoes[jogador]}")


if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('VOCÊ GANHOU')
    elif jogador == 2:
        print('VOCÊ PERDEU')
    else:
        print('Digite uma opção válida')

elif computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    else:
        print('Digite uma opção válida')

elif computador == 2:
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATOU')
    else:
        print('Digite uma opção válida')

