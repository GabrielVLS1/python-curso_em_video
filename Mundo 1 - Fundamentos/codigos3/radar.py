velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Multado! Você excedeu o limite de 80km!')
    multa = (velocidade-80)*7
    print('Sua multa é de R${:.2f}' .format(multa))
print('Tenha um bom dia e dirija com segurança!')
