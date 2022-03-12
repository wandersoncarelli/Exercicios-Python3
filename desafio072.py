# ==================================================== DESAFIO 072 =====================================================
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu
# programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# ======================================================================================================================
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print('Digite um número entre 0 e 20 para vê-lo escrito por extenso.')

while True:
    print()
    num = int(input('Número: '))
    if 0 <= num <= 20:
        print(f'O número {num} escrito por extenso é {extenso[num]}.')
        break
    else:
        print('Número inválido.')
