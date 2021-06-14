def checarSomas(lista, k):
    for i in lista:
        for j in lista:
            if i != j and i + j == k: 
                return True
    return False

lista = [1,2,3,5,6,7]
k = int(input('Digite um valor: '))

print( checarSomas(lista, k) )