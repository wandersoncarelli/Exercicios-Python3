# Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite uma distância em metros: '))
cm = m * 100
mm = m * 1000
print()

print('{} metros = {} centímetros.'.format(m, cm))
print('{} metros = {} milímetros .'.format(m, mm))
