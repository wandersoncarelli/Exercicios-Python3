# ==================================================== DESAFIO 043 =====================================================
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 24.9: Peso ideal
# - 25 até 29.9: Sobrepeso
# - 30 até 34.9: Obesidade grau 1
# - 35 até 39.9: Obesidade grau 2
# - Acima de 40: Obesidade mórbida
# ======================================================================================================================
from format import style, text
print('Para calcular seu {}IMC{}, digite seu {}peso{} e {}altura{}.'.format(text['magenta'], text['reset'],
                                                                            text['verde'], text['reset'], text['azul'],
                                                                            text['reset']))
peso = float(input('{}Peso (Kg){}: '.format(text['verde'], text['reset'])))
altura = float(input('{}Altura (m){}: '.format(text['azul'], text['reset'])))
imc = peso / (altura ** 2)
print()
if imc < 18.5:
    status = '{}Abaixo do peso{}'.format(text['amarelo'], text['reset'])
elif imc < 25:
    status = 'com {}Peso ideal{}'.format(text['verde'], text['reset'])
elif imc < 30:
    status = 'com {}{}Sobrepeso{}'.format(style['negrito'], text['magenta'], text['reset'])
elif imc < 35:
    status = 'com {}Obesidade grau 1{}'.format(text['vermelho claro'], text['reset'])
elif imc < 40:
    status = 'com {}Obesidade grau 2{}'.format(text['vermelho'], text['reset'])
else:
    status = 'com {}{}Obesidade mórbida{}'.format(style['negrito'], text['vermelho'], text['reset'])
print('Seu {}IMC{} é {}{:.1f}{} e você está {}.'.format(text['magenta'], text['reset'], text['magenta'], imc,
                                                        text['reset'], status))
