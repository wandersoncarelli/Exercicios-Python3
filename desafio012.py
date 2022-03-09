# ==================================================== DESAFIO 012 =====================================================
# Crie um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
# ======================================================================================================================
from format import text
print('Digite o {}preço{} de um produto para calcular seu valor com {}5% de desconto{}.'.format(
    text['azul'], text['reset'], text['verde'], text['reset']))
print()
p = float(input('Qual é o {}preço atual{} do produto?\nR$'.format(text['azul'], text['reset'])))
np = p - (p * 5 / 100)
print()
print('O produto que custava {}R${:.2f}{}, com {}5% de desconto{} passa a custar {}R${:.2f}{}.'.format(
    text['azul'], p, text['reset'], text['verde'], text['reset'], text['verde'], np, text['reset']))
