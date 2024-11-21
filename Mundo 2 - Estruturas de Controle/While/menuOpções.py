opcao = 0
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))

while opcao != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos valores
    [5] Sair do programa
    ''')
    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = v1 + v2
        print(f'A soma entre {v1} + {v2} é {soma}')

    elif opcao == 2:
        produto = v1 * v2
        print(f'O resultado entre {v1} x {v2} é {produto}')

    elif opcao == 3:
        if v1 > v2:
            print(f'{v1} é o maior valor')
        elif v1 < v2:
            print(f'{v2} é o maior valor')
        else:
            print('Os valores são iguais')

    elif opcao == 4:
        v1 = float(input('Primeiro valor: '))
        v2 = float(input('Segundo valor: '))

    elif opcao == 5:
        print('Volte sempre!')

    else:
        print('Opção inválida, tente novamente.')
print('Fim do programa')
