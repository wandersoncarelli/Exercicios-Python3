# ==================================================== DESAFIO 074 =====================================================
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.
# ======================================================================================================================
from random import randint
aleatorios = []
maior = menor = 0

for cont in range(0, 5):
    num = randint(0, 100)
    aleatorios.append(num)
    if menor == maior or num < menor:
        menor = num
    if num > maior:
        maior = num
print(f'Foram gerados 5 números aleatórios entre 0 e 100, e foram eles:')
print(*aleatorios, sep=', ', end='.')
print('\n')
print(f'O menor número gerado foi {menor}.')
print(f'O maior número gerado foi {maior}.')
