print('-' * 41)
print('{:^41}'.format('Listagem de Preços'))
print('-' * 41)

lista = ('Lápis', 1.75, 'Borracha', 2.0, 'Caderno', 15.9, 'Estojo', 25.0,
         'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3,
         'Livro', 34.90)

for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<32}', end='')
    elif i % 2 != 0:
        print(f'R${lista[i]:>7.2f}')