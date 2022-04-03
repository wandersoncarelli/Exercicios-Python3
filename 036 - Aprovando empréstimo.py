# ==================================================== DESAFIO 036 =====================================================
# Crie um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
# ======================================================================================================================
print(20 * '=', 'CALCULADORA DE EMPRÉSTIMOS', 20 * '=')
print('Para fazer a análise do empréstimo, digite o valor da casa, o salário do comprador e em quantos anos deseja '
      'pagar.')
print()
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Tempo em anos para pagar: '))
prestacao = casa / (anos * 12)
print()
if prestacao < (salario * 30 / 100):
    print('Empréstimo aprovado!')
    print('O valor da prestação mensal será de R${:.2f}.'.format(prestacao))
else:
    print('Empréstimo negado!')
    print('O valor da prestação mensal seria de R${:.2f}, mas excede o limite de 30% do salário do comprador.'
          .format(prestacao))
