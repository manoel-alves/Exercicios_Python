extenso = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze','dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

n = -1
while n < 0 or n > 20:
    n = int(input('Digite um número entre 0 e 20: '))

print(f'Você digitou o número {extenso[n]}')

