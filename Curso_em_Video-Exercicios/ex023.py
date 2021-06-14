x = int(input('Informe um número: '))
print('Analisando o número {}'.format(x))

#mil = x / 1000
#cent = (x - (mil * 1000)) // 100
#dez = ((x - (mil * 1000)) - (cent * 100)) // 10
#uni = (x - (mil * 1000)) - (cent * 100) - (dez * 10)

mil = x // 1000 % 10
cent = x // 100 % 10
dez = x // 10 % 10
uni = x //1 % 10

print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cent))
print('Milhar: {}'.format(mil))