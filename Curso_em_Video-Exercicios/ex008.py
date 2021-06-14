medida = float(input('Uma distância em metros: '))

print('A medida de {:.1f}m corresponde a'.format(medida))
print('{}km'.format((medida / 1000)))
print('{}hm'.format((medida / 100)))
print('{}dam'.format((medida / 10)))
print('{:.0f}dm'.format((medida * 10)))
print('{:.0f}cm'.format((medida * 100)))
print('{:.0f}mm'.format(medida * 1000))