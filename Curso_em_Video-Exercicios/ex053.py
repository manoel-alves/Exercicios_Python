frase = str(input('Digite a frase: ')).strip().upper()
lista = frase.split()
frasej = ''.join(lista)

invert = ''
for i in range(len(frasej) - 1, -1, -1):
    invert += frasej[i]

print(f'A frase {frasej}, invertida fica {invert}')

if frasej == invert:
    print('E é um palíndromo!')
else:
    print('Não é um palíndromo!')
