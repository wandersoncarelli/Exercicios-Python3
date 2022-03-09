# ==================================================== DESAFIO 057 =====================================================
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a
# digitação novamente até ter um valor correto.
# ======================================================================================================================
sexo = ''

while True:
    sexo = input('Digite o seu sexo (M/F): ').upper()
    if sexo == 'M' or sexo == 'F':
        print()
        break
    else:
        print('Opção inválida. Digite apenas "M" ou "F".')
        print()
if sexo == 'M':
    print('Você é do sexo masculino.')
else:
    print('Você é do sexo feminino.')
