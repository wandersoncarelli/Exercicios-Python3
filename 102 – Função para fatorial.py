# ==================================================== DESAFIO 102 =====================================================
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.
# ======================================================================================================================

def fatorial(num, show=False):
    """
    - Calcula o fatorial de um número
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial do número num
    """

    cont = num
    fat = 1
    while cont > 0:
        if show:
            print(f'{cont}', end='')
            print(' x ' if cont > 1 else ' = ', end='')
        fat *= cont
        cont -= 1
    return fat


print(fatorial(5))
help(fatorial)