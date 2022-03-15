# Crie um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('Digite o valor de duas notas.')
print()

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print()

print('Média entre {:.1f} e {:.1f} = {:.1f}.'.format(n1, n2, m))
