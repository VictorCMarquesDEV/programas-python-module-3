def fatorial(numero=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param numero: O número a ser calculado
    :param show: Mostrar ou não a conta
    :return: O valor do fatorial
    """
    f = 1
    print(f'{numero}! = ', end='')
    for i in range(numero, 0, -1):
        f *= i
        if show:
            print(f'{i}', end='')
            if i != 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


print(fatorial(5, True))
help(fatorial)
