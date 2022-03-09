# ==================================================== DESAFIO 065 =====================================================
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.
# ======================================================================================================================
print('Digite alguns números inteiros. Ao final, irei mostrar a média entre todos eles e os maiores e menores.\n')

valores = list()
num = int(input('Número: '))
valores.append(num)
maior = menor = num

while True:
    opcao = input('Deseja adicionar mais números? (S/N): ').upper()
    print()
    if opcao == 'N':
        print('Você saiu do programa.')
        print()
        break
    elif opcao == 'S':
        num = int(input('Número: '))
        valores.append(num)
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    else:
        print('Opção inválida.')

media = sum(valores) / len(valores)
print(f'A média entre todos os valores digitados é {media:.1f}.')
print(f'O maior número digitado foi {maior}.')
print(f'O menor número digitado foi {menor}.')


