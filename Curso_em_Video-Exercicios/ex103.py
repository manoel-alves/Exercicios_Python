def ficha(nome='<desconhecido>', gols=0):
    frase = f'O jogador {nome} fez {gols} gol(s) no campeonato.'
    return frase


print('-' * 20)
name = input('Nome do jogador: ').strip().capitalize()
g = input('Número de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if name.strip() == '':
    print(ficha(gols=g))
else:
    print(ficha(name, g))