print('Dados da primeira pessoa:')
nome1 = str(input('Nome: ')).title()
idade1 = int(input('Idade: '))

print('Dados da segunda pessoa:')
nome2 = str(input('Nome: ')).title()
idade2 = int(input('Idade: '))

print(f'A idade media de {nome1} e {nome2} eh de {(idade1 + idade2) / 2} anos')