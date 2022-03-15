# ==================================================== DESAFIO 023 =====================================================
# Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1
# ======================================================================================================================
from format import style, text
from time import sleep
print('Digite um {}número{} para analisarmos qual é o valor da {}unidade{}, {}dezena{}, {}centena{} e {}milhar{}.'.
      format(style['sublinhado'], style['reset'], text['azul'], text['reset'], text['verde'], text['reset'],
             text['ciano'], text['reset'], text['amarelo'], text['reset']))
num = int(input('{}Número: {}'.format(style['negrito'], style['reset'])))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print()
print('{}Analisando o número {}...{}'.format(text['magenta'], num, text['reset']))
sleep(1.5)
print('{}Unidade{}: {}{}{}'.format(text['azul'], text['reset'], text['azul'], u, text['reset']))
print('{}Dezena{}: {}{}{}'.format(text['verde'], text['reset'], text['verde'], d, text['reset']))
print('{}Centena{}: {}{}{}'.format(text['ciano'], text['reset'], text['ciano'], c, text['reset']))
print('{}Milhar{}: {}{}{}'.format(text['amarelo'], text['reset'], text['amarelo'], m, text['reset']))
