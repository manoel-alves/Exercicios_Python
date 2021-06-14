print('=' * 40)
print('{:' '^40}'.format('BANCO CEV'))
print('=' * 40)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de R${ced:.2f}')
        if ced == 50:
            ced = 20
            totced = 0
        elif ced == 20:
            ced = 10
            totced = 0
        elif ced == 10:
            ced = 1
            totced = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre ao banco CEV! Tenha um bom dia!')