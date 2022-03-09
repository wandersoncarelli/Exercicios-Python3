# ==================================================== DESAFIO 035 =====================================================
# Crie um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# ======================================================================================================================
from format import style, text
print('Digite o {}comprimento de três retas{}, e eu vou dizer se elas {}podem{} ou {}não{} {}formar um triângulo{}.'.
      format(style['sublinhado'], style['reset'], text['verde'], text['reset'], text['vermelho'], text['reset'],
             style['negrito'], style['reset']))
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print()
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima {}podem{} formar um triângulo!'.format(text['verde'], text['reset']))
else:
    print('Os segmentos acima {}não podem{} formar um triângulo!'.format(text['vermelho'], text['reset']))
