# ==================================================== DESAFIO 087 =====================================================
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
# ======================================================================================================================
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
soma_par = soma_coluna = 0

for c in range(0, 3):
    for l in range(0, 3):
        matriz[c][l] = int(input(f'[{c}][{l}] = '))
print()

for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
        if matriz[c][l] % 2 == 0:
            soma_par += matriz[c][l]
    print()

for i in range(0, 3):
    soma_coluna += matriz[i][2]
print()

print(f'Soma dos pares: {soma_par}.')
print(f'Soma da terceira coluna: {soma_coluna}.')
print(f'Maior valor da segunda linha: {max(matriz[1])}.')
