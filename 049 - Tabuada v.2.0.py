# ==================================================== DESAFIO 049 =====================================================
# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.
# ======================================================================================================================
num = int(input('Digite um número para ver sua tabuada: '))
tab = 0
res = 0
print()
print(15 * '=')
for c in range(1, 11):
    tab = tab + 1
    res = num * tab
    print('{} x {} = {}'.format(num, tab, res))
print(15 * '=')
