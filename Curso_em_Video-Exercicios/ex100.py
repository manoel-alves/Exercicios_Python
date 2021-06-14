from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        x = randint(0, 9)
        if x in lista:
            while x in lista:
                x = randint(0, 9)
        print(x, end=' ')
        lista.append(x)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somapar(numeros)