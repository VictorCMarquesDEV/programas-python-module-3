def cabecalho(msg):
    print('=' * 40)
    print('{:^40}'.format(msg))
    print('=' * 40)


def somador(a, b):
    soma = a + b
    print(f'{a} + {b} = {soma}')


def contador(*num):
    print(f'Há {len(num)} elementos')


def dobra(lista):
    for i in range(0, len(lista)):
        lista[i] *= 2


cabecalho('SISTEMA DE ALUNOS')
somador(4, 5)
contador(1, 2, 3, 4, 5)
contador(1, 2, 3)
valores = [6, 3, 9, 1, 0, 2]
print('Lista original: ', valores)
dobra(valores)
print('Lista dobrada: ', valores)
