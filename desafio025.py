# ==================================================== DESAFIO 025 =====================================================
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
# ======================================================================================================================
from format import style, text
print('Me diga seu nome completo e eu vou dizer {}se{} você tem {}"Silva"{} no nome.'.
      format(style['sublinhado'], style['reset'], style['negrito'], style['reset']))
nome = input('Qual é o seu nome completo?\n').strip()
print()
if 'silva' in nome.lower():
    print('Você {}tem{} Silva no nome.'.format(text['verde'], text['reset']))
else:
    print('Você {}não tem{} Silva no nome.'.format(text['vermelho'], text['reset']))
