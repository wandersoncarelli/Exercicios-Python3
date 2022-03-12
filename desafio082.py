# ==================================================== DESAFIO 082 =====================================================
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
# listas geradas.
# ======================================================================================================================
valores = []
pares = []
impares = []
print('Digite alguns números inteiros. Para sair, digite um número negativo.')

while True:
    n = int(input('Número: '))
    if n < 0:
        break
    valores.append(n)
for i in range(0, len(valores)):
    if valores[i] % 2 == 0:
        pares.append(valores[i])
    else:
        impares.append(valores[i])
print()
print('Números digitados: ', end='')
print(*valores)
print('Números pares: ', end='')
print(*pares)
print('Números ímpares: ', end='')
print(*impares)
