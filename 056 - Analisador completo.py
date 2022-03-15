# ==================================================== DESAFIO 056 =====================================================
# Crie um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres tem menos de 20 anos.
# ======================================================================================================================
soma_idade = mais_velho = nome_homem = menos_vinte = 0

print('Digite o nome, idade e sexo de 4 pessoas.\n')

for cont in range(0, 4):
    print(f'Pessoa {cont + 1}:')
    nome = input('Nome: ').title()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper()
    print()
    soma_idade += idade
    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_homem = nome
    if sexo == 'F' and idade < 20:
        menos_vinte += 1

media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade:.1f} anos.')
print(f'O nome do homem mais velho do grupo é {nome_homem} com {mais_velho} anos.')
print(f'{menos_vinte} mulheres tem menos de 20 anos.')
