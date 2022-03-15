# ==================================================== DESAFIO 075 =====================================================
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
# ======================================================================================================================
valores = (int(input('1º valor: ')), int(input('2º valor: ')), int(input('3º valor: ')), int(input('4º valor: ')))

print()
print(*valores)
print(f'O número 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O número 9 foi digitado pela primeira vez na posição {valores.index(3)}')
else:
    print('O número 3 não foi digitado.')
print('Números pares digitados: ', end='')
for i in valores:
    if i % 2 == 0:
        print(i, end=' ')
