# ==================================================== DESAFIO 020 =====================================================
# O mesmo professor do desafio anterior, quer sortear a ordem de apresentação de trabalhos dos alunos. Crie um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.
# ======================================================================================================================
from random import shuffle
print('Digite o nome dos quatro alunos para sortear a ordem de apresentação do trabalho.\n')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print()
print('A ordem de apresentação será:')
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
