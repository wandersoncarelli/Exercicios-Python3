# ==================================================== DESAFIO 077 =====================================================
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.
# ======================================================================================================================
palavras = ('Abacate', 'Televisao', 'Liquidificador', 'Mochila', 'Mala', 'Espelho', 'Porta', 'Chaveiro')
print(*palavras, sep=', ', end='.')
print('\n')

for i in range(0, len(palavras)):
    print(f'{palavras[i]} tem as vogais: ', end='')
    if 'A' in (palavras[i]).upper():
        print(f'A', end=' ')
    if 'E' in (palavras[i]).upper():
        print(f'E', end=' ')
    if 'I' in (palavras[i]).upper():
        print(f'I', end=' ')
    if 'O' in (palavras[i]).upper():
        print(f'O', end=' ')
    if 'U' in (palavras[i]).upper():
        print(f'U', end=' ')
    print()
