# Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Qual é o seu nome?\n').strip()
print()
print('Olá {}, prazer em te conhecer!'.format(nome))
