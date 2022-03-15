# ==================================================== DESAFIO 036 =====================================================
# Crie um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
# ======================================================================================================================
from format import style, text
print(20 * '\033[30;1m=', 'CALCULADORA DE EMPRÉSTIMOS', 20 * '=', '\033[m')
print('Para fazer a {}análise do empréstimo{}, digite o {}valor da casa{}, o \n{}salário do comprador{} e em {}quantos '
      'anos{} ele deseja pagar.'.format(text['magenta'], text['reset'], text['azul'], text['reset'], text['ciano'],
                                        text['reset'], text['ciano claro'], text['reset']))
print()
casa = float(input('{}Valor da casa{}: R$'.format(text['azul'], text['reset'])))
salario = float(input('{}Salário do comprador{}: R$'.format(text['ciano'], text['reset'])))
anos = int(input('{}Tempo em anos para pagar{}: '.format(text['ciano claro'], text['reset'])))
prestacao = casa / (anos * 12)
print()
if prestacao < (salario * 30 / 100):
    print('{}Empréstimo aprovado!{}'.format(text['verde'], text['reset']))
    print('O valor da prestação mensal será de {}R${:.2f}{}.'.format(text['verde'], prestacao, text['reset']))
else:
    print('{}Empréstimo negado!{}'.format(text['vermelho'], text['reset']))
    print('O valor da prestação mensal seria de {}R${:.2f}{}, o que excede o limite de 30% do salário do comprador.'.
          format(text['vermelho'], prestacao, text['reset']))
