lista = ['a','a','b','a','b','a','b','b']

print('\nLista original:',lista)

pos = 0
for i in range(0, len(lista)):
    if lista[i] == lista[pos]:
        lista[i], lista[pos + 1] = lista[pos + 1], lista[i]
        pos += 1
        
print('-' * (16 + len(lista) * 5))
print('Lista ordenada:', lista, '\n')