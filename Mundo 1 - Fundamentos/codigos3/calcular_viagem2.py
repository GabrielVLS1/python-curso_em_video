distancia = float(input('Digite uma distância: '))
print('Você irá realizar uma viagem de {}Km' .format(distancia))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('O preço da sua passagem será: R${:.2f} ' .format(preco))