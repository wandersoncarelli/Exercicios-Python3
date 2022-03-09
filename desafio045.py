# ==================================================== DESAFIO 045 =====================================================
# Crie um programa que faça o computador jogar Jokenpô com você.
# ======================================================================================================================
from format import style, text
from random import randint
from time import sleep
print('{}{}------------ Vamos jogar Jokenpô? ------------{}'.format(style['negrito'], text['branco'], style['reset']))
print('Veja o número referente a cada opção do jogo:')
print()
itens = ('{}Pedra{}'.format(text['cinza'], text['reset']), '{}Papel{}'.format(text['branco'], text['reset']),
         '{}Tesoura{}'.format(text['ciano claro'], text['reset']))
print('''{}00 -> {}
{}01 -> {}
{}02 -> {}'''.format(text['cinza'], itens[0], text['branco'], itens[1], text['ciano claro'], itens[2]))
computador = randint(0, 2)
jogador = int(input('Digite sua escolha: '))
print()
if jogador >= 3:
    print('{}Jogada inválida.{}'.format(text['vermelho'], text['reset']))
else:
    print('JO')
    sleep(0.6)
    print('KEN')
    sleep(0.6)
    print('PO!!')
    print()
    print('Computador jogou {}.'.format(itens[computador]))
    print('Jogador jogou {}.'.format(itens[jogador]))
    if jogador == computador:
        print('{}Empate!{}'.format(text['azul'], text['reset']))
    elif jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 2 and computador == 0:
        print('{}O computador venceu.{}'.format(text['vermelho'], text['reset']))
    elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
        print('{}O jogador venceu{}'.format(text['verde'], text['reset']))
