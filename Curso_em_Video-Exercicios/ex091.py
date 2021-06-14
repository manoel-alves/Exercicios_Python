from random import randint
from operator import itemgetter

players = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6)}
print('Valores sorteados:')
for i, j in players.items():
    print(f'Jogador {i} tirou {j} no dado.')

print('\n', '=-' * 15)
print(f'== RANKING DOS JOGADORES ==')
ranking = {}
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
cont = 0
for i, j in ranking:
    print(f'{cont + 1}o lugar: Jogador {i} com {j}')
    cont += 1