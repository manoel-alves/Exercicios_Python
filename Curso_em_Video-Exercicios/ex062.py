print('Gerador de PA')
print('-=-' * 5)
ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
termo = 10
acresc = -1
while acresc != 0:
    while cont < termo:
        print(f'{ptermo} -> ', end='')
        ptermo += razao
        cont += 1
    print('PAUSA')
    acresc = int(input('Quantos termos você quer mostrar a mais? '))
    termo += acresc
print(f'Progressão finalizada com {cont} termos mostrados.')