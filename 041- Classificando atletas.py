# ==================================================== DESAFIO 041 =====================================================
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
# ======================================================================================================================
from datetime import date
print('Digite o ano de nascimento do atleta para ver sua categoria.')
nascimento = int(input('Nascimento: '))
atual = date.today().year
idade = atual - nascimento
print()
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('A categoria do atleta é MIRIM.')
elif idade <= 14:
    print('A categoria do atleta é INFANTIL.')
elif idade <= 19:
    print('A categoria do atleta é JUNIOR.')
elif idade <= 25:
    print('A categoria do atleta é SÊNIOR.')
else:
    print('A categoria do atleta é MASTER.')
