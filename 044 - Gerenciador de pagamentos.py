# ==================================================== DESAFIO 044 =====================================================
# Crie um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
# ======================================================================================================================
print('Digite o valor do produto para saber as formas de pagamento e preço final.')
preco = float(input('Preço: R$'))
print()
print('Agora veja as formas de pagamento e digite o número referente a opção desejada:')
print('01 -> À vista no dinheiro/cheque')
print('02 -> À vista no cartão')
print('03 -> Parcelado no cartão')
condicao = int(input('Opção: '))
print()
if condicao == 1:
    desconto = preco * 10 / 100
    print('Efetuando o pagamento à vista no dinheiro/cheque, você ganha 10% de desconto.')
    print('O preço final a se pagar pelo produto, será de R${:.2f}.'.format(preco - desconto))
elif condicao == 2:
    desconto = preco * 5 / 100
    print('Efetuando o pagamento à vista no cartão, você ganha 5% de desconto.')
    print('O preço final a se pagar pelo produto, será de R${:.2f}'.format(preco - desconto))
elif condicao == 3:
    parcelas = int(input('Digite em quantas parcelas deseja pagar: '))
    print()
    if parcelas == 2:
        print('Sua compra será parcelada em 2x de R${:.2f}, você não pagará juros.'.format(preco / 2))
        print('O preço final a se pagar pelo produto será de R${:.2f}.'.format(preco))
    elif parcelas >= 3:
        juros = preco * 20 / 100
        print('Sua compra será parcelada em {}x de R${:.2f}, pois houve acréscimo de juros de 20%.'
              .format(parcelas, (preco + juros) / parcelas))
        print('O preço final a se pagar pelo produto, será de R${:.2f}.'.format(preco + juros))
    else:
        print('Quantidade inválida. Opção disponível apenas para parcelamentos em 2x ou mais.')
else:
    print('Opção inválida.')

