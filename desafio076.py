# ==================================================== DESAFIO 076 =====================================================
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.
# ======================================================================================================================
produtos = ('Monitor', 1240,
            'Teclado', 225,
            'Mouse', 120.50,
            'Gabinete', 248.90,
            'Placa-mãe', 340,
            'Processador', 1450,
            'Memória RAM', 400,
            'SSD', 340,
            'Fonte', 280)
print(47 * '=')
print(f'{"LISTA DE PRODUTOS":^47}')
print(47 * '=')
print()
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<37}', end='')
    else:
        print(f'R${produtos[i]:>8.2f}')
