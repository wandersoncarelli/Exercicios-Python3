# ==================================================== DESAFIO 103 =====================================================
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.
# ======================================================================================================================

def ficha(nome='', gol=''):
    if nome == '':
        nome = '<desconhecido>'

    if gol == '':
        gol = 0

    return nome, gol

jogador, gols = ficha(input('Nome do jogador: '), input('Número de gols: '))
print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')