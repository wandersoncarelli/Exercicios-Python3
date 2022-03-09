# ==================================================== DESAFIO 010 =====================================================
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27
# ======================================================================================================================
from format import text
reais = float(input('Para saber quantos {}Dólares{} você pode comprar, digite quanto {}dinheiro{} você tem:\n{}R${}'
                    .format(text['ciano'], text['reset'], text['verde'], text['reset'], text['verde'], text['reset'])))
dolares = reais / 3.27
print()
print('Com {}R${:.2f}{} você pode comprar {}US${:.2f}{}.'.format(text['verde'], reais, text['reset'], text['ciano'],
                                                                 dolares, text['reset']))
