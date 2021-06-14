lista = []
for i in range(0, 5):
    x = int(input('Digite um valor: '))
    if i == 0 or x > lista[-1]:
        lista.append(x)
        print('Adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if x <= lista[pos]:
                lista.insert(pos, x)
                break
            pos += 1
        print(f'Adicionando na posição {pos} da lista...')
print('=-' * 30)
print(f'Valores adicionados na lista: {lista}')