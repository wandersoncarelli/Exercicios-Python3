# ==================================================== DESAFIO 046 =====================================================
# Crie um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 0 segundo entre eles.
# ======================================================================================================================
from format import style, text
from emoji import emojize
from time import sleep
from random import shuffle
print('{}Contagem regressiva{} para o estouro de {}fogos de artifício{}:'.format(style['sublinhado'], style['reset'],
                                                                                 text['magenta claro'], text['reset']))
fogos0 = emojize('{}:fireworks:'.format(text['vermelho']))
fogos1 = emojize('{}:fireworks:'.format(text['verde']))
fogos2 = emojize('{}:fireworks:'.format(text['amarelo claro']))
fogos3 = emojize('{}:fireworks:'.format(text['azul']))
fogos4 = emojize('{}:fireworks:'.format(text['magenta claro']))
fogos5 = emojize('{}:fireworks:'.format(text['ciano claro']))
fogos = [fogos0, fogos1, fogos2, fogos3, fogos4, fogos5]
shuffle(fogos)
print()
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print()
print(fogos[0], fogos[1], fogos[2], fogos[3], fogos[4], fogos[5])
