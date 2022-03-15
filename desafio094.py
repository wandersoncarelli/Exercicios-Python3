# ==================================================== DESAFIO 094 =====================================================
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
# ======================================================================================================================
cadastro = {}
dados = []
opcao = ''
soma_idade = 0

while opcao != 'N':
    cadastro['Nome'] = input('Nome: ')
    cadastro['Sexo'] = input('Sexo (M/F): ').upper()
    while cadastro['Sexo'] != 'M' or cadastro['Sexo'] != 'F':
        if cadastro['Sexo'] == 'M' or cadastro['Sexo'] == 'F':
            break
        else:
            print('Opção inválida.\n')
            cadastro['Sexo'] = input('Sexo (M/F): ').upper()
    cadastro['Idade'] = int(input('Idade: '))
    soma_idade += cadastro['Idade']
    while opcao != 'N' or opcao != 'S':
        opcao = input('Deseja continuar? (S/N): ').upper()
        if opcao == 'S' or opcao == 'N':
            break
        else:
            print('Opção inválida.')
            print()
    dados.append(cadastro)
    cadastro = {}
    print()

media = int(soma_idade / len(dados))
print(f'Pessoas cadastradas: {len(dados)}.')
print(f'Média de idade: {media}.')
print('Mulheres cadastradas: ', end='')
for i in range(0, len(dados)):
    if dados[i]['Sexo'] == 'F':
        print(f'[{dados[i]["Nome"]}] ', end='')
print()
print('Pessoas com idade acima da média: ', end='')
for i in range(0, len(dados)):
    if dados[i]['Idade'] > media:
        print(f'[{dados[i]["Nome"]}] ', end='')
print()
