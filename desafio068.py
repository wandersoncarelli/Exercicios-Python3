# ==================================================== DESAFIO 068 =====================================================
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
# ======================================================================================================================
from random import randint

vitorias = 0
print('Vamos jogar PAR ou ÍMPAR.')

while True:
    while True:
        print()
        escolha_jogador = input('Você escolhe Par ou Ímpar? (P/I): ').upper()
        if escolha_jogador == 'P':
            escolha_computador = 'I'
            break
        elif escolha_jogador == 'I':
            escolha_computador = 'P'
            break
        else:
            print('Opção inválida.')

    while True:
        num_jogador = int(input('Digite um número entre 1 a 10: '))
        if 1 <= num_jogador <= 10:
            print()
            break
        else:
            print('Opção inválida.')
            print()

    num_computador = randint(1, 10)

    print(f'Você escolheu o número {num_jogador} e o computador {num_computador}.')
    if (num_jogador + num_computador) % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'A soma de {num_jogador} e {num_computador} é igual a {num_jogador + num_computador}, e é um número '
          f'{resultado}.')
    if escolha_jogador == 'P' and resultado == 'PAR' or escolha_jogador == 'I' and resultado == 'ÍMPAR':
        print('Você venceu!\n')
        print('Vamos jogar novamente...')
        vitorias += 1
    else:
        print('Você perdeu!\n')
        break
print(f'Nós jogamos {vitorias + 1} vezes e você venceu {vitorias} vezes.')
