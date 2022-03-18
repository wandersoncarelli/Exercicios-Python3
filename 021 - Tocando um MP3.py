# ==================================================== DESAFIO 021 =====================================================
# Crie um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# ======================================================================================================================
from time import sleep
import pygame
# INICIAR O MIXER PYGAME
# pygame.mixer.init()
# INICIAR O PYGAME
# pygame.init()
print('Veja a lista de músicas e escolha uma para tocar:')
print()
print('01 -> Música 01')
print('02 -> Música 02')
print('03 -> Música 03')
m1 = '021 - Musica 01.mp3'
m2 = '021 - Musica 02.mp3'
m3 = '021 - Musica 03.mp3'
print()
tocar = int(input('Digite o número referente à música escolhida: '))
if tocar <= 0 or tocar >= 4:
    print('Opção inválida.')
else:
    print('Iniciando...')
    pygame.mixer.init()
    pygame.init()
    if tocar == 1:
        pygame.mixer.music.load(m1)
        pygame.mixer.music.play()
        sleep(1.5)
        print('Tocando: Música 01')
    if tocar == 2:
        pygame.mixer.music.load(m2)
        pygame.mixer.music.play()
        sleep(0.5)
        print('Tocando: Música 02')
    if tocar == 3:
        pygame.mixer.music.load(m3)
        pygame.mixer.music.play()
        sleep(1)
        print('Tocando: Música 03')
    pygame.event.wait()
