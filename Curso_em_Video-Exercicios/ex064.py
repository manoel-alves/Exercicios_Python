x = -1
soma = cont = 0
while x != 0:
    x = int(input('Digite um número [0 para parar]: '))
    if x != 0:
        soma += x
        cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')