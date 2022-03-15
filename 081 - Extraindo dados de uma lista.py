# ==================================================== DESAFIO 081 =====================================================
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
# ======================================================================================================================
valores = []
print('Digite alguns números inteiros. Para sair, digite um número negativo.')

while True:
    n = int(input('Número: '))
    if n < 0:
        break
    valores.append(n)
print()
print(f'Números digitados: ', end='')
print(*valores)
print(f'Foram digitados {len(valores)} números.')
print(f'Números digitados em ordem decrescente: ', end='')
print(*reversed(sorted(valores)))
if 5 in valores:
    print(f'O número 5 foi digitado e está na posição {valores.index(5)} da lista.')
else:
    print('O número 5 não foi digitado.')
