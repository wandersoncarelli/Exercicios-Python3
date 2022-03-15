# ==================================================== DESAFIO 054 =====================================================
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
# ======================================================================================================================
from datetime import date
ano_atual = date.today().year
maior = menor = 0

print('Digite o ano de nascimento de 7 pessoas para saber quantas são maiores de idade e quantas são menores.\n')
for cont in range(0, 7):
    ano = int(input(f'Pessoa {cont + 1}: '))
    if ano_atual - ano >= 18:
        maior += 1
    else:
        menor += 1

print(f'\nNo total, {maior} pessoas são maiores de idade e {menor} pessoas são menores de idade.')
