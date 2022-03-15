# Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

a = input('Digite alguma coisa e saiba algumas informações sobre o que você digitou:\n')
print()
print('O tipo primitivo do que foi digitado é {}'.format(type(a)))
print('É alfabético?', 'Sim' if a.isalpha() else 'Não')
print('É numérico?', 'Sim' if a.isnumeric() else 'Não')
print('É alfanumérico?', 'Sim' if a.isalnum() else 'Não')
print('É decimal?', 'Sim' if a.isdecimal() else 'Não')
print('É um dígito?', 'Sim' if a.isdigit() else 'Não')
print('Está em letras minúsculas?', 'Sim' if a.islower() else 'Não')
print('Está em letras maiúsculas?', 'Sim' if a.isupper() else 'Não')
print('É um espaço vazio?', 'Sim' if a.isspace() else 'Não')
print('É um título?', 'Sim' if a.istitle() else 'Não')
