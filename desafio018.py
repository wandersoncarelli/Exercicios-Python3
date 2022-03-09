# ==================================================== DESAFIO 018 =====================================================
# Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# ======================================================================================================================
from format import text
from math import radians, sin, cos, tan
a = float(input('Digite um {}ângulo{} para saber seu valor do {}seno{}, {}cosseno{} e {}tangente{}: '.format(
    text['magenta'], text['reset'], text['verde'], text['reset'], text['azul'], text['reset'], text['ciano'],
    text['reset'])))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print()
print('O {}ângulo{} de {}{}{} tem o {}SENO{} de {}{:.2f}{}'.format(text['magenta'], text['reset'], text['magenta'], a,
                                                                   text['reset'], text['verde'], text['reset'],
                                                                   text['verde'], s, text['reset']))
print('O {}ângulo{} de {}{}{} tem o {}COSSENO{} de {}{:.2f}{}'.format(text['magenta'], text['reset'], text['magenta'],
                                                                      a, text['reset'], text['azul'], text['reset'],
                                                                      text['azul'], c, text['reset']))
print('O {}ângulo{} de {}{}{} tem a {}TANGENTE{} de {}{:.2f}{}'.format(text['magenta'], text['reset'], text['magenta'],
                                                                       a, text['reset'], text['ciano'], text['reset'],
                                                                       text['ciano'], t, text['reset']))
