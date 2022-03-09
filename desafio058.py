# ==================================================== DESAFIO 058 =====================================================
# Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
# ======================================================================================================================
from random import randint

tentativas = 0
computador = randint(0, 10)
print('Estou pensando em um número entre 0 e 10. Tente adivinhar...')

while True:
    jogador = int(input('Em que número eu pensei? '))
    tentativas += 1
    if jogador == computador:
        print()
        print(f'Você acertou! Eu estava pensando no número {computador}.')
        print(f'Você usou {tentativas} tentativas para acertar o número.')
        break
    else:
        print()
        print(f'Você errou. Tente novamente.')
