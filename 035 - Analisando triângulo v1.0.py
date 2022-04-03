# ==================================================== DESAFIO 035 =====================================================
# Crie um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# ======================================================================================================================
print('Digite o comprimento de três retas, e eu vou dizer se elas podem ou não formar um triângulo.')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print()
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos informados podem formar um triângulo!')
else:
    print('Os segmentos informados não podem formar um triângulo!')
