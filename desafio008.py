# ==================================================== DESAFIO 008 =====================================================
# Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# ======================================================================================================================
from format import text
m = float(input('Digite uma distância em {}metros{} para converter em {}centímetros{} e {}milímetros{}: '.format(
    text['magenta'], text['reset'], text['azul'], text['reset'], text['ciano'], text['reset'])))
cm = m * 100
mm = m * 1000
print()
print('{}{:.2f} metros{} corresponde a {}{:.2f} centímetros{} e {}{:.2f} milímetros{}.'.format(
    text['magenta'], m, text['reset'], text['azul'], cm, text['reset'], text['ciano'], mm, text['reset']))
