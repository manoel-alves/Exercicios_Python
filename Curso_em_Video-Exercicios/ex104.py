def leiaint(msg):
    x = str(input(msg))
    while not x.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.]\033[m')
        x = str(input(msg))
    return x


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')