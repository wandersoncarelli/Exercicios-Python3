# ==================================================== DESAFIO 040 =====================================================
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
# ======================================================================================================================
print('Digite duas notas para ver a média do aluno e saber se foi aprovado, reprovado ou ficou em recuperação.')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print()
if media < 5:
    print('A média do aluno foi {:.1f}.\nO aluno foi reprovado.'.format(media))
elif 5 <= media < 7:
    print('A média do aluno foi {:.1f}.\nO aluno está em recuperação'.format(media))
else:
    print('A média do aluno foi {:.1f}.\nO aluno foi aprovado!'.format(media))
