x = int(input('Digite um número inteiro: '))
opcao = int(input('Escolha uma das bases para conversão:\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL\nSua opção:'))

if opcao == 1:
    sistema = 'BINÁRIO'
    convert = bin(x)
elif opcao == 2:
    sistema = 'OCTAL'
    convert = oct(x)
else:
    sistema = 'HEXADECIMAL'
    convert = hex(x)

print(f'{x} convertido para {sistema} é igual a {convert[2:]}')