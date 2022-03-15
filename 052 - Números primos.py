# ==================================================== DESAFIO 052 =====================================================
# Crie um programa que leia um número inteiro e diga se ele é ou não um número primo.
# ======================================================================================================================
num = int(input('Digite um número: '))
total = 0
for cont in range(1, num + 1):
    if num % cont == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{cont} ', end='')
print(f'\n\033[mO número {num} foi dividido {total} vezes.')
if total == 2:
    print('Então ele é um número primo!')
else:
    print('Então ele não é um número primo!')
