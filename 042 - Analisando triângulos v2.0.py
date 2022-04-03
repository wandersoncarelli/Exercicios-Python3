# ==================================================== DESAFIO 042 =====================================================
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
# ======================================================================================================================
print('Digite o comprimento de três retas, e eu vou dizer se elas podem ou não formar um triângulo, e qual o tipo de '
      'triângulo formado.')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print()
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um Triângulo', end=' ')
    if r1 == r2 == r3:
        print('Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
