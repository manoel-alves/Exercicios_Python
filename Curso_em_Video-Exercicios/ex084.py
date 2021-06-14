pessoas = []
dados = []
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    check = str(input('Quer continuar? [S/N] ')).strip().lower()
    if check == 'n':
        break

print('=-' * 30)
print(f'O maior peso foi {maior:.1f}Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == maior:
        print(f'[{i[0]}] ', end='')
print(f'\nO menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == menor:
        print(f'[{i[0]}] ', end='')
