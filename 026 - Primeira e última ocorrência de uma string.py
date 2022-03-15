# ==================================================== DESAFIO 026 =====================================================
# Crie um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.
# ======================================================================================================================
from format import style, text
print('Digite uma {}frase qualquer{} e eu direi {}quantas{} letras {}"A"{} contém na frase e em qual posição ela '
      'aparece pela {}primeira{} e {}última{} vez.'.format(style['sublinhado'], style['reset'], text['verde'],
                                                           text['reset'], style['negrito'], style['reset'],
                                                           text['azul'], text['reset'], text['ciano'], text['reset']))
frase = input('Frase:\n').strip().lower()
print()
print('A letra A aparece {}{} vezes{} na frase.'.format(text['verde'], frase.count('a'), text['reset']))
print('A {}primeira{} letra A apareceu na {}{}ª{} posição.'.format(text['azul'], text['reset'], text['azul'],
                                                                   frase.find('a')+1, text['reset']))
print('A {}última{} letra A apareceu na {}{}ª{} posição.'.format(text['ciano'], text['reset'], text['ciano'],
                                                                 frase.rfind('a')+1, text['reset']))
