# ==================================================== DESAFIO 032 =====================================================
# Crie um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
# ======================================================================================================================
from datetime import date
print('Me diga um ano e eu vou dizer se ele é BISSEXTO ou não. Para analisar o ano atual, coloque 0.')
ano = int(input('Ano: '))
print()
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))
