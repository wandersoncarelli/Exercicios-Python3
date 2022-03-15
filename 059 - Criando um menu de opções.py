# ==================================================== DESAFIO 059 =====================================================
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
# ======================================================================================================================
menu = '\nMENU:\n' \
       '[1] SOMAR\n' \
       '[2] MULTIPLICAR\n' \
       '[3] MAIOR\n' \
       '[4] NOVOS NÚMEROS\n' \
       '[5] SAIR DO PROGRAMA\n'

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print(menu)
while True:
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print(f'A soma de {num1} + {num2} é igual a {num1 + num2}.')
        print(menu)
    elif opcao == 2:
        print(f'A multiplicação de {num1} x {num2} é igual a {num1 * num2}.')
        print(menu)
    elif opcao == 3:
        if num1 > num2:
            print(f'O maior número digitado é {num1}.')
            print(menu)
        else:
            print(f'O maior número digitado é {num2}.')
            print(menu)
    elif opcao == 4:
        print()
        num1 = int(input('Digite um novo número: '))
        num2 = int(input('Digite outro número: '))
        print(menu)
    elif opcao == 5:
        print('Você saiu do programa.')
        break
    else:
        print('\nOpção inválida.')
