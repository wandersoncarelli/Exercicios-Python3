# ==================================================== DESAFIO 066 =====================================================
# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).
# ======================================================================================================================
qtd = soma = 0

print('Digite alguns números, ao final, será exibido quantos números foi digitado e a soma entre eles.')
print('Para sair, digite o número "999".\n')

while True:
    num = int(input('Número: '))
    if num == 999:
        print()
        print('Você saiu do programa.')
        break
    else:
        qtd += 1
        soma += num

print(f'Ao total, foram digitados {qtd} números, e a soma entre eles é igual a {soma}.')