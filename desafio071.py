# ==================================================== DESAFIO 071 =====================================================
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere
# que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
# ======================================================================================================================
print(60 * '=')
print(21 * ' ', 'CAIXA ELETRÔNICO')
print(60 * '=')
print()
cedulas = [50, 20, 10, 1]

valor = int(input('Digite o valor que deseja sacar: R$'))
print()
print('Serão entregues: ')
for cont in range(len(cedulas)):
    if valor >= cedulas[cont]:
        print(f'{int(valor / cedulas[cont])} cédulas de R${cedulas[cont]}.')
        valor = valor % cedulas[cont]
