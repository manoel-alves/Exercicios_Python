def notas(*num, sit=False):
    dic = {}
    '''lista = []
    for i in num:
        lista.append(i)'''

    soma = cont = 0
    for i, j in enumerate(num):
        if i == 0:
            maior = j
            menor = j
        else:
            if j > maior:
                maior = j
            if j < menor:
                menor = j
        soma += j
        cont += 1
    dic['Total'] = cont
    dic['Maior'] = maior
    dic['menor'] = menor
    dic['Média'] = soma / cont

    if sit == True:
        if dic['Média'] <= 5:
            situ = 'RUIM'
        elif dic['Média'] <= 6.9:
            situ = 'REGULAR'
        elif dic['Média'] <= 8.9:
            situ = 'BOA'
        else:
            situ = 'EXCELENTE'
        dic['situação'] = situ
    return dic


x = input('Quantos notas você quer registrar? ')
x = int(x)
lis =[]
for c in range(0, x):
    lis.append(float(input(f'   Nota {c+1}: ')))
check = ' '
while check not in 'SN':
    check = str(input('Quer visualizar a situação? [S/N] ')).strip().upper()
    if check not in 'SN':
        print('ERRO! Digite S ou N.')
if check == 'S':
    print(notas(lis, sit=True))
else:
    print(notas(lis))