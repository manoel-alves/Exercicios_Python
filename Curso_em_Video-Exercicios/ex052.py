x = int(input('Digite um número: '))

check = 0
for i in range(1, x + 1):
    if x % i == 0:
        print('\033[33m', end=(''))
        check += 1
    else:
        print('\033[31m', end=(''))
    print(f'{i}', end=' ')

print('\033[m')
if check == 2:
    print(f'O número {x} foi divisível {check} vezes\nE por isso ele É PRIMO!')
else:
    print(f'O número {x} foi divisível {check} vezes\nE por isso ele NÀO É PRIMO!')