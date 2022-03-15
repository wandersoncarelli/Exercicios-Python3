# ==================================================== DESAFIO 037 =====================================================
# Crie um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
# ======================================================================================================================
print('Digite um número e em seguida escolha se deseja converter para binário, octal ou hexadecimal.')
num = int(input('Número: '))
print()
print('''Veja a opção correspondente à conversão desejada:
01 -> Converter para BINÁRIO
02 -> Converter para OCTAL
03 -> Converter para HEXADECIMAL''')
conversao = int(input('Opção: '))
print()
if conversao == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif conversao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif conversao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')
