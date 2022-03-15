# ==================================================== DESAFIO 019 =====================================================
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.
# ======================================================================================================================
from format import style, text
from random import choice
print('Digite o nome dos {}quatro alunos{} para sortear quem irá apagar o quadro.\n'.format(style['sublinhado'],
                                                                                            style['reset']))
a1 = input('{}Primeiro aluno{}: '.format(text['vermelho'], text['reset']))
a1 = '{}{}{}'.format(text['vermelho'], a1, text['reset'])
a2 = input('{}Segundo aluno{}: '.format(text['verde'], text['reset']))
a2 = '{}{}{}'.format(text['verde'], a2, text['reset'])
a3 = input('{}Terceiro aluno{}: '.format(text['azul'], text['reset']))
a3 = '{}{}{}'.format(text['azul'], a3, text['reset'])
a4 = input('{}Quarto aluno{}: '.format(text['ciano'], text['reset']))
a4 = '{}{}{}'.format(text['ciano'], a4, text['reset'])
lista = [a1, a2, a3, a4]
sorteado = choice(lista)
print()
print('O aluno sorteado para apagar o quadro foi {}.'.format(sorteado))
