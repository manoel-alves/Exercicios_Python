from random import randint
from time import sleep
print('-' * 41)
print('{:^41}'.format('JOGA NA MEGA SENA'))
print('-' * 41)

x = int(input('Quantos jogos você quer que eu sorteie? '))
lista = []
for i in range(0, x):
    lista.append([])
    for j in range(0, 6):
        n = randint(0, 60)
        while n in lista[i]:
            n = randint(0, 60)
        lista[i].append(n)
    sleep(1)
    lista[i].sort()
    print(f'Jogo {i + 1}: {lista[i]}')
sleep(1)
print('-=' * 6, '{:^14}'.format('< BOA SORTE! >'), '-=' * 6)

