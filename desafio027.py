# ==================================================== DESAFIO 027 =====================================================
# Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza
# ======================================================================================================================
from format import text
n = input('Me diga seu {}nome completo{}, e eu vou dizer qual é seu {}primeiro{} e {}último{} nome:\n'.
          format(text['magenta'], text['reset'], text['verde'], text['reset'], text['azul'], text['reset'])).strip()
nome = n.split()
print()
print('Seu {}primeiro{} nome é {}{}{}.'.format(text['verde'], text['reset'], text['verde'], nome[0], text['reset']))
print('Seu {}último{} nome é {}{}{}.'.format(text['azul'], text['reset'], text['azul'], nome[len(nome)-1],
                                             text['reset']))
