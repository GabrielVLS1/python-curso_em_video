while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)

    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')

    print('-' * 40)
print('PROGRAMA DA TABUADA V3.0 TURBO ENCERRADO!')