from random import randint
numeros = []


def linha():
    print('=' * 50)


def sorteia():
    linha()
    for i in range(0, 5):
        numeros.append(randint(1, 10))
    print('A lista é:', numeros)


def somaPar(lista):
    soma = 0
    print('Soma entre todos os pares: ', end='')
    for i in lista:
        if i % 2 == 0:
            soma += i
            print(i, end=', ')
    print(f'é igual a {soma}.')
    linha()


sorteia()
somaPar(numeros)
