# Crie um programa que converta uma temperatura digitada em °C para °F.

c = float(input('Temperatura em °C: '))
f = 9 * c / 5 + 32
print('{:.1f}°C = {:.1f}°F.'.format(c, f))
