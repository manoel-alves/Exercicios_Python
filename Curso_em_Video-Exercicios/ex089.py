alunos = [[], []]
cont = 0
while True:
    alunos[0].append(str(input('Nome: ')).strip().capitalize())
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    alunos[1].append((n1 + n2) / 2)
    cont += 1
    check = str(input('Quer continuar? [S/N] ')).strip().upper()
    if check == 'N':
        break
print('=-' * 15)
print('{:<4} {:<10} {:>8}'.format('No.', 'NOME', 'MÉDIA'))
print('-' * 24)
for i in range(0, cont):
    print(f'{i:<4} {alunos[0][i]:<10} {alunos[1][i]:>8.1f}')