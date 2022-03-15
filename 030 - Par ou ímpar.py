# ==================================================== DESAFIO 030 =====================================================
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
# ======================================================================================================================
from format import style, text
print('Me diga um {}número{}, e eu vou dizer se ele é {}PAR{} ou {}ÍMPAR{}.'.format(style['sublinhado'], style['reset'],
                                                                                    text['azul'], text['reset'],
                                                                                    text['ciano'], text['reset']))
numero = int(input('Número: '))
resto = numero % 2
print()
if resto == 0:
    print('O número {}{}{} é {}PAR{}.'.format(text['azul'], numero, text['reset'], text['azul'], text['reset']))
else:
    print('O número {}{}{} é {}ÍMPAR{}.'.format(text['ciano'], numero, text['reset'], text['ciano'], text['reset']))
