lista = []
while True:
    x = input('Digite um valor: ')
    if not x.isnumeric():
        while not x.isnumeric():
            x = input('Caracter inválido! Digite novamente: ')
    x = int(x)

    if x in lista:
        print('Valor duplicado... Não adicionado!')
    else:
        lista.append(x)
        print('Valor adicionado com sucesso...')

    check = ' '
    while check not in 'SN':
        check = str(input('Quer continuar? [S/N] ')).strip().upper()
    if check == 'N':
        break

print('=-=' * 20)
lista.sort()
print(f'Você digitou os valores {lista}')