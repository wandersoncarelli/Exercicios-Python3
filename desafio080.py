# ==================================================== DESAFIO 080 =====================================================
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
# ======================================================================================================================
valores = []
for i in range(0, 5):
    n = int(input('Número: '))
    if i == 0 or n > valores[-1]:
        valores.append(n)
        print(f'O número {n} foi adicionado ao final da lista.')
    else:
        p = 0
        while p < len(valores):
            if n <= valores[p]:
                valores.insert(p, n)
                print(f'O número {n} foi adicionado na posição {p}')
                break
            p += 1
print()
print(f'Valores digitados: ', end='')
print(*valores)
