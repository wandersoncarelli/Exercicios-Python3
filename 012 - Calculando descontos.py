# Crie um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input('Preço do produto: R$'))
np = p - (p * 5 / 100)
print()
print('O produto que custava R${:.2f}, com 5% de desconto passa a custar R${:.2f}'.format(p, np))
