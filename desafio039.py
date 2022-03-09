# ==================================================== DESAFIO 039 =====================================================
# Crie um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# ======================================================================================================================
from format import text
from datetime import date
print('Digite o {}ano de seu nascimento{} para saber se você {}já{} precisa ou {}não{} se alistar ao serviço militar.'.
      format(text['magenta'], text['reset'], text['verde'], text['reset'], text['vermelho'], text['reset']))
nasc = int(input('{}Nascimento{}: '.format(text['magenta'], text['reset'])))
atual = date.today().year
idade = atual - nasc
print()
print('Quem nasceu em {}{}{} tem {}{} anos{} em {}.'.format(text['magenta'], nasc, text['reset'], text['magenta'],
                                                            idade, text['reset'], atual))
if idade < 18:
    print('Você {}não tem{} idade para se alistar! Ainda faltam {}{}{} anos.'.
          format(text['ciano claro'], text['reset'], text['ciano claro'], 18 - idade, text['reset']))
    print('Seu alistamento será em {}{}{}.'.format(text['ciano claro'], nasc + 18, text['reset']))
elif idade == 18:
    print('Você {}já tem{} idade para se alistar!'.format(text['verde'], text['reset']))
    print('Seu alistamento é {}esse ano{}.'.format(text['verde'], text['reset']))
else:
    print('Você {}já passou{} da idade de se alistar! Você deveria ter se alistado há {}{}{} anos.'.
          format(text['vermelho'], text['reset'], text['vermelho'], idade - 18, text['reset']))
    print('Seu alistamento foi em {}{}{}.'.format(text['vermelho'], nasc + 18, text['reset']))

