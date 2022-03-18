# ==================================================== DESAFIO 017 =====================================================
# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.
# ======================================================================================================================
from math import hypot
print('Digite o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo para calcular o '
      'comprimento da hipotenusa.')
print()
# MÉTODO 01 - FAZER O CÁLCULO
co1 = float(input('Comprimento do cateto oposto: '))
ca1 = float(input('Comprimento do cateto adjacente: '))
h1 = (co1 ** 2 + ca1 ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(h1))
print()

# MÉTODO 02 - USANDO A LIBRARY MATH
co2 = float(input('Comprimento do cateto oposto: '))
ca2 = float(input('Comprimento do cateto adjacente: '))
h2 = hypot(co2, ca2)
print('A hipotenusa vai medir {:.2f}.'.format(h2))
