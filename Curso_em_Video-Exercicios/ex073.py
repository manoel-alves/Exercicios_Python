lista = ('Macaco', 'Jiboia', 'Pombo', 'Gato', 'Cachorro', 'Tartaruga', 'Coelho', 'Cavalo', 'Rato', 'Urso')
cont = 0
while True:
    print('-=' * 15)
    if cont == 0:
        print(f'Lista Completa: {lista}')
    elif cont == 1:
        print(f'5 primeiros itens: {lista[:5]}')
    elif cont == 2:
        print(f'4 últimos itens: {lista[-4:]}')
    elif cont == 3:
        print(f'Em ordem alfabética: {sorted(lista)}')
    elif cont == 4:
        nome = str(input('Quem você quer procurar? ')).strip().capitalize()
        print(f'O {nome} está na {lista.index(nome) + 1}a posição')
    else:
        break
    cont += 1