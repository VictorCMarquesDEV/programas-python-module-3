def leiaDinheiro(msg):
    txt = str(input(msg)).replace(',', '.').strip()
    while txt.isalpha() or txt == '':
        print(f'\033[0;49;31mERRO: "{txt}" é um preço inválido!\033[m')
        txt = str(input(msg))
    return float(txt)


def leiaInt(msg):
    a = str(input(msg))
    while not a.isnumeric():
        print('\033[0;49;31mERRO! Digite um número inteiro válido.\033[m')
        a = str(input(msg))
    return int(a)


def leiaFloat(msg):
    a = str(input(msg)).strip()
    while a.isalpha() or a == '':
        print('\033[0;49;31mERRO! Digite um número inteiro válido.\033[m')
        a = str(input(msg)).strip()
    return float(a)


def leiaString(msg):
    a = str(input(msg)).strip()
    while not a.isalpha() and a.isspace():
        print('\033[0;49;31mERRO! Digite um nome válido.\033[m')
        a = str(input(msg)).strip()
    return a


def cabecalho():
    print('\033[7;49;34m=\033[m' * 54)
    print('\033[7;49;34m', '|', ' ' * 16, '{:^}'.format('MENU PRINCIPAL'), ' ' * 16, '|', '\033[m')
    print('\033[7;49;34m=\033[m' * 54)


def op():
    print('\033[0;49;34m1 -\033[m Ver pessoas cadastradas')
    print('\033[0;49;34m2 -\033[m Cadastrar nova pessoa')
    print('\033[0;49;34m3 -\033[m Sair do Sistema')


def visualizacao():
    print('=' * 54)
    print(' ' * 17, '{:^}'.format('PESSOAS CADASTRADAS'), ' ' * 17)
    print('=' * 54)
    with open('pessoas.txt', 'r') as arquivo:
        texto = arquivo.read()
        print(texto)


def cadastro():
    print('=' * 54)
    print(' ' * 20, '{:^}'.format('NOVO CADASTRO'), ' ' * 20)
    print('=' * 54)
    nome = leiaString('Nome: ')
    idade = leiaInt('Idade: ')
    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write('{:45} {} anos\n'.format(nome, idade))
    print('Pessoa cadastrada com sucesso.')


def finalizar():
    print('\033[7;49;34m=\033[m' * 54)
    print('\033[7;49;34m', '|', ' ' * 7, '{:^}'.format('PROGRAMA FINALIZADO COM SUCESSO'), ' ' * 8, '|', '\033[m')
    print('\033[7;49;34m=\033[m' * 54)
