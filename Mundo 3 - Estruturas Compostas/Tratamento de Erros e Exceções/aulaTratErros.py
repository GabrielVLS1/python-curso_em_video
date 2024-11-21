try:
    a = int(input('Numerador: '))
    b = int(input('Denomidador: '))
    r = a / b
except:
    print('Infelizmente tivemos um problema :(')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito Obrigado!')



#######################################################################################
print('\n')



try:
    a = int(input('Numerador: '))
    b = int(input('Denomidador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito Obrigado!')



#######################################################################################
print('\n')



try:
    a = int(input('Numerador: '))
    b = int(input('Denomidador: '))
    r = a / b
except (ValueError, TypeError):   # Se tiver problema com valor E tipo de dado:
    print(f'Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito Obrigado!')


