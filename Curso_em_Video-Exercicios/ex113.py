def leiaint(msg):
    while True:
        try:
            a = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não giditar esse número.\033[m')
            break
        else:
            return a


def leiafloat(msg):
    while True:
        try:
            b = str(input(msg)).replace(',', '.').strip()
            b = float(b)
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não giditar esse número.\033[m')
            break
        else:
            return b


x = leiaint('Digite um inteiro: ')
y = leiafloat('Digite um real: ')
print(f'O valor inteiro foi {x} e o valor real foi {y:.1f}')
