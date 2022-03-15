# ==================================================== DESAFIO 041 =====================================================
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
# ======================================================================================================================
from format import style, text
from datetime import date
print('Digite o {}ano de nascimento{} do atleta para ver sua {}categoria{}.'.format(style['sublinhado'], style['reset'],
                                                                                    text['magenta'], text['reset']))
nasc = int(input('Nascimento: '))
atual = date.today().year
idade = atual - nasc
print()
print('O atleta tem {}{}{} anos.'.format(text['magenta'], idade, text['reset']))
if idade <= 9:
    print('A {}categoria{} do atleta é {}MIRIM{}.'.format(text['magenta'], text['reset'], text['magenta'],
                                                          text['reset']))
elif idade <= 14:
    print('A {}categoria{} do atleta é {}INFANTIL{}.'.format(text['magenta'], text['reset'], text['magenta'],
                                                             text['reset']))
elif idade <= 19:
    print('A {}categoria{} do atleta é {}JUNIOR{}.'.format(text['magenta'], text['reset'], text['magenta'],
                                                           text['reset']))
elif idade <= 25:
    print('A {}categoria{} do atleta é {}SÊNIOR{}.'.format(text['magenta'], text['reset'], text['magenta'],
                                                           text['reset']))
else:
    print('A {}categoria{} do atleta é {}MASTER{}.'.format(text['magenta'], text['reset'], text['magenta'],
                                                           text['reset']))
