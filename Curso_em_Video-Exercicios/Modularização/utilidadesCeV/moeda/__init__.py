def moeda(x):
    return f'R${x:.2f}'


def aumentar(x, p, fm=False):
    if fm == True:
        return moeda(x + ((x * p) / 100))
    else:
        return x + ((x * p) / 100)


def diminuir(x, p, fm=False):
    if fm == True:
        return moeda(x - ((x * p) / 100))
    else:
        return x - ((x * p) / 100)


def dobro(x, fm=False):
    if fm == True:
        return moeda(x * 2)
    else:
        return x * 2


def metade(x, fm=False):
    if fm == True:
        return moeda(x / 2)
    else:
        return x / 2


def resumo(x, pa, pd, f=False):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'{"Preço analisado:":<30}{moeda(x)}')
    print(f'{"Dobro do Preço:":<30}{dobro(x, f)}')
    print(f'{"Metade do Preço:":<30}{metade(x, f)}')
    print(f'{f"{pa}% de aumento:":<30}{aumentar(x, pa, f)}')
    print(f'{f"{pd}% de redução:":<30}{diminuir(x, pd, f)}')
    print('-' * 40)
