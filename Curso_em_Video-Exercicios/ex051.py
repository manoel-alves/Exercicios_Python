print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(termo, termo + (10 * razao), razao):
    print(f'{i} -> ', end='')
print('ACABOU')