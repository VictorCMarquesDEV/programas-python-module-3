from time import sleep


def cabecalho1(msg):
    print('=' * 40)
    print('\033[7;49;32m{:^40}\033[m'.format(msg))
    print('=' * 40)


def cabecalho2(msg):
    print('=' * 40)
    print('\033[7;49;34m{:^40}\033[m'.format(msg))
    print('=' * 40)


def ajuda(string):
    print('\033[7;49;37m')
    help(string)
    print('\033[m')


while True:
    cabecalho1('SISTEMA DE AJUDA PyHELP')
    esc = str(input('Função ou Biblioteca [FIM para sair]: ')).lower()
    if esc == 'fim':
        cabecalho2('PROGRAMA ENCERRADO')
        break
    cabecalho2(f'Acessando o manual do comando "'f"{esc}"'"')
    sleep(3)
    ajuda(esc)
