# ==================================================== DESAFIO 105 =====================================================
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# - Quantidade de notas
# – A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# ======================================================================================================================

def notas(*num, sit=False):
    """
    - Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias notas)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """

    soma = 0

    if len(num) > 0:
        maior = menor = num[0]
    else:
        maior = menor = 0

    for i in range(0, len(num)):
        if num[i] > maior:
            maior = num[i]

        if num[i] < menor:
            menor = num[i]

        soma += num[i]

    media = soma / len(num)

    aluno = dict()
    aluno['total'] = len(num)
    aluno['maior'] = maior
    aluno['menor'] = menor
    aluno['media'] = f'{media:.2f}'

    if sit:
        if media >= 7:
            aluno['situação'] = 'BOA'
        elif 5 >= media < 7:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'

    return aluno

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)