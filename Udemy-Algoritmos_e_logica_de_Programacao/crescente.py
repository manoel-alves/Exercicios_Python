c = 0
while True:
    if c == 0:
        print('Digite dois numeros: ')
    else:
        print('Digite outros dois numeros: ')
    x = int(input())
    y = int(input())

    if x == y:
        break
    elif x < y:
        print('CRESCENTE!')
    else:
        print('DECRESCENTE!')

    c += 1