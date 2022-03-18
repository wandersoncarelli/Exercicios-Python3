# ==================================================== DESAFIO 024 =====================================================
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
# ======================================================================================================================
cid = input('Em que cidade você nasceu?\n').strip()
print()
if cid[:5].lower() == 'santo':
    print('O nome da cidade em que você nasceu começa com Santo.')
else:
    print('O nome da cidade em que você nasceu não começa com Santo.')
