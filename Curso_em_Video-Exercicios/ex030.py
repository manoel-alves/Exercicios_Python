x = int(input('Me diga um número qualquer: '))

if x % 2 == 0:
    check = 'PAR'
else:
    check = 'ÍMPAR'

print('O número {} é {}'.format(x, check))