# ==================================================== DESAFIO 034 =====================================================
# Crie um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
# ======================================================================================================================
from format import text
print('Digite o {}salário atual{} do funcionário para calcular seu {}novo salário{} com aumento.'.
      format(text['magenta'], text['reset'], text['verde'], text['reset']))
salario = float(input('{}Salário atual{}: R$'.format(text['magenta'], text['reset'])))
print()
# MÉTODO 01
if salario <= 1250:
    print('Quem ganhava {}R${:.2f}{} passa a ganhar {}R${:.2f}{}.'.
          format(text['magenta'], salario, text['reset'], text['verde'], (salario + (salario * 15 / 100)),
                 text['reset']))
else:
    print('Quem ganhava {}R${:.2f}{} passa a ganhar {}R${:.2f}{}.'.
          format(text['magenta'], salario, text['reset'], text['verde'], (salario + (salario * 10 / 100)),
                 text['reset']))

# MÉTODO 02
if salario <=1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava {}R${:.2f}{} passa a ganhar {}R${:.2f}{}.'.format(text['magenta'], salario, text['reset'],
                                                                      text['verde'], novo, text['reset']))
