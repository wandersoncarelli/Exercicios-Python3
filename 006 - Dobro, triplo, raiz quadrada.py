# Crie um programa que leia um número e mostre o seu doro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print()
print('Dobro de {}: {}'.format(n, d))
print('Triplo de {}: {}'.format(n, t))
print('Raiz quadrada de {}: {}'.format(n, r))
