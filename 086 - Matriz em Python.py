# ==================================================== DESAFIO 086 =====================================================
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a
# matriz na tela, com a formatação correta.
# ======================================================================================================================
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for c in range(0, 3):
    for l in range(0, 3):
        matriz[c][l] = int(input(f'[{c}][{l}] = '))

for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()
