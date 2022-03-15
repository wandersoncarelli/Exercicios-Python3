# ==================================================== DESAFIO 084 =====================================================
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
# ======================================================================================================================
pessoas = []
temp = []
opcao = ''
maior = menor = 0

while opcao != 'N':
    temp.append(input('Nome: ').upper())
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    while opcao != 'N' or opcao != 'S':
        opcao = input('Deseja continuar? (S/N): ').upper()
        if opcao == 'N' or opcao == 'S':
            break
        else:
            print('Opção inválida.\n')
    print()

print(f'Foram cadastradas {(len(pessoas) / 2):.0f} pessoas.')
print(f'O maior peso é de {maior:.2f}kg. Peso de: ', end='')
for i in pessoas:
    if i[1] == maior:
        print(f'[{i[0]}]', end=' ')
print()
print(f'O menor peso é de {menor:.2f}kg. Peso de: ', end='')
for i in pessoas:
    if i[1] == menor:
        print(f'[{i[0]}]', end=' ')
