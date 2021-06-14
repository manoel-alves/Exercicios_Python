from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))

idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade < 18:
    falta = 18 - idade
    print(f'Ainda faltam {falta} anos para o alistamento')
    ano = atual + falta
    print(f'Seu alistamento será em {ano}')
elif idade > 18 :
    atraso = idade - 18
    print(f'Você já deveria ter se alistado há {atraso} anos.')
    anoc = atual - atraso
    print(f'Seu alistamento deveria ter sido em {anoc}')
else:
    print('Você deve se alistar IMEDIATAMENTE!')