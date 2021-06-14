soma = 0
for i in range(1, 7):
    x = int(input(f'n{i}: '))
    if x % 2 == 0:
        soma += x
if soma != 0:
    print(f'Soma = {soma}')
else:
    print('Nenhum número par digitado!')