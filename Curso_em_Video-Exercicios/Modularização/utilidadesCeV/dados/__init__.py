def leiaDinheiro():
    valido = False
    while not valido:
        prec = str(input('Digite um valor: R$')).replace(',', '.').strip()
        if prec.isalpha() or prec == '':
            print(f'\033[31mERRO! "{prec}" é um preço inválido!\033[m')
        else:
            valido = True
    return float(prec)


def check():
    check = ' '
    while check not in 'SN':
        check = str(input('Quer formatar os valores? [S/N] ')).strip().upper()
        if check not in 'SN':
            print('\033[31mERRO! Digite S ou N.\033[m')
    if check in 'S':
        f = True
    else:
        f = False
    return f