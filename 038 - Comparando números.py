# ==================================================== DESAFIO 038 =====================================================
# Crie um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
# ======================================================================================================================
from format import text
print('Digite {}dois números{}, e eu vou fazer uma comparação, dizendo qual é o {}maior{} entre eles.'.
      format(text['magenta'], text['reset'], text['verde'], text['reset']))
n1 = int(input('{}Primeiro número{}: '.format(text['azul'], text['reset'])))
n2 = int(input('{}Segundo número{}: '.format(text['ciano'], text['reset'])))
print()
if n1 > n2:
    print('O {}primeiro{} número é maior, sendo o {}número {}{}.'.format(text['azul'], text['reset'], text['azul'], n1,
                                                                         text['reset']))
elif n2 > n1:
    print('O {}segundo{} número é maior, sendo o {}número {}{}.'.format(text['ciano'], text['reset'], text['ciano'], n2,
                                                                        text['reset']))
else:
    print('Os {}dois números{} são {}iguais{}.'.format(text['magenta'], text['reset'], text['magenta'], text['reset']))
