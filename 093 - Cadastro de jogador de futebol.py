# ==================================================== DESAFIO 093 =====================================================
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
# ======================================================================================================================
jogos = dict()
jogos['Nome'] = input('Nome do jogador: ')
jogos['Jogos'] = int(input(f'Quantas partidas {jogos["Nome"]} jogou? '))
jogos['Gols'] = 0
print()
print(f'Digite a quantidade de gols que {jogos["Nome"]} fez em cada partida.')
for i in range(0, jogos['Jogos']):
    jogos[f'Partida {i + 1}'] = int(input(f'Partida {i + 1}: '))
    jogos['Gols'] += jogos[f'Partida {i + 1}']
print()
print(f'{jogos["Nome"]} jogou {jogos["Jogos"]} partidas e fez o total de {jogos["Gols"]} gols.')
for i in range(0, jogos['Jogos']):
    print(f'  - Na partida {i + 1}, fez {jogos[f"Partida {i+1}"]} gols.')
