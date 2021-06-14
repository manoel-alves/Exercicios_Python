from time import sleep


def info(* num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    sleep(1)
    for i in num:
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        print(i, end=' ')
        sleep(0.5)
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {maior}.')


info(5, 9, 3, 4, 7, 1)