# ==================================================== DESAFIO 089 =====================================================
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
# ======================================================================================================================
alunos = []
opcao = boletim = ''

while opcao != 'N':
    nome = input('Nome do aluno: ')
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    alunos.append([nome, [n1, n2], (n1 + n2) / 2])
    while opcao != 'S' or opcao != 'N':
        opcao = input('Deseja continuar? (S/N): ').upper()
        if opcao == 'S' or opcao == 'N':
            break
        else:
            print('Opção inválida.')
            print()
    print()

print(25 * '=')
print(f'{"Nº":<5}{"ALUNO":<15}{"MEDIA"}')
print(25 * '=')
for i in range(0, len(alunos)):
    print(f'{i:<5}{alunos[i][0]:<15}{alunos[i][2]:>5.1f}')

while boletim != 999:
    print()
    while boletim != 999 or 0 <= boletim <= len(alunos):
        boletim = int(input('Digite o número do aluno para ver seu boletim (999 para sair): '))
        if 0 <= boletim < len(alunos):
            print(f'As notas de {alunos[boletim][0]} são: {alunos[boletim][1][0]} e {alunos[boletim][1][1]}.')
            print()
        elif boletim == 999:
            break
        else:
            print('Número inválido.')
            print()
print('Você saiu do programa.')
