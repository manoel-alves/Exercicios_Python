print('-' * 30, '\nSequência de Fibonacci')
print('-' * 30)
quant = int(input('Quantos termos você quer ver? '))
t1 = 0
t2 = 1
print('~' * (quant * 5))
print(f'{t1} -> {t2} -> ', end='')
cont = 2
while cont < quant:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('~' * (quant * 5))