# ==================================================== DESAFIO 051 =====================================================
# Crie um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 10
# primeiros termos dessa progressão.
# ======================================================================================================================
from format import text
print('Digite o {}Termo{} e a {}Razão{} de uma Progressão Aritmética, e eu vou mostrar os {}10 primeiros termos{} dessa'
      ' progressão.'.format(text['azul'], text['reset'], text['ciano'], text['reset'], text['magenta'], text['reset']))
print()
termo = int(input('{}Termo: '.format(text['azul'])))
razao = int(input('{}Razão:{} '.format(text['ciano'], text['reset'])))
print()
print('Os {}10 primeiros termos{} da PA são:'.format(text['magenta'], text['reset']))
soma = termo
for c in range(1, 11):
    soma = termo
    termo = termo + razao
    print(soma, end=', ')
print()
