#from math import sqrt
from math import hypot

opo = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))

#hipo = sqrt((pow(opo, 2)) + (pow(adj, 2)))
hipo = hypot(opo, adj)

print('A hipotenusa vai medir {:.2f}'.format(hipo))