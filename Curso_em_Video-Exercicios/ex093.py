fut = {}

fut['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
x = int(input('Qauntas partidas Zico jogou? '))
total = 0
fut['Gols'] = list()
for i in range(0, x):
    gol = int(input(f'Quantos gols na partida {i + 1}? '))
    total += gol
    fut['Gols'].append(gol)
fut['Total'] = total

print('-=' * 30)
print(fut)
print('-=' * 30)
for i, j in fut.items():
    print(f'O campo {i} tem o valor {j}')
print('-=' * 30)
print(f'O jogador {fut["Nome"]} jogou {x} partidas.')
for i, j in enumerate(fut['Gols']):
    print(f'    => Na partida {i + 1}, fez {j} gols.')
print(f'Foi um total de {fut["Total"]} gols.')


