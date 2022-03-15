# ==================================================== DESAFIO 079 =====================================================
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.
# ======================================================================================================================
valores = []

print('Digite vários números inteiros para cadastrar em uma lista. Para sair, digite um número negativo.')
while True:
    num = int(input('Número: '))
    if num < 0:
        break
    if num not in valores:
        valores.append(num)
print()
print(*sorted(valores))
