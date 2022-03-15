# ==================================================== DESAFIO 067 =====================================================
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
# ======================================================================================================================
print('Digite um número para ver sua tabuada, em seguida, digite ou número.')
print('Para sair do programa, digite um valor negativo.')

while True:
    print()
    num = int(input('Número: '))
    if num < 0:
        break
    print(f'A tabuada de {num} é:\n')
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')

print('Você saiu do programa.')
