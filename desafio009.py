# ==================================================== DESAFIO 009 =====================================================
# Crie um programa que leia um número inteiro e mostre na tela a sua tabuada.
# ======================================================================================================================
from format import text
n = int(input('Digite um {}número{} para ver sua {}tabuada{}: '.format(text['azul'], text['reset'], text['magenta'],
                                                                       text['reset'])))
print()
print('='*15)
print('{}{}{} x {}{}{} = {}{}{}'.format(text['azul'], n, text['reset'], text['magenta'], 1, text['reset'],
                                        text['verde'], n*1, text['reset']))
print('{}{}{} x {}{}{} = {}{}{}'.format(text['azul'], n, text['reset'], text['magenta'], 2, text['reset'],
                                        text['verde'], n*2, text['reset']))
print('{}{}{} x {}{}{} = {}{}{}'.format(text['azul'], n, text['reset'], text['magenta'], 3, text['reset'],
                                        text['verde'], n*3, text['reset']))
print('{}{}{} x {}{}{} = {}{}{}'.format(text['azul'], n, text['reset'], text['magenta'], 4, text['reset'],
                                        text['verde'], n*4, text['reset']))
print('{}{}{} x {}{}{} = {}{}{}'.format(text['azul'], n, text['reset'], text['magenta'], 5, text['reset'],
                                        text['verde'], n*5, text['reset']))
print('{}{}{} x {}{}{} = {}{}{}'.format(text['azul'], n, text['reset'], text['magenta'], 6, text['reset'],
                                        text['verde'], n*6, text['reset']))
print('{}{}{} x {}{}{} = {}{}{}'.format(text['azul'], n, text['reset'], text['magenta'], 7, text['reset'],
                                        text['verde'], n*7, text['reset']))
print('{}{}{} x {}{}{} = {}{}{}'.format(text['azul'], n, text['reset'], text['magenta'], 8, text['reset'],
                                        text['verde'], n*8, text['reset']))
print('{}{}{} x {}{}{} = {}{}{}'.format(text['azul'], n, text['reset'], text['magenta'], 9, text['reset'],
                                        text['verde'], n*9, text['reset']))
print('{}{}{} x {}{}{} = {}{}{}'.format(text['azul'], n, text['reset'], text['magenta'], 10, text['reset'],
                                        text['verde'], n*10, text['reset']))
print('='*15)
