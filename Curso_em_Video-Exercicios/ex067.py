while True:
    x = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if x < 0:
        break
    for i in range(1, 11):
        print(f'{x} x {i:2} = {x * i}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')