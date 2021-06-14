aluno = {}

aluno['Nome'] = str(input('Nome: ')).strip().capitalize()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print('=-' * 18)
for i, j in aluno.items():
    print(f'- {i} é igual a {j}')