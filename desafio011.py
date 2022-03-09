# ==================================================== DESAFIO 011 =====================================================
# Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
# ======================================================================================================================
from format import text
print('Digite a {}largura{} e {}altura{} de uma parede para saber sua {}área total{} e quanta {}tinta{} será '
      'necessário para pintá-la.'.format(text['verde'], text['reset'], text['azul'], text['reset'], text['magenta'],
                                         text['reset'], text['ciano'], text['reset']))
print()
l = float(input('Digite a {}largura{}: '.format(text['verde'], text['reset'])))
a = float(input('Digite a {}altura{}: '.format(text['azul'],text['reset'])))
p = l * a
print()
print('Sua parede tem a dimensão de {}{:.2f}{}x{}{:.2f}{} e sua área total é de {}{:.2f}m²{}.'.format(
    text['verde'], l, text['reset'], text['azul'], a, text['reset'], text['magenta'], p, text['reset']))
t = p / 2
print('Para pintar essa parede, você precisará de {}{:.2f}l{} de tinta.'.format(text['ciano'], t, text['reset']))
