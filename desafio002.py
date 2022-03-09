# ==================================================== DESAFIO 002 =====================================================
# Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
# ======================================================================================================================
from format import text
nome = input('Qual é o seu nome?\n').strip()
print()
print('Olá {}{}{}, prazer em te conhecer!'.format(text['azul'], nome, text['reset']))
