from random import randint
computador = randint(0, 10)

print('''
Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Consegue adivinhar qual foi?
''')

acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    elif computador > jogador:
        print('Mais... tente novamente')
    else:
        print('Menos... tente novamente')

if tentativas == 1:
    print('Acertou de primeira, parabéns! 🎉')
else:
    print(f'Acertou com {tentativas} tentativas.')
