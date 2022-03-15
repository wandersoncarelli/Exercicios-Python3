# ==================================================== DESAFIO 048 =====================================================
# Crie um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
# ======================================================================================================================
from format import text
print('Todos os números {}ímpares{} que são {}múltiplos de três{} no intervalo entre 1 e 500 são:'.
      format(text['magenta'], text['reset'], text['magenta'], text['reset']))
print()
soma = 0
for c in range(1, 50):
    if c % 2 == 1:
        if c % 3 == 0:
            print(c, end=', ')
            soma = soma + c
print()
print('A {}soma{} entre todos esses números dá {}{}{}.'.format(text['magenta'], text['reset'], text['magenta'], soma,
                                                               text['reset']))
