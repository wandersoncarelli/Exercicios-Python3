# ==================================================== DESAFIO 085 =====================================================
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# ======================================================================================================================
valores = [[], []]
for i in range(0, 7):
    num = int(input('Número: '))
    if num % 2 == 0:
        valores[1].append(num)
    else:
        valores[0].append(num)
print()
print(f'Números pares: ', end='')
print(*sorted(valores[1]), end=' ')
print()
print(f'Números ímpares: ', end='')
print(*sorted(valores[0]), end=' ')
