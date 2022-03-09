# ==================================================== DESAFIO 007 =====================================================
# Crie um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
# ======================================================================================================================
from format import style, text
print('Digite o valor de {}duas notas{} para calcular e saber sua {}média{}.'.format(
    style['sublinhado'], style['reset'], text['verde'], text['reset']))
print()
n1 = float(input('{}Primeira nota{}: '.format(text['azul'], text['reset'])))
n2 = float(input('{}Segunda nota{}: '.format(text['magenta'], text['reset'])))
m = (n1 + n2) / 2
print()
print('A {}média{} entre {}{:.1f}{} e {}{:.1f}{} é igual a {}{:.1f}{}.'.format(
    text['verde'], text['reset'], text['azul'], n1, text['reset'], text['magenta'], n2, text['reset'], text['verde'], m,
    text['reset']))
