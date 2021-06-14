from datetime import date

dados = {}
atual = date.today().year

while True:
    dados['Nome'] = str(input('Nome: ')).strip().capitalize()
    nasc = int(input('Ano de Nascimento: '))
    dados['Idade'] = atual - nasc
    dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if dados['ctps'] == 0:
        dados['ctps'] = 'Não Possui'
        break
    else:
        dados['Contratação'] = int(input('Ano de contratação: '))
        dados['Salário'] = float(input('Salário: R$'))
        dados['Aposentadoria'] = (dados['Contratação'] - nasc) + 35
        break

print('=-' * 30)
for i, j in dados.items():
    if i == 'Salário':
        print(f'  - {i}: R${j:.2f}')
    else:
        print(f'  - {i}: {j}')