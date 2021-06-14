import os

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print('Departamento Estadual de Metereologia')
    print('-' * 37)
    print(' ' * 6,'Medição de temperaturas', ' ' * 5)
    print('-' * 37)
    print(' >>  Insira "f" para finalizar!  <<\n')

    soma = maior = menor = quantidade = 0

    while True:
        
        temperatura = input('Digite a medição -> ')

        try:
            temperatura = float(temperatura)
        except:
            temperatura

        if type(temperatura) == float:

            soma += temperatura
            quantidade += 1

            if quantidade == 1:
                maior = temperatura
                menor = temperatura
            else:
                if( temperatura > maior):
                    maior = temperatura

                if( temperatura < menor):
                    menor = temperatura

        elif temperatura != 'f':

            print('Valor Inválido!')

        else:
            break

    os.system('cls' if os.name == 'nt' else 'clear')

    print('-' * 31)
    print(' ' * 10, 'Relatório')
    print('-' * 31)

    if quantidade != 0:

        print('Média das temperaturas: {:.1f} °C'.format(soma / quantidade))
        print('Maior temperaturas:',  maior, '°C')
        print('Menor temperaturas:',  menor, '°C')
        print('-' * 31, '\n')

    else:
        print('  Nenhuma temperatura medida!')
        print('-' * 31, '\n')
    
    while True:
        opcao = input('Deseja fazer outra medição? (s/n) ')
    
        if opcao == 's' or opcao == 'n':
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print(">> Opção Inválida! Digite novamente. <<")
            print('-' * 39)

    if opcao == 'n':
        break