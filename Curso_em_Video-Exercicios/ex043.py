peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))

imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc <= 40:
    if imc < 18.5:
        print('Abaixo do Peso')
    elif 18.5 <= imc < 25:
        print('Peso ideal')
    elif 25 <= imc < 30:
        print('Sobrepeso')
    else:
        print('Obesidade')
else:
    print('Obesidade mórbida')