# Crie um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
s = n + 1
a = n - 1
print()

print('Sucessor de {}: {}'.format(n, s))
print('Antecessor de {}: {}'.format(n, a))
