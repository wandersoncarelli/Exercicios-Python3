# Crie um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 10
# primeiros termos dessa progressão.
print('Digite o Termo e a Razão de uma Progressão Aritmética.')
print()
termo = int(input('Termo: '))
razao = int(input('Razão: '))
print()
print('Os 10 primeiros termos da PA são:')
soma = termo
for c in range(1, 11):
    soma = termo
    termo = termo + razao
    print(soma, end=', ')
print()
