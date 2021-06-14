print('Digite dois numeros: ')
x = int(input())
y = int(input())

if x > y:
    hold = x
    x = y
    y = hold

soma = 0
for i in range(x+1, y):
    if i % 2 != 0:
        soma += i

print(f'SOMA DOS IMPARES = {soma}')
