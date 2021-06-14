pessoas = [{}]

cont = soma = 0
while True:
    pessoas.append({})

    pessoas[cont]['Nome'] = input('Nome: ').strip().capitalize()

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
        if sexo not in 'MF':
            print('ERRO! Responda apenas M ou F.')
    pessoas[cont]['Sexo'] = sexo

    idade = ' '
    while idade.isnumeric() == False:
        idade = input('Idade: ').strip()
        if idade.isnumeric() == False:
            print('ERRO! Por favor, digite um número!')
    idade = int(idade)
    soma += idade
    pessoas[cont]['Idade'] = idade

    check = ' '
    while check not in 'SN':
        check = str(input('Quer continuar? [S/N] ')).strip().upper()
        if check not in 'SN':
            print('ERRO! Responda apenas S OU N.')
    if check in 'N':
        cont += 1
        break
    else:
        cont += 1
print('=-' * 30)
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
media = soma / cont
print(f'B) A média de idade é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for i in range(0, cont):
    if pessoas[i]['Sexo'] == 'F':
        print(pessoas[i]['Nome'], end=' ')
print(f'\nD) Lista das pessoas que estão acima da média:')
for i in range(0, cont):
    if pessoas[i]['Idade'] > media:
        print(f'    nome = {pessoas[i]["Nome"]}; sexo = {pessoas[i]["Sexo"]}; idade = {pessoas[i]["Idade"]};')
print('<< ENCERRADO >>')