# ==================================================== DESAFIO 022 =====================================================
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas.
# - O nome com todas as letras minúsculas.
# - Quantas letras ao total (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
# ======================================================================================================================
from format import style, text
from time import sleep
nome = input('Qual é o seu nome completo?\n').strip()
print()
print('{}Analisando seu nome...{}'.format(text['magenta'], text['reset']))
sleep(1.5)
print('Seu nome em {}maiúsculo{} é'.format(text['verde'], text['reset']), nome.upper())
print('Seu nome em {}minúsculo{} é'.format(text['amarelo'], text['reset']), nome.lower())
print('Seu nome {}ao todo{} tem {}{}{} letras.'.format(text['azul'], text['reset'], text['azul'],
                                                       (len(nome) - nome.count(' ')), text['reset']))
# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separado = nome.split()
print('Seu {}primeiro{} nome é {}{}{} e ele tem {}{}{} letras.'.format(text['ciano'], text['reset'], text['ciano'],
                                                                       separado[0], text['reset'], text['ciano'],
                                                                       len(separado[0]), text['reset']))
