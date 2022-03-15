# ==================================================== DESAFIO 021 =====================================================
# Crie um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# ======================================================================================================================
from format import style, text
from time import sleep
import pygame
# INICIAR O MIXER PYGAME
# pygame.mixer.init()
# INICIAR O PYGAME
# pygame.init()
print('{}Veja a lista de músicas e escolha uma para tocar:{}'.format(text['branco'], text['reset']))
print()
print('{}01 -> Oasis - Stop Crying Your Heart Out{}'.format(text['azul'], text['reset']))
print('{}02 -> Johnny Cash - Hurt{}'.format(text['azul claro'], text['reset']))
print('{}03 -> KALEO - Way Down We Go{}'.format(text['ciano'], text['reset']))
m1 = '021 - Musica 01.mp3'
m2 = '021 - Musica 02.mp3'
m3 = '021 - Musica 03.mp3'
print()
tocar = int(input('Digite o {}número{} referente à música escolhida: '.format(style['sublinhado'], style['reset'])))
if tocar == 1:
    print('{}Iniciando...{}'.format(text['magenta'], text['reset']))
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load(m1)
    pygame.mixer.music.play()
    sleep(1.5)
    print('Tocando agora: {}Oasis - Stop Crying Your Heart Out{}'.format(text['azul'], text['reset']))
    pygame.event.wait()
if tocar == 2:
    print('{}Iniciando...{}'.format(text['magenta'], text['reset']))
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load(m2)
    pygame.mixer.music.play()
    sleep(0.5)
    print('Tocando agora: {}Johnny Cash - Hurt{}'.format(text['azul claro'], text['reset']))
    pygame.event.wait()
if tocar == 3:
    print('{}Iniciando...{}'.format(text['magenta'], text['reset']))
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load(m3)
    pygame.mixer.music.play()
    sleep(1)
    print('Tocando agora: {}KALEO - Way Down We Go{}'.format(text['ciano'], text['reset']))
    pygame.event.wait()
if tocar >= 4:
    print('{}{}Opção inválida.'.format(style['negrito'], text['branco']))
