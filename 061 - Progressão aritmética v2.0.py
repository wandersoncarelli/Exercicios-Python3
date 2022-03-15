# ==================================================== DESAFIO 061 =====================================================
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
# ======================================================================================================================
print('Digite o Termo e a Razão de uma Progressão Aritmética para ver os 10 primeiros termos desta progressão.\n')

termo = int(input('Termo: '))
razao = int(input('Razão: '))
soma = termo
cont = 0

print('\nOs 10 primeiros termos são:')
while cont < 10:
    print(f'{soma}', end='')
    print(', ' if cont < 9 else '.', end='')
    soma += razao
    cont += 1
print()
