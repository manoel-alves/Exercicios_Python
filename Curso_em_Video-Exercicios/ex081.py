lista = []
while True:
    x = int(input('Digite um valor: '))
    if cont == 0 or x < lista[-1]:
        lista.append(x)
    else:
        pos = 0
        while pos < len(lista):
            if x > lista[pos]:
                lista.insert(pos, x)
                break
            pos += 1

    check = str(input('Quer continuar? [S/N] ')).strip().upper()
    if check == 'N':
        break

print('=-' * 30)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')