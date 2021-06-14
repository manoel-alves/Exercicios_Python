maior = homens = mulheres = idade = 0

while True:
    sexo = check = ' '
    num = False

    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)

    while num == False:
        idade = input('Idade: ')
        num = idade.isnumeric()

    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    idade = int(idade)
    if idade >= 18:
        maior += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulheres += 1

    print('-' * 30)
    while check not in 'SN':
        check = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if check == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')