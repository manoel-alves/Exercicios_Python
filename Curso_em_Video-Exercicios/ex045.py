from random import randint
from time import sleep

print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
player = int(input('Qual é a sua jogada? '))
comp = randint(0, 2)

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

print('-=' * 18)
print(f'Jogador escolheu {opcoes[player]}')
print('-=' * 18)

sleep(2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

sleep(1)

print('-=' * 18)
print(f'Computador escolheu {opcoes[comp]}')
print('-=' * 18)

sleep(1)

if player == comp:
    print('Empate!')
else:
    if player == 0:
        if comp == 1:
            print('\nVOCÊ PERDEU! :/')
        else:
            print('\nVOCÊ GANHOU!!! :)')
    elif player == 1:
        if comp == 0:
            print('\nVOCÊ GANHOU!!! :)')
        else:
            print('\nVOCÊ PERDEU! :/')
    elif player == 2:
        if comp == 1:
            print('\nVOCÊ GANHOU!!! :)')
        else:
            print('\nVOCÊ PERDEU! :/')
