tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
'''vogais = ('a', 'e', 'i', 'o', 'u')

for i in range(0, len(tupla)):
    print(f'\nNa palavra {tupla[i].upper()} temos ', end='')

    for j in range(0, 5):
        if vogais[j] in tupla[i]:
            print(f'{vogais[j]} ' * tupla[i].count(vogais[j]), end='')'''

for i in tupla:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for j in i:
        if j.lower() in 'aeiou':
            print(j, end=' ')
