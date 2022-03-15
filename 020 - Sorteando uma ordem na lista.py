# ==================================================== DESAFIO 020 =====================================================
# O mesmo professor do desafio anterior, quer sortear a ordem de apresentação de trabalhos dos alunos. Crie um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.
# ======================================================================================================================
from format import style, text
from random import shuffle
print('Digite o nome dos {}quatro alunos{} para sortear a ordem de apresentação do trabalho.\n'.format(
    style['sublinhado'], style['reset']))
a1 = input('{}Primeiro aluno{}: '.format(text['vermelho'], text['reset']))
a1 = '{}{}{}'.format(text['vermelho'], a1, text['reset'])
a2 = input('{}Segundo aluno{}: '.format(text['verde'], text['reset']))
a2 = '{}{}{}'.format(text['verde'], a2, text['reset'])
a3 = input('{}Terceiro aluno{}: '.format(text['azul'], text['reset']))
a3 = '{}{}{}'.format(text['azul'], a3, text['reset'])
a4 = input('{}Quarto aluno{}: '.format(text['ciano'], text['reset']))
a4 = '{}{}{}'.format(text['ciano'], a4, text['reset'])
lista = [a1, a2, a3, a4]
shuffle(lista)
print()
print('A ordem de apresentação será:')
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
