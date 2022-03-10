# ==================================================== DESAFIO 075 =====================================================
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
# ======================================================================================================================
valores = []
pares = []
print('Digite 4 números inteiros.')

for cont in range(0, 4):
    num = int(input('Número: '))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)

print()
print(f'O valor 9 foi digitado {valores.count(9)} vezes na lista.')
if 3 in valores:
    print(f'O número 3 foi digitado pela primeira vez no {valores.index(3) + 1}º número.')
else:
    print('O número 3 não foi digitado na lista.')
if len(pares) > 0:
    print(f'Os números pares digitados foram: ', end='')
    print(*pares, sep=', ', end='.')
else:
    print('Não foram digitados números pares na lista.')
