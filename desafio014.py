# ==================================================== DESAFIO 014 =====================================================
# Crie um programa que converta uma temperatura digitada em °C para °F.
# ======================================================================================================================
from format import text
print('Digite uma temperatura em {}°C{} para converter em {}°F{}.'.format(text['azul'], text['reset'], text['ciano'],
                                                                          text['reset']))
print()
c = float(input('Informe a temperatura em {}°C{}: '.format(text['azul'], text['reset'])))
f = 9 * c / 5 + 32
print('A temperatura de {}{}°C{} corresponde a {}{}°F{}!'.format(text['azul'], c, text['reset'], text['ciano'], f,
                                                                 text['reset']))
