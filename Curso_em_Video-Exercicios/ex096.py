def area(a, b):
    print(f'A área de um Terreno {a} x {b} é de {a * b}m².')

    
def linha(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


# main
linha('Área de Terreno')
x = float(input('Comprimento (m): '))
y = float(input('Largura (m): '))
area(x, y)
