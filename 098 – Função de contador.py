# ==================================================== DESAFIO 098 =====================================================
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
# ======================================================================================================================
import time

def contador(inicio, fim, passo):
    step = passo
    end = fim

    if passo == 0:
        step = 1
        passo = 1

    if passo < 0:
        step = abs(passo)
        end -= step


    if inicio > fim:
        step = step * -1
        end += step
        if passo < 0:
            end -= step
    else:
        end += 1

    print('=' * 30)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:')
    for i in range(inicio, end, step):
        print(i, end=' ')
        time.sleep(.1)
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

print('=' * 30)
print('Personalize a contagem:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
