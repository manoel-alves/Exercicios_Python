from utilidadesCeV import moeda

preco = float(input('Digite um preço: R$'))
check = ' '
while check not in 'SN':
    check = str(input('Quer formatar os valores? [S/N] ')).strip().upper()
    if check not in 'SN':
        print('ERRO! Digite S ou N.')
if check in 'S':
    f = True
else:
    f = False

print('~' * 31)
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, f)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, f)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, f)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, f)}')