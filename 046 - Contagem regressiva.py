# ==================================================== DESAFIO 046 =====================================================
# Crie um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 0 segundo entre eles.
# ======================================================================================================================
from emoji import emojize
from time import sleep
print('Contagem regressiva para o estouro de fogos de artifício:')
fogos1 = emojize(':fireworks:')
fogos2 = emojize(':fireworks:')
fogos3 = emojize(':fireworks:')
fogos = [fogos1, fogos2, fogos3]
print()
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print()
print(fogos[0], fogos[1], fogos[2])
