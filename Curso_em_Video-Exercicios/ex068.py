from random import randint, choice
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

vit = 0
while True:
    vplayer = int(input('Diga um valor: '))
    escplayer = ' '
    while escplayer not in 'PI':
        escplayer = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]

    vcomp = randint(0, 10)
    lista = ['P', 'I']
    esccomp = choice(lista)

    total = vplayer + vcomp

    print('--' * 15)
    print(f'Você jogou {vplayer} e o computador {vcomp}. Total de {total}', end=' ')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')

    if escplayer == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vit += 1
        else:
            print('Você PERDEU!')
            break
    else:
        if total % 2 != 0:
            print('Você VENCEU!')
            vit += 1
        else:
            print('Você PERDEU!')
            break
    print('--' * 15, '\n')

    print('=-' * 15)
    print('Vamos jogar novamente...')
    print('=-' * 15)

print(f'GAME OVER! você venceu {vit} vezes.')