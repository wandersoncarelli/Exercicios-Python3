# ==================================================== DESAFIO 033 =====================================================
# Crie um programa que leia três números e mostre qual é o maior e qual é o menor.
# ======================================================================================================================
print('Digite três números para saber qual é o menor e o maior.')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
print()
# Verificar quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificar quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))
