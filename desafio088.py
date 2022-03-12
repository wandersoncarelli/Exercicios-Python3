# ==================================================== DESAFIO 088 =====================================================
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
# ======================================================================================================================
from random import sample
jogos = []
n = int(input('Quantos jogos serão gerados? '))

print()
for i in range(0, n):
    jogos.append(sample(range(60), 6))
    print(f'{i + 1}º jogo = ', end='')
    print(sorted(jogos[i]))
