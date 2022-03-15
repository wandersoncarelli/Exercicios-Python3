# ==================================================== DESAFIO 091 =====================================================
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# ======================================================================================================================
from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
for i in range(0, 4):
    jogadores[input(f'Jogador {i + 1}: ')] = randint(1, 6)

print()
for k, v in jogadores.items():
    print(f'{k} tirou {v}...')
    sleep(1.5)

print()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
posicao = 1

print(10 * '=', 'RANKING', 10 * '=')
for i in range(0, 4):
    if i == 0:
        print(f'{posicao}º - {ranking[i][0]} com {ranking[i][1]} pontos.')
    elif ranking[i][1] == ranking[i - 1][1]:
        print(f'     {ranking[i][0]} com {ranking[i][1]} pontos.')
    else:
        posicao += 1
        print(f'{posicao}º - {ranking[i][0]} com {ranking[i][1]} pontos.')