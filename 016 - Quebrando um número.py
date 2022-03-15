# ==================================================== DESAFIO 016 =====================================================
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.
# ======================================================================================================================
from format import text
print('Digite um {}número real{} qualquer para saber qual é seu {}valor inteiro{}.'.format(
    text['azul'], text['reset'], text['verde'], text['reset']))
print()

# MÉTODO 01 - IMPORTAR LIBRARY MATH
from math import trunc
n = float(input('Digite um número: '))
print('O número {}{}{} tem a parte inteira {}{}{}.\n'.format(text['azul'], n, text['reset'], text['verde'], trunc(n),
                                                             text['reset']))

# MÉTODO 02 - FUNÇÃO INT
n2 = float(input('Digite um número: '))
print('O número {}{}{} tem a parte inteira {}{}{}.'.format(text['azul'], n2, text['reset'], text['verde'], int(n2),
                                                           text['reset']))
