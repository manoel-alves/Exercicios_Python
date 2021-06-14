b = float(input('Base do retângulo: '))
h = float(input('Altura do Retângulo: '))

print(f'AREA = {b * h:.4f}')
print(f'PERIMETRO = {(b * 2) + (h * 2):.4f}')
print(f'DIAGONAL = {((b ** 2) + (h ** 2))**(1/2):.4f}')