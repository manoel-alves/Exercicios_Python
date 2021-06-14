fut = [{}]
cont = 0
while True:
    fut[cont]['Jogador'] = str(input('Nome do jogador: ')).strip().capitalize()
    part = ' '
    while part.isnumeric() == False:
        part = input(f'Quantas partidas {fut[cont]["Jogador"]} jogou? ')
        if part.isnumeric() == False:
            print('ERRO! Digite um número.')
    fut[cont]['Partidas'] = int(part)
    fut[cont]['Gols'] = []
    for i in range(0, fut[cont]['Partidas']):
        gol = ' '
        while gol.isnumeric() == False:
            gol = input(f'    Quantos gols na partida {i + 1}? ')
            if gol.isnumeric() == False:
                print('        ERRO! Digite um número.')
        fut[cont]['Gols'].append(int(gol))
    total = 0
    for i in range(0, len(fut[cont]['Gols'])):
            total += fut[cont]['Gols'][i]
    fut[cont]['Total'] = total

    check = ' '
    while check not in 'SN':
        check = str(input('Quer continuar? [S/N] ')).strip().upper()
        if check not in 'SN':
            print('ERRO! Digite S ou N.')
    if check == 'N':
        break
    else:
        cont += 1
        fut.append({})

print('-=' * 22)
print(f'{"|Cód.|":<7}{"|Nome|":<15}{"|Gols|":<15}{"|Total|":>5}')
print('-' * 44)
for i, j in enumerate(fut):
    print(f' {i:<6}', end='')
    for c, n in j.items():
        if 'Gols' != c != 'Partidas':
            print(f' {n:<13} ', end='')
        elif c == 'Gols':
            print(n, end='')
            print(' ' * (15 - (len(n) * 3)), end='')
    print()
indices = []
for i in range(0, len(fut)):
    indices.append(i)
indices.append(-1)

while True:
    print('-' * 44)
    x = -2
    while x not in indices:
        x = int(input('Mostrar dados de qual jogador? (-1 para parar) '))
        if x not in indices:
            print(f'ERRO! Não existe jogador com código {x}!')
    if x == -1:
        break

    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {fut[x]["Jogador"]}:')
        for i, j in enumerate(fut[x]['Gols']):
            print(f'    No jogo {i + 1} fez {j} gols.')
print('<< VOLTE SEMPRE >>')