# ==================================================== DESAFIO 101 =====================================================
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
# ======================================================================================================================
from datetime import date

ano_atual = date.today().year

def voto(ano):
    if ano_atual - ano < 16:
        return 'NEGADO'
    elif 16 <= ano_atual - ano < 18 or ano_atual - ano > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATORIO'

ano_nasc = int(input('Digite o ano de nascimento: '))
print(f'Com {ano_atual - ano_nasc} anos, o voto é {voto(ano_nasc)}!')
