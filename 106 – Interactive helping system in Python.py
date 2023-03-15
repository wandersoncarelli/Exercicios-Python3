# ==================================================== DESAFIO 106 =====================================================
# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
# ======================================================================================================================

def ajuda(cmd):
    """
    - Função para mostrar a ajuda dos comandos ou bibliotecas do Python
    :param cmd: Comando ou biblioteca para obter ajuda
    :return: explicação do comando ou biblioteca
    """
    msg = f'Acessando o manual do comando {cmd}'
    print('\033[1;44m=' * (len(msg) + 4))
    print(f'\033[1;44m  {msg}  ')
    print('\033[1;44m=' * (len(msg) + 4))
    print('\033[m', end='')

    print('\033[7m', end='')
    return help(cmd)



while True:
    print('\033[1;47m=' * 27)
    print('\033[1;47m  SISTEMA DE AJUDA PyHELP  ')
    print('\033[1;47m=' * 27)
    print('\033[m', end='')

    cmd = input('Função ou biblioteca: ')
    if cmd.upper() == 'FIM':
        print('\033[1;41m=' * 30)
        print('\033[1;41m  VOCÊ SAIU DO MENU DE AJUDA  ')
        print('\033[1;41m=' * 30)
        break

    ajuda(cmd)
    print('\033[m', end='')
