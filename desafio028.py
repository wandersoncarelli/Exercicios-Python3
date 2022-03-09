# ==================================================== DESAFIO 028 =====================================================
# Crie um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# ======================================================================================================================
from random import randint
from time import sleep
from format import style, text
computador = randint(0, 5)
print('Vou pensar em um número {}entre 0 e 5{}. Tente adivinhar...'.format(style['sublinhado'], style['reset']))
jogador = int(input('Em que número eu pensei? '))
print('{}PROCESSANDO...{}'.format(text['magenta'], text['reset']))
sleep(1)
print()
if jogador == computador:
    print('{}Você acertou!{} Eu estava pensando no número {}{}{}.'.format(text['verde'], text['reset'], text['verde'],
                                                                          computador, text['reset']))
else:
    print('{}Você errou!{} Eu estava pensando no número {}{}{}, e não no número {}{}{}.'.
          format(text['vermelho'], text['reset'], text['vermelho'], computador, text['reset'], text['vermelho'],
                 jogador, text['reset']))
