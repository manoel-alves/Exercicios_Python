print('=' * 12, ' LOJAS MANOLA ', '=' * 12)
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n'
      '[ 1 ] à vista dinheiro/cheque\n'
      '[ 2 ] à vista cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1 :
    precofinal = preco - (preco * 10 / 100)
elif opcao == 2 :
    precofinal = preco - (preco * 5 / 100)
elif opcao == 3 :
    parcela = preco / 2
    precofinal = preco
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
else:
    parcelas = int(input('Quantas parcelas? '))
    juros = preco * 20 / 100
    precofinal = preco + juros
    parcela = precofinal / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${parcela:.2f} COM JUROS')

print(f'Sua compra de R${preco:.2f} vai custar R${precofinal:.2f} no final.')