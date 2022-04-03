# ==================================================== DESAFIO 045 =====================================================
# Crie um programa que faça o computador jogar Jokenpô com você.
# ======================================================================================================================
from random import randint
from time import sleep
print('------------ Vamos jogar Jokenpô? ------------')
print('Veja o número referente a cada opção do jogo:')
print()
itens = 'Pedra', 'Papel', 'Tesoura'
print('''00 -> {}
01 -> {}
02 -> {}'''.format(itens[0], itens[1], itens[2]))
computador = randint(0, 2)
jogador = int(input('Digite sua escolha: '))
print()
if jogador >= 3:
    print('Jogada inválida.')
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
        print('Empate!')
    elif jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 2 and computador == 0:
        print('O computador venceu.')
    elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
        print('O jogador venceu')
