form = str(input('Digite a expressão: '))

cont = []
for i in form:
    if i == '(':
        cont.append(i)
    elif i == ')':
        if len(cont) > 0:
            cont.pop()
        else:
            cont.append(')')
            break

if len(cont) == 0:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')