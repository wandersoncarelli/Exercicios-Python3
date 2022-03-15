# Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

print('Digite a largura e altura de uma parede.')
print()
l = float(input('Largura: '))
a = float(input('Altura: '))
p = l * a
t = p / 2
print()

print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área total é de {:.2f}m².'.format(l, a, p))
print('Para pintar essa parede, você vai precisar de {:.2f}l de tinta.'.format(t))
