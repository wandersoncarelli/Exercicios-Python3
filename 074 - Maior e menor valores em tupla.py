# ==================================================== DESAFIO 074 =====================================================
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.
# ======================================================================================================================
from random import sample
aleatorios = tuple(sample(range(100), 5))

print(*aleatorios, sep=' ')
print()
print(f'Maior número gerado: {max(aleatorios)}.')
print(f'Menor número gerado: {min(aleatorios)}.')
