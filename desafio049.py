# ==================================================== DESAFIO 049 =====================================================
# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.
# ======================================================================================================================
from format import text
num = int(input('Digite um {}número{} para ver sua {}tabuada{}: '.format(text['azul'], text['reset'], text['magenta'],
                                                                         text['reset'])))
tab = 0
res = 0
print()
print(15 * '=')
for c in range(1, 11):
    tab = tab + 1
    res = num * tab
    print('{}{}{} x {}{}{} = {}{}{}'.format(text['azul'], num, text['reset'], text['magenta'], tab, text['reset'],
                                            text['verde'], res, text['reset']))
print(15 * '=')
