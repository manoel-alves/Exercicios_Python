soma = cont = 0
inercia = 'S'
while inercia != 'N':
    x = float(input('Digite um número: '))
    if cont == 0:
        maior = x
        menor = x
    elif x > maior:
        maior = x
    elif x < menor:
        menor = x
    soma += x
    cont += 1
    inercia = str(input('Quer continuar [S/N]? ')).strip().upper()
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior:.0f} e o menor foi {menor:.0f}')