total = totmil = precoBarato = cont = 0
prodBarato = ''

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

    total += preco

    if preco >= 1000:
        totmil += 1

    if cont == 1 or preco < precoBarato:
        prodBarato = produto
        precoBarato = preco

print(f'O total da compra foi: R${total:.2f}')
print(f'Temos {totmil} produto(s) custando mais de R$1000')
print(f'O produto mais barato foi "{prodBarato}" que custa R${precoBarato} ')