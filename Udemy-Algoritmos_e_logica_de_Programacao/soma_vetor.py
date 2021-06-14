n = int(input('Quantos numeros voce vai digitar? '))

vet = [0 for i in range(n)]

for i in range(0, n):
    vet[i] = float(input('Digite um numero: '))

print(f'VALORES = ', end='')
soma = 0
for i in vet:
    print(f'{i:.1f}', end='  ')
    soma += i
print()
print(f'SOMA = {soma:.2f}')
print(f'MEDIA = {soma / n:.2f}')