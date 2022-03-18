# ==================================================== DESAFIO 022 =====================================================
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas.
# - O nome com todas as letras minúsculas.
# - Quantas letras ao total (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
# ======================================================================================================================
nome = input('Qual é o seu nome completo?\n').strip()
print()
print('Seu nome em maiúsculo:', nome.upper())
print('Seu nome em minúsculo:', nome.lower())
print('Seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
separado = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separado[0], len(separado[0])))
