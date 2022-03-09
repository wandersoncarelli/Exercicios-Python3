# ==================================================== DESAFIO 013 =====================================================
# Crie um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# ======================================================================================================================
from format import text
print('Digite o {}salário atual{} de um funcionário para calcular seu novo salário com {}15% de aumento.{}'.format(
    text['azul'], text['reset'], text['verde'], text['reset']))
print()
s = float(input('Qual é o {}salário atual{} do funcionário?\nR$'.format(text['azul'], text['reset'])))
ns = s + (s * 15 / 100)
print()
print('Um funcionário que recebe {}R${:.2f}{}, com {}15% de aumento{}, passará a receber {}R${:.2f}{}.'.format(
    text['azul'], s, text['reset'], text['verde'], text['reset'], text['verde'], ns, text['reset']))
