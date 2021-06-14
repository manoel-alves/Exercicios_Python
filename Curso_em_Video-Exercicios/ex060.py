x = int(input('''Digite um número para
calcular seu fatorial: '''))
dim = x
fat = 1
print(f'Calculando {x}! =', end='')
while dim > 0:
    print(f' {dim} ', end='')
    if dim != 1:
        print('x', end='')
    else:
        print('= ', end='')
    fat *= dim
    dim -= 1
print(f'{fat}')
