frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase' .format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}' .format(frase.find('A')+1))
print('A última letra "A" apareceu na posição {}' .format(frase.rfind('A')+1))

################################################################################


frase = str(input('Digite uma frase: ')).upper().strip()
print(f"A letra 'A' aparece {frase.count('A')} vezes na frase")
print(f"A primeira letra 'A' apareceu na posição {frase.find('A')+1}")
print(f"A última letra 'A' apareceu na posição {frase.rfind('A')+1}")