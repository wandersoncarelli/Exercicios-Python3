# ==================================================== DESAFIO 019 =====================================================
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.
# ======================================================================================================================
from random import choice
print('Digite o nome dos quatro alunos para sortear quem irá apagar o quadro.\n')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
sorteado = choice(lista)
print()
print('O aluno sorteado para apagar o quadro foi {}.'.format(sorteado))
