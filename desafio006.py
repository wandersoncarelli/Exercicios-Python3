# ==================================================== DESAFIO 006 =====================================================
# Crie um programa que leia um número e mostre o seu doro, triplo e raiz quadrada.
# ======================================================================================================================
from format import text
n = int(input('Digite um {}número{} para saber seu valor em {}dobro{}, {}triplo{} e {}raiz quadrada{}: '.format(
    text['amarelo'], text['reset'], text['azul'], text['reset'], text['magenta'], text['reset'], text['ciano'],
    text['reset'])))
d = n * 2
t = n * 3
r = n ** (1/2)
print()
print('O {}dobro{} de {}{}{} vale {}{}{}.'.format(text['azul'], text['reset'], text['amarelo'], n, text['reset'],
                                                  text['azul'], d, text['reset']))
print('O {}triplo{} de {}{}{} vale {}{}{}.'.format(text['magenta'], text['reset'], text['amarelo'], n, text['reset'],
                                                   text['magenta'], t, text['reset']))
print('A {}raiz quadrada{} de {}{}{} vale {}{}{}.'.format(text['ciano'], text['reset'], text['amarelo'], n,
                                                          text['reset'], text['ciano'], r, text['reset']))
