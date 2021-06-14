x = float(input('Largura da parede: '))
y = float(input('Altura da parede: '))

area = x * y
tinta = area / 2

print('Sua parede tem dimensão de {}x{} e sua área é de {}m2.'.format(x, y, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))