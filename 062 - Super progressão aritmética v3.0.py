# ==================================================== DESAFIO 062 =====================================================
# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos.
# ======================================================================================================================
print('Digite o Termo e a Razão de uma Progressão Aritmética para ver os 10 primeiros termos desta progressão.\n')

termo = int(input('Termo: '))
razao = int(input('Razão: '))
soma = termo
cont = 0
qtd = 10

print('\nOs 10 primeiros termos são:')
while True:
    while cont < qtd:
        print(f'{soma}', end='')
        print(', ' if cont < (qtd - 1) else '.', end='')
        soma += razao
        cont += 1
    print()
    print('\nDeseja ver mais termos? Se não, digite 0.')
    qtd = int(input('Quantidade de termos: '))
    if qtd == 0:
        print()
        break
    else:
        print()
        print(f'Os próximos {qtd} termos são: ')
        cont = 0
print('Você saiu do programa.')
