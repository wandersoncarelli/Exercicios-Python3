# ==================================================== DESAFIO 063 =====================================================
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
# ======================================================================================================================
qtd = int(input('Digite a quantidade de elementos para exibir da Sequência de Fibonacci: '))
num1 = 0
num2 = 1
cont = 3

print(f'{num1} - {num2}', end='')
while cont <= qtd:
    soma = num1 + num2
    print(f' - {soma}', end='')
    num1 = num2
    num2 = soma
    cont += 1
print(' - FIM')
