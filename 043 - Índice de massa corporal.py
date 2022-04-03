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
print('Para calcular seu IMC, digite seu peso e altura.')
peso = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))
imc = peso / (altura ** 2)
print()
if imc < 18.5:
    status = 'Abaixo do peso'
elif imc < 25:
    status = 'com Peso ideal'
elif imc < 30:
    status = 'com Sobrepeso'
elif imc < 35:
    status = 'com Obesidade grau 1'
elif imc < 40:
    status = 'com Obesidade grau 2'
else:
    status = 'com Obesidade mórbida'
print('Seu IMC é {:.1f} e você está {}.'.format(imc, status))
