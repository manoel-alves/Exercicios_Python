dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

valor = (60 * dias) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(valor))