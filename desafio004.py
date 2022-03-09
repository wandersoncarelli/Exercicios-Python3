# ==================================================== DESAFIO 004 =====================================================
# Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.
# ======================================================================================================================
from format import text
a = input('Digite alguma coisa e saiba algumas informações sobre o que você digitou:\n')
print()
print('O tipo primitivo do que foi digitado é{}'.format(text['magenta']), type(a))
print('\033[mÉ alfabético?', ('{}Sim{}'.format(text['verde'], text['reset'])) if a.isalpha() else (
    '{}Não{}'.format(text['vermelho'], text['reset'])))
print('É numérico?', ('{}Sim{}'.format(text['verde'], text['reset'])) if a.isnumeric() else (
    '{}Não{}'.format(text['vermelho'], text['reset'])))
print('É alfanumérico?', ('{}Sim{}'.format(text['verde'], text['reset'])) if a.isalnum() else (
    '{}Não{}'.format(text['vermelho'], text['reset'])))
print('É decimal?', ('{}Sim{}'.format(text['verde'], text['reset'])) if a.isdecimal() else (
    '{}Não{}'.format(text['vermelho'], text['reset'])))
print('É um dígito?', ('{}Sim{}'.format(text['verde'], text['reset'])) if a.isdigit() else (
    '{}Não{}'.format(text['vermelho'], text['reset'])))
print('Está em letras minúsculas?', ('{}Sim{}'.format(text['verde'], text['reset'])) if a.islower() else (
    '{}Não{}'.format(text['vermelho'], text['reset'])))
print('Está em letras maiúsculas?', ('{}Sim{}'.format(text['verde'], text['reset'])) if a.isupper() else (
    '{}Não{}'.format(text['vermelho'], text['reset'])))
print('É um espaço vazio?', ('{}Sim{}'.format(text['verde'], text['reset'])) if a.isspace() else (
    '{}Não{}'.format(text['vermelho'], text['reset'])))
print('É um título?', ('{}Sim{}'.format(text['verde'], text['reset'])) if a.istitle() else (
    '{}Não{}'.format(text['vermelho'], text['reset'])))
