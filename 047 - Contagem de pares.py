# ==================================================== DESAFIO 047 =====================================================
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
# ======================================================================================================================
from format import text
print('Todos os números {}pares{} que estão no intervalo entre {}1 e 50{} são:'.format(text['magenta'], text['reset'],
                                                                                       text['magenta'], text['reset']))
print()
pares = 0
for c in range(1, 51):
    if c % 2 == 0:
        pares = pares + 1
        print(c, end=', ')
print()
print('O total de números {}pares{} são de {}{}{} números.'.format(text['magenta'], text['reset'], text['magenta'],
                                                                   pares, text['reset']))
