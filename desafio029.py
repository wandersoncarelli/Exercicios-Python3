# ==================================================== DESAFIO 029 =====================================================
# Crie um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite.
# ======================================================================================================================
from format import style, text
print('Me diga a {}velocidade atual{} do carro, e eu vou dizer se está {}acima{} ou {}abaixo{} do {}limite máximo{} de '
      'velocidade.'.format(style['sublinhado'], style['reset'], text['vermelho'], text['reset'], text['verde'],
                           text['reset'], text['magenta'], text['reset']))
vel = int(input('Velocidade atual: '))
mul = (vel - 80)*7
print()
if vel > 80:
    acima = vel - 80
    print('Você está {}{}km/h acima{} do {}limite máximo{} permitido que é de {}80km/h{} e foi multado em {}R${:.2f}{}.'.
          format(text['vermelho'], acima, text['reset'], text['magenta'], text['reset'], text['magenta'], text['reset'],
                 text['vermelho'], mul, text['reset']))
else:
    print('Você está {}abaixo{} do {}limite máximo{} permitido que é de {}80km/h{}. Dirija com cuidado!'.
          format(text['verde'], text['reset'], text['magenta'], text['reset'], text['magenta'], text['reset']))
