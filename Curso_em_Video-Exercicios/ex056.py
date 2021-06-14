soma = 0
nvelho = ''
ivelho = 0
count = 0
for i in range (0, 4):
    print('-' * 5, f'{i + 1}a PESSOA', '-' * 5)
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    soma += idade

    if i == 0 and sexo == 'M':
        nvelho = nome
        ivelho = idade
    else:
        if sexo == 'M' and idade > ivelho:
            nvelho = nome
            ivelho = idade

    if sexo == 'F' and idade < 20:
        count += 1

media = soma / 4

print(f'A média de idade do grupo é de {media:.1f} anos')
print(f'O homem mais velho tem {ivelho} anos e se chama {nvelho}.')
print(f'Ao todo são {count} mulheres com menos de 20 anos')
