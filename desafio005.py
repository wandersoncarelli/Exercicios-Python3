# ==================================================== DESAFIO 005 =====================================================
# Crie um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
# ======================================================================================================================
from format import text
n = int(input('Digite um {}número{} para saber seu {}sucessor{} e {}antecessor{}: '.format(
    text['azul'], text['reset'], text['verde'], text['reset'], text['vermelho'], text['reset'])))
s = n + 1
a = n - 1
print()
print('O {}sucessor{} de {}{}{} é {}{}{}, e seu {}antecessor{} é {}{}{}.'.format(
    text['verde'], text['reset'], text['azul'], n, text['reset'], text['verde'], s, text['reset'], text['vermelho'],
    text['reset'], text['vermelho'], a, text['reset']))
