distancia = float(input('Digite uma distância: '))
print('Você irá realizar uma viagem de {}Km' .format(distancia))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('O preço da sua passagem será: R${:.2f} ' .format(preco))