# ==================================================== DESAFIO 026 =====================================================
# Crie um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.
# ======================================================================================================================
frase = input('Digite uma frase qualquer:\n').strip().lower()
print()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na {}ª posição.'.format(frase.find('a') + 1))
print('A última letra A apareceu na {}ª posição.'.format(frase.rfind('a') + 1))
