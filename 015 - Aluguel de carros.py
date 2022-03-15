# Crie um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.

d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos KMs foram rodados? '))
t = d * 60 + km * 0.15
print()
print('O valor a ser pago pelo aluguel é de R${:.2f}.'.format(t))
