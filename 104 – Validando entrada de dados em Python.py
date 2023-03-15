# ==================================================== DESAFIO 104 =====================================================
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex:
# n = leiaInt('Digite um n: ')
# ======================================================================================================================

def leiaInt(num):
    if num.isnumeric():
        return True
    else:
        return False

while True:
    n = input('Digite um número: ')
    if leiaInt(n):
        print(f'Você digitou o número {n}.')
        break
    else:
        print('ERRO. Digite um número inteiro válido.')
