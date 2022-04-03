# ==================================================== DESAFIO 050 =====================================================
# Crie um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado
# for ímpar, desconsidere-o.
# ======================================================================================================================

print('Digite seis números inteiros para ver a soma dos números pares.')
print()
soma = 0
for c in range(1, 7):
    num = int(input('Número: '))
    if num % 2 == 0:
        soma = soma + num
print()
if soma > 0:
    print('A soma dos números pares é igual a {}.'.format(soma))
else:
    print('Não houve nenhum número par digitado.')
