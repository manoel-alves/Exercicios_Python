#from random import choice
from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

#range = [0, 1, 2, 3, 4, 5]
#comp = random.choice(range)

n = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
comp = randint(0, 5)


if n == comp:
    print('PARABÉNS! Você conseguiu me vencer! Pensei no número {}.'.format(comp))
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(comp, n))