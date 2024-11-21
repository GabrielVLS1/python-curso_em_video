frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)

inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

# inverso = junto[::-1]

print(f'"{frase}"', end=' → ')
if junto == inverso:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')