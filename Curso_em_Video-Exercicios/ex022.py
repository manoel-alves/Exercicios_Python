nome = input('Digite seu nome completo: ')

print('Analisando seu nome...')

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
num = len(nome)
esp = len(nome.split())
letras = num - (esp - 1)
print('Seu nome tem ao todo {} letras'.format(letras))
lista = nome.split()
nprim = len(lista[0])
print('Seu primeiro nome é {} e ele tem {} letras'.format(lista[0].capitalize(), nprim))