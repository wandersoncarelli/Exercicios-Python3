# ==================================================== DESAFIO 099 =====================================================
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
# ======================================================================================================================
import time

def maior(*num):
    print('=' * 40)
    print('Analisando os valores informados...')
    if len(num) > 0:
        maior_num = num[0]
    else:
        maior_num = 0

    for i in range(0, len(num)):
        if num[i] > maior_num:
            maior_num = num[i]
        print(num[i], end=' ')
        time.sleep(.2)

    print(f'\nForam informados {len(num)} valores.')
    print(f'O maior valor informado foi {maior_num}.')
    print()


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()