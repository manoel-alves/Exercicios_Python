lista = (int(input(f'Digite um número: ')),
         int(input(f'Digite outro número: ')),
         int(input(f'Digite mais um número: ')),
         int(input(f'Digite o último número: ')))

print(f'Você digitou os valores: {lista}')

if 9 in lista:
    print(f'O valor 9 apareceu {lista.count(9)} vezes')
else:
    print('O valor 9 não foi digitado!')

if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3)}a posição')
else:
    print('O valor 3 não foi digitado!')

check = 0
for i in lista:
    if i % 2 == 0:
        check = 1
if check == 1:
    print('Os valores pares digitados foram ', end='')
    for i in lista:
        if i % 2 == 0:
            print(i, end=' ')
else:
    print('Nenhum número par digitado!')
