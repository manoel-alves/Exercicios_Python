from time import sleep


def cont(x, y, z):
    print('-=' * 20)
    print(f'Contagem de {x} até {y} de {z} em {z}')

    if y < x:
        z = z * -1
    if z < 0:
        for i in range(x, y - 1, z):
            print(i, end=' ')
            sleep(0.5)
    else:
        for i in range(x, y + 1, z):
            print(i, end=' ')
            sleep(0.5)
    print('FIM!')


# Main
cont(0, 10, 1)

cont(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
init = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
cont(init, fim, passo)
