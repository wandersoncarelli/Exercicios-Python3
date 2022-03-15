# ==================================================== DESAFIO 053 =====================================================
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# (Palíndromo são frases ou palavras que podem ser lidas de trás pra frente sem que mudem o significado)
# Ex:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA
# ======================================================================================================================
frase = input('Frase: ').strip().upper()
print(f'Você digitou a frase: {frase}')
junto = ''.join(frase.split())
inverso = junto[::-1]
if inverso == junto:
    print('E ela é um palíndromo!')
else:
    print('E ela não é um palíndromo!')
