from math import radians, sin, cos, tan

ang = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('O ângulo de {} tem SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(ang, tan))