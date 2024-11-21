def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
ngols = str(input('Número de Gols: '))
if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0
if nome.strip() == '':
    ficha(gol=ngols)
else:
    ficha(nome, ngols)