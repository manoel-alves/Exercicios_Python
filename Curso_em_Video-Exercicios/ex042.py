seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 < (seg2 + seg3) and seg2 < (seg1 + seg3) and seg3 < (seg1 + seg2):
    if seg1 == seg2 == seg3:
        print('Podem formar Triângulo, EQUILÁTERO!')
    elif seg1 == seg2 or seg2 == seg3 or seg1 == seg3:
        print('Podem formar Triângulo, ISÓSCELES!')
    else:
        print('Podem formar Triângulo, ESCALENO!')
else:
    print('Não formam triângulo!')
