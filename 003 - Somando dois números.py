# Crie um programa que leia dois números e mostre a soma entre eles.

print('Digite dois números para ver a soma entre eles.\n')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
s = n1 + n2
print()
print('A soma entre {:.2f} e {:.2f} é igual a {:.2f}.'.format(n1, n2, s))
