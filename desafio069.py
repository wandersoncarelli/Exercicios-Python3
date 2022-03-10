# ==================================================== DESAFIO 069 =====================================================
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
# ======================================================================================================================
mais_dezoito = homens = mulheres_vinte = 0
sexo = opcao = ''

print('Para cadastrar pessoas, digite a idade e o sexo delas.\n')

while opcao != 'N':
    idade = int(input('Idade: '))
    if idade > 18:
        mais_dezoito += 1
    while sexo != 'M' or sexo != 'F':
        sexo = input('Sexo (M/F): ').upper()
        if sexo == 'M':
            homens += 1
            break
        elif sexo == 'F':
            if idade < 20:
                mulheres_vinte += 1
            break
        else:
            print('Opção inválida.\n')
    while opcao != 'S' or opcao != 'N':
        opcao = input('Deseja cadastrar mais pessoas? (S/N): ').upper()
        print()
        if opcao == 'S' or opcao == 'N':
            break
        else:
            print('Opção inválida.\n')

print('Você saiu do programa.\n')
print(f'{mais_dezoito} pessoas que foram cadastradas, tem mais de 18 anos.')
print(f'{homens} pessoas cadastradas são homens.')
print(f'{mulheres_vinte} pessoas cadastradas são mulheres com menos de 20 anos.')
