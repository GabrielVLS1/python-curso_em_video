from utilidades import moeda, dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)


'''
valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentando 10% temos {moeda.aumentar(valor, 10, True)}')
print(f'Reduzindo 15% temos {moeda.diminuir(valor, 15, True)}')
'''