# ==================================================== DESAFIO 039 =====================================================
# Crie um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# ======================================================================================================================
from datetime import date
print('Digite o ano de seu nascimento para saber se você já precisa ou não se alistar ao serviço militar.')
nasc = int(input('Nascimento: '))
atual = date.today().year
idade = atual - nasc
print()
print('Quem nasceu em {} completa {} anos em {}.'.format(nasc, idade, atual))
if idade < 18:
    print('Você não tem idade para se alistar! Ainda faltam {} anos.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(nasc + 18))
elif idade == 18:
    print('Você já tem idade para se alistar!')
    print('Seu alistamento é esse ano.')
else:
    print('Você já passou da idade de se alistar! Você deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(nasc + 18))

