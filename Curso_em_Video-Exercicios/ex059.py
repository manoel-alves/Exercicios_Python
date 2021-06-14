from time import sleep
x = int(input('Primeiro valor: '))
y = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:

    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        result = x + y
        print('=-=' * 15)
        print(f'A soma entre {x} + {y} é {result}')
        print('=-=' * 15)
        sleep(1)
    elif opcao == 2:
        result = x * y
        print('=-=' * 15)
        print(f'A multiplicação entre {x} x {y} é {result}')
        print('=-=' * 15)
        sleep(1)
    elif opcao == 3:
        if x > y:
            result = x
        else:
            result = y
        print('=-=' * 15)
        print(f'O maior entre {x} e {y} é {result}')
        print('=-=' * 15)
        sleep(1)
    elif opcao == 4:
            print('Informe os números novamente:')
            sleep(1)
            x = int(input('Primeiro valor: '))
            y = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Encerrando o programa...')
        sleep(1.5)
    else:
        print('Opção Inválida. Digite novamente:')
        sleep(1)

sleep(1)
print('\nFim do programa! Até mais!')
