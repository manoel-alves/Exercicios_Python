lista = []
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]

        if lista[i] < menor:
            menor = lista[i]

print('=-' * 20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, j in enumerate(lista):
    if j == maior:
        print(f'{i:.<4} ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, j in enumerate(lista):
    if j == menor:
        print(f'{i:.<4} ', end='')