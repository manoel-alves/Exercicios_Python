print('-=-' * 15)
print('Analisador de Triângulos')
print('-=-' * 15)

n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))


if n1 > (n2 + n3) or n2 > (n1 + n3) or n3 > (n1 + n2):
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
else:
    print('Os segmentos acima PODEM FORMAR triângulo')