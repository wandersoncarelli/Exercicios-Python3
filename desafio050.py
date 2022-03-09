# ==================================================== DESAFIO 050 =====================================================
# Crie um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado
# for ímpar, desconsidere-o.
# ======================================================================================================================
from format import style, text
print('Digite {}seis números inteiros{}, e eu vou lhe mostrar a {}soma{} de todos os {}números pares{}.'.
      format(style['sublinhado'], style['reset'], text['verde'], text['reset'], text['magenta'], text['reset']))
print()
soma = 0
for c in range(1, 7):
    num = int(input('Número: '))
    if num % 2 == 0:
        soma = soma + num
print()
if soma > 0:
    print('A {}soma{} dos {}números pares{} dá um total de {}{}{}.'.
          format(text['verde'], text['reset'], text['magenta'], text['reset'], text['verde'], soma, text['reset']))
else:
    print('{}Não houve nenhum número par digitado.'.format(text['vermelho']))
