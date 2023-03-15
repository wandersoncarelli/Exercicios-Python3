# ==================================================== DESAFIO 096 =====================================================
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
# ======================================================================================================================

def area(l, c):
    tamanho = l * c
    print(f'A área do terreno {l}x{c} é de {tamanho:.1f}m².')

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)
