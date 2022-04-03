# ==================================================== DESAFIO 031 =====================================================
# Crie um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM
# para viagens de até 200KM e R$0,45 para viagens mais longas.
# ======================================================================================================================
print('Me diga a distância da viagem em KM para ver o preço da passagem.')
distancia = float(input('Distância: '))
print()

# MÉTODO 01
if distancia <= 200:
    print('Em uma viagem de {:.2f}KM, o preço da passagem será de R${:.2f}.'.format(distancia, (distancia * 0.50)))
else:
    print('Em uma viagem de {:.2f}KM, o preço da passagem será de R${:.2f}.'.format(distancia, (distancia * 0.45)))

# MÉTODO 02
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Em uma viagem de {:.2f}KM, o preço da passagem será de R${:.2f}.'.format(distancia, preco))
