# ==================================================== DESAFIO 040 =====================================================
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
# ======================================================================================================================
from format import style, text

print('Digite o valor das {}duas notas{}, e eu calcular a {}média{} e dizer se você foi {}aprovado{}, {}reprovado{} ou '
      'ficou em {}recuperação{}.'.format(style['sublinhado'], style['reset'], text['magenta'], text['reset'],
                                         text['verde'], text['reset'], text['vermelho'], text['reset'], text['azul'],
                                         text['reset']))
n1 = float(input('{}Primeira nota{}: '.format(text['ciano'], text['reset'])))
n2 = float(input('{}Segunda nota{}: '.format(text['ciano claro'], text['reset'])))
media = (n1 + n2) / 2
print()
if media < 5:
    print('A {}média{} do aluno foi {}{:.1f}{}.\nO aluno foi {}reprovado{}.'.
          format(text['magenta'], text['reset'], text['vermelho'], media, text['reset'], text['vermelho'],
                 text['reset']))
elif 5 <= media < 7:
    print('A {}média{} do aluno foi {}{:.1f}{}.\nO aluno está em {}recuperação{}'.
          format(text['magenta'], text['reset'], text['azul'], media, text['reset'], text['azul'], text['reset']))
else:
    print('A {}média{} do aluno foi {}{:.1f}{}.\nO aluno foi {}aprovado{}!'.
          format(text['magenta'], text['reset'], text['verde'], media, text['reset'], text['verde'], text['reset']))
