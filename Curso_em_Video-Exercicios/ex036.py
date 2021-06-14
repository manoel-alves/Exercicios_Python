preco = float(input('Qual o valor do ímovel? R$'))
salario = float(input('Qual o seu salário? R$'))
tempo = int(input('Por quanto tempo pretende pagar? '))

prest = preco / (tempo * 12)
porcent = salario * 30 / 100

print(f'Para pagar um imóvel de R${preco:.2f} em {tempo} anos, a prestação será de R${prest:.2f}!')

if prest <= porcent:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')