from time import sleep


def text(msg, col):
    tam = len(msg) + 6
    print(f'\033[30;{col}m', end='')
    print('~' * tam)
    print(f'   {msg}')
    print('~' * tam)
    print('\033[m', end='')


while True:
    text('SISTEMA DE AJUDA PyHELP', 42)
    x = str(input('Função ou Biblioteca ("fim" para sair)> ')).strip().lower()
    if x == 'fim':
        text('ATÉ LOGO!', 41)
        break
    sleep(0.3)
    text(f'Acessando o manual do comando "{x}"', 44)
    sleep(1)
    print('\033[7;30m', end='')
    help(x)
    print('\033[m', end='')

