# ==================================================== DESAFIO 015 =====================================================
# Crie um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.
# ======================================================================================================================
from format import text
print('Para calcular o {}preço total{} do aluguel do carro, digite por quantos {}dias{} foi alugado e a quantidade de '
      '{}KMs{} rodados.'.format(text['verde'], text['reset'], text['azul'], text['reset'], text['ciano'],
                                text['reset']))
print()
d = int(input('Por quantos {}dias{} o carro foi alugado? '.format(text['azul'], text['reset'])))
km = float(input('Quantos {}KMs{} foram rodados? '.format(text['ciano'], text['reset'])))
t = d * 60 + km * 0.15
print()
print('O total a pagar pelo aluguel é de {}R${:.2f}{}.'.format(text['verde'], t, text['reset']))
