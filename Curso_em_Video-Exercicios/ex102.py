def fatorial(num, show):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser fatorado.
    :param show: (opcional) Mostra ou não o processo.
    :return: O valor fatorial de num
    """
    if show == True:
        for i in range(num, 0, -1):
            if i == 1:
                print(i, '= ', end='')
            else:
                print(i, 'x ', end='')
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
    return fat


print('-' * 40)
x = int(input('Qual número? '))
check = str(input('Deseja ver o processo? [S/N] ')).strip().upper()
if check == 'S':
    check = True
else:
    check = False
print(f"{fatorial(x, check)}")
