frutas = ('nectarina', 'laranja', 'amora', 'damasco', 'abacaxi', 'pera', 'heisteria', 'tangerina', 'romã',
          'melancia', 'umbu', 'tamarindo', 'tâmara', 'banana', 'veludo', 'nêspera', 'olho-de-boi', 'zimbro',
          'figo', 'uva', 'groselha', 'yamamomo', 'bacuri', 'seriguela', 'embaúba', 'xixá', 'carambola', 'mamão',
          'goiaba', 'lichia', 'durião', 'kiwi', 'framboesa', 'limão', 'wampee', 'jabuticaba', 'caju', 'cacau',
          'sapoti', 'pêssego', 'buriti', 'physalis', 'abacate', 'marmelo', 'graviola', 'quina', 'ingá', 'jambo')


print(f'Lista de frutas: {frutas}')
print(f'As 5 primeiras são: {frutas[:5]}')
print(f'As 4 últimas são: {frutas[-4:]}')
print(f'Frutas em ordem alfabética: {sorted(frutas)}')
print(f'→ {frutas[18]} está na {frutas.index("figo")+1}ª posição')