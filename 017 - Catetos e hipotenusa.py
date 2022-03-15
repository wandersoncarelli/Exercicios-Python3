# ==================================================== DESAFIO 017 =====================================================
# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.
# ======================================================================================================================
from format import text
print('Digite o comprimento do {}cateto oposto{} e do {}cateto adjacente{} de um triângulo retângulo para calcular o '
      'comprimento da {}hipotenusa{}.'.format(text['azul'], text['reset'], text['ciano'], text['reset'],
                                              text['magenta'], text['reset']))
print()
# MÉTODO 01 - FAZER O CÁLCULO
co1 = float(input('Comprimento do {}cateto oposto{}: '.format(text['azul'], text['reset'])))
ca1 = float(input('Comprimento do {}cateto adjacente{}: '.format(text['ciano'], text['reset'])))
h1 = (co1 ** 2 + ca1 ** 2) ** (1/2)
print('A {}hipotenusa{} vai medir {}{:.2f}{}.'.format(text['magenta'], text['reset'], text['magenta'], h1,
                                                      text['reset']))
print()

# MÉTODO 02 - IMPORTAR LIBRARY MATH
from math import hypot
co2 = float(input('Comprimento do {}cateto oposto{}: '.format(text['azul'], text['reset'])))
ca2 = float(input('Comprimento do {}cateto adjacente{}: '.format(text['ciano'], text['reset'])))
h2 = hypot(co2, ca2)
print('A {}hipotenusa{} vai medir {}{:.2f}{}.'.format(text['magenta'], text['reset'], text['magenta'], h2,
                                                      text['reset']))
