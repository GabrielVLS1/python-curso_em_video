def maiorNum(* num):
    from time import sleep
    print('-='*30)
    maior = cont = 0
    for valor in num:
        print(f'{valor} ', end='')          # ", flush=True" não foi necessário
        sleep(0.4)
        if valor == 0 or valor > maior:
            maior = valor
    cont += 1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')



maiorNum(2, 5, 3, 7)
maiorNum(4, 2, 9, 1, 6)
maiorNum(1, 2)
maiorNum()