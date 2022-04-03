# ==================================================== DESAFIO 030 =====================================================
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
# ======================================================================================================================
print('Me diga um número, e eu vou dizer se ele é PAR ou ÍMPAR.')
numero = int(input('Número: '))
print()
if numero % 2 == 0:
    print('O número {} é PAR.'.format(numero))
else:
    print('O número {} é ÍMPAR.'.format(numero))
