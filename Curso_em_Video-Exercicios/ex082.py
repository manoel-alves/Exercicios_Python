lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))

    check = str(input('Quer continuar? [S/N] ')).strip().upper()
    if check == 'N':
        break

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print('=-' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')