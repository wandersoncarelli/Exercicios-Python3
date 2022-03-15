# ==================================================== DESAFIO 044 =====================================================
# Crie um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
# ======================================================================================================================
from format import style, text
print('Digite o {}valor do produto{} para saber as {}formas de pagamento{} e {}preço final{}.'.
      format(style['sublinhado'], style['reset'], text['magenta'], text['reset'], text['magenta'], text['reset']))
preco = float(input('Preço: R$'))
print()
print('Agora veja as {}formas de pagamento{} e digite o {}número{} referente a opção desejada:'.
      format(text['magenta'], text['reset'], style['sublinhado'], style['reset']))
print('{}01{} -> {}À vista no dinheiro/cheque{}'.format(text['verde'], text['reset'], text['verde'], text['reset']))
print('{}02{} -> {}À vista no cartão{}'.format(text['azul'], text['reset'], text['azul'], text['reset']))
print('{}03{} -> {}Parcelado no cartão{}'.format(text['ciano'], text['reset'], text['ciano'], text['reset']))
condicao = int(input('Opção: '))
print()
if condicao == 1:
    desconto = preco * 10 / 100
    print('Efetuando o pagamento {}à vista no dinheiro/cheque{}, você ganha {}10% de desconto{}.'.
          format(text['verde'], text['reset'], text['verde'], text['reset']))
    print('O {}preço final{} a se pagar pelo produto, será de {}R${:.2f}{}.'.
          format(text['verde'], text['reset'], text['verde'], preco - desconto, text['reset']))
elif condicao == 2:
    desconto = preco * 5 / 100
    print('Efetuando o pagamento {}à vista no cartão{}, você ganha {}5% de desconto{}.'.
          format(text['azul'], text['reset'], text['azul'], text['reset']))
    print('O {}preço final{} a se pagar pelo produto, será de {}R${:.2f}{}'.
          format(text['azul'], text['reset'], text['azul'], preco - desconto, text['reset']))
elif condicao == 3:
    parcelas = int(input('Digite em {}quantas parcelas{} deseja pagar: '.format(style['sublinhado'], style['reset'])))
    print()
    if parcelas == 2:
        print('Sua compra será {}parcelada em 2x de R${:.2f}{}, você pagará o preço normal.'.
              format(text['ciano claro'], preco / 2, text['reset']))
        print('O {}preço final{} a se pagar pelo produto será de {}R${:.2f}{}.'.
              format(text['ciano claro'], text['reset'], text['ciano claro'], preco, text['reset']))
    elif parcelas >= 3:
        juros = preco * 20 / 100
        print('Sua compra será {}parcelada em {}x de R${:.2f}{}, pois houve {}acréscimo de juros de 20%{}.'.
              format(text['vermelho'], parcelas, (preco + juros) / parcelas, text['reset'], text['vermelho'],
                     text['reset']))
        print('O {}preço final{} a se pagar pelo produto, será de {}R${:.2f}{}.'.
              format(text['vermelho'], text['reset'], text['vermelho'], preco + juros, text['reset']))
    else:
        print('{}Quantidade inválida. Opção disponível apenas para parcelamentos em 2x ou mais.{}'.
              format(text['vermelho'], text['reset']))
else:
    print('{}Opção inválida.{}'.format(text['vermelho'], text['vermelho']))

