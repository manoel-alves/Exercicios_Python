n = int(input('Qual a ordem da matriz? '))

mat = [[0 for i in range(n)] for j in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))

print('DIAGONAL PRINCIPAL:')
neg = 0
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            print(f'{mat[i][j]}', end=' ')
        if mat[i][j] < 0:
            neg += 1

print(f'\nQUANTIDADE DE NEGATIVOS = {neg}')
