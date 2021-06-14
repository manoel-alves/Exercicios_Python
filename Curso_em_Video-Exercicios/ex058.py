from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que consegue adivinhar qual foi?\n')
comp = randint(0, 10)
x = -1
cont = 0
while x != comp:
    x = int(input('Qual é seu palpite? '))
    if x < 0 or x > 10:
        print('Vamos lá... não está nem dentro dos limites :/')
    else:
        if x > comp:
            print('Menos... Tente mais uma vez.')
        elif x < comp:
            print('Mais... Tente mais uma vez.')
        cont += 1
    print('\n')
print(f'Acertou com {cont} tentativas. Parabéns')