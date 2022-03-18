# ==================================================== DESAFIO 025 =====================================================
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
# ======================================================================================================================
nome = input('Qual é o seu nome completo?\n').strip()
print()
if 'silva' in nome.lower():
    print('Você tem Silva no nome.')
else:
    print('Você não tem Silva no nome.')
