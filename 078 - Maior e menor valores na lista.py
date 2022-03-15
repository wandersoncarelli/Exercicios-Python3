# ==================================================== DESAFIO 078 =====================================================
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.
# ======================================================================================================================
valores = []
for i in range(0, 5):
    valores.append(int(input('Número: ')))

print()
print(f'Menor número digitado: {min(valores)} e está na posição {valores.index(min(valores))}.')
print(f'Maior número digitado: {max(valores)} e está na posição {valores.index(max(valores))}.')
