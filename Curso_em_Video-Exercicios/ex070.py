print('-' * 35)
print('{:' '^35}'.format('LOJA SEI LA O QUE'))
print('-' * 35)

total = mil = cont = 0

while True:
    check = ' '
    num = False

    produto = str(input('Nome do produto: ')).strip().capitalize()

    while num != True:
        preco = input('Preço: R$')
        num = preco.isnumeric()
        preco = int(preco)

    total += preco

    if preco > 1000:
        mil += 1

    if cont == 0:
        nbarato = produto
        menor = preco
    elif preco < menor:
        nbarato = produto
        menor = preco

    cont += 1

    while check not in 'SN':
        check = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if check == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nbarato} que custa R${menor:.2f}')