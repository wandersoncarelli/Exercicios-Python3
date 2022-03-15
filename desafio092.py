# ==================================================== DESAFIO 092 =====================================================
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# ======================================================================================================================
from datetime import date

dados = dict()
dados['Nome'] = input('Nome: ')
dados['Nascimento'] = int(input(f'Ano de nascimento: '))
dados['Idade'] = date.today().year - dados['Nascimento']
dados['CTPS'] = int(input(f'Nº da CTPS (0 se não tiver): '))
if dados['CTPS'] > 0:
    dados['Contratação'] = int(input(f'Ano de contratação: '))
    dados['Salario'] = float(input(f'Salário: R$'))
    dados['Aposentadoria'] = 30 - (date.today().year - dados['Contratação']) + dados['Idade']
print()
print(f'{dados["Nome"]} tem {dados["Idade"]} anos e ', end='')
if dados['CTPS'] > 0:
    print(f'CTPS nº {dados["CTPS"]}.')
    print(f'{dados["Nome"]} foi contratado em {dados["Contratação"]} e recebe R${dados["Salario"]:.2f}.')
    if dados['Aposentadoria'] <= 60:
        print(f'{dados["Nome"]} irá se aposentar com 60 anos, por tempo de contribuição.')
    elif 60 < dados['Aposentadoria'] < 65:
        print(f'{dados["Nome"]} irá se aposentar com {dados["Aposentadoria"]} anos, por tempo de contribuição')
    else:
        print(f'{dados["Nome"]} irá se aposentar com 65 anos, por idade.')
else:
    print('não tem carteira de trabalho.')
