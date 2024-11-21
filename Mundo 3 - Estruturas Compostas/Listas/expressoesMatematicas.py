expr = str(input('Digite a expressão: '))
lista = []
for simb in expr:
    if simb == '(':
        lista.append(')')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')

if len(lista) == 0:
    print('A expressão é válida')
else:
    print('A expressão é inválida')

print(lista)