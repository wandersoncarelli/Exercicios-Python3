# ==================================================== DESAFIO 031 =====================================================
# Crie um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM
# para viagens de até 200KM e R$0,45 para viagens mais longas.
# ======================================================================================================================
from format import text
from time import sleep
print('Me diga a {}distância da viagem em KM{}, e eu vou calcular e lhe dizer o {}preço{}.'.
      format(text['azul claro'], text['reset'], text['verde'], text['reset']))
distancia = float(input('Distância: '))
print('{}CALCULANDO...{}'.format(text['magenta'], text['reset']))
sleep(1)
print()
if distancia <= 200:
    print('Em uma {}viagem de {:.2f}KM{}, o preço da passagem será de {}R${:.2f}{}.'.
          format(text['azul claro'], distancia, text['reset'], text['verde'], (distancia * 0.50), text['reset']))
else:
    print('Em uma {}viagem de {:.2f}KM{}, o preço da passagem será de {}R${:.2f}{}.'.
          format(text['azul claro'], distancia, text['reset'], text['verde'], (distancia * 0.45), text['reset']))

# MÉTODO 02

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Em uma {}viagem de {:.2f}KM{}, o preço da passagem será de {}R${:.2f}{}.'.
      format(text['azul claro'], distancia, text['reset'], text['verde'], preco, text['reset']))
