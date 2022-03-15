# ==================================================== DESAFIO 095 =====================================================
# Aprimore o desafio 93 para que ele funcione com vários jogos, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.
# ======================================================================================================================
jogos = {}
dados = []
opcao = ''

while opcao != 'N':
    jogos['Nome'] = input('Nome do jogador: ')
    jogos['Jogos'] = int(input(f'Quantas partidas {jogos["Nome"]} jogou? '))
    jogos['Gols'] = 0
    print()
    print(f'Digite a quantidade de gols que {jogos["Nome"]} fez em cada partida.')
    for i in range(0, jogos['Jogos']):
        jogos[f'Partida {i + 1}'] = int(input(f'Partida {i + 1}: '))
        jogos['Gols'] += jogos[f'Partida {i + 1}']
    print()
    while opcao != 'N' or opcao != 'S':
        opcao = input('Deseja cadastrar mais jogadores? (S/N): ').upper()
        if opcao == 'S' or opcao == 'N':
            break
        else:
            print('Opção inválida.\n')
    dados.append(jogos)
    jogos = {}
    print()

print(29 * "=")
print(f'{"TABELA DE JOGADORES":^30}')
print(29 * "=")
print(f'{"Nº":<4}{"NOME":<20}{"GOLS":>5}')
print(29 * "-")
for i in range(0, len(dados)):
    print(f'{i:<4}{dados[i]["Nome"]:<20}{dados[i]["Gols"]:>5}')
print()

print('Para ver o aproveitamento, digite o número do jogador.')
while True:
    jogador = int(input('Número do jogador (999 para sair): '))
    if jogador == 999:
        break
    elif jogador < 0 or jogador > len(dados):
        print('Número inválido.')
    else:
        print()
        print(f'{dados[jogador]["Nome"]} jogou {dados[jogador]["Jogos"]} partidas e fez o total de '
              f'{dados[jogador]["Gols"]} gols.')
        for i in range(0, dados[jogador]['Jogos']):
            print(f'  - Na partida {i + 1}, fez {dados[jogador][f"Partida {i + 1}"]} gols.')
    print()
