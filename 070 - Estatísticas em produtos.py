# ==================================================== DESAFIO 070 =====================================================
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
# ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
# ======================================================================================================================
total = mais_mil = preco_barato = 0
opcao = mais_barato = ''
print('Digite o nome e o preço dos produtos para calcular sua compra.')

while opcao != 'N':
    print()
    nome_produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    if preco_barato == 0 or preco < preco_barato:
        mais_barato = nome_produto
        preco_barato = preco
    total += preco
    if preco > 1000:
        mais_mil += 1
    while opcao != 'S' or opcao != 'N':
        opcao = input('Deseja continuar? (S/N): ').upper()
        if opcao == 'S' or opcao == 'N':
            break
        else:
            print('Opção inválida.\n')
print()
print('Você saiu do programa.\n')
print(f'O valor total gasto na compra foi de R${total:.2f}.')
print(f'{mais_mil} produtos custam mais de R$1000.')
print(f'O produto mais barato é {mais_barato} e custa R${preco_barato:.2f}.')
