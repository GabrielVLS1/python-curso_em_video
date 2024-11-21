def leiaDinheiro(msg):
    valido = False
    while not valido:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO: "{valor}" é um preço inválido.\033[m')
        else:
            valido = True
            return float(valor)


