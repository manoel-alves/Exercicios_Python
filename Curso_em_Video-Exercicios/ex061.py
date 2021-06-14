print('Gerador de PA')
print('-=-' * 5)
ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão de PA: '))
cont = 0
while cont < 10:
    print(f'{ptermo} -> ', end='')
    ptermo += razao
    cont += 1
print('FIM')