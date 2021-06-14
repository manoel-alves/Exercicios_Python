def escreva(msg):
    tam = len(msg) + 6
    print('~' * tam)
    print(f'   {msg}')
    print('~' * tam)


#Main
frase = str(input('Frase: ')).strip().title()
escreva(frase)
