x = int(input('Digite um número para ver sua tabuada: '))

for i in range(0, 10):
    print(f'{x} x {i + 1:2} = {x * (i + 1)}')