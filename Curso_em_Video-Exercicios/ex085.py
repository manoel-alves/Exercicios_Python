num = [[], []]
for i in range(0, 7):
    x = int(input(f'Digite o {i + 1}o. valor: '))
    if x % 2 == 0:
        num[0].append(x)
    else:
        num[1].append(x)

print('=-' * 30)
num[0].sort()
print(f'Os valores pares digitados foram: {num[0]}')
num[1].sort()
print(f'Os valores impares digitados foram: {num[1]}')