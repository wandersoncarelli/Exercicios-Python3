# ==================================================== DESAFIO 029 =====================================================
# Crie um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite.
# ======================================================================================================================
print('Me diga a velocidade atual do carro, e eu vou dizer se está acima ou abaixo do limite máximo de velocidade.')
vel = int(input('Velocidade atual: '))
print()
if vel > 80:
    acima = vel - 80
    multa = (vel - 80)*7
    print('Você está {}km/h acima do limite máximo permitido de 80km/h e foi multado em R${:.2f}.'.format(acima, multa))
else:
    print('Você está abaixo do limite máximo permitido de 80km/h. Dirija com cuidado!')
