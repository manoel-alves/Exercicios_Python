n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

if 0 <= n1 <= 10 >= n2 >= 0:

    media = (n1 + n2) / 2
    print(f'MÉDIA = {media:.1f}')

    if media < 5:
        print('REPROVADO!')
    elif media >= 7 :
        print('APROVADO! Parabéns!')
    else:
        print('RECUPERAÇÃO!')

else:

    print('Notas inválidas!')