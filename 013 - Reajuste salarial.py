# Crie um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Salário atual: R$'))
ns = s + (s * 15 / 100)
print()
print('Novo salário com 15% de aumento: R${:.2f}.'.format(ns))
