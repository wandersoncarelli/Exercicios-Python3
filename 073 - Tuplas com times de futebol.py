# ==================================================== DESAFIO 073 =====================================================
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
# ======================================================================================================================
times = ('Atlético MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América',
         'Atlético GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico PR', 'Cuiabá', 'Juventude',
         'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print(60 * '=')
print(16 * ' ', 'CAMPEONATO BRASILEIRO 2021')
print(60 * '=')
print()

print('Os 5 primeiros colocados da tabela são:')
for cont in range(0, 5):
    print(times[cont], end='')
    print(', ' if cont < 4 else '.', end='')
print('\n')

print('Os 4 últimos colocados da tabela são: ')
for cont in range(len(times) - 4, len(times)):
    print(times[cont], end='')
    print(', ' if cont < len(times) - 1 else '.', end='')
print('\n')

print('Os times da tabela, classificados por ordem alfabética, são:')
print(*sorted(times), sep=', ', end='.')  # Colocar um * no inicio faz com que a lista seja impressa sem os colchetes.
print('\n')

print(f'O time da Chapecoense está em {times.index("Chapecoense") + 1}º lugar na classificação.')
