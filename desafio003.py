# ==================================================== DESAFIO 003 =====================================================
# Crie um programa que leia dois números e mostre a soma entre eles.
# ======================================================================================================================
from format import text
print('Digite dois números para saber a soma entre eles.\n')
n1 = float(input('{}Primeiro número{}: '.format(text['azul'], text['reset'])))
n2 = float(input('{}Segundo número{}: '.format(text['magenta'], text['reset'])))
s = n1 + n2
print()
print('A soma entre {}{:.2f}{} e {}{:.2f}{} é igual a {}{:.2f}{}.'.format(
    text['azul'], n1, text['reset'], text['magenta'], n2, text['reset'], text['verde'], s, text['reset']))
