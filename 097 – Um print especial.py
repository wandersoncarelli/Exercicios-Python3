# ==================================================== DESAFIO 097 =====================================================
# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~
# ======================================================================================================================

def escreva(texto):
    tamanho = len(texto)
    print('~' * (tamanho + 4))
    print(f'  {texto}  ')
    print('~' * (tamanho + 4))

text = input('Escreva o texto: ')

escreva(text)
