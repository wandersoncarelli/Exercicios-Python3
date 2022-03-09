# ==================================================== DESAFIO 024 =====================================================
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
# ======================================================================================================================
from format import style, text
print('Me diga em qual cidade você nasceu e eu vou dizer se o nome dela {}começa ou não{} com o nome {}"Santo"{}.'.
      format(style['sublinhado'], style['reset'], style['negrito'], style['reset']))
cid = input('Em que cidade você nasceu?\n').strip()
print()
if cid[:5].lower() == 'santo':
    print('O nome da cidade em que você nasceu {}começa{} com Santo.'.format(text['verde'], text['reset']))
else:
    print('O nome da cidade em que você nasceu {}não começa{} com Santo.'.format(text['vermelho'], text['reset']))
