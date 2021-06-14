for i in range(0, 6):
    peso = float(input(f'Peso da {i + 1}a pessoa: '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'Maior peso = {maior}')
print(f'Menor peso = {menor}')