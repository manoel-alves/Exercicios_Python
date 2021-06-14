from random import choice

lista = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
esc = ''
cont = 0
x = ''

print(f'Os valores escolhidos foram: ', end='')

for i in range(0, 5):

    while True:
        if x in esc:
            x = choice(lista)
        else:
            break

    if cont == 0:
        maior = x
        menor = x
    else:
        if x > maior:
            maior = x
        elif x < menor:
            menor = x

    esc += x + ' '

    cont += 1

print(esc)
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
