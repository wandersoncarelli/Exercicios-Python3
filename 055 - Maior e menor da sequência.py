# ==================================================== DESAFIO 055 =====================================================
# Crie um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
# ======================================================================================================================
print('Digite o peso de 5 pessoas.\n')
peso = maior = menor = 0

for cont in range(0, 5):
    peso = float(input(f'Peso da pessoa {cont + 1}: '))
    if peso > maior:
        maior = peso
    if menor == 0 or peso < menor:
        menor = peso

print(f'\nO maior peso lido foi de {maior:.2f}kg, e o menor peso lido foi de {menor:.2f}kg.')
