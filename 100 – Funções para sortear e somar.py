# ==================================================== DESAFIO 100 =====================================================
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.
# ======================================================================================================================
import random

numeros= []

def sorteia():
    print('Sorteando 5 números...')
    for i in range(0, 5):
        num = random.randint(0, 10)
        print(num, end=' ')
        numeros.append(num)
    print('FIM!')


def somaPar():
    soma = 0
    for i in range(0, len(numeros)):
        if numeros[i] % 2 == 0:
            soma += numeros[i]
    print(f'Somando os valores pares de {numeros}, temos o total de {soma}.')

sorteia()
somaPar()
